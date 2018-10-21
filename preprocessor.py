infile = "newtrace.txt" #input file

num = ['-','0','1','2','3','4','5','6','7','8','9'] # using array num to seperate numbers
# input path to file path here 
with open(infile) as f:
    f = f.readlines()

#from itertools import islice
#with open(infile) as f:                            #slicing one trace block using ##
#    f = f.readlines()
#index = [x for x in range(len(f)) if '#' in f[x].lower()]
#print(index)

#LOGIC TO READ REGISTER VALUES AND STORE THEM IN A DATA STRUCTURE
for line in f:
    
    c = str()
    if 'str' in line or 'stc' in line or 'strex' in line:
        sline = line[10:18]
        #THE CODE TO ADD REGISTER OFFSET
        #LOGIC TO FIND REGISTER IN THE LINE ie finding r1, r6, r9 etc
        #adding program counter to the register value according to register number
        #BELOW IS THE CODE TO ADD IMMEDIATE VALUE OFFSET
        if '#' in line:
            #print(line)
            index = line.find('#')
            hline = line[index+1:]
            for i in hline:
                if i in num:
                    c = c + i
                else:
                    break       
            print('W' + ' ' + hex(int(sline,16) + int(hex(int(c,10)),16))) # adding the decimal offset to hexadecimal PC and then printing the trace; can input to file also
        else:
            print('W' + ' 0x' + sline)

    if 'ldr' in line or 'ldm' in line or 'ldrex' in line or 'lsl' in line or 'lsr' in line: # checking for load
        
        lline = line[10:18] # the program counter
        if '#' in line:  # checking for offset
            #print(line)
            index = line.find('#')  #setting array index of #          
            hline = line[index+1:] # getting decimal offset
            for i in hline:
                if i in num:
                    c = c + i # getting the decimal value of offset
                else:
                    break         
            print('R' + ' ' + hex(int(lline,16) + int(hex(int(c,10)),16))) # printing the value ; can output to a file as well
        else:
            print('R' + ' 0x' + lline)
    #print(c)
        

#print(important)


