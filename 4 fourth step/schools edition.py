import re

realData = open('schools.txt', 'r')
editedfile = open('schools after edition.txt', 'w')
realLines = realData.readlines()
for i in range(0, len(realLines)):
    record = realLines[i].strip('\n').split('\t')
    town = record[0].strip('"')
    line = record[1].strip('"').split(';')
    singl = ''
    for j in range(0, len(line)):
        a = re.findall(r'\d+', line[j])
        if (len(line[j].strip()) == 0):
            break     
        newline = ''
        if (len(a) != 0):
            if (a[0] in town):
                if (line[j] in town):
                    town = town.replace(line[j] + ';', '')
                else:
                    town = town.replace(a[0] + ';', '')
            b = re.findall(r'(СОШ)|(\wкола)|(ФМШ)|(ФТШ)', line[j])
            if (len(b) != 0):
                newline += "школа" +  ' '
            c = re.findall(r'(\wицей)|(ФМЛ)|(ФТЛ)', line[j])
            if (len(c) != 0):
                newline += "лицей" + ' '
            d = re.findall(r'\wимназия', line[j])
            if (len(d) != 0):
                newline += "гимназия" + ' '
            e = re.findall(r'(ЦО)|(\wентр образования)', line[j])
            if (len(e) != 0):
                newline += "ЦО" + ' '
            newline += a[0] + ';'
        else: newline += re.sub(r'(\w+УО)|(\w+ОУ)', ' ', line[j]).strip() + ';'
        if (newline not in singl):
            singl += newline;
            
        if (newline in town):
            town = town.replace(newline + ';', '') # еще раз проверяем входит ли название школы в город
            
        s = re.search(r'(,)|(г\.)|(города)|(город)', line[j])
        if (s != None):
            newtown = re.split(r'(,)|(г\.)|(города)|(город)', line[j], maxsplit = 1)[-1]
            if (newtown not in town):
                town += newtown + ';'
                
    singltown = ''
    if (len(town.strip()) > 0):
        town = town.split(';')
        for j in range(0, len(town)):
            if (town[j] not in singltown):
                singltown += town[j] + ';';         
    print(singltown + '\t' + singl, file  = editedfile)
                
                
        
            
            
            
    """line = realLines[i].replace("МАОУ", '')
    print(line)
    line = line.replace("СОГБОУ", '')
    line = line.replace("ГБОУ", '')
    line = line.replace("МКОУ", '')
    line = line.replace("МБОУ", '')
    line = line.replace("ГБНОУ", '')
    line = line.replace("МОУ", '')
    line = line.replace("ОГАОУ", '') 
    line = line.replace("АОУ", '')
    line = line.replace("КСОШ", "школа")
    line = line.replace("СОШ", "школа")
    line = line.replace("№", '')
    line = line.replace("ПФМЛ", "лицей")
    line = line.replace("Пятьдесят седьмая школа", "школа 57")
    line = line.replace("?", '')
    line = line.replace("РМ", '')
    line = line.replace("НОУ", '')
    line = line.replace("МИОО", '')
    line = line.replace("АНО", '')
    line = line.replace("ФМЛ", "лицей")
    line = line.replace("Президентский", '')
    line = line.replace("АОУ", '')
    line = line.replace("Физико-Математический Лицей", "лицей")
    line = line.replace("Специализированный учебно-научный центр (факультет) — школа-интернат имени А.Н.Колмогорова Московского ", "СУНЦ МГУ")
    line = line.replace("«", '')
    line = line.replace("»", '')
    line = line.replace("ФГБОУ", '')
    line = line.replace("физико-математический лицей", "лицей")
    line = line.replace("Физико-технический Лицей", "лицей")
    line = line.replace("Вторая Санкт-Петербургская гимназия", "гимназия 2, Санкт-Петербург")
    line = line.replace("Общеобразовательный", '')
    line = line.replace("Многопрофильный", '')
    line = line.replace("ОГАОУ", '')
    line = line.replace("АГ", "Академическая Гимназия")
    line = line.replace("Средняя", '')
    line = line.replace("ЧОУ", '')
    line = line.replace("л2ш", "Лицей Вторая школа")
    line = line.replace("ФТЛ", '')
    line = line.replace("РСЯ ЛИ", '')
    line = line.replace("ФМШ", "Физматшкола")
    line = line.replace(" гимназия им. ак. Н.Г. Басова при ВГУ", "гимназия имени Басова")
    line = line.replace("    гим. Басова", "гимназия имени Басова")
    line = line.replace("УО", '')
    line = line.replace("МОБУ ", '')
    line = line.replace(" ГОУ ВПО МГУПС - ", '')
    line = line.replace("НЧОУ", '')
    line = line.replace("МКОУ ", '')
    line = line.replace(" - Центр", '')
    line = line.replace("РЛЦОД", "Республиканский лицей для одаренных детей")
    line = line.replace(" КГБОШИ ", '')
    line = line.strip(' ')
    print(line, file = editedfile) """
    
realData.close()
editedfile.close() 

    
    
    
    
    
    