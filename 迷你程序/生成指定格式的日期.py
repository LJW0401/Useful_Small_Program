import datetime as dt
# 格式
# ***2023.3.1 w3***<br>
# &emsp;&emsp;<br>

start_time=input('输入起始日期(y-m-d):')
days=int(input('输入天数:'))
out_days=[]
start_day=dt.datetime.strptime(start_time,'%Y-%m-%d')

#build times
for i in range(days):
    t=start_day+dt.timedelta(days=i)
    Year=int(dt.datetime.strftime(t,'%Y'))
    Month=int(dt.datetime.strftime(t,'%m'))
    Day=int(dt.datetime.strftime(t,'%d'))
    Week=int(dt.datetime.strftime(t,'%w'))

    item=f'***{Year}.{Month}.{Day} w{Week}***<br>\n&emsp;&emsp;<br>'

    out_days.append(item)
    # print(item)

print('---已生成指定的日期---')

# save document
with open('---path---/dates.txt','w') as f:
    f.write('\n\n'.join(out_days))

print('---已保存到文件中---')
