import random
a=int(input("enter the lower bound:-- "))
b=int(input("enter the upper bound:-- "))
Cnumber=random.randrange(a,b+1)
count=0
flag=True
round=1
while flag:
    print("  ")
    print("Round",round)
    print("  ")
    for i in range(1,4):
        userInput=int(input("Enter Your Number:---"))
        if userInput==Cnumber:
            print("CONGRATS!!\nYour guess number is equal\nyour score is",count+1)
            Cnumber=random.randrange(a,b+1)
            count+=1
            flag=True
            break
        elif Cnumber>userInput:
            print("Have One More Try\nYour guess number is too low")
            flag=False
        else:
            print("Have One More Try\nYour Guess Number is Too High")
            flag=False
    round+=1

print("your final score is",count)
if count==0:
    print("Better Luck Next Time")
elif 1<=count<3:
    print("Good One")
elif 3<=count<6:
    print("Better")
else:
    print("Excellent")