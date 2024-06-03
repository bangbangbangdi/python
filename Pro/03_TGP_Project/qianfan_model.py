# -------------------- 文心一言:接口调用测试 --------------------
import os
import qianfan


# os.environ["QIANFAN_AK"] = "PvSiq0beNph79ljuFcCqFPsI"
# os.environ["QIANFAN_SK"] = "ict6qgdnVdu0zs6tNJRexENlt9JCItoY"
#
# chat = qianfan.ChatCompletion()
# resp = chat.do(
#     endpoint="ernie-char-8k",
#     messages=[{
#         "role": "user",
#         "content": "谁是奇诺"
#     }]
# )
#
# print(resp.body['result'])

# ---------------- 将上述代码简单封装一下 ----------------
def chat(question):
    os.environ["QIANFAN_AK"] = "PvSiq0beNph79ljuFcCqFPsI"
    os.environ["QIANFAN_SK"] = "ict6qgdnVdu0zs6tNJRexENlt9JCItoY"

    robot = qianfan.ChatCompletion()
    resp = robot.do(
        endpoint="ernie-char-8k",
        messages=[{
            "role": "user",
            "content": question
        }]
    )

    print(resp.body['result'])


def main():
    question = '奇诺之旅是什么样的作品?'
    chat(question)


if __name__ == '__main__':
    main()
