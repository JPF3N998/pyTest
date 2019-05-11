from pyswip import Prolog
import random

prolog = Prolog()

prolog.assertz("ingredient(strawberries)")

print(str(prolog.query("ingredient(apples)")))

def printRandoms():
		Sum = 0
		for i in range(0,100):
			newNum = random.randint(0,100)
			print("Iteration "+ str(i+1)+" >>> "+ str(newNum))
			Sum += newNum
		print("Total sum is "+ str(Sum))
		exit(0)

printRandoms()

