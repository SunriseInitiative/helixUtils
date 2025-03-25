class vectors:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
    def generateRangedVectorSet2(self, vectors, range):
        vectorSet = []
        for i in range(range):
            for j in vectors:
                vectorSet.append((j[0] * i, j[1] * i))
        return vectorSet
    def generateRangedVectorSet(self, vectors, range):
        vectorSet = []
        for i in range(range):
            for j in vectors:
                vectorSet.append((j[0] * i, j[1] * i, j[2] * i))
        return vectorSet

def startup():
    print("This is a licsensed HelixInteractive script")