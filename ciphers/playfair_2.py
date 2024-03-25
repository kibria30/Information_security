def generateList(key):
    Matrix = []
    list = []
    for x in key:
        if x not in list:
            list.append(x)

    for x in alphas:
        if x not in list:
            list.append(x)

    return list

def generateMatrix(key):
    Matrix = []
    list = generateList(key)
    print(list)

    while list != []:
        Matrix.append(list[:5])
        list = list[5:]

    return Matrix

def search(element, Matrix):
    for i in range(5):
        for j in range(5):
            if(Matrix[i][j] == element):
                return i, j
               
def splitting(text):
    splitedText =[]
    for x in range(0, len(text), 2):
        splitedText.append(text[x] + text[x+1])

    return splitedText

def encrypt(splittedText, Matrix):
    encrypted = []
    for x in splittedText:
        row0, col0 = search(x[0], Matrix)
        row1, col1 = search(x[1], Matrix)
        print(type(row0))
        print(row0, col0)
        print(row1, col1)
        if(row0 == row1):
            encrypted.append(Matrix[row0][col0+1])+Matrix[row1][col1+1])
        elif(col0 == col1):
            encrypted.append(Matrix[row0+1][col0]+Matrix[row1+1][col1])

    return encrypted
           
alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

key = "monarchy"
Matrix = generateMatrix(key)
print(Matrix)
splittedText = splitting("st")
print(splittedText)
encrypted = encrypt(splittedText, Matrix)
print(encrypted)