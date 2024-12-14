def monty():
    from random import randint
    choice=int(input('Open door 1,2 or 3: '))
    a=randint(1,4)
    if a==choice:
        second_choice=input('Open the door,revealing a car\nDo you want to switch the door(Y/N):')
        second_choice.casefold()
        if second_choice=='y':
            final_choice=int(input('Enter the final choice:'))
            if final_choice==a:
                print('Congrats you won the car')
            else:
                print('Congrats you won a goat')
    else:
        second_choice=input('Opens the door,revealing a goat\nDo you want to switch your door(Y/N):')
        if second_choice=='n':
            final_choice=int(input('Enter your final choice: '))
            if final_choice==a:
                print('Congrats you won a car')
            else:
                print('Congrats you won a goat')
        else:
            print('Congrats you won a goat')
monty()
