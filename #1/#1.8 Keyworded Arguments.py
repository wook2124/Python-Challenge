# Positional argument와 다르게 "="로 명명해주는 것
def plus(a, b):
  return(a + b)
  print("lalalalalalala")

result = plus(b=10, a=12)

print(result)


# f(format)을 붙이기 전
def say_hello(name, age):
  return "Hello {name} you are {age} years old, right?"

Hello = say_hello("Young Wook", 27)
print(Hello)

# f(format)을 붙이니 {}가 argumentation(인자화)됨
def say_hello(name, age):
  return f"Hello {name} you are {age} years old, right?"

Hello = say_hello("Young Wook", 27)
print(Hello)

# Keyworded argument 활용
def say_hello(name, age):
  return f"Hello {name} you are {age} years old, right?"

Hello = say_hello(age=27, name="Young Wook")
print(Hello)

# Argument를 좀 더 추가해서 연습
def say_hello(name, age, are_from, fav_food):
  return f"Hello {name} you are {age} years old, right? And you are from {are_from}, also you like {fav_food}!"

Hello = say_hello(age=27, name="Young Wook", fav_food="Pizza", are_from="Korea")
print(Hello)