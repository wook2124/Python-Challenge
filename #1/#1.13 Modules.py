# import로 python에 내장되있는 function을 쓸 수 있음
# ceil은 올림값 반환, fabs는 절대값 반환
import math

print(math.ceil(1.2))
print(math.fabs(-1.6))


# math 전체를 가져오는 것이 아니라
# 그 안에서 필요한 method만 import 할 수도 있음
from math import ceil, fsum

print(ceil(1.2))
print(fsum([1, 3, 5, 6, 9]))

# 원할 경우에는 as로 method를 재명명할 수 있음
# 이렇게 하면 fsum으로는 쓸 수 없음
from math import fsum as plus

print(plus([1, 3, 5, 6, 9]))