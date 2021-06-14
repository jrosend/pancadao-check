import requests
import json

date = '2021-06-12'

while date is not None:
    print(f'Date: {date}')
    response = requests.get(f'https://www.pancadaodepremios.com.br/api/raffle/result/raffle-date/{date}')
    data = response.json()
    date = data['nextResult']
    for result in data['results']:
        for winner in result['winners']:
            if 'ROSENDO' in winner['name']:
                prize = {
                    'date': date,
                    'winner': winner['name'],
                    'city': winner['city'],
                    'state': winner['state'],
                    'prize': result['prizeDescription'],
                    'value': result['netTotal']
                }
                print(prize)
                with open(f'pancadao-{date}.json', 'w') as outfile:
                    json.dump(prize, outfile, indent=4)

