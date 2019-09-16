import requests, re
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
response = requests.get('https://www.dmmsee.icu/SSNI-577',headers=header)
data = re.findall('tr*',response.text)