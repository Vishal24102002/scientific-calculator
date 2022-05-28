from play import speak
from raj import calcu

ch='yes'
while ch=='yes':
    speak("welcome to the scientific calculator")
    speak("how to begin your calculation ")
    print("how to begin your calculation ->")
    speak("type-1 for voice operating ")
    print("type-1 for voice operating ")
    speak("type-2 for keyboard typing")
    print("type-2 for keyboard typing ")
    speak("enter your choice from above mentioned options")
    choice=int(input("enter your choice from above list"))
    speak("you have typed",choice)
    if (choice == 1):
        speak("enter the operation to be calculated")
        get_audio()
        operation = input("enter the operation to be calculated")

        if 'multiplication' in operation:
            speak("you have chossen multiplication")
            a = int(input("enter numbers to be calculated"))
            b = int(input("enter your value"))
            c = a*b
            sin()
            print("the soution of the numbers is :", c)
            speak(c)
        elif 'addition' in operation:
            speak("you have chossen addition as an operation")
            e = int(input("enter numbers to be calculated"))
            g= int(input("enter your value"))
            f = e+g
            sin()
            print("the solution of the numbers is :", f)
            speak(f)
        elif 'division' in operation:
            speak("you have chossen division as an operation")
            h= int(input("enter numbers to be calculated"))
            i = int(input("enter your value"))
            d = h/i
            sin()
            print("the solution of the numbers is :", d)
            speak(d)
        elif 'subtract' in operation:
            speak("you have chossen subtraction as an operation")
            h= int(input("enter numbers to be calculated"))
            i = int(input("enter your value"))
            d=h-i
            sin()
            print("the solution of the numbers is :",d)
        elif 'tan' in operation:
            speak("do you want to calculate tan theta")
            d =
            speak("")
            print("the solution of the numbers is :", d)
        else:
            print("enter a valid choice")
    elif choice == 2:
        speak("thanks for using keyboard as input unit")
        calcu()
    else:
        speak("enter a correct choice from the above options")
        print("enter a correct choice from the above options")
else:
    speak("thanks for using the calculator")
speak("do you want to continue")
ch=input("do you want to continue ->")

