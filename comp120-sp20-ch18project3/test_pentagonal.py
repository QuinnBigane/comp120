from io import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()

import pentagonal

s = mystdout.getvalue()

sys.stdout = old_stdout

correct_ans = [[1, 5, 12, 22, 35, 51, 70, 92, 117, 145],
    [176, 210, 247, 287, 330, 376, 425, 477, 532, 590],
    [651, 715, 782, 852, 925]]

ans = [[int(str) for str in line.strip().split(" ")] for line in s.split("\n")]

if correct_ans == ans:
    print("Correct")
else:
    print("Incorrect")
    print("You should print out:")
    for row in correct_ans:
        for col in row:
            print(col, end = ' ')
        print()
    print()
    print("You print out:")
    for row in ans:
        for col in row:
            print(col, end = ' ')
        print()
    print()
