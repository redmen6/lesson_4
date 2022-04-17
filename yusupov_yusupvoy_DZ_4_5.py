import utils
from sys import argv

codeval = argv
# codeval = input('код валюты: ')
if len(codeval) == 1 or len(codeval) > 2:
    print('неправильный параметр кода валюты')
else:
    print(utils.currency_rates(codeval[1]))
