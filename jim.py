import time
from datetime import datetime
quote = ("hei jeg heter")
run = input(f"Type this sentence: '{quote}' \npress enter to start")

now = datetime.now()
if run != "":
    quit()
print("timer has started")
run = True


while run:
    if input() == quote:
        then = datetime.now()
        print("Seconds used:", (then.second + (then.minute*60))-(now.second + (now.minute*60)))
        quit()
