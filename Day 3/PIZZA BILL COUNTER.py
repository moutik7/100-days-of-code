# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total = 0

if size == "S":
    if add_pepperoni == "Y":
       total = 17
    elif add_pepperoni == "N":
       total = 15
elif size == "M":
    if add_pepperoni == "Y":
       total = 23
    elif add_pepperoni == "N":
       total = 20
elif size == "L":
    if add_pepperoni == "Y":
       total = 28
    elif add_pepperoni == "N":
       total = 25

if extra_cheese == "Y":
 total = int(total) + 1

print(f"Your final bill is {total}") 