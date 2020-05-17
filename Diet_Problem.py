import random
# Diet Problem -- Question 6 of Final Exam

# Cake -- 3 sugar, 4 fat, 5 enjoyment
# Brownie -- 4 sugar, 5 fat, 6 enjoyment

# MAX 12 sugar, 20 Fat

# We want to find the most enjoyment while not crossing our restraints

# Dictionaries holding details of each treat
Brownie = {"Name": "Brownie", "Sugar": 3, "Fat": 4, "Enjoyment": 6}
Cake = {"Name": "Cake", "Sugar": 4, "Fat": 5, "Enjoyment": 6}

# List of possible treats to be randomized
food = [Brownie, Cake]

# Max conditions to be our checks
MAXSUG = 12
MAXFAT = 20
MAXENJOYMENT = 0

# Counts to be compared to our conditional checks
countSUG = 0
countFAT = 0
countEnjoyment = 0

# Temporary holder list and final list
final = []
new = []

# Kind of lazy, but running 100 times as the correct answer will come in that time with randomization
NumRuns = 0


while NumRuns < 100:
    NumRuns +=1
    # Checking that we have not gone over our conditions
    while countSUG <= MAXSUG and countFAT <= MAXFAT:
        # Taking one of our foods randomly
        randomfood = food[random.randint(0, 1)]
        countSUG += randomfood["Sugar"]
        countFAT += randomfood["Fat"]
        countEnjoyment += randomfood["Enjoyment"]

        #reset for next run if broken
        if countSUG > MAXSUG or countFAT > MAXFAT:
            countSUG = 0
            countFAT = 0
            countEnjoyment = 0
            new = []
            break
        # otherwise we are checking if this is a new best
        else:
            new.append(randomfood.copy())
            if countEnjoyment >= MAXENJOYMENT:
                MAXENJOYMENT = countEnjoyment
                final = new
    
print(final)
    
    
    
    

