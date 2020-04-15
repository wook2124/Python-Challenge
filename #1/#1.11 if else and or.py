# if, else는 들여쓰기 주의
def plus(a, b):
  if type(a & b) is int or float :
    return a + b
  else:
    return None

print(plus(12, 10))


# elif는 if의 또 다른 condition임
# elif의 condition까지 만족시키지 못하면 else가 실행됨
def age_check(age):
  print(f"You are {age}")
  if age < 18:
    print("You can't drink!")
  elif age == 18 or 19:
    print("You are new to this!")
  elif age > 19 and age < 25:
    print("You are still kind of young!")
  else:
    print("Enjoy your drink!")

age_check(19)