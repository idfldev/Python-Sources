# adding two numbers without using "+" operator

def add(a, b):
   sum = a + b
   return sum

def add_use_subtraction(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    add = num1 - (-num2)
    return print(add)


def add1(a, b):
    if b == 0:
        return a
    else:
        return add(a ^ b, (a & b) << 1)

def add_use_bitwise(a, b):
   while b != 0:
      sum_without_carry = a ^ b
      carry = (a & b) << 1
      a = sum_without_carry
      b = carry
   return a

def add_use_recursive(a, b):
   if b == 0:
      return a
   else:
      return add_use_recursive(a ^ b, (a & b) << 1)
   
# =================================================================
# print(add_use_bitwise(2, 5))
# print(add1(12, 11))
# print(add_use_recursive(6, 3))


