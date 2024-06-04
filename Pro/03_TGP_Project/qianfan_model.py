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

    print(resp.body)


# ---------------- 上述代码没办法联系上下文,因此需要再改进一下 ----------------

def chat2():
    os.environ["QIANFAN_AK"] = "PvSiq0beNph79ljuFcCqFPsI"
    os.environ["QIANFAN_SK"] = "ict6qgdnVdu0zs6tNJRexENlt9JCItoY"

    robot = qianfan.ChatCompletion()
    message = []
    while True:
        question = input("Please enter your question: ") or "exit"
        if question == "exit":
            break
        que_dic = {"role": "user", "content": question}
        message.append(que_dic)
        resp = robot.do(
            endpoint="ernie-char-8k",
            messages=message
        )
        print(resp.body['result'])
        message.append({"role": "assistant", "content": resp.body["result"]})


def main():
    # question = '奇诺之旅怎么样的作品?'
    # question = '奇诺是谁?'
    # chat(question)

    chat2()


if __name__ == '__main__':
    main()
