import schedule
import requests
import time

url_for_checks = ['https://admin.ggkala.shop', 'https://netherlands.ggkala.shop']

api_addres_for_report = 'https://check.ggkala.shop/report_connection_problem'
report_problem_text = "🔴 The Server Is Probably Blocked"
check_every__min = 5

def report(text):
    return requests.post(api_addres_for_report, data={'message': text})


def check():
    for url in url_for_checks:
        try:
            status = requests.get(url, timeout=5)

            if status.status_code == 200:

                get_json = status.json()
                if get_json['success']:
                    print('OK')
                    continue

                return report(f'{report_problem_text}\nstatus code: {status.status_code}\nreason: {status.reason}')

        except Exception as e:
            report(f'{report_problem_text}\nSERVER: {url}\n'
                      f'error type: {type(e).__name__}\nerror: {e}')

schedule.every(check_every__min).minutes.do(check)

while True:
    schedule.run_pending()
    time.sleep(1)
