import requests, re
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
response = requests.get('https://www.dmmsee.icu/',headers=header)
list_a = re.findall('<a class="movie-box" href="(.*?)">',response.text)
print(list_a)

for m in list_a:
    response2 = requests.get(m)
    data = re.findall('href="magnet:*"',response2.text)
    print(data)