from BlockGame import Game

def fileToList(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    text = text.split(',')
    numberList = []
    for n in text:
        numberList.append(int(n))
    return numberList

def addMemory(numbers):
    for _ in range(len(numbers)*100):
        numbers.append(0)
    return numbers

def partone():
    code = fileToList("input.txt")
    code = addMemory(code)
    board = Game(code)
    board.main()
    

def parttwo():
    code = fileToList("input2.txt")
    code = addMemory(code)
    board = Game(code)
    board.main()
   

if __name__ == "__main__":
    # partone()
    parttwo()
    