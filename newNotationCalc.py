import math
import sys

firstPrimes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541]
hardcodedOut = ["0", "(0)", "((0))", "((0)0)", "(((0)))", "((0)00)", "((0)(0))", "((0)000)", "(((0)0))", "(((0))0)", "((0)0(0))", "((0)0000)", "((0)((0)))", "((0)00000)", "((0)00(0))", "((0)(0)0)", "((((0))))"]
#print(len(firstPrimes))
number = -1
while number == -1:
    try:
        number = int(input("What's the number you want to convert?"))
    except:
        number = -1
    if number <= 0:
        number = -1
    if int(number) != float(number):
        number = -1
    if number == -1:
        print("You need to input a positive whole number.")
print(str(number))

#Get prime factors
number2 = number
curPrime = 0
primeFact = []
for x in range(100):
    primeFact.append(0)
while number2 >= 2 and curPrime <= 99:
    testNum = number2 / firstPrimes[curPrime]
    print(str(number2) + " divided by " + str(firstPrimes[curPrime]) +" is " + str(testNum))
    if int(testNum) == float(testNum):
        primeFact[curPrime] = primeFact[curPrime] + 1
        number2 = int(testNum)
    else:
        curPrime += 1
print(primeFact)

#Get highest prime factor
highestFact = 99
while True:
    if primeFact[highestFact] == 0:
        highestFact -= 1
    else:
        break
print(highestFact)
primeFact = primeFact[0:highestFact+1]
print(primeFact)
print(primeFact[highestFact])

#Convert to notation
primeCount = highestFact
output = ""
while primeCount >= 0:
    output += hardcodedOut[primeFact[primeCount]]
    primeCount -= 1
print(output)
