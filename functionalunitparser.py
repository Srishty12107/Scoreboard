#functionalUnitparser
#f=open('Functional unit.txt','r')
add={}
mult={}
div={}
inti={}
def func_parse(filename):
    f=open(filename)
    lines=f.readlines()
    for i in range(0,3):
        word=lines[i].split()
        #print (word)
        for words in word:
            if(words=='Adder:'):
                s=word[2].split(',')
                add['no.']=s[0]
                add['clock']=s[1]
            if(words=='Mult:'):
                s=word[2].split(',')
                print (s)
                mult['no.']=s[0]
                mult['clock']=s[1]
            if(words=='Div:'):
                s=word[2].split(',')
                print (s)
                div['no.']=s[0]
                div['clock']=s[1]
            if(words=='Int:'):
                s=word[2].split(',')
                print (s)
                inti['no.']=s[0]
                inti['clock']=s[1]
    return(add,mult,div,inti)
#print (func_parse())          
    
