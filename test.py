import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib.request import urlopen
response_body = urlopen("https://10.1.11.227:8080/api/4/apiVer").read()
print(response_body)



