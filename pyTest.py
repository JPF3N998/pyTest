import random
import os

def printRandoms():
		Sum = 0
		for i in range(0,100):
			newNum = random.randint(0,100)
			print("Iteration "+ str(i+1)+" >>> "+ str(newNum))
			Sum += newNum
		print("Total sum is "+ str(Sum))
		exit(0)
		
printRandoms()
""""
cwd = os.path.dirname(os.path.abspath(__file__))+str(chr(92)*2)
cwd +=("prologSample.pl")

testFile = open(cwd,'r')
contents = testFile.readlines()
testFile.close()

print("Looking @ " + cwd)


def getTags(contents):
	print(contents)
	print(len(contents))
	tags = []
	for i in range(0,len(contents)):
		switch = 1
		tagName = ""
		for j in range(0,len(contents[i])):
			if(contents[i][j]=='('):
					switch=0
			if(switch == 1):
				print("Adding " + contents[i][j])
				tagName += contents[i][j]
			else:
				if(contents[i][j]==')'):
					print("Adding " + tagName+ " to list")
					tags += [tagName]
					break;
	return tags

print(getTags(contents))

"""