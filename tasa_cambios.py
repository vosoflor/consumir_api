import requests

r = requests.get('https://rest.coinapi.io/v1/exchangerate/ETH/EUR?apikey=F772D077-2F75-4D0D-8758-345724A1EB74')

print(r.status_code)
print(r.text)