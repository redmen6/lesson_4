from requests import get
import xmltodict
import datetime


def currency_rates(cod_val):
    cod_val = cod_val.upper()
    res_out = dict()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    res_content = xmltodict.parse(response.text)
    for item in res_content['ValCurs']['Valute']:
        if item['CharCode'] == cod_val:
            res_out['Name'] = item['Name']
            res_out['Value'] = item['Value']
            date = datetime.datetime.strptime(res_content['ValCurs']['@Date'], "%d.%m.%Y")
            res_out['date'] = date.strftime('%Y.%m.%d')
    if 'Value' in res_out:
        return res_out
    else:
        return None
