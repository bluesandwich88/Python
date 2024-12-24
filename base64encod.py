#!/usr/bin/env python
# coding=utf-8
'''
Author: Kevin.Ching
Date: 2024-12-10 18:52:04
LastEditors: KevinCheng
LastEditTime: 2024-12-10 19:10:00
Email: lampard_cheng@hotmail.com
'''
import base64

def encrypt(text):
    encoded_data = base64.b64encode(text.encode('utf-8'))
    encoded_str = encoded_data.decode('utf-8')
    return encoded_str

def decrypt(encoded_str):
    encoded_data = encoded_str.encode('utf-8')
    decoded_data = base64.b64decode(encoded_data)
    decoded_str = decoded_data.decode('utf-8')
    return decoded_str

if __name__ == '__main__':
    do_type = input("1：加密  2：解密")
    do_string = input(f'输入文字')
 
    if do_type == '1':
        do_result = encrypt(do_string)
    elif do_type == '2':
        do_result = decrypt(do_string)

    print(f"结果：{do_result}")
