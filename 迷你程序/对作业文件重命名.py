import os
NameList = {}
def new_name(name):#输出格式化文件名
    global NameList
    PName = ''
    Number = ''
    for i in range(0,len(name)):
        if name[i:i+2] in NameList:#查询姓名
            PName = name[i:i+2]
            Number = NameList[PName]
            break
        elif name[i:i+3] in NameList:
            PName = name[i:i+3]  
            Number = NameList[PName]
            break
    return f'3班-{PName}-{Number}'

FileName = input("输入文件夹名：")
dir=os.path.dirname(__file__)+f'/{FileName}'

with open('---path---\名单.txt') as f:
    for line in f:
        line = line[:-1]
        NameList[line.split('\t')[1]] = line.split('\t')[0]

for name in os.listdir(dir):#重命名
    NewName = new_name(name)
    ext = os.path.splitext(name)[1][1:]
    #print(name,'------->',f'{NewName}.{ext}')
    if name != f"{NewName}.docx":#重命名
        os.rename(os.path.join(dir, name),os.path.join(dir,f"{NewName}.{ext}"))
