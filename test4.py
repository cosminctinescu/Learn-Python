import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from urllib.request import urlopen

values = """
  {

    "pwd": "admin"
  }
"""
values = values.encode('utf-8')
request = urlopen('https://10.1.11.227:8080/api/4/auth/check', values).read()
print(request)
