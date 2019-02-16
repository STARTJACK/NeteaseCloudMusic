import base64
from Crypto.Cipher import AES


class AESCipher:

    def __init__(self, key):
        self.key = key[0:16]  # 只截取16位
        self.iv = "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"  # 16位字符，用来填充缺失内容，可固定值也可随机字符串，具体选择看需求。

    def __pad(self, text):
        """填充方式，加密内容必须为16字节的倍数，若不足则使用self.iv进行填充"""
        text_length = len(text)
        pad = AES.block_size - (text_length % AES.block_size)
        return text + pad * chr(pad)

    def __unpad(self, text):
        pad = ord(text[-1])
        return text[:-pad]

    def encrypt(self, raw):
        """加密"""
        raw = self.__pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        """解密"""
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.__unpad(cipher.decrypt(enc).decode("utf-8"))


if __name__ == '__main__':
    e = AESCipher('8ymWLWJzYA1MvLF8')
    secret_data = "6860795567181583<REQDATA></REQDATA>242BB99CE386F2B1EA19CCCF606D2234"
    enc_str = e.encrypt(secret_data)
    print('enc_str: ' + enc_str.decode())
    dec_str = e.decrypt(enc_str)
    print('dec str: ' + dec_str)
