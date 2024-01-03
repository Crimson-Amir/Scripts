import re
import requests
from bs4 import BeautifulSoup
import json
from sqlite_manager import ManageDb
from datetime import datetime
import sqlite3
import pandas as pd
import os
import uuid


class GetSocialInfo(ManageDb):
    """
    This code scrapes the Social Blade site and is written for educational purposes.
    There are no commercial purposes
    """

    def __init__(self):
        super().__init__("social_info")
        self.response = requests.Session()
        self.response.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})

        with open('database_culomn.json') as json_file:
            self.table = json.load(json_file)
        self.create_table(self.table)

    def youtube(self, youtuber: str, offline=True):
        """
        :param youtuber: preferred youtuber username
        :param offline: If set False, it will directly return online scrap results
        """
        self.all_youtuber_info = self.table['youtube']

        if offline:
            select_from_db = self.select(table='youtube', where=f"LOWER(youtuber_name) = '{youtuber}' OR REPLACE(youtuber_username, '@', '') = REPLACE('{youtuber}', '@', '')")
            if select_from_db:
                select_from_db = select_from_db[0][1:]
                self.youtuber_info = {key: select_from_db[num] for num, key in enumerate(list(self.all_youtuber_info.keys())[1:])}
                return f"{self.youtuber_info} \nThis is offline search. last update at {self.youtuber_info['data_update']}"

        url = 'https://socialblade.com/youtube/c/{0}'.format(youtuber)
        self.get_youtuber = self.response.get(url)

        if self.get_youtuber.status_code == 200:
            bs = BeautifulSoup(self.get_youtuber.text, 'html.parser')
            if not bs.h1:
                return 'Not Found'

            self.youtuber_name = bs.h1.text
            self.youtuber_username = bs.h4.text
            youtuber_banner_raw = bs.find(id='YouTubeUserTopHeaderBackground')['style']
            self.channel_avatar = re.findall(r"'(.*?)'", youtuber_banner_raw)[0]
            self.channel_banner = bs.find(id='YouTubeUserTopInfoAvatar')['src']

            self.youtuber_uploads = bs.find(id='youtube-stats-header-uploads').text
            self.youtuber_subscribers = bs.find(id='youtube-stats-header-subs').text
            self.youtuber_views = f"{int(bs.find(id='youtube-stats-header-views').text):,}"
            self.youtuber_country = bs.find(id='youtube-stats-header-country').text
            self.youtuber_channel_type = bs.find(id='youtube-stats-header-channeltype').text
            self.youtuber_channel_created = bs.find_all(class_='YouTubeUserTopInfo')[5].text.replace('User Created', '')
            self.youtuber_social_media = " ".join([link['href'] for link in bs.find_all(class_='core-button') if 'https' in link['href']])

            culomn_2_raw = bs.find(id='socialblade-user-content')
            youtuber_content = culomn_2_raw.find_all('div')

            contents = {'total_grade': 2, 'subscriber_rank': 13, 'video_views_rank': 20, 'country_rank': 27, 'channel_type_rank': 34}
            for key, value in contents.items():
                setattr(self, key, youtuber_content[value].text.replace(' ', '').replace('\n', ''))

            try:
                self.subscribers_for_last_30_days = youtuber_content[42].p.text.replace(youtuber_content[42].sup.text, '').replace(' ', '').replace('\n', '')
                __subscriber_for_30_days_raw = youtuber_content[42].sup.text.replace(' ', '').replace('\n', '')
                self.subscribers_for_last_30_days_progress = "+" + __subscriber_for_30_days_raw \
                    if "up" in str(youtuber_content[42].sup.span.i['class']) else "-" + __subscriber_for_30_days_raw
            except AttributeError:
                self.subscribers_for_last_30_days = '---'
                self.subscribers_for_last_30_days_progress = '---'

            self.video_views_for_the_last_30_days = youtuber_content[44].p.text.replace(youtuber_content[44].sup.text, '').replace(' ', '').replace('\n', '')
            __view_for_30_days_raw = youtuber_content[44].sup.text.replace(' ', '').replace('\n', '')
            self.video_views_for_the_last_30_days_progress = "+" + __view_for_30_days_raw \
                if "up" in str(youtuber_content[44].sup.span.i['class']) else "-" + __view_for_30_days_raw

            self.estimated_monthly_earnings = youtuber_content[43].p.text.replace(' ', '').replace('\n', '').replace('\xa0-\xa0', '-')
            self.estimated_yearly_earnings = youtuber_content[47].p.text.replace(' ', '').replace('\n', '').replace('\xa0-\xa0', '-')

            self.youtuber_info = {key: getattr(self, key) for key in list(self.all_youtuber_info.keys())[2:]}

            self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            __set_in_db = self.youtuber_info.copy()
            __set_in_db.update(data_update=self.now)

            try:
                self.insert(table='youtube', rows=[__set_in_db])
            except sqlite3.IntegrityError:
                yn = __set_in_db.pop('youtuber_username')
                self.update(table={'youtube': __set_in_db}, where=f"where youtuber_username = '{yn}'")

            return self.youtuber_info
        else:
            return f"SOMTHING WENT WRONG IN SEND REQUESTE. STATUS CODE: {self.get_youtuber.status_code}\ntry offline mod"

    def update_db(self, func, name=None, pk=None, log=True, add_list=None):
        if add_list:
            for name in add_list:
                func(name)
                print(f'{name} added!')
            return
        table_pk = self.select(table=name, column=pk)
        start = datetime.now()
        for _, table in enumerate(table_pk):
            try:
                updated = func(table[0], offline=False)
                print(table[0], 'updated!')
            except:
                continue
        if not log:
            print("Update successfully!")
            return
        end = datetime.now()
        time_ = str(end - start)
        times = datetime.strptime(time_, "%H:%M:%S.%f")
        print(f'\n{_ + 1} update in {times.strftime("%S Sec (%H:%M:%S)")}')

    def create_csv_file(self, list_of_username: list = None):
        if not os.path.exists('csv-files'):
            os.mkdir('csv-files')

        if list_of_username:
            self.update_db(self.youtube, add_list=list_of_username)
            _list_of_username = [f"'{key}'" for key in list_of_username]
            db_res = self.select(table='youtube', where=f'REPLACE(youtuber_username, "@", "") IN ({", ".join(_list_of_username)})')
            listable = [list(k) for k in db_res]
            df = pd.DataFrame(listable, columns=list(self.table['youtube'].keys()))
            hash_name = str(uuid.uuid4()) + '.csv'
            df.to_csv(f'csv-files/{hash_name}')
            return hash_name
        __yt_info = {key: [value] for key, value in self.youtuber_info.items()}
        __csv_addres = f"csv-files/{self.youtuber_info.get('youtuber_username').replace('@', '')}.csv"
        df = pd.DataFrame(__yt_info)
        df.to_csv(__csv_addres)

    def create_xlsc_file(self, list_of_username: list = None):
        """
        :param list_of_username: without at-sign(@)
        """
        if not os.path.exists('xlsx-files'):
            os.makedirs('xlsx-files')

        if list_of_username:
            self.update_db(self.youtube, add_list=list_of_username)
            _list_of_username = [f"'{key}'" for key in list_of_username]
            db_res = self.select(table='youtube', where=f'REPLACE(youtuber_username, "@", "") IN ({", ".join(_list_of_username)})')
            listable = [list(k) for k in db_res]
            df = pd.DataFrame(listable, columns=list(self.table['youtube'].keys()))
            hash_name = str(uuid.uuid4()) + '.xlsx'
            df.to_excel(f'xlsx-files/{hash_name}')
            return hash_name

        __yt_keys = [key for key in self.youtuber_info.keys()]
        __yt_values = [value for value in self.youtuber_info.values()]
        __xlxs_addres = f"xlsx-files/{self.youtuber_info.get('youtuber_username').replace('@', '')}.xlsx"
        df = pd.DataFrame([__yt_values], index=['youtuber'], columns=[__yt_keys])
        df.to_excel(__xlxs_addres)


# info = GetSocialInfo()
# g = info.youtube('mehran mk')
# print(g)
# info.update_db('youtube', 'youtuber_username', info.youtube)
# info.create_xlsc_file(['dream', 'pikaso', 'kinxron'])
# print(info.youtuber_name)
# print(info.youtuber_username)
# print(info.youtuber_banner)
# print(info.youtuber_avatar)
# print(info.youtuber_uploads)
# print(info.youtuber_subscribers)
# print(info.youtuber_views)
# print(info.youtuber_country)
# print(info.youtuber_channel_type)
# print(info.youtuber_channel_created)
