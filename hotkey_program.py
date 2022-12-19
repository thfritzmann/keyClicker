import keyboard
import mouse
import time

keys = []

while True:
    userInput =input(str("Enter the button or combination of buttons you want to repeat -> Hit enter when complete\n"))

    userInput_parsed = userInput.strip()

    yesNoResponse = input("Is "+ userInput_parsed + " the correct hotkey? (y/n)")

    if (yesNoResponse == "y" or yesNoResponse == "Y"):
        inputClicks = input("Enter how many times you want to click:")
        print("Left click to start")
        while True:
            if (mouse.is_pressed("left")):
                for i in range(int(inputClicks)):
                    keyboard.send(userInput_parsed)
                    time.sleep(1.5)
    print("Complete!")
        
