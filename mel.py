lines = ["Hello there mel ",
         "I just wanna tell you that",
         "I love you to the moon and back and u are everything i got "]

from time import sleep
import sys

for line in lines:
    for c in line:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.1)
    print('')