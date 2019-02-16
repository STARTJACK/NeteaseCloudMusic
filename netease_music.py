
import json
import requests
from Crypto.Cipher import AES
import codecs
import base64
from binascii import hexlify
import os


def a(a):
    return hexlify(os.urandom(a))[:16].decode("utf-8")


def b(a, b):
    iv = "0102030405060708"
    pad = 16 - len(a) % 16
    a = a + pad * chr(pad)
    f = AES.new(b, AES.MODE_CBC, iv).encrypt(a)
    f = base64.b64encode(f)  # JS中的AES默认加密后在base64加密
    return f.decode('utf-8')


def c(a, b, c):
    a = a[::-1]
    rs = int(codecs.encode(a.encode('utf-8'), 'hex_codec'), 16)**int(b, 16) % int(c, 16)
    return format(rs, 'x').zfill(256)


# ids=input("歌曲id名：")
ids = '26090160'
i = a(16)
h = {}
d = '{"ids":"[%s]","br":128000,"csrf_token":""}' % ids

g = "0CoJUm6Qyw8W8jud"
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
h['params'] = b(b(d, g), i)
h['encSecKey'] = c(i, e, f)
headers = {
    'Referer': 'https://music.163.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=70f52297b7aa81f2cccc5ad38b5d6ac1,1539961295179; _ntes_nuid=70f52297b7aa81f2cccc5ad38b5d6ac1; __utmc=94650624; __utmz=94650624.1539961296.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_TID=ygGExoiwarhEFAEFFUNpLZHx95GTcT0X; WM_NI=I41QM4WyIT6Oe%2FfaqQuzjf63sc4lhGHHEj4tYrhegvrbKCHCTnCvLx3j%2FZ1AzYySK1n2xK3vdAXTt9lqJFEZw6LiQJUF1W%2B1b5%2B7LaXWw%2BCYIwZLsFW%2Fe7T64rH9tJscVno%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeccf44795b58bb2d921b3b48ab6d55a829b8eabb85c8b979fd9fb488692f786c72af0fea7c3b92a8becffb2d04095a787b5b545a7f1aa82f45bb7a6a687b539b1bdfc8deb4d8c988b8bb7809baea886e67eb2be85a4cb4998b28d97cf74f1b6e1bbb44bba87b7b4ca3baeeeb8acb27ea89f98b5f733b0af86a7c852b5ea848ad442979affb8aa3ba2ebe5d8cf6b9c89b9ccc2538ba996adf24e95f1abd8d73ef8ae88daf742b1bd9a8fee37e2a3; JSESSIONID-WYYY=Iyz2eWVCbrUp1pKXf9XNsd42Ft88Y09TpGa7HNnAgbqPcBqvqkYn%2B76kcFHFMWenqKAGIZScIY%2BU7A%2BZt7lYJP%2FWhxQuKk68fXtWd277NfjmW3HSkTA6jdqqk3Nh%2BrYkGCpwasJdwGKgsqDdhP%2Fhe%2FaYrVaVvo%2B%2B%2FVhn8%2F%5C1%5C9zAduGK%3A1540031698887; __utma=94650624.1394380025.1539961296.1540028107.1540029974.7; __utmb=94650624.9.10.1540029974; playerid=26668656',
}
url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token= '

res = requests.post(url=url, headers=headers, data=h)
print(res.text)
