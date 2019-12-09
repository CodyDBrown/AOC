import numpy as np

def readInFile(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    orbits = []
    text = text.split('\n')
    for orbit in text:
        orbits.append(orbit)
    for idx in range(len(orbits)):
        orbits[idx] = orbits[idx].split(')')
    return orbits

def TraceBack(start, orbits):
    branch = [start]
    FLAG = True
    while FLAG:
        for orbit in orbits:
            if branch[-1] == orbit[1]:
                branch.append(orbit[0])
        if branch[-1] == 'COM':
            FLAG = False
    return branch

def LongestList(branches):
    LongBranch = []
    for branch in branches:
        if len(branch) > len(LongBranch):
            LongBranch = branch
    return LongBranch

def OrbitSum(branches):
    global ORBIT_SUM
    # Find the longest branch
    LongestBranch = LongestList(branches)
    ORBIT_SUM += len(LongestBranch)-1
    orbitID = LongestBranch[0]
    print("Removing", orbitID)
    # Remove that orbit from all branches
    for branch in branches:
        if orbitID in branch:
            branch.remove(orbitID)
    return branches
    
    

def partOneMain():
    global ORBIT_SUM
    ORBIT_SUM = 0
    FLAG = True
    orbits = readInFile("test.txt")
    orbits = np.array(orbits)
    branches = []
    primaryObjects = orbits[:,0]
    secondaryObjects = orbits[:,1]
    startingPoints = []
    for secondary in secondaryObjects:
        if secondary not in primaryObjects:
            startingPoints.append(secondary)
    for start in startingPoints:
        branch = TraceBack(start, orbits)
        branches.append(branch)
    
    while FLAG:
        branches = OrbitSum(branches)

        if len(branches[0]) == 0:
            FLAG = False
    print("Answer for part one is:", ORBIT_SUM)
        
    
            
    

def partTwoMain():
    global ORBIT_SUM
    ORBIT_SUM = 0
    orbits = readInFile("input.txt")
    orbits = np.array(orbits)
    branches = []
    primaryObjects = orbits[:,0]
    secondaryObjects = orbits[:,1]
    startingPoints = []
    for secondary in secondaryObjects:
        if secondary not in primaryObjects:
            startingPoints.append(secondary)
    for start in startingPoints:
        branch = TraceBack(start, orbits)
        branches.append(branch)
    
    for branch in branches:
        if branch[0] == "YOU":
            youBranch = branch
        elif branch[0] == "SAN":
            sanBranch = branch
    MyDistanceToCommonNode = set(youBranch).difference(sanBranch)
    SanDistanceToCommonNode =set(sanBranch).difference(youBranch)
    TotalJumps = len(MyDistanceToCommonNode) + len(SanDistanceToCommonNode) - 2
    print("Answer for part two is: ", TotalJumps)
if __name__ == "__main__":
    partOneMain()
    partTwoMain()
