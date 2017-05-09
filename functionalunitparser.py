#functionalUnitparser
#f=open('Functional unit.txt','r')
add={}
mult={}
div={}
inti={}
icache={}
import re
def func_parse(filename):
    f=open(filename)
    global add
    global mult
    global div
    global inti
    global icache
    lines=f.readlines()
    for i in range(0,4):
        word=lines[i].split()
        #print (word)
        if(word[1]=='adder:'):
                s=word[2].split(',')
                print('add',s)
                add['no.']=s[0]
                add['clock']=word[3]
        if(word[1]=='Multiplier:'):
                s=word[2].split(',')
                print (s)
                mult['no.']=s[0]
                mult['clock']=word[3]
        if(word[1]=='divider:'):
                s=word[2].split(',')
                print (s)
                div['no.']=s[0]
                div['clock']=word[3]
        if(word[1]=='I-Cache:'):
                s=word[2].split(',')
                print (s)
                icache['no.']=s[0]
                icache['clock']=word[3]
    inti['no.']=1
    inti['clock']=1
    return(add,mult,div,inti,icache)
#print (func_parse('Functional unit.txt'))          
    
