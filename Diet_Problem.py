import random
# Diet Problem -- Question 6 of Final Exam

# Cake -- 3 sugar, 4 fat, 5 enjoyment
# Brownie -- 4 sugar, 5 fat, 6 enjoyment

# MAX 12 sugar, 20 Fat

# We want to find the most enjoyment while not crossing our restraints


Brownie = {"Name": "Brownie", "Sugar": 3, "Fat": 4, "Enjoyment": 6}
Cake = {"Name": "Cake", "Sugar": 4, "Fat": 5, "Enjoyment": 6}
food = [Brownie, Cake]


MAXSUG = 12
MAXFAT = 20
MAXENJOYMENT = 0

countSUG = 0
countFAT = 0
countEnjoyment = 0

final = []
new = []
NumRuns = 0


while NumRuns < 100:
    NumRuns +=1
    while countSUG <= MAXSUG and countFAT <= MAXFAT:
        randomfood = food[random.randint(0, 1)]
        countSUG += randomfood["Sugar"]
        countFAT += randomfood["Fat"]
        countEnjoyment += randomfood["Enjoyment"]

        #reset for next run
        if countSUG > MAXSUG or countFAT > MAXFAT:
            countSUG = 0
            countFAT = 0
            countEnjoyment = 0
            new = []
            break
        else:
            new.append(randomfood.copy())
            if countEnjoyment >= MAXENJOYMENT:
                MAXENJOYMENT = countEnjoyment
                final = new
    
print(final)
    
    
    
    

