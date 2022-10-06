# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

merged = name1 + name2
merged = merged.lower()
count_t = int(merged.count("t"))
count_r = int(merged.count("r"))
count_u = int(merged.count("u"))
count_e = int(merged.count("e"))
count_l = int(merged.count("l"))
count_o = int(merged.count("o"))
count_v = int(merged.count("v"))

total_1 = int(count_t+count_u+count_r+count_e)
total_2 = int(count_l+count_o+count_v+count_e)

final = int(str(total_1) + str(total_2))

if final<10 or final>90:
    print(f"Your score is {final}, you go together like coke and mentos.")
elif final>40 and final<50:
    print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}.")