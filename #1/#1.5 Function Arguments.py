# argument(인자)
def say_hello(who):
    print("Hello", who)

say_hello("Young Wook")


# default value(기본값)을 설정할 수도 있음
def plus(a, b):
    print(a + b)

def minus(a, b=10):
    print(a - b)

plus(10, 3)
minus(3)


# argument(인자)에 default value(기본값)을 설정해도
# 그에 맞는 input이 있으면 기본값은 무시됨
def say_hello(name="Anonymous"):
    print("Hello", name)

say_hello()
say_hello("Young Wook")
