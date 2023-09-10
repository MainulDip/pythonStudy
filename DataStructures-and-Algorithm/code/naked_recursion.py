import time
from datetime import datetime

def naked_recursion(c):
    if c == 0:
        return 0
    c -= 1
    # time.sleep(1)
    val1 = naked_recursion(c)
    
    # print(val1, c, "time: ", datetime.now().strftime("%H:%M:%S"))
    print(val1, c)

    return val1 + c

# a, b = naked_recursion(7)

print(naked_recursion(4))

