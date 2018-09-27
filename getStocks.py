import requests
import json


symb = ['aapl', 'fb', 'ge', 'mu', 'bac', 'qqq', 'jd', 'chk', 'm', 'baba', 'intc', 'tvix', 'nxpi', 'csco', 'tqqq', 'nvda', 'uslv', 'bili', 'crzo']

full = {"db":[]}

for s in symb:
    URL = "https://api.iextrading.com/1.0/stock/"+s+"/chart/5y"
    req = requests.get(url = URL)
    data = req.json()
    newdict = {s:data}
    full["db"].append(newdict)


with open('stocks.json', 'w') as sf:
    json.dump(full, sf)
