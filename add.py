import random

def add(x, y):
  return x + y

def sayhi(line:str, num:int):
  for i in range(num):
    print(line)

print(add(6, 7))

line = "ur gonna crash out"
num = random.randrange(1,11)

sayhi(line, num)
print("the number was", num)
print("and the line was", line)
