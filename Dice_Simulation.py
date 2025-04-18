import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice=[]
t1=0
t2=0
t3=0
t4=0
t5=0
t6=0
num_of_dice=int(input("Enter number of dice: "))
for die in range(num_of_dice):
    dice.append(random.randint(1,6))


for cheak in dice:
    if(cheak==1):
        t1+=1
    elif(cheak==2):
        t2+=1
    elif(cheak==3):
        t3+=1
    elif(cheak==4):
        t4+=1
    elif(cheak==5):
        t5+=1
    elif(cheak==6):
        t6+=1

for die in range(5):
    for line in dice:
        print(dice_art.get(line)[die], end=" ")
    print()


print(f"The Probability of getting 1 is {t1/num_of_dice}")
print(f"The Probability of getting 2 is {t2/num_of_dice}")
print(f"The Probability of getting 3 is {t3/num_of_dice}")
print(f"The Probability of getting 4 is {t4/num_of_dice}")
print(f"The Probability of getting 5 is {t5/num_of_dice}")
print(f"The Probability of getting 6 is {t6/num_of_dice}")

