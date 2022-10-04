# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
agediff = 90 - int(age)
#Write your code below this line 👇

month = agediff * 12
day = agediff * 365
week = agediff * 52

print("You have " + str(day) +" days, " + str(week)+" weeks, and "+ str(month)+" months left.")


