# https://docs.python.org/3/library/


# This is "list" - [] (JavaScript - "Array")
# Mutable
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]

# sequence(s)에 대한 여러가지 method가 있음
days.append("Sat", "Sun")
days.reverse()

print(days in "Mon")

print(len(days))


# And this is "tuple" - ()
# Immutable
days = ("Mon", "Tue", "Wed", "Thur", "Fri")

print(type(days))


# And this is "dictionary" - {}
# Mutable
wook = {
    "name": "Wook",
    "age": 27,
    "korean": True,
    "fav_food": ["Kimchi", "Ramen"]
}

print(wook)

# 이렇게 바로 추가할 수 있음
wook["handsome"] = True

print(wook)

# 사전처럼 특정적인 부분만 출력할 수 있음
print(wook["fav_food"])