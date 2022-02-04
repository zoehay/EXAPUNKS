# create function definitions for different instructions

regs = {'X': 0,  'Y': 0, 'F': 0}
codes = ['copy', 'addi', 'subi', 'multi', 'divi', 'modi']

def processInput(inputstring):
    inputstring.split()
    print(inputstring)

def validate_instructions(instr):
    if instr[0] in codes:
        pass
    else:
        return('Invalid instruction')
    #check case of copy
    if instr[0] == 'copy':
        if instr[1]:
            pass
            #valid input
        else:
             'Invalid args'
     #else its one of the other instructions


#COPY R/N R
def copy(num,reg):
    '''Copy the value of the first operand into the second operand'''
    regs[reg] = num
    return regs[reg]

#ADDI R/N R/N R
def addi(num1,num2,reg):
    '''Add the value of the first operand to the value of the second operand and
        store the result in the third operand'''
    regs[reg] = num1 + num2
    return regs[reg]

#`SUBI R/N R/N R`  
  
def subi(num1,num2,reg):
    '''Subtract the value of the first operand from the value of second operand
        and store the result in the third operand'''
    reg = num2 - num1
    return reg

#`MULI R/N R/N R`
def muli(num1,num2,reg):
    '''multiplies first two operands and stores result in third.'''
    reg = num1 * num2
    return reg

def divi(num1,num2,reg):
    '''Divides first two operands and stores result in third.'''
    reg = num1 / num2
    return reg

def modi(num1, num2, reg):
    '''Modulo first two operands and stores result in third.'''
    reg = num1 % num2
    return reg
