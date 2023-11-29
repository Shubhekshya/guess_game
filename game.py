#lets set a hit number
hit = 22
 #lets initailize the no of tries as 3 
count = 1
#using while loop we can take 3 guess to get the number
print("Guess a number between 0-50, you are given 3 chances to hit correct guess")
while (count <= 3):
    guess= int(input("guess a number: "))
    count += 1
    if guess == hit:
        print("Congrtaulation!! correct guess.")
        break
    else:
        print("TRY again")
        if count <= 3 :
            trys = count - 1
            print(trys," try/s finished")
    


