# Select  Six Lucky Number!
import random

# insert loop number
input_num = int(input("Insert Loop number : "))
 
# Error Correction
if input_num > 100:
    print("input below integer 100")
       
elif input_num < 1:
    print("input over integer zero")

else: 
    set_numbers = 6

# make a list of lucky numbers
    lucky_list =[]

    for i in range(input_num):
        lucky = random.sample(range(1, 46), set_numbers)
        lucky_list.append(lucky)
        print(lucky_list[i])

