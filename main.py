class Students:
    
    def __init__(self, name, hand, vision, height, attention, compatibility):
        self.name = name
        self.hand = hand
        self.vision = vision
        self.height = height
        self.attention = attention
        self.compatibility = compatibility
        self.busy = False
        self.desk = 5

        if self.vision == '1-2 парты':
            self.desk = 0
        elif self.vision == '1-3 парты':
            self.desk = 1

        if self.attention == "TRUE":
            self.desk -= 1

        if self.height == 'Низкий':
            self.desk = 3
        elif self.height == "Средний":
            self.desk -= 2



def createInfo(file):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.split("\n")
    arr = []

    for i in range(len(text)):
        arr.append(text[i].split(","))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(len(arr[i][j])):
                if arr[i][j][k] == '"':
                    arr[i][j] = arr[i][j] + arr[i][j + 1]
                    arr[i][j] = arr[i][j][1:-1]
    for i in range(len(arr)):
        if len(arr[i]) == 6:
            del arr[i][-3]
    
    return arr
        
        
def createArrStud(arrStud, arrComp):
    names = arrComp[0][1:]
    
    studentComp = []
    for studentIndex, studentName in enumerate(arrComp[1:]):
        studentComp.append([])
        for i, student in enumerate(studentName[1:]):
            if student == "": continue
            studentComp[studentIndex].append({"name":names[i], "code":student})

    out = []
    for i in range(len(arrStud)):
        stud = arrStud[i]
        out.append(Students(stud[0], stud[1], stud[2], stud[3], stud[4], studentComp[i]))
    return out

cabinet = [
    [1, 1], [1, 1], [1, 1],
    [1, 1], [1, 1], [1, 1],
    [1, 1], [1, 1], [1, 1],
    [1, 1], [1, 1], [1, 1],
    [1, 1], [1, 1], [1, 1],
    [0, 0], [0, 0], [1, 1]
]
def seatingArran():
    global out
    for i in range(len(cabinet)):
        for j in range(len(cabinet[i])):
            for k in range(len(out)):
                if cabinet[i][j] != 1:
                    continue
                else:
                    if out[k].vision == "1 парта средний ряд":
                        if  cabinet[1][0] == 1:
                            cabinet[1][0] = out[k]
                            out[k].busy = True
                        else:
                            cabinet[1][1] = out[k]
                            out[k].busy = True
    
    out = sorted(out, key=lambda student: student.desk)                    
    for i in range(len(cabinet)):
        for j in range(len(cabinet[i])):
            for k in range(len(out)):
                if cabinet[i][j] == 1:
                    if out[k].busy:
                        continue
                    else:
                        if out[k].hand == 'Левая':
                            cabinet[i][0] = out[k]
                            out[k].busy = True
                        elif out[k].hand == 'Правая':
                            cabinet[i][j] = out[k]
                            out[k].busy = True
    for i in range(len(cabinet)):
        for j in range(len(cabinet[i])):
            for k in range(len(out)):
                if cabinet[i][j] == 1:
                    if out[k].busy:
                        continue
                    else:
                        if out[k].hand == 'Левая':
                            cabinet[i][0] = out[k]
                            out[k].busy = True
                        elif out[k].hand == 'Правая':
                            cabinet[i][j] = out[k]
                            out[k].busy = True
    return cabinet

def createCVS():
   with open("result.csv", 'w', encoding='utf-8') as file:
        outData = "Место,Имя"
        for i, stud in enumerate(result):
            if stud == 1 or stud == 0: continue
            if i == 34: i = 30
            if i == 35: i = 31
            outData += f"\n{i+1},{stud.name}"
        file.write(outData)

arrStud = createInfo("info.csv")
arrComp = createInfo("Comp.csv")
out = createArrStud(arrStud, arrComp)
cabinet = seatingArran()

result = []
for i in cabinet:
    for j in i:
        result.append(j)
createCVS()