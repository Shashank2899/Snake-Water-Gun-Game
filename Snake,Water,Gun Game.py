import random
count=1
Win=0
Equal=0
loose=0
while count<=10:
    user=input('Snake or Water or Gun:')
    if user=='Gun':
        lst=["Snake","Water","Gun"]
        choice=random.choice(lst)
        print('Computer:',choice)
        if choice=='Snake':
            Win=Win+1
            print('You Won')
        elif choice=='Water':
            loose =loose+1    
            print('You Loose ')
        else:
            Equal=Equal+1
            print('Tie')
    elif user=='Water':
        lst=["Snake","Water","Gun"]
        choice=random.choice(lst)
        print('Computer:',choice)
        if choice=='Snake':
            loose=loose+1
            print('You Loose')
        elif choice=='Gun':
            Win=Win+1
            print('You Win')
        else:
            Equal=Equal+1
            print('Tie')
    else:
        lst=["Snake","Water","Gun"]
        choice=random.choice(lst)
        print('Computer:',choice)
        if choice=='Water':
            Win=Win+1
            print('You Win')
        elif choice=='Gun':
            loose=loose+1
            print('You Loose')
        else:
            Equal=Equal+1
            print('Tie')
    count=count+1 
print('Game Over')    
print('The number of times you Won:',Win)  
print('The number of times Computer win :',loose)
if Win>loose:
    print('Congratulation Finally YOU Won')
elif loose>Win:
    print('Sorry You Finally Loose ')
else:
    print('Game Tie')
       

