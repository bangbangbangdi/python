# coding=utf-8
import os
import qianfan

def gpt(question):

    with open("QIANFAN_ACCESS_KEY",'r',encoding='utf-8') as f:
        QIANFAN_ACCESS_KEY = f.read()
    with open("QIANFAN_SECRET_KEY","r",encoding="utf-8") as f:
        QIANFAN_SECRET_KEY = f.read()

    os.environ["QIANFAN_ACCESS_KEY"] = QIANFAN_ACCESS_KEY
    os.environ["QIANFAN_SECRET_KEY"] = QIANFAN_SECRET_KEY

    chat_robot = qianfan.ChatCompletion()
    resp = chat_robot.do(
        messages=[{
            "role":"user",
            "content":question
        }]
    )
    return resp.body['result']

print(gpt('你好'))