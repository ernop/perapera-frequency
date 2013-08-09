import sqlite3
import codecs,re
import sys,time

try:
    con=sqlite3.connect('C:/Users/e/AppData/Roaming/Mozilla/Firefox/Profiles/kasabxl9.default/extensions/chineseperakun@gmail.com/dict.sqlite')
    cur=con.cursor()
except:
    print 'you have to set the location of your perapera-kun sqlite dictionary; itll be something like the above but with a random profile name.'
    time.sleep(10)
    sys.exit()

try:
    blob=codecs.open('./internet-zh.num','r','utf8').readlines()
except:
    print 'you need to have the frequency file here too'
    time.sleep(10)
    sys.exit()

#SETTING LEVELS

#VERY BASIC words appear more frequently than 200 times/million words in this corpus.  These are the first 500 most common words of chinese.  They are all *really* common.

#It is useless to study words which appear 1 time / million words when there are words you don't know which appear 50/million.

levels={200:'very basic', #1-477            = 500              cum 500
    100:'basic',           #477-1016         = 500              1000
    50:'very common',      #1017-2060       = 1000            2000
    25:'common',           #2060-3760      = 1700            3700
    13:'uncommon',       #3760-6313       = 2600            6300
    7:'rare',            #6300-10050     = 3750            10000
    2:'very rare',       #10500-18600    = 8100            18000
    0:'obscure'}          #18600-50000       = 31400              50000
    
slevels=sorted(levels.items(),key=lambda x:-1*x[0])
words=sorted([w.upper() for w in levels.values()],key=lambda x:-1*len(x))

for ii,line in enumerate(blob):
	
    line=line.strip()
    if line.count(' ')!=2:
        continue
    cardinality, permillion, char=line.split()
    sql='select * from dict where simp="%s"'%char
    cur.execute(sql)
    res=cur.fetchall()
    permillion=float(permillion)
    if res:
        for num,name in slevels:
            if permillion>num:
                description=name
                break
        entry=res[0][3]
        for w in words: #clean old if you run it multiple times
            w=w.upper()
            entry=entry.replace(' '+w,'')
        newentry=entry.strip().replace('"','')+' '+description.upper()
        sql='update dict set entry="%s" where simp="%s" and entry="%s"'%(newentry,char,entry.replace('"','""'))
        #fixed this to let it display multiple entries again...
        if ii%100==0:
            print repr(sql)
            print ii
        ii+=1
        try:
            cur.execute(sql)
        except:
            import ipdb;ipdb.set_trace()
    else:
        #word was in internet-freq but not pera pera dict
        pass
        
con.commit()