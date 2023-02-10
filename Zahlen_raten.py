import random

def Zahl_erraten(x):
    random_number = random.randrange(1, x)
    print(f"Es wurde eine natürliche Zahl zwischen 1 und {x} generiert.")
    print("Versuche diese Zahl zu erraten!")
    guess = None
    counter = 0
    while guess != random_number:
        guess = int(input("Deine Vermutung ist: "))     
        if guess >= 1 and guess <= x:                    
            if guess < random_number:
                counter+=1
                print(f"Die gesuchte Zahl ist größer als {guess}")
            elif guess > random_number:
                counter+=1
                print(f"Die gesuchte Zahl ist kleiner als {guess}")
            else: 
                counter+=1
                print("Du hast die Zahl herausgefunden!")
                print(f"Es war die {random_number}")
                if counter == 1:
                    print(f"Du hast nur {counter} Versuch gebraucht")
                else: 
                    print(f"Du hast {counter} Versuche gebraucht")  
        else: 
            print("Deine Eingabe war ungültig")     
            print(f"Die Zahl muss zwischen 1 und {x} liegen")  


Zahl_erraten(100)