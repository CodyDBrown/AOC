def DoubleDigits(number):
    for i in range(5):
        if number[i] == number[i+1]:
            return True
    return False

def NeverDecrease(number):
    for i in range(5):
        if number[i+1] < number[i]:
            return False
    return True

def partOneMain():
    test = range(256310, 732736)
    passwordCount = 0
    for t in test:
        t = str(t)
        if DoubleDigits(t):
            if NeverDecrease(t):
                passwordCount += 1
                
    print("There are", passwordCount, "passwords that work")



def CountCheck(number):
    for idx in range(len(number)):
        # Can't believe I forgot about the count function!!!!
        if number.count(number[idx]) == 2:
            return True
       
            

def partTwoMain():
    test = range(256310, 732736)
    #test = ["112233", "123444", "111122", "232213", "222334", "223450", "111122", "023339", "122222"]
    passwordCount = 0
    for t in test:
        t = str(t)
        #print("Checking number", t)
        global M
        M = 0
        if NeverDecrease(t):
            if CountCheck(t):
                passwordCount += 1    
        
                
    print("There are", passwordCount, "passwords that work in part two")    

if __name__ == "__main__":
    partOneMain()
    partTwoMain()