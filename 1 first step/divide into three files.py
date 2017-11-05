def loadList(fileName):
    fin = open(fileName, 'r')
    lines = fin.readlines()
    ans = []
    for line in lines:
        data = line.strip('\n').split('\t')
        ans.append(data)
    return ans
    
def saveList(fileName, dataList): 
    fout = open(fileName, 'w')
    for record in dataList:
        fout.write('\t'.join(record))
        fout.write('\n')
    fout.close()
    
def getColumn(line):
    return line.split('\t')

#def setElem(fileName):
    
    
def getColumns(fileName):
    columns = []
    fin = open(fileName, 'r')
    line1 = fin.readline().strip('\n').split('\t')
    for i in range(0, len(line1)):
        columns.append([line1[i]])
    lines = fin.readlines()    
    for line in lines:
        result = line.strip('\n').split('\t')
        for i in range(0, len(columns)):
            columns[i].append(result[i])
    return columns
           
def ruleSet(fileNameList):
    setElem = [] 
    for file in fileNameList:
        fin = open(file, 'r')
        Rset = set(fin.readline().split(', '))
        setElem.append(Rset)
    return setElem
        
def IndexColumn(column, ruleSet):
    rsetCount = [0]*len(ruleSet)    
    for j in range(0, len(ruleSet)):
        if all( not rElem.isdigit() for rElem in ruleSet[j]):  
            for i in range(0, len(column)):
                if any( rElem in column[i] for rElem in ruleSet[j]):
                    rsetCount[j] = rsetCount[j] + 1
        else: 
            for i in range(0, len(column)):
                if any( rElem == column[i] for rElem in ruleSet[j]):
                    rsetCount[j] = rsetCount[j] + 1            
    if all(ritem == 0 for ritem in rsetCount):
        return None
    max = rsetCount[0]
    mx = 0
    for j in range(1, len(ruleSet)):
        if rsetCount[j] > max:
            max = rsetCount[j]
            mx = j;
    return (mx, max) # в какой по счету колонке сколько раз встречается совпадение

def sortFile(ruleSetList, fileName, goodfileName):
    columns = getColumns(fileName)
    goodrulesCount = [0]*len(ruleSetList) #количество совпадений для каждого столбца
    goodColumns = [[]]*len(ruleSetList) #столбцы уже хорошие
    lines = []
    for i in range(0, len(columns[1])):
        lines.append([])
    for column in columns:
        index = IndexColumn(column, ruleSetList)
        if index is not None:
            maxCount = index[1] # кол-во совпадений для текущего столбца 
            if maxCount > goodrulesCount[index[0]]: 
                goodrulesCount[index[0]] = maxCount            
                goodColumns[index[0]] = column # записываем в хорошую колонку только если количество совпадений увеличилось по сравнению с предыдущими
    lines = sortColumns(goodColumns, ruleSetList)
    saveList2(goodfileName, lines, findOlymp(fileName, ruleSet(['dictOlymp.txt'])))  
    
    
def sortColumns(goodColumns, ruleSetList):
    maxLenIndex = 0;
    for i in range(0, len(goodColumns)):
        if (len(goodColumns[i]) > len(goodColumns[maxLenIndex])):
            maxLenIndex = i
    minskip = len(goodColumns[maxLenIndex])
    for i in range(0, len(goodColumns)):
        if (len(goodColumns[i]) == 0):
            continue
        skip = 0
        for j in range(0, len(goodColumns[i])):
            if not any(rElem in goodColumns[i][j] for rElem in ruleSetList[i]):
                skip = skip + 1
            else:
                break
        minskip = min(minskip, skip)
        
    lines = []
    for i in range(minskip, len(goodColumns[maxLenIndex])):
        lines.append([]) 
        
    for i in range(0, len(goodColumns)):
        if len(goodColumns[i]) < minskip:
            for j in range(0, len(lines)):
                lines[j].append("")
        else:
            for j in range(minskip, len(goodColumns[i])):
                lines[j - minskip].append(goodColumns[i][j])                               
    return lines
                       
                       
def findOlymp(fileName, ruleSetList):
    columns = getColumns(fileName)
    maxCount = 0
    maxIndex = 0
    for i in range(0, len(columns)):
        index = IndexColumn(columns[i], ruleSetList)
        if index is not None:
            if maxCount < index[1]: 
                maxCount = index[1]
                maxIndex = i
    maxCount = 0
    maxIndexJ = 0
    for i in range(0, len(columns[maxIndex])):
        index = IndexColumn([columns[maxIndex][i]], ruleSetList)
        if index is not None:
            if maxCount < index[1]: 
                maxCount = index[1]
                maxIndexJ = i 
    return columns[maxIndex][maxIndexJ]

def personFind(personList, fio, gradYear):
    maxId = -1
    for record in personList:
        #print(record)
        if  record[0] == '' or int(record[0]) > maxId :
            maxId = int(record[0])
        if record[1] == fio and record[2] == gradYear:
            return record[0]
    personList.append([str(maxId + 1), fio, gradYear])
    return str(maxId + 1)
    
def olympFind(olympList, subject, olympName, olympYear):
    maxOid = -1
    for record in olympList:
        if int(record[0]) > maxOid:
            maxOid = int(record[0])
        if record[1] == subject and record[2] == olympName and record[3] == olympYear:
            return record[0]
    olympList.append([str(maxOid + 1), subject, olympName, olympYear])
    return str(maxOid + 1)

def recordFind(recordList, pid, oid):
    for record in recordList:
        if record[0] == pid and record[1] == oid:
            return True
    return False
    
def addRecord(recordList, record):
    for rec in recordList:
        if rec == record:
            return
    recordList.append(record)
    
def gradYear(olympYear, classnum):
    return str((11 - int(classnum.strip('\n'))) + int(olympYear.strip('\n')))

def addData(fileName, personList, olympList, recordList):
    fin = open(fileName, 'r')
    line1 = fin.readline().strip('\n').split('\t')
    subject = line1[0]
    print(subject, ' ')
    olympName = line1[1]
    print(olympName, ' ')
    olympYear = line1[2]
    print(olympYear, ' ')
    oid = olympFind(olympList, subject, olympName, olympYear)
    lines = fin.readlines()
    for line in lines:
        result = line.strip('\n').split('\t')
        #print(result[0], result[1])
        if result[1] != '':
            gyear = gradYear(olympYear, result[1])
        else:
            gyear = " "
        pid = personFind(personList, result[0], gyear)
        record = [pid, oid, result[2], result[3], result[4], result[5]]
        if not recordFind(recordList, pid, oid):
            addRecord(recordList, record)
        
                        
personList = loadList('name.txt')
olympList = loadList('olymp.txt')
recordList = loadList('records.txt')

#sortFile(ruleSet(['dictLastname.txt',  'dictClass.txt', 'dictResult.txt', 'dictReg.txt', 'dictCities.txt', 'dictSchools.txt']), 'it infa1 11 2012-2013.txt', 'common file.txt')
addData('start file.txt', personList, olympList, recordList)

saveList('name.txt', personList)
saveList('olymp.txt', olympList)
saveList('records.txt', recordList)