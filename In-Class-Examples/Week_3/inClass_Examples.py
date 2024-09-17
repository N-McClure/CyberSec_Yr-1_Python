intOne = int(input("Enter a number: "))
if intOne % 5 == 0:
    print("HiFive!")
elif intOne % 2 == 0:
    print("HiEven!")
else:
    print("HiNobody!")

print()

num = float(input("Enter a float number: "))
if num > 0:
    sq = num ** 2
    cu = num ** 3
    print("Num Squared = ", sq)
    print("Num Cubed = ", cu)

#Write a program to calculate the total payments of movie
#tickets. One ticket is $7.50. If you buy 10 or more, you get
#a 2% discount. If you are a VIP, you get another 10%
#discount. If it is weekend, you get another 5% discount.

ticketsNum = int(input("enter the number of tickets you want: "))
uVIP = input("Are you VIP? (y/n): ")
weekend = input("Is it the weekend? (y/n): ")

# If statements:
if ticketsNum > 10:
    ticketsDiscount = 0.02
else:
    ticketsDiscount = 0.00

if uVIP == 'y':
    vipDiscount = 0.10
elif uVIP == 'n':
    vipDiscount = 0.00
while uVIP != 'y' and uVIP != 'n':
    print("Enter one of the 2 options!")
    uVIP = input("Are you VIP? (y/n): ")

if weekend == 'y':
    weekDiscount = 0.05
elif weekend == 'n':
    weekDiscount = 0.00
while weekend != 'y' and weekend != 'n':
    print("Enter one of the 2 options!")
    weekend = input("Is it the weekend? (y/n): ")

totalDiscount = ticketsDiscount + weekDiscount + vipDiscount
total = (ticketsNum * 7.50) - ((ticketsNum * 7.50) * totalDiscount)
print("Total cost: $", total)
