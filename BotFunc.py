def ListToStr(L):
    return str(L).replace('[','').replace(']','').replace("'",'').replace(',','')

def CreateFullList(id):
    Lfull = []
    for q in open('chats/'+id+'/dt_full.csv', 'r', encoding='utf8'):
        Lfull.append(q.split(',')[:-1] + [q.split(',')[-1].replace('\n', '')])
    return Lfull

def CreateDayList(week,weekday,id):
    id=str(id)
    if weekday==0: weekday=1
    st = (weekday-1)*14+(1-week%2)
    en = weekday*14+(1-week%2)
    LdayF = CreateFullList(id)[st:en:2]
    Lday = []
    for q in LdayF:
        if q[2] == '':
            pass
        elif q[2][:6] == 'кр. 17':
            if week != 17:
                q[2] = q[2][9:]
                Lday.append(q)
        elif q[2][:5] == 'кр. 1':
            if week != 1:
                q[2] = q[2][8:]
                Lday.append(q)
        elif q[2][:12] == '3,7,11,15 н.':
            if week in [3, 7, 11, 15]:
                q[2] = q[2][13:]
                Lday.append(q)
        else:
            Lday.append(q)
    return Lday

def StrFromDL(DayList):
    sfdl=str(DayList).replace('[','').replace('], ','\n\n').replace(']','').replace("'",'').replace(' ,','')[:-1]
    return sfdl

def NewSub(username):
    f=open('subs.txt','w+')
    f.writelines(username)
    f.close()

def AllSubs():
    AS=[]
    for q in open('subs.txt'):
        AS.append(q)
    return AS

'''for q in CreateFullList('-1001671555407'):
    print(q)
print(StrFromDL(CreateDayList(2,4,'-1001671555407')))'''