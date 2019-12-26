import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd
import tushare as ts

e = ts.get_today_all()
e.to_csv('zane.csv')
#print("\n")
#print(e)
#print("\n")

#print(e[0])
code = e[u'code']   
name = e[u'name']  
per = e[u'per']    
tt = e[u'turnoverratio']    
cc = e[u'changepercent']   
mm = e[u'mktcap']         
high = e[u'high']
low = e[u'low']
opens = e[u'open']
trade = e[u'trade']

'''
idx = len(name)
total = 0
while idx > 0:
    idx -= 1
    if per[idx] < 30 and per[idx] > 0 and tt[idx] > 1 and cc[idx] > 2:
        print(code[idx],name[idx],":",per[idx],":",tt[idx],":",cc[idx],":",mm[idx]/10000)
        total += 1
print("total:" ,total,"/",len(name))
'''

idx = len(name)
total = 0
while idx > 0:
    idx -= 1
    if (abs(high[idx] - low[idx])/abs(trade[idx] - opens[idx])) >= 4:
        print(code[idx],name[idx],":",per[idx],":",tt[idx],":",cc[idx],":",mm[idx]/10000)
        total += 1
print("total:" ,total,"/",len(name))
'''
idx = len(name)
total = 0
while idx > 0:
    idx -= 1
    if per[idx] < 30 and per[idx] > 0 and tt[idx] > 1 and cc[idx] > 2 and mm[idx] > 2000000:
        print(code[idx],name[idx],":",per[idx],":",tt[idx],":",cc[idx],":",mm[idx]/10000)
        #print
        total += 1
print("total:" ,total,"/",len(name))

idx = len(name)
total = 0
while idx > 0:
    idx -= 1

    if cc[idx] > 9.9:
        total += 1
        print("@@@@:",code[idx],":",name[idx],":",cc[idx])
print("total:",total,"/",len(name))
'''

'''
idx = len(name)
total = 0
data = []
while idx > 0:
    idx -= 1

    if mm[idx] > 1000000:
        total += 1
        #data = data.append(e[idx])
        #print("@@@@:",code[idx],":",name[idx],":",cc[idx])
        print()
print("total:",total,"/",len(name))
#data.to_csv('more_than_100.csv')
#print("")
'''
