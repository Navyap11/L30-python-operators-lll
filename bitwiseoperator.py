mark1= int(input("Enter mark 1: "))
mark2= int(input("Enter mark 2: "))
mark3= int(input("Enter mark 3: "))
mark4= int(input("Enter mark 4: "))
mark5= int(input("Enter mark 5: "))

total= mark1+mark2+mark3+mark4+mark5 
avg=total/5

if avg>=91 and avg<=100:
    print("Your grade is A")
elif avg>=81 and avg<91:
    print("Your grade is A-")
elif avg>=71 and avg<81:
    print("Your grade is B")
elif avg>=61 and avg<71:
    print("Your grade is B-")
elif avg>=51 and avg<61:
    print("Your grade is C")
elif avg>=41 and avg<51:
    print("Your grade is C-")
elif avg>=31 and avg<41:
    print("Your grade is D")
elif avg>=21 and avg<31:
    print("Your grade is D-")
elif avg>=11 and avg<21:
    print("Your grade is E")
elif avg>=1 and avg<11:
    print("Your grade is E-")
else:
    print("Your grade is F")