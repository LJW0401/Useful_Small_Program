import os
import datetime
StartTime = datetime.datetime.now()
CompletedName = {}
Classify_University = {}
Classify_Provence = {}
Classify_City = {}
Infor_UPC = {}
infor = []
RecordNum = 0
def LoadCompleteUniversityName():#加载学校全称文件
    global CompletedName
    temp = []
    with open(os.path.dirname(__file__) + '/CompleteUniversityName.txt') as fin:
        for line in fin:
            line = line[:-1]
            temp.append(line.split(','))
    CompletedName = dict(temp)

def CompleteUniName(OriginalName):#将学校简写转换为全称
    if OriginalName in list(CompletedName):
        return CompletedName[OriginalName]
    else:
        return OriginalName
    
def LoadUniversitieForEachStudent():#加载每位学生录取学校文件内容
    global infor,RecordNum
    with open(os.path.dirname(__file__) + '/UniversitieForEachStudent.txt') as fin:
        for line in fin:
            line = line[:-1]
            infor.append(line.split('  '))
            RecordNum += 1

def DealUni_stu():#按照学校记录学生分布
    global infor,Classify_University
    for item in infor:
        if item[1] in list(Classify_University):
            Classify_University[item[1]].append(item[0])
        else:
            Classify_University[item[1]] = []
            Classify_University[item[1]].append(item[0])

def ShowUni_StuNum():#以学校人数为关键字倒序显示
    for item in sorted(Classify_University.items(),key=lambda x:len(x[1]),reverse=True):
        print(CompleteUniName(item[0]),'有',len(item[1]),'位同学')

def LoadUni_Prov_City():#加载 学校-省份-城市 文件内容
    global Infor_UPC
    with open(os.path.dirname(__file__) + '/Uni_Prov_City_Full.txt') as fin:
        for line in fin:
            line = line[:-1]
            Infor_UPC[line.split('\t')[0]] = []
            Infor_UPC[line.split('\t')[0]].append(line.split('\t')[1])
            Infor_UPC[line.split('\t')[0]].append(line.split('\t')[2])
            
def DealProv_Stu():#按照省份记录学生分布
    global Classify_Provence
    for uni in list(Classify_University):
        if Infor_UPC[CompleteUniName(uni)][0] in Classify_Provence:
            for stu in Classify_University[uni]:
                Classify_Provence[Infor_UPC[CompleteUniName(uni)][0]].append(stu)
        else:
            Classify_Provence[Infor_UPC[CompleteUniName(uni)][0]] = []
            for stu in Classify_University[uni]:
                Classify_Provence[Infor_UPC[CompleteUniName(uni)][0]].append(stu)

def ShowProv_StuNum():#以省份人数为关键字倒序显示
    for item in sorted(Classify_Provence.items(),key=lambda x:len(x[1]),reverse=True):
        print(item[0],'有',len(item[1]),'位同学')

def OutputUniversities():#输出有被录取的学校
    results = []
    for item in list(Classify_University):
        results.append(CompleteUniName(item))
    #print(results)
    with open(os.path.dirname(__file__) + '/录取学校.txt','w') as fout:
        fout.write('\n'.join(results))

def DealCity_Stu():#按照城市记录学生分布
    global Classify_City
    for uni in list(Classify_University):
        if Infor_UPC[CompleteUniName(uni)][1] in Classify_City:
            for stu in Classify_University[uni]:
                Classify_City[Infor_UPC[CompleteUniName(uni)][1]].append(stu)
        else:
            Classify_City[Infor_UPC[CompleteUniName(uni)][1]] = []
            for stu in Classify_University[uni]:
                Classify_City[Infor_UPC[CompleteUniName(uni)][1]].append(stu)

def ShowCity_StuNum():#以城市人数为关键字倒序显示
    for item in sorted(Classify_City.items(),key=lambda x:len(x[1]),reverse=True):
        print(item[0],'有',len(item[1]),'位同学')

def FindMateMax(location,InList):#按条件找到校友最多的地点
    k = 0
    if location != '学校':
        string = InList[0][0]
        while len(InList[k][1]) == len(InList[k + 1][1]):
            k += 1
            string = string + '，' + InList[k][0]
    else:
        string = CompleteUniName(InList[0][0])
        while len(InList[k][1]) == len(InList[k + 1][1]):
            k += 1
            string = string + '，' + CompleteUniName(InList[k][0])
    return f'校友最多的{location}是{string}，有{len(InList[0][1])}人。'

def ReturnIs_EachIs(item,mode = 'Univ'):#按1来区分用是或分别是
    if mode == 'Univ':
        if len(item[1]) > 1:
            return CompleteUniName(item[0]) + f' 有{len(item[1])}位同学，分别是 '
        else:
            return CompleteUniName(item[0]) + f' 有{len(item[1])}位同学，是 '
    else:
        if len(item[1]) > 1:
            return item[0] + f' 有{len(item[1])}位同学，分别是 '
        else:
            return item[0] + f' 有{len(item[1])}位同学，是 '

def OutputInformation():#输出大学录取信息分析
    Tmp_Univ = []
    Tmp_Prov = []
    Tmp_City = []
    with open(os.path.dirname(__file__) + f'/大学录取信息分析#{RecordNum}.txt','w') as fout:
        Tmp_Univ = sorted(Classify_University.items(),key=lambda x:len(x[1]),reverse=True)
        Tmp_Prov = sorted(Classify_Provence.items(),key=lambda x:len(x[1]),reverse=True)
        Tmp_City = sorted(Classify_City.items(),key=lambda x:len(x[1]),reverse=True)
        #信息写入文件
        fout.write(f'共有{RecordNum}人参与统计，分布在{len(list(Tmp_Prov))}个省份，{len(list(Tmp_City))}座城市，{len(list(Tmp_Univ))}座大学。\n')
        fout.write(FindMateMax('省份',Tmp_Prov) + '\n')
        fout.write(FindMateMax('城市',Tmp_City) + '\n')
        fout.write(FindMateMax('学校',Tmp_Univ) + '\n')
        fout.write('\n---按大学整合---\n')
        for item in Tmp_Univ:
            fout.write(ReturnIs_EachIs(item,mode = 'Univ'))
            fout.write(','.join(item[1]) + '\n')
        fout.write('\n---按省份整合---\n')
        for item in Tmp_Prov:
            fout.write(ReturnIs_EachIs(item,mode = 'Prov'))
            fout.write(','.join(item[1]) + '\n')
        fout.write('\n---按城市整合---\n')
        for item in Tmp_City:
            fout.write(ReturnIs_EachIs(item,mode = 'City'))
            fout.write(','.join(item[1]) + '\n')
    print('已保存到大学录取信息分析.txt')

#----------正式运行区----------
#文件加载-----
LoadCompleteUniversityName()#加载学校全称文件
LoadUniversitieForEachStudent()#加载每位学生录取学校文件内容
LoadUni_Prov_City()#加载 学校-省份-城市 文件内容
#分类处理学生录取信息
DealUni_stu()#按照学校记录学生分布
DealProv_Stu()#按照省份记录学生分布
DealCity_Stu()#按照城市记录学生分布
#数据显示-----
print(f'---共有{RecordNum}条记录参与---')
print('---按大学整合---')
ShowUni_StuNum()#按照录取学校人数倒序显示
print('---按省份整合---')
ShowProv_StuNum()#按照省份人数倒序显示
print('---按城市整合---')
ShowCity_StuNum()#以城市人数为关键字倒序显示
#数据输出-----
OutputUniversities()#输出有被录取的学校
OutputInformation()#输出大学录取信息分析

#----------程序运行效果分析区----------
EndTime = datetime.datetime.now()
DeltaTime = EndTime - StartTime
print('\n程序执行时间:',DeltaTime,'\n')