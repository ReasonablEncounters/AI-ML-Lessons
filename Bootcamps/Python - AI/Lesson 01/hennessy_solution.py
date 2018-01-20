import random

count = 0
a = random.randint(1,9)
Answer = input("guess the number from 1-9:")

while Answer != a:    
    elif a == Answer:
        print("wtf nice guess...\n")
        count = count + 1
        break       
    elif a > Answer:
        print("too low noob.\n")
        Answer = int(input("guess the number from 1-9:"))
        count = count + 1
    elif a < Answer:
        print("too high f00l.\n")
        Answer = int(input("guess the number from 1-9:"))
        count = count + 1
		
print('\nTook you this many times to guess:',count, 'the answer is', a )

input()