import requests
import sys
import re
from lxml import etree

url = 'http://www.123.com'

# # # print(url + a)
response = requests.get(url=url)
# # address_search = re.findall('<(\S*?)[^>]*>.*?|<.*? /> ',response.text,re.S)
def change_find(response):
    address_search = re.sub('<(\S*?)[^>]*>.*?|<.*?/>','',response)
    # address_search1 =re.sub('-->','',address_search)
    address_search2 =re.sub('^\s*|\s*','  ',address_search)
    # address_search4 =re.sub('\s\s','',address_search2)
    address_search3 =re.findall('[^(^\s*|\s*)]',address_search2,re.S)
    # if address_search3 == address_search3:
    #     print('1')
    # else:
    #     print('2')
    # print(type(address_search3))
    # print(address_search3[0])
    return  address_search3
# change_find(response.text)
print(change_find(response.text))
print('"and 1=1 --a')
#
# a =[]
# print(type(a))
# print(type((change_find(response.text))))
