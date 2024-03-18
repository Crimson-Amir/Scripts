import pandas as pd
from sqlite_manager import ManageDb

number_range = range(264, 315)

gercli = pd.read_csv('gercl.csv')
new_ids = pd.DataFrame({'id': number_range})
gercli.update(new_ids)

gercli['inbound_id'] = gercli['inbound_id'].replace(2, 9)
gercli['inbound_id'] = gercli['inbound_id'].replace(5, 10)
gercli['inbound_id'] = gercli['inbound_id'].replace(7, 11)


sqlite_manager = ManageDb('Netherlands')

print(gercli)

for index, client in gercli.iterrows():
    data = {
        'id': client['id'],
        'inbound_id': client['inbound_id'],
        'enable': client['enable'],
        'email': client['email'],
        'up': client['up'],
        'down': client['down'],
        'expiry_time': client['expiry_time'],
        'total': client['total'],
        'reset': client['reset']
    }
    print(data['email'])
    sqlite_manager.insert(table='client_traffics', rows=[data])
