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
            b = re.findall(r'(���)|(\w����)|(���)|(���)', line[j])
            if (len(b) != 0):
                newline += "�����" +  ' '
            c = re.findall(r'(\w����)|(���)|(���)', line[j])
            if (len(c) != 0):
                newline += "�����" + ' '
            d = re.findall(r'\w�������', line[j])
            if (len(d) != 0):
                newline += "��������" + ' '
            e = re.findall(r'(��)|(\w���� �����������)', line[j])
            if (len(e) != 0):
                newline += "��" + ' '
            newline += a[0] + ';'
        else: newline += re.sub(r'(\w+��)|(\w+��)', ' ', line[j]).strip() + ';'
        if (newline not in singl):
            singl += newline;
            
        if (newline in town):
            town = town.replace(newline + ';', '') # ��� ��� ��������� ������ �� �������� ����� � �����
            
        s = re.search(r'(,)|(�\.)|(������)|(�����)', line[j])
        if (s != None):
            newtown = re.split(r'(,)|(�\.)|(������)|(�����)', line[j], maxsplit = 1)[-1]
            if (newtown not in town):
                town += newtown + ';'
                
    singltown = ''
    if (len(town.strip()) > 0):
        town = town.split(';')
        for j in range(0, len(town)):
            if (town[j] not in singltown):
                singltown += town[j] + ';';         
    print(singltown + '\t' + singl, file  = editedfile)
                
                
        
            
            
            
    """line = realLines[i].replace("����", '')
    print(line)
    line = line.replace("������", '')
    line = line.replace("����", '')
    line = line.replace("����", '')
    line = line.replace("����", '')
    line = line.replace("�����", '')
    line = line.replace("���", '')
    line = line.replace("�����", '') 
    line = line.replace("���", '')
    line = line.replace("����", "�����")
    line = line.replace("���", "�����")
    line = line.replace("�", '')
    line = line.replace("����", "�����")
    line = line.replace("��������� ������� �����", "����� 57")
    line = line.replace("?", '')
    line = line.replace("��", '')
    line = line.replace("���", '')
    line = line.replace("����", '')
    line = line.replace("���", '')
    line = line.replace("���", "�����")
    line = line.replace("�������������", '')
    line = line.replace("���", '')
    line = line.replace("������-�������������� �����", "�����")
    line = line.replace("������������������ ������-������� ����� (���������) � �����-�������� ����� �.�.����������� ����������� ", "���� ���")
    line = line.replace("�", '')
    line = line.replace("�", '')
    line = line.replace("�����", '')
    line = line.replace("������-�������������� �����", "�����")
    line = line.replace("������-����������� �����", "�����")
    line = line.replace("������ �����-������������� ��������", "�������� 2, �����-���������")
    line = line.replace("�������������������", '')
    line = line.replace("���������������", '')
    line = line.replace("�����", '')
    line = line.replace("��", "������������� ��������")
    line = line.replace("�������", '')
    line = line.replace("���", '')
    line = line.replace("�2�", "����� ������ �����")
    line = line.replace("���", '')
    line = line.replace("��� ��", '')
    line = line.replace("���", "�����������")
    line = line.replace(" �������� ��. ��. �.�. ������ ��� ���", "�������� ����� ������")
    line = line.replace("    ���. ������", "�������� ����� ������")
    line = line.replace("��", '')
    line = line.replace("���� ", '')
    line = line.replace(" ��� ��� ����� - ", '')
    line = line.replace("����", '')
    line = line.replace("���� ", '')
    line = line.replace(" - �����", '')
    line = line.replace("�����", "��������������� ����� ��� ��������� �����")
    line = line.replace(" ������ ", '')
    line = line.strip(' ')
    print(line, file = editedfile) """
    
realData.close()
editedfile.close() 

    
    
    
    
    
    