import pyautogui, time, random

print("Starting")

_re = ["9b1deb4d-3b7d", "1b9d6bcd-bbfd", "6ec0bd7f-11c0", "9bdd-2b0d7b3dcb6d", "9b5d-ab8dfbbd4bed", "975e-2a8ad9ebae0b"]
def message():
    return random.choice(_re)

try:
    print("Starting Sleep")
    time.sleep(5)
    while True: 
        time.sleep(0.2)
        for r in _re:
            pyautogui.typewrite(message())
            pyautogui.press("tab")

        _ot = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        print("Starting Box filling")
        for o in _ot: 
            pyautogui.press("space")
            pyautogui.press("tab")
        
        # Submit Form
        pyautogui.press("space")
        time.sleep(2)
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.press("tab")

finally: 
    print("Exiting Gracefully . . .")
