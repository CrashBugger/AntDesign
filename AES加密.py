from Crypto.Cipher import AES

if __name__ == '__main__':
    # 初始化aes时传入密钥，加密模式，和iv
    aes1 = AES.new(b'63f09k56nv2b10cf', AES.MODE_CBC, b'01pv928nv2i5ss68')
    message = b"1234567890123456"
    # 加密操作
    ciper_text = aes1.encrypt(message)
    # 解密操作,传入相同密钥加密模式和iv
    aes2 = AES.new(b"63f09k56nv2b10cf", AES.MODE_CBC, b'01pv928nv2i5ss68')
    # 解密
    plain_text = aes2.decrypt(bytes(ciper_text))
    print(ciper_text)
    print(plain_text)
    # javascript混淆可以使用eval(atob("..."))
    #执行eval可以拿到源代码
    #atob可以解码base64
    #AAEncode和JJEncode删除最后一组括号
