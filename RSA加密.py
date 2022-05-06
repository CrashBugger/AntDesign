import base64

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

if __name__ == '__main__':
    message = "async"
    # 初始化rsa对象
    rsa = RSA.generate(1024, Random.new().read())
    # 生成私钥
    private_key = rsa.exportKey()
    # 生成公钥
    public_key = rsa.public_key().exportKey()
    # 打印私钥和公钥
    print(private_key.decode("utf-8"))
    print(public_key.decode("utf-8"))
    # 将私钥和公钥存入对应的文件
    with open("private.pem", 'wb') as f:
        f.write(private_key)
    with open("public.pem", 'wb') as f:
        f.write(public_key)
    with open('public.pem', 'r') as f:
        # 从文件中加载公钥
        pub = f.read()
        pubkey = RSA.importKey(pub)
        # 用公钥加密消息原文
        cipher = PKCS1_v1_5.new(pubkey)
        c = base64.b64encode(cipher.encrypt(message.encode("utf-8"))).decode("utf-8")
    with open("private.pem", 'r') as f:
        # 从文件中加载私钥
        pri = f.read()
        prikey = RSA.importKey(pri)
        # 用私钥解密密文
        cipher = PKCS1_v1_5.new(prikey)
        m = cipher.decrypt(base64.b64decode(c), 'error').decode("utf-8")
    print("原文: %s\n消息密文:%s\n 解密结果:%s", (message, c, m))
