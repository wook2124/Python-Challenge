# 프로그램은 return이 실행되지 않는 print의 값을 None으로 봄
def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return(a + b)

p_result = p_plus(10, 3)
r_result = r_plus(10, 3)

print(p_result, r_result)


# Python에서 return이 실행되고 나면 그대로 행동이 끝남
# 때문에 print는 실행되지 않음
def r_plus(a, b):
  return(a + b)
  print("lalalalalalala")

r_result = r_plus(10, 3)

print(r_result)


# 프로그램은 print를 신경쓰지 않고 return을 신경씀