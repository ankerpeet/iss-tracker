import requests

def get_data():
    r = requests.get('https://isstracker.spaceflight.esa.int/tledata.txt', auth=('user', 'pass'))
    print(r.text)

get_data()