def comp(line):
    return line[1], line[3]

names = open('newname.txt', 'r')
olymps = open('olymp.txt', 'r')
records = open('newrecords.txt', 'r')
lines = olymps.readlines()
#print(len(lines))
olympiads = []
for i in range(0, len(lines)):
    line = lines[i].strip('\n').split('\t')
   # print(line)
    olympiads.append(line)
count_olymp = int(olympiads[len(olympiads) - 1][0]) + 1
olympiads = sorted(olympiads, key = comp)

namelines = names.readlines()
namemaxid = int(namelines[len(namelines) - 1].split('\t')[0]) + 1
data =  [ ([' '] * 3) for row in range(0, len(namelines))]
table = [ ([' '] * count_olymp) for row in range(0, len(namelines))]
for record in records.readlines():
    record = record.strip('\n').split('\t')
    record0 = int(record[0])
    record1 = int(record[1])
    # print(record0, ' ',record1, ' ', record[2]) 
    table[record0][record1] = record[2]
    if len(record) > 3:
        if not record[3] in data[record0][0]:
            data[record0][0] += record[3] + ';'
    if len(record) > 4:
        if not record[4] in data[record0][1]:
            data[record0][1] += record[4] + ';'
    if len(record) > 5:
        if not record[5] in data[record0][2]:
            data[record0][2] += record[5] + ';'       
        
#print(table)

result = open('result.txt', 'w')
print('ФИО' + '\t' + 'Год выпуска' + '\t' + 'регион' + '\t' + 'город' + '\t' + 'школа', file = result, end = '\t')
for i in range(0, len(olympiads) - 1):
    olympiada = olympiads[i]
    print(olympiada[2] + ' ' + olympiada[1] + ' ' + olympiada[3], file = result, end = '\t')
print(olympiads[len(olympiads) - 1][2] + ' ' + olympiads[len(olympiads) - 1][1] + ' ' + olympiads[len(olympiads) - 1][3], file = result, end = '\n') 


print( len(namelines), ' ', len(table))
print(len(olympiads), ' ', len(table[1]))
for i in range(0, len(namelines)):
    name = namelines[i].strip('\n').split('\t')
    print(name[1] + '\t' + name[2] + '\t' + data[i][0] + '\t' + data[i][1] + '\t' + data[i][2], file = result, end = '\t')
    for j in range(0, len(olympiads)):
        print(len(table[i]),' ', int(olympiads[j][0]))
        print(table[i][int(olympiads[j][0])], file = result, end = '\t')
    print(' ', file = result)

names.close()
olymps.close()
records.close()
result.close()

for line in lines:
    line = line.strip('\n').split('\t')
    student = line[0]
#for olympiada in olympiads:
    

