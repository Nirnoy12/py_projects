print(" WELCOME TO MY GAME ")
playing = input("\nDO YOU WANT TO PLAY THE GAME? ")
playing = playing.lower()

if playing == "yes":
    print("Okay! Let's play ")
    score = 0
else:
    print ("Bye")
    quit()
    
    
answer_1 = input("WHAT DOES CPU STAND FOR? ")
answer_1 = answer_1.lower()
if answer_1 =="central processing unit":
    print ("correct")
    score +=1
else:
    print("incorrect")
        
print("\nNext Question")
        
answer_2 = input("WHAT DOES GPU STAND FOR? ")
answer_2 = answer_2.lower()
if answer_2 =="graphics processing unit":
    print ("correct")
    score +=1
else:
    print("incorrect")
        
print("\nNext Question")
        
answer_3 = input("WHAT DOES RAM STAND FOR? ")
answer_3 = answer_3.lower()
if answer_3 =="random access memory":
    print ("correct")
    score +=1
else:
    print("incorrect")
        
print("\nFinal Question")
        
answer_4 = input("WHAT DOES PSU STAND FOR? ")
answer_4 = answer_4.lower()
if answer_4 =="power supply":
    print ("correct")
    score +=1
else:
    print("incorrect")
    
print("Your Score is "+ str(score)+" out of 4 and you got "+ str(score)+" Questions Correct")