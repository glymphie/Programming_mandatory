

def fibonacciLastDigit(largestFib):
    x = 0
    fibNumbers = [0,1]
    while largestFib >= fibNumbers[-1]:
        fibNumbers.append(fibNumbers[0+x] + fibNumbers[1+x])
        x += 1
    return fibNumbers

def fibonacciAmount(amountFib):
    fibNumbers = [0,1]
    for x in range(amountFib):
        fibNumbers.append(fibNumbers[0+x] + fibNumbers[1+x])
    return fibNumbers

def milesToKm(mile):
    fibo = fibonacciLastDigit(mile) 
    km = 0
    while mile > 0: #Miles gets divided into portions, so when mile = 0 there are no miles left
        for x in range(1,len(fibo)): 
            if fibo[-x] <= mile: #If the fibo number is smaller or equal to miles, it is able to convert to km 
                mile = mile-fibo[-x] #the remainder of miles is saved
                km += fibo[-x+1] #The number in fibo after the number being converted is equal to km
                break  
    return km

def kmToMiles(km): #same as milesToKm, but get the fibo number before the number being converted
    fibo = fibonacciLastDigit(km) 
    mile = 0
    while km > 0: 
        for x in range(1,len(fibo)): 
            if fibo[-x] <= km: 
                km = km-fibo[-x] 
                mile+= fibo[-x-1] 
                break  
    return mile

selectionDicktionary = {
    "1":kmToMiles,
    "2":milesToKm
}
    
def main():
    fiboNumbers = fibonacciAmount(1609)
    goldenRatio = (fiboNumbers[-1]+fiboNumbers[-2])/fiboNumbers[-1]
    print(("This is the golden ratio: %.20f") % goldenRatio)
    
    while True:
        selection = input("\nWhat do you want to convert? \nKM to Miles: 1 \nMiles to KM: 2 \nq to quit\n\n")
        if selection == 'q':
            break
        try:
            convert = int(input("what number do you want to convert? "))
            print("%i gets converted to %i" % (convert,selectionDicktionary[selection](convert)))
        except:
            print("\nPlease enter valid input")
main()