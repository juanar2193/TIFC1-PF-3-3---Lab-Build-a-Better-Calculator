"""
def main():
  print("Hello learners!")

if __name__=="__main__":
  main()
"""
def addmultiplenumbers(numbers):
  total = 0
  for num in numbers:
    total += num
  return total

def multiplymultiplenumbers(numbers):
  result = 1
  for num in numbers:
    result *= num
  return result

def isitaninteger(num):
  return float(num).is_integer()

def isiteven(num):
  return isitaninteger(num) and num % 2 == 0

def main():
  print("Suma [5, 7, 9]:", addmultiplenumbers([5, 7, 9]))
  print("Multiplicación [4, 5, 6, 7]:", multiplymultiplenumbers([4, 5, 6, 7]))
  print("¿6 es par?:", isiteven(6))
  print("¿-3.8 es par?:", isiteven(-3.8))
  print("¿3 es entero?:", isitaninteger(3))
  print("¿7.3 es entero?:", isitaninteger(7.3))

if __name__=="__main__":
  main()