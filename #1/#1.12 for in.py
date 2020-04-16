# for문
# x라는 변수는 for문이 실행되면서 만들어짐
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for x in days:
  print(x)

for x in [1, 2, 3, 4, 5]:
  print(x)


# for loop 중단
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for x in days:
  if x == "Wed":
    break
  else:
    print(x)


# Python에선 str도 배열임
# str, tuple or list를 순차적으로 나타냄
for x in "Young Wook":
  print(x)