import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib.request import urlopen

values = """
  {
    "pwd": "admin",
    "remember": 1
  }
"""
values = values.encode('utf-8')
request = urlopen ('https://10.1.11.227:8080/api/4/auth/login', values).read()
print (request)



values2 = """
  {
    newPass: "admin2",
    oldPass: "admin"
  }
"""
values2 = values2.encode('utf-8')
html = urlopen ('https://10.1.11.227:8080/api/4/auth/change', values2).read()
print (html)