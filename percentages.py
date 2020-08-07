import os
import time
os.system('clear')

portfolio = float(input("Portfolio? "))
print()

print("75%%: %d" %(0.75 * portfolio))
print("25%%: %d" %(0.25 * portfolio))
print("(0.9)75%%: %d" %(0.75 * .9 * portfolio))
print("(0.1)75%%: %d" %(0.75 * .1 * portfolio))
print("(0.75)75%%: %d" %(0.75 * .75 * portfolio))
print("(0.25)75%%: %d" %(0.75 * .25 * portfolio))
print("10%%: %d" %(0.1 * portfolio))
print("5%%: %d" %(0.05 * portfolio))
print("(1.25)75%%: %d" %(1.25 * 0.75 * portfolio))
print("(0.25)75%%: %d" %(0.25 * portfolio))
print("(0.25)75%% + 100%%: %d" %(0.25 * 0.75 * portfolio + portfolio))
print()