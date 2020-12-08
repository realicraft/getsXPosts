# Ver 1.2

import math
import sys

#Get primes
def getPrimes(num):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541]
    for i in primes:
        if num % i == 0:
            num /= i
            num = int(num)
    currNumber = 549
    isPrime = True
    while currNumber <= num:
        if currNumber % 2 == 0 or currNumber % 3 == 0 or currNumber % 5 == 0 or currNumber % 7 == 0 or currNumber % 11 == 0 or currNumber % 13 == 0 or currNumber % 15 == 0 or currNumber % 17 == 0:
            currNumber += 1
            continue
        isPrime = True
        for i in range(2, math.ceil(math.sqrt(currNumber)) + 1):
            if (i % 2 == 0 and i > 2) or (i % 3 == 0 and i > 3) or (i % 5 == 0 and i > 5) or (i % 7 == 0 and i > 7) or (i % 11 == 0 and i > 11) or (i % 13 == 0 and i > 13) or (i % 17 == 0 and i > 17) or (i % 19 == 0 and i > 19):
                continue
            if currNumber % i == 0:
                #print("tried " + str(i) + " on " + str(currNumber) + ", false")
                isPrime = False
                break
            else:
                #print("tried " + str(i) + " on " + str(currNumber) + ", true")
                pass
        if isPrime:
            primes.append(currNumber)
        currNumber += 1
    return primes
            

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
#print(str(number))

#Warn for high numbers
if number > 1000000:
    print("This number, " + str(number) + ", is large. It might take a while to convert it. Or it might not. Depends on the factors.\nIt's conversion might also be large.")

neededPrimes = getPrimes(number)

#Get prime factors
number2 = number
curPrime = 0
primeFact = []
for x in range(len(neededPrimes) + 1):
    primeFact.append(0)
while number2 >= 2:
    testNum = number2 / neededPrimes[curPrime]
    #print(str(number2) + " divided by " + str(neededPrimes[curPrime]) +" is " + str(testNum))
    if int(testNum) == float(testNum):
        primeFact[curPrime] = primeFact[curPrime] + 1
        number2 = int(testNum)
    else:
        curPrime += 1
#print(primeFact)

#Get highest prime factor
highestFact = len(neededPrimes)
while True:
    if primeFact[highestFact] == 0:
        highestFact -= 1
    else:
        break
#print(highestFact)
primeFact = primeFact[0:highestFact+1]
#print(primeFact)
#print(primeFact[highestFact])

#Convert to notation
primeCount = highestFact
output = ""
while primeCount >= 0:
    output += hardcodedOut[primeFact[primeCount]]
    primeCount -= 1
print(output)
