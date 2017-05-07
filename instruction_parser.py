#instructionparser

f=open('instruction set.txt','r')
lines=f.readlines()
instruc={}
g1=len(lines)
#d=g+1
#print(g)
for i in range(0,g1):
    instruc[i]=lines[i]
#print(instruc)
#print(instruc
#print(instruc[5])
def call_instruction(n):
    ins=instruc[n]
    g=ins.split()
   # print(g)
    if(g[0]=='LD'):
        op='Load'
        unit='integer'
        d=g[1].split(',')
        dest=d[0]
        f1=g[2].split('(')
        f2=f1[1].split(')')
        src1=f2[0]
        src2=None
    if(g[0]=='LI'):
        unit='integer'
        d=g[1].split(',')
        dest=d[0]
        src1=g[2]
        src2=None
    if(g[0]=='ADDD'):
        unit='adder'
        d=g[1].split(',')
        dest=d[0]
        d1=g[2].split(',')
        src1=d1[0]
        src2=g[3]
    if(g[0]=='MULD'):
        unit='multi'
        d=g[1].split(',')
        dest=d[0]
        d1=g[2].split(',')
        src1=d1[0]
        src2=g[3]
    if(g[0]=='DIVD'):
        unit='divide'
        d=g[1].split(',')
        dest=d[0]
        d1=g[2].split(',')
        src1=d1[0]
        src2=g[3]
        #dest=g[2]
    if(g[0]=='SUBD'):
        unit='adder'
        d=g[1].split(',')
        dest=d[0]
        d1=g[2].split(',')
        src1=d1[0]
        src2=g[3]
        #dest=g[2]
    return(unit,dest,src1,src2)
print (call_instruction(5))
        
        
        
#print (call_instruction(0))
