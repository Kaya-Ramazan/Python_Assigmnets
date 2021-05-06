num_list = []

for num in range(100):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                num_list.append(num) 
                break
        else:
            num_list.append(num)
            
            
print(num_list)  