#instructionparser
import re
f=open('instruction set1.txt','r')
lines=f.readlines()
instruc={}
g1=len(lines)
'''label=''
unit=''
dest=''
src1=''
src2=''
op1=''
'''
#d=g+1
#print(g)
for i in range(0,g1):
    instruc[i]=lines[i]
#print(instruc)
#print(instruc
#print(instruc[5])
def call_instruction(n):
    ins=instruc[n]
    if(ins[2]==':'):
        print('found')
        g=ins.split()
        label=g[0]
        w=g[1]
        if(w=='L.D'):
            op='Load'
            op1='LD'
            ins_no=n
            unit='integer'
            d=g[2].split(',')
            dest=d[0]
            f1=g[3].split('(')
            f2=f1[1].split(')')
            src1=f2[0]
            src2=None
        if(w=='LI'):
            unit='integer'
            op1='LI'
            ins_no=n
            d=g[w].split(',')
            dest=d[0]
            src1=g[3]
            src2=None
        if(g[1]=='ADDD'):
            unit='adder'
            op1='ADD.D'
            d=g[2].split(',')
            dest=d[0]
            ins_no=n
            d1=g[3].split(',')
            src1=d1[0]
            src2=g[5]
        if(g[1]=='MULD'):
            unit='multi'
            op1='MUL.D'
            d=g[2].split(',')
            dest=d[0]
            d1=g[3].split(',')
            src1=d1[0]
            src2=g[4]
        if(g[1]=='DIVD'):
            unit='divide'
            op1='DIV.D'
            ins_no=n
            d=g[2].split(',')
            dest=d[0]
            d1=g[3].split(',')
            src1=d1[0]
            src2=g[4]
            #dest=g[2]
        if(g[1]=='SUBD'):
            unit='adder'
            op1='SUB.D'
            ins_no=n
            d=g[2].split(',')
            dest=d[0]
            d1=g[3].split(',')
            src1=d1[0]
            src2=g[4]
        if(g[1]=='DADD'):
            unit='adder'
            op1='DADD'
            ins_no=n
            d=g[2].split(',')
            dest=d[0]
            d1=g[3].split(',')
            src1=d1[0]
            src2=g[4]
        if(g[1]=='DADDI'):
            unit='adder'
            op1='DADDI'
            ins_no=n
            d=g[2].split(',')
            dest=d[0]
            d1=g[3].split(',')
            src1=d1[0]
            src2=g[4]
        if(g[1]=='DSUBI'):
            unit='adder'
            op1='SUBI'
            ins_no=n
            d=g[2].split(',')
            dest=d[0]
            d1=g[3].split(',')
            src1=d1[0]
            src2=g[4]
        if(g[1]=='DSUB'):
            unit='adder'
            op1='DSUB'
            ins_no=n
            d=g[2].split(',')
            dest=d[0]
            d1=g[3].split(',')
            src1=d1[0]
            src2=g[5]

    else:
        g=ins.split()
        print(g)
        if(g[0]=='L.D'):
            op1='LD'
            unit='integer'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            f1=g[2].split('(')
            f2=f1[1].split(')')
            src1=f2[0]
            src2=None
        if(g[0]=='LW'):
            op1='LD'
            unit='integer'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            f1=g[2].split('(')
            f2=f1[1].split(')')
            src1=f2[0]
            src2=None
        if(g[0]=='LI'):
            unit='integer'
            op1='LI'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            src1=g[2]
            src2=None
        if(g[0]=='ADD.D'):
            unit='adder'
            op1='ADDD'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            d1=g[2].split(',')
            src1=d1[0]
            src2=g[3]
        if(g[0]=='MUL.D'):
            unit='multi'
            op1='MUL.D'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            d1=g[2].split(',')
            src1=d1[0]
            src2=g[3]
        if(g[0]=='DIVD'):
            unit='divide'
            op1='DIV.D'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            d1=g[2].split(',')
            src1=d1[0]
            src2=g[3]
            #dest=g[2]
        if(g[0]=='SUB.D'):
            unit='adder'
            op1='SUB.D'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            d1=g[2].split(',')
            src1=d1[0]
            src2=g[3]
        if(g[0]=='DADD'):
            unit='adder'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            d1=g[2].split(',')
            src1=d1[0]
            src2=g[3]
        if(g[0]=='DADDI'):
            unit='adder'
            ins_no=n
            op1='DADDI'
            d=g[1].split(',')
            dest=d[0]
            d1=g[2].split(',')
            src1=d1[0]
            src2=g[3]
        if(g[0]=='DSUBI'):
            unit='adder'
            op1='DSUBI'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            d1=g[2].split(',')
            src1=d1[0]
            src2=g[3]
        if(g[0]=='DSUB'):
            unit='adder'
            op1='DSUB'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            d1=g[2].split(',')
            src1=d1[0]
            src2=g[3]
        if(g[0]=='BEQ'):
            unit='compare'
            op1='BEQ'
            ins_no=n
            d=g[1].split(',')
            dest=d[0]
            d1=g[2].split(',')
            src1=d1[0]
            src2=g[3]
        if(g[0]=='BNE'):
            unit='compare'
            op1='BNE'
            d=g[1].split(',')
            dest=d[0]
            ins_no=n
            d1=g[2].split(',')
            src1=d1[0]
            src2=g[3]
        #dest=g[2]
    return(unit,dest,src1,src2,op1,ins_no)
print (call_instruction(5))
              
        
#print (call_instruction(0))
