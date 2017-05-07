#scoreboard
import functionalunitparser as fp
import instruction_parser as ip
f1=open('Functional unit.txt','r')
f2=open('instruction set.txt','r')
#fetch functional unit
func_unit=fp.func_parse('Functional unit.txt') 
add=fp.add
a1={'busy':0}
add.update(a1)
mult=fp.mult
mult.update(a1)
div=fp.div
div.update(a1)
inti=fp.inti
inti.update(a1)

add_count=0
multi_count=0
div_count=0

diff_add=0
diff_mul=0
diff_div=0
#number of instructions
lines=f2.readlines()
n=len(lines)
#print(n)
j=1
#global clock cycle
clock=1

#initializing fetch
fetch =0

register={}
instruction ={}
#clock
#for every instruction make a pipeline
for i in range(0,n):
    instruction[i]={'F':0,'I':0,'R':0,'E':0,'W':0}

#fetch_flag set
#print(instruction[1]['F'])

fetch_flag=0
fetch_1={}
for i in range(0,n):
    fetch_1[i]=0

issue={}
for i in range(0,n):
    issue[i]={}

read={}
for i in range(0,n):
    read[i]={}

execute={}
for i in range(0,n):
    execute[i]={}

write={}
for i in range(0,n):
    write[i]={}
    
##src=
##dest={}

#print (ip.call_instruction(11))
#writeback set
write_flag=0
def write(n):
    write_flag=0
    return write_flag

#for instruction 1 fill register sets
inst=ip.call_instruction(0)
register[inst[1]]=1
register[inst[2]]=1
register[inst[3]]=1

dest={}
src={}
l=[]
insq=ip.call_instruction(0)
##dest[0]=insq[1]
##l.append(insq[2])
##l.append(insq[3])
##src[0]=l
for de in range(0,7):
   dest[de]=0

raw=1

##dest=[]
##dest.append(inst[1])
##src=[]
##src.append(inst[2])
##src.append(inst[3])
#src[inst[3]]=1

#scoreboard_implement
#clok variables
latency_clock_add=0
latency_clock_multi=0
latency_clock_divide=0

inti_free=0
add_free=0
mul_free=0
div_free=0


def scoreboard():
    global n
    #print ('n',n)
    #print('enter')
    global clock
    global raw
    #print (clock)
    flag=1
    fetch_flag=0
    add_count=0
    multi_count=0
    div_count=0
    global diff_add
    global diff_mul
    global diff_div
    global init_free
    #print ('inti_free',inti_free)
    global add_free
    global mul_free
    global div_free
    while(clock<150 and flag==1):# and flag): #or instruction[n-2]['W']!=0):
       #print (clock)
       for i in range(0,n):
            in1=ip.call_instruction(i)
            #print('ihf',i)
            #print ('i:',in1)
            if(instruction[i]['F']==0):# and fetch_flag==0):
                if(fetch_flag==0 and fetch_1[i]==0):
                    fetch_1[i]=1
                    instruction[i]['F']=clock
                    fetch_flag=1
      
            #issue
            if(instruction[i]['F']!=0 and instruction[i]['I']==0 and clock!=instruction[i]['F']):
               #print ('enter issue')
               ins=ip.call_instruction(i)
##               print('iwiuwp',i)
##               print ('issue ins',ins)
               op=ins[0]
##               print('op issue',op)
               if(op=='integer'):
                  #print ('found unit in issue')
                  if(inti['busy']==0):#or clock==inti_free):
                     issue[i]=1
                     fetch_flag=0
                     inti['busy']=1
                     instruction[i]['I']=clock
                  

               if(op=='adder'):
                  w=add['no.']
                  if(add_count<=int(w) or clock==add_free):
                     issue[i]=1
                     fetch_flag=0
                     add_count+=1
                     instruction[i]['I']=clock
                    
               if(op=='multi'):
                  w1=mult['no.']
                  if(multi_count<=int(w1) or clock==mul_free):
                     issue[i]=1
                     fetch_flag=0
                     multi_count+=1
                     instruction[i]['I']=clock
##                  
               if(op=='divide'):
                  w2=div['no.']
                  if(div_count<=int(w2) or clock==div_free):
                     issue[i]=1
                     fetch_flag=0
                     div_count+=1
                     instruction[i]['I']=clock
##          read          
            if(instruction[i]['F']!=0 and instruction[i]['I']!=0 and instruction[i]['R']==0 and clock!=instruction[i]['I']):# and clock!=instruction[i]['W']):
               #print ('enter read',clock)
               ins1=ip.call_instruction(i)
               #print ('i23',i)
               #print ('ins1',ins1)
               op1=ins1[0]
               #print('op1',op1)
               #flag=0
               f=[]
               if(op1=='integer'):
                  #print('g',ins[2],ins[3])
                  for s in range(0,len(dest)):
##                        if(clock==3 and ins1[1]==dest[s]):
##                           instruction[i]['R']=clock
##                           #break
                        if(ins1[2]==dest[s] or ins1[3]==dest[s]):
                           print ('found')
                           raw=raw+1
                           break
                        # and clock):
                        
                        else:
                           if(ins1[2]!=dest[s] or ins1[3]!=dest[s]):
                              dest[i]=ins1[1]
                              f.append(ins1[2])
                              f.append(ins1[3])
                              src[i]=f
                              instruction[i]['R']=clock
                              read[i]=1
                           
                     
               if(op1=='adder'):
                  for s in range(0,len(dest)):
##                        if(clock==3 and ins1[1]==dest[s]):
##                           instruction[i]['R']=clock
                        if(ins1[2]==dest[s] or ins1[3]==dest[s]):
                           print('foundwip')
                           raw=raw+1
                           break
                        else:
                           if(ins1[2]!=dest[s] or ins1[3]!=dest[s]):
                              dest[i]=ins1[1]
                              f.append(ins1[2])
                              f.append(ins1[3])
                              src[i]=f
                              instruction[i]['R']=clock
                              read[i]=1
                        
                                
               if(op1=='multi'):
                  for s in range(0,len(dest)):
##                        if(clock==3 and ins1[1]==dest[s]):
##                           instruction[i]['R']=clock
                        if(ins1[2]==dest[s] or ins1[3]==dest[s]):
                           raw=raw+1
                           break
                        else:
                           if(ins1[2]!=dest[s] or ins1[3]!=dest[s]):
                              dest[i]=ins1[1]
                              f.append(ins1[2])
                              f.append(ins1[3])
                              src[i]=f
                              instruction[i]['R']=clock
                              read[i]=1
               if(op1=='divide'):
                  for s in range(0,len(dest)):
##                        if(clock==3 or ins1[1]==dest[s]):
##                           instruction[i]['R']=clock
##                        
                        if(ins2[2]==dest[s] or ins1[3]==dest[s]):
                           raw=raw+1
                           break
                        else:
                           if(ins1[2]!=dest[s] or ins1[3]!=dest[s]):
                              dest[i]=ins1[1]
                              f.append(ins1[2])
                              f.append(ins1[3])
                              src[i]=f
                              instruction[i]['R']=clock
                              read[i]=1
                  
              
            #execute
            if(instruction[i]['F']!=0 and instruction[i]['I']!=0 and instruction[i]['R']!=0 and instruction[i]['E']==0 and clock!=instruction[i]['R']):
               ins2=ip.call_instruction(i)
               op2=ins2[0]
               #print('enter execute')
               if(op2=='integer'):
                  #print('enter integer execute')
                  instruction[i]['E']=clock
                  execute[i]=1
               if(op2=='adder'):
                  #print(' enter add execute')
                  latency_clock_add=int(add['clock'])
                  diff_add=diff_add+1
                  if(diff_add==latency_clock_add):
                     instruction[i]['E']=clock
                     execute[i]=1
                     
                  
               if(op2=='multi'):
                  #print('enter multi execute')
                  latency_clock_multi=int(mult['clock'])
                  diff_mul= diff_mul+1
                  #d=clock+lat
                  if(diff_mul==latency_clock_multi):
                     instruction[i]['E']=clock
                     execute[i]=1
               
##                  
               if(op2=='divide'):
                  latency_clock_divide=int(div['clock'])
                  diff_div=diff_div+1
                  if(diff_div==latency_clock_divide):
                     instruction[i]['E']=clock
                     execute[i]=1
                
            if(instruction[i]['F']!=0 and instruction[i]['I']!=0 and instruction[i]['R']!=0 and instruction[i]['E']!=0 and instruction[i]['W']==0 and clock!=instruction[i]['E']):
               ins3=ip.call_instruction(i)
               op3=ins3[0]
               if(op3=='integer'):
                  inti['busy']=0
                  inti_free=clock
               if(op3=='adder' and add_count>0):
                  add_count-=1
                  add_free=clock
               if(op3=='multi' and multi_count>0):
                  multi_count-=1
                  mul_free=clock
               if(op3=='divide' and div_count >0):
                  div_count-=1
                  div_free=clock
                  
               instruction[i]['W']=clock
               dest[i]=0
               if(instruction[n-1]['W']!=0):
                  flag=0
               
               #write[i]=1
       clock=clock+1
    print (dest)
    return instruction
    
print(scoreboard())

   
      

      
            
               
               
                  
               
                  
                  
                  
                  
                           
                     
                     
                     
                  
               
                  
##                issue[i]=1
##                fetch_flag=0
##                instruction[i][1]==1
##                
##            #read
##            if(issue_1[i]==1):
##                ins=ip.call_instruction(i)
##                op=ins[0]
##                if(op=='integer'):
##                    if(inti['busy']==1):
##                        break
##                    elif(inti['busy']=0):
##                        for j in range(0,len(dest)):
##                            if(ins[1]==dest[i]):
##                                break
##                            elif(ins[1]!=dest[i]):
##                                instruction[i][2]=clock
##                                read[i]=1
##                                for k in range(0,len(src)):
##                                    if(ins[2]!=src[k]):
##                                        src.append(ins[2])
##                                    if(ins[3]!=src[k]):
##                                        src.append(ins[3])
##            if(op=='adder'):
##               if(add['busy']==1:o
##                  break
##               elif(add['busy']=0):
##                  for j in range(0,len(dest)):
##                            if(ins[1]==dest[i]):
##                                break
##                            elif(ins[1]!=dest[i]):
##                                 instruction[i][2]=clock
##                                 read[i]=1
##                                 for k in range(0,len(src)):
##                                       if(ins[2]!=src[k]):
##                                          src.append(ins[2])
##                                       if(ins[3]!=src[k]):
##                                          src.append(ins[3])
##            if(op=='multi'):
##                  if(mult['busy']==1):
##                      break
##                  elif(mult['busy']=0):
##                      for j in range(0,len(dest)):
##                         if(ins[1]==dest[i]):
##                                    break
##                              elif(ins[1]!=dest[i]):
##                                  instruction[i][2]=1
##                                  read[i]=1
##                                  for k in range(0,len(src)):
##                                      if(ins[2]!=src[k]):
##                                          src.append(ins[2])
##                                      if(ins[3]!=src[k]):
##                                          src.append(ins[3])
##             if(op=='multi'):
##                  if(mult['busy']==1):
##                      break
##                  elif(mult['busy']=0):
##                      for j in range(0,len(dest)):
##                           if(ins[1]==dest[i]):
##                                 break
##                           elif(ins[1]!=dest[i]):
##                                 instruction[i][2]=1
##                                 read[i]=1
##                                 for k in range(0,len(src)):
##                                    if(ins[2]!=src[k]):
##                                       src.append(ins[2])
##                                    if(ins[3]!=src[k]):
##                                       src.append(ins[3])
##            if(op=='divide'):
##                  if(div['busy']==1):
##                        break
##                  elif(div['busy']=0):
##                        for j in range(0,len(dest)):
##                           if(ins[1]==dest[i]):
##                                 break
##                           elif(ins[1]!=dest[i]):
##                                instruction[i][2]=clock
##                                read[i]=1
##                                for k in range(0,len(src)):
##                                    if(ins[2]!=src[k]):
##                                       src.append(ins[2])
##                                    if(ins[3]!=src[k]):
##                                       src.append(ins[3])
##                        
##                         
##                #Execute
##            if(instruction[i][0]==1 and ):
##                
##                            
##                for i in range(0, len(register)):
##                    if(ins[1]!=register[i]):
##                            register[ins[1]]=1
##                        else:
##                            continue
##                        if(ins[2]!=register[i]):
##                            register[ins[1]]=1
##                        else:
##                            continue
##                        if(ins[3]!=register[i]):
##                            register[ins[1]]=1
##                        else:
##                            continue
##                
##                
##                
##                
##                
##            
##        
##    
##    
##        
##    
##        
##    
##
##
##
