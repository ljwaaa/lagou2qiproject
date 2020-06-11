def func():
    print("这是无参数的打印")


func()


def func1(a):
    print(f"这是有参数的打印:{a}")


func1("有参数a")


def func2(a, b):
    return a + b


print(f"有返回值打印：{func2(3, 2)}")


def func3(a, b):
    return


print(f"无返回值打印：{func3(3, 2)}")
