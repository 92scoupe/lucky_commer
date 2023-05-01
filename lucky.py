# Select  Six Lucky Number!
import random

input_num = int(input("Insert Loop number : "))

# Set number
set_numbers = 6

# Choose six numbers in 45.
lucky_list =[]

for i in range(input_num):
    lucky = random.sample(range(1, 46), set_numbers)
    lucky_list.append(lucky)
    print(lucky_list[i])

