Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.
  
num1,num2 = 1,1
list_num = []

while num1 <= 55:
    list_num.append(num1)
    num1, num2 = num2, num1 + num2
print(list_num)    
