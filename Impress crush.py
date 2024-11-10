import pyautogui as py
import time

message = "I Love You "
count = 1

time.sleep(2)

for i in range(19):
    py.typewrite(message + " " + str(count))
    py.press("Enter")
    count = count + 1


py.typewrite("I Love You 20")
py.press("Enter")





