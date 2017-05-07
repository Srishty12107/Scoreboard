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

dest=[]
dest.append(inst[1])
src=[]
src.append(inst[2])
src.append(inst[3])
#src[inst[3]]=1

#scoreboard_implement
#clok variables
latency_clock_add=0
latency_clock_multi=0
latency_clock_divide=0

##dest={}
##src={}
##l=[]
##insq=ip.call_instruction(0)
##dest[0]=insq[1]
##l.append(insq[2])
##l.append(insq[3])
##src[0]=l
##clock=1

def scoreboard():
    #print('enter')
    
    print (clock)
    fetch_flag=0
    add_count=0
    multi_count=0
    div_count=0
    while(clock<=62):
        global clock
        
        for i in range(0,6):
            if(instruction[i]['F']==0):# and fetch_flag==0):
                if(fetch_flag==0 and fetch_1[i]==0):
                    fetch_1[i]=1
                    instruction[i]['F']=clock
                    #print(i,'-',instruction[i]['F'])
                    fetch_flag=1
      
            #issue
            if(instruction[i]['F']!=0 and instruction[i]['I']==0 and clock!=instruction[i]['F']):
               print ('enter issue')
               ins=ip.call_instruction(i)
               op=ins[0]
               if(op=='integer'):
                  #print ('found unit in issue')
                  if(inti['busy']==0):
                     issue[i]=1
                     fetch_flag=0
                     inti['busy']=1
                     instruction[i]['I']=clock
##                     for g1 in range(0,len(instruction)):
##                        if(clock!=instruction[1]['W']):
##                           instruction[i]['I']=clock
##                     
####                  else:
##                     if(inti['busy']!=0):
##                        continue
               if(op=='adder'):
                  w=add['no.']
                  if(add_count<=int(w)):
                     issue[i]=1
                     fetch_flag=0
                     add_count+=1
                     instruction[i]['I']=clock
                     #high
##                     for g1 in range(0,len(instruction)):
##                        if(clock!=instruction[g1]['W']):
##                           instruction[i]['I']=clock
##                  else:
##                     if(add_count>w):
##                        continue
               if(op=='multi'):
                  w1=mult['no.']
                  if(multi_count<=int(w1)):
                     issue[i]=1
                     fetch_flag=0
                     multi_count+=1
                     instruction[i]['I']=clock
##                     for g1 in range(0,len(instruction)):
##                        if(clock!=instruction[g1]['W']):
##                           instruction[i]['I']=clock
##                  else:
##                     continue
               if(op=='divide'):
                  w2=div['no.']
                  if(div_count<=int(w2)):
                     issue[i]=1
                     fetch_flag=0
                     div_count+=1
                     instruction[i]['I']=clock
##                     for g1 in range(0,len(instruction)):
##                        if(clock!=instruction[g1]['W']):
##                           instruction[i]['I']=clock
##                  else:
##                     continue
            #read
            if(instruction[i]['F']!=0 and instruction[i]['I']!=0 and instruction[i]['R']==0 and clock!=instruction[i]['I']):# and clock!=instruction[i]['W']):
               print ('enter read',clock)
               ins1=ip.call_instruction(i)
               op1=ins1[0]
               print ('op1',i)
               if(op=='integer'):
##                   if(clock==1):
##                        instruction[i]['R']=clock
##                        print('done for 1')
##                   else:
##                     for s in range(0,i-1):
##                        if(ins1[2]==dest[i-1] or ins1[3]==dest[i-1]):
##                           raw=raw+1
##                        # and clock):
##                        
##                        else:
##                           dest[i]=ins1[1]
##                           f.append(ins1[2])
##                           f.append(ins1[3])
##                           src[i]=f
##                           instruction[i]['R']=clock
##                           read[i]=1
                        
                  for j in range(0,len(dest)):
                     #print(dest,ins1[1])
                     if(ins1[1]==dest[j] or clock==1):
                        print ('enter check point',clock)
                        instruction[i]['R']=clock
                        continue
                     else:
                        if(ins1[1]!=dest[j]):
                           dest.append(ins1[1])
                           read[i]=1
                           instruction[i]['R']=clock
                           
                           print('update read clock')
                           for k in range(0,len(src)):
                              if(ins1[2]==src[k]):
                                 continue
                              else:
                                 src.append(ins1[2])
                              if(ins1[3]==src[k]):
                                 continue
                              else:
                                 src.append(ins1[3])
               if(op=='adder'):
##                   if(clock==1):
##                        instruction[i]['R']=clock
##                        print('done for 1')
##                   else:
##                     for s in range(0,i-1):
##                        if(ins1[2]==dest[i-1] or ins1[3]==dest[i-1]):
##                           raw=raw+1
##                        # and clock):
##                        
##                        else:
##                           dest[i]=ins1[1]
##                           f.append(ins1[2])
##                           f.append(ins1[3])
##                           src[i]=f
##                           instruction[i]['R']=clock
##                           read[i]=1
                        
                  for j in range(0,len(dest)):
                     if(ins1[1]==dest[j] or clock==1):
                        instruction[i]['R']=clock
                     else:
                        if(ins1[1]!=dest[j]):
                           dest.append(ins1[1])
                           read[i]=1
                           instruction[i]['R']=clock
                           for k in range(0,len(src)):
                              if(ins1[2]==src[k]):
                                 continue
                              else:
                                 src.append(ins1[2])
                              if(ins1[3]==src[k]):
                                 continue
##                              else:
##                                 src.append(ins1[3])
               if(op=='multi'):
##                   if(clock==1):
##                        instruction[i]['R']=clock
##                        print('done for 1')
##                   else:
##                     for s in range(0,i-1):
##                        if(ins1[2]==dest[i-1] or ins1[3]==dest[i-1]):
##                           raw=raw+1
##                        # and clock):
##                        
##                        else:
##                           dest[i]=ins1[1]
##                           f.append(ins1[2])
##                           f.append(ins1[3])
##                           src[i]=f
##                           instruction[i]['R']=clock
##                           read[i]=1
##                        
                   for j in range(0,len(dest)):
                     if(ins1[1]==dest[j] or clock==1):
                        instruction[i]['R']=clock
                        #continue
                     else:
                        if(ins1[1]!=dest[j]):
                           dest.append(ins1[1])
                           read[i]=1
                           instruction[i]['R']=clock
                           for k in range(0,len(src)):
                              if(ins1[2]==src[k]):
                                 continue
                              else:
                                 src.append(ins1[2])
                              if(ins1[3]==src[k]):
                                 continue
                              else:
                                 src.append(ins1[3])
               if(op=='divide'):
##                   if(clock==1):
##                        instruction[i]['R']=clock
##                        print('done for 1')
##                  else:
##                     for s in range(0,i-1):
##                        if(ins1[2]==dest[i-1] or ins1[3]==dest[i-1]):
##                           raw=raw+1
##                        # and clock):
##                        
##                        else:
##                           dest[i]=ins1[1]
##                           f.append(ins1[2])
##                           f.append(ins1[3])
##                           src[i]=f
##                           instruction[i]['R']=clock
##                           read[i]=1
                        
                   for j in range(0,len(dest)):
                     if(ins1[1]==dest[j] or clock==1):
                        instruction[i]['R']=clock
                        #continue
                     else:
                        if(ins1[1]!=dest[j]):
                           dest.append(ins1[1])
                           #read[i]=1
                           read[i]=1
                           instruction[i]['R']=clock
                           for k in range(0,len(src)):
                              if(ins1[2]==src[k]):
                                 continue
                              else:
                                 src.append(ins1[2])
                              if(ins1[3]==src[k]):
                                 continue
                              else:
                                 src.append(ins1[3])
                              
              
               #execute
            if(instruction[i]['F']!=0 and instruction[i]['I']!=0 and instruction[i]['R']!=0 and instruction[i]['E']==0 and clock!=instruction[i]['R']):
               ins2=ip.call_instruction(i)
               op=ins2[0]
               print('enter execute')
               if(op=='integer'):
                  print('enter integer execute')
                  instruction[i]['E']=clock
                  execute[i]=1
               if(op=='adder'):
                  print(' enter add execute')
                  latency_clock_add=int(add['clock'])
                  if(clock==latency_clock_add):
                     instruction[i]['E']=clock
                     execute[i]=1
                     
                  #instruction[i]['E']=clock
##                  for g in range(0,latency_clock_add):
##                     d=latency_clock_add-clock
##                     if(.d==0):
##                        clock=latency_clock_add
##                        execute[i]=1
               if(op=='multi'):
                  print('enter multi execute')
                  latency_clock_multi=int(mult['clock'])
                  #d=clock+lat
                  if(clock==latency_clock_multi):
                     instruction[i]['E']=clock
                     execute[i]=1
               
##                  instruction[i]['E']=clock
##                  for g in range(0,latency_clock_multi):
##                     d=latency_clock_multi-clock
##                     print ('d:1',d)
##                     if(d==0):
##                        clock=latency_clock_multi
##                        print('clock update', clock)
##                        print('done updation of clock')
##                        execute[i]=1
               if(op=='divide'):
                  latency_clock_divide=int(div['clock'])
                  if(clock==latency_clock_divide):
                     instruction[i]['E']=clock
                     execute[i]=1
                  
##                  instruction[i]['E']=clock
##                  for g in range(0,latency_clock_divide):
##                     d=latency_clock_divide-clock
##                     if(d==0):
##                        clock=latency_clock_divide
##                        execute[i]=1

               #writeback
            if(instruction[i]['F']!=0 and instruction[i]['I']!=0 and instruction[i]['R']!=0 and instruction[i]['E']!=0 and instruction[i]['W']==0 and clock!=instruction[i]['E']):
               ins3=ip.call_instruction(i)
               op3=ins3[0]
               if(op=='integer'):
                  inti['busy']=0
               if(op=='adder' and add_count>0):
                  add_count-=1
               if(op=='multi' and multi_count>0):
                  multi_count-=1
               if(op=='divide' and div_count >0):
                  div_count-=1
                  
               instruction[i]['W']=clock
               
               #write[i]=1
        clock=clock+1
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
