def func (line1, line2, recordlines):
    line1 = line1.replace('¸','å').strip('\n').split('\t')
    line2 = line2.replace('¸','å').strip('\n').split('\t')
    fio1 = line1[1].strip(' ').split(' ')
    fio2 = line2[1].strip(' ').split(' ')
    if (fio1[0] != fio2[0]):
        return False
    if (fio1 == fio2):
        return True
    if (len(fio1) > 1 and len(fio2) > 1 and fio1[0] == fio2[0] and fio1[1] != fio2[1]):
        return False
    if (len(fio1) > 2 and len(fio2) > 2 and fio1[0] == fio2[0] and fio1[2] != fio2[2]):
        return False 
    if (fio1[0] == fio2[0] and line1[2] == line2[2] and len(fio1) > 1 and len(fio2) > 1 and fio1[1][0] == fio2[1][0]):
        return True
    if (fio1[0] == fio2[0] and line1[2] == line2[2]):      
        reg1 = set()
        reg2 = set()
        city1 = set()
        city2 = set()
        sch1 = set()
        sch2 = set()
        for i in range(0, len(recordlines)):
            record = recordlines[i].strip('\n').split('\t')
            if (record[0] == line1[0]):
                if (len(record) > 3):
                    reg1.add(record[3])
                if (len(record) > 4):
                    city1.add(record[4])
                if (len(record) > 5):    
                    sch1.add(record[5])
            if (record[0] == line2[0]):
                if (len(record) > 3):
                    reg2.add(record[3])
                if (len(record) > 4):
                    city2.add(record[4])
                if (len(record) > 5):    
                    sch2.add(record[5])   
        if (len(reg1) != 0 and len(reg2) != 0 and (reg1.issubset(reg2) or reg2.issubset(reg1))):
            return True
        if (len(city1) != 0 and len(city2) != 0 and (city1.issubset(city2) or city2.issubset(city1))):
            return True
        if (len(sch1) != 0 and len(sch2) != 0 and (sch1.issubset(sch2) or sch2.issubset(sch1))):
            return True
        
def func2 (line1, line2):
    line1 = line1.strip('\n').split('\t')
    line2 = line2.strip('\n').split('\t')
    fio1 = line1[1].split(' ')
    fio2 = line2[1].split(' ')
    if (len(fio1) < len(fio2)):
        line1[1] = (' ').join(fio2)
    if (len(line1[2]) < len(line2[2])):
        line1[2] = (' ').join(line2[2])
    
def newrecord(i, j, records):
    for k in range(0, len(records)):
        record = records[k].strip('\n').split('\t')
        intrec = record[0]
        intj = j
        if (int(intrec) == int(intj)):
            record[0] = str(i)
            records[k] = ('\t').join(record) + '\n'
            # print(('\t').join(record), file = newrecords, end = '\n')
    
    
names = open('name.txt', 'r')
records = open('records.txt', 'r')
newnames = open('newname.txt', 'w')
newrecords = open('newrecords.txt', 'w')
nameline = names.readlines()
recordlines = records.readlines()

i = 0
while i < len(nameline):
    j = i + 1
    while j < len(nameline):
        if (func(nameline[i], nameline[j], recordlines) == True):
            func2(nameline[i], nameline[j])
            ID = nameline[j].strip('\n').split('\t')[0]
            newid = nameline[i].strip('\n').split('\t')[0]
            newrecord(newid, ID, recordlines)
            del nameline[j]
        else:
            j += 1
    print('.')
    # newrecord(i, i, recordlines, newrecords)
    # print((nameline[i]), file = newnames, end = '')
    i += 1

for i in range(0, len(nameline)):
    namel = nameline[i].split('\t')
    newrecord(i, namel[0], recordlines)
    namel[0] = str(i)
    print(('\t').join(namel), file = newnames, end = '')
for i in range(0, len(recordlines)):
    print(recordlines[i], file = newrecords, end = '')
names.close()
records.close()
newnames.close()
newrecords.close() 
