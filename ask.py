# 您的程序应询问用户的姓名和出生年月，然后用 您自己的名字（例如“ Sanaa”），用户名（例如“ Tom”）和用户的年龄，格式类似： “嗨，亲爱的汤姆，我是萨那。你真的19岁吗？”
# coding=utf-8
# python3写法


def printer(name,age):
    print("Dear", name, "This is NASA.Are you really", age, "year`s old?", )


def askName():
    name = input("what`s your name ?")
    return name


def askAge():
    age = input("How old are you ?")
    return age


if __name__ == '__main__':
    type(askName(), askAge())
