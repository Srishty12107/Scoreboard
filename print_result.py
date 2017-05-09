import functionalunitparser as fp
import instruction_parser as ip
f1=open('Functional unit.txt','r')
f2=open('instruction set.txt','r')
f3=open('result.txt','w+')
lines=f2.readlines()
p='instruction'+'\t'+'\t'+'Fetch'+'\t'+'Issue'+'\t'+'Read'+'\t'+'Execute'+'\t'+'\t'+'Write'+'\n'
print (p)
p1="hello"
f3.write(p)
instruction={0: {'R': 3, 'F': 1, 'E': 4, 'W': 5, 'I': 2}, 1: {'R': 6, 'F': 2, 'E': 7, 'W': 8, 'I': 5}, 2: {'R': 9, 'F': 5, 'E': 10, 'W': 11, 'I': 8}, 3: {'R': 12, 'F': 8, 'E': 13, 'W': 14, 'I': 11}, 4: {'R': 15, 'F': 11, 'E': 16, 'W': 17, 'I': 14}, 5: {'R': 18, 'F': 14, 'E': 19, 'W': 20, 'I': 17}, 6: {'R': 21, 'F': 17, 'E': 22, 'W': 23, 'I': 20}, 7: {'R': 22, 'F': 20, 'E': 24, 'W': 25, 'I': 21}, 8: {'R': 23, 'F': 21, 'E': 0, 'W': 0, 'I': 22}, 9: {'R': 24, 'F': 22, 'E': 54, 'W': 55, 'I': 23}, 10: {'R': 25, 'F': 23, 'E': 0, 'W': 0, 'I': 24}, 11: {'R': 26, 'F': 24, 'E': 0, 'W': 0, 'I': 25}, 12: {'R': 0, 'F': 25, 'E': 0, 'W': 0, 'I': 0}, 13: {'R': 0, 'F': 0, 'E': 0, 'W': 0, 'I': 0}, 14: {'R': 0, 'F': 0, 'E': 0, 'W': 0, 'I': 0}, 15: {'R': 0, 'F': 0, 'E': 0, 'W': 0, 'I': 0}}

def line(line,i,instruction):
    #f=len(instruction)
    #print('instruction','\t','Fetch','\t','Issue','\t','Read','\t','Execute','\t','Writ
    sm=str(line)+'\t'+'\t'+'\t'+str(instruction[i]['F'])+'\t'+str(instruction[i]['I'])+'\t'+str(instruction[i]['R'])+'\t'+str(instruction[i]['E'])+'\t'+'\t'+str(instruction[i]['W'])+'\n'
    f3.write(sm)
    return sm
def print1(instruction):
    lines=f2.readlines()
    for i in range(0,len(lines)):
        print (lines[i])
        print(line(lines[i],i,instruction))
#print(line(lines[0],0,instruction))
print1(instruction)
f3.close() 
          
