from unicodedata import numeric
import EXAPUNKS_data
import string
####################
# "code" instruction definitions

#COPY R/N R
def copy(num,reg):
    '''Copy the value of the first operand into the second operand'''
    EXAPUNKS_data.regs[reg] = num
    return EXAPUNKS_data.regs[reg]

#ADDI R/N R/N R
def addi(num1,num2,reg):
    '''Add the value of the first operand to the value of the second operand and
        store the result in the third operand'''
    EXAPUNKS_data.regs[reg] = num1 + num2
    return EXAPUNKS_data.regs[reg]

#`SUBI R/N R/N R`  
  
def subi(num1,num2,reg):
    '''Subtract the value of the first operand from the value of second operand
        and store the result in the third operand'''
    EXAPUNKS_data.regs[reg] = num1 - num2
    return EXAPUNKS_data.regs[reg]

#`MULI R/N R/N R`
def muli(num1,num2,reg):
    '''multiplies first two operands and stores result in third.'''
    EXAPUNKS_data.regs[reg] = num1 * num2
    return EXAPUNKS_data.regs[reg]

def divi(num1,num2,reg):
    '''Divides first two operands and stores result in third.'''
    EXAPUNKS_data.regs[reg] = num1 / num2
    return EXAPUNKS_data.regs[reg]

def modi(num1, num2, reg):
    '''Modulo first two operands and stores result in third.'''
    EXAPUNKS_data.regs[reg] = num1 % num2
    return EXAPUNKS_data.regs[reg]

#######################
# input checking helper functions
def check_reg_or_num(arg):
    if arg.isnumeric():
        return True
    elif arg in EXAPUNKS_data.regs:
        return True
    else:
        return False

def to_int(thing):
    if thing.isnumeric():
        return int(thing)
    if thing in EXAPUNKS_data.regs.keys():
        return EXAPUNKS_data.regs[thing]


def check_copy_code(instr):
    """checks for vaild inputs to the copy function
    returns True if valid, error if not"""
    # check len of 2
    if len(instr[1]) != 2:
        raise ValueError(f'wrong number of inputs')
    # check rest of inputs
    if check_reg_or_num(instr[1][0]):
        if instr[1][1] in EXAPUNKS_data.regs:
            return True
            
        else:
            raise ValueError(f'not a valid register destination')
    else:
        raise ValueError(f'invalid input argument')
    
def check_code(instr):
    """checks for vaild inputs to the other functions
    returns True if valid, error if not"""
    #check len of 3 
    if len(instr[1]) != 3:
        return ValueError(f'wrong number of inputs')
    #check rest of inputs
    if check_reg_or_num(instr[1][0]) and check_reg_or_num(instr[1][1]):
        if instr[1][2] in EXAPUNKS_data.regs:
            return True
        else:
            return ValueError(f'not a valid register destination')
    else:
        raise ValueError(f'invalid input argument')


####################
# input processing functions 
def read_lines(instructions):
    l_instr =[]
    '''reads lines of instructions, creates tuples of instructions and returns it as a list'''
    list_lines = instructions.split('\n')
    for line in list_lines:
        l_words = line.split()
        # creates tuples from instructions
        instr = ( l_words[0] , l_words[1:])
        # creates a list of tuples       
        l_instr.append(instr)
    #returns a list of tuples  
    return l_instr    

def validate_instructions(instr):
    '''takes a tuple as an argument and checks the instruction and operands'''
    if instr[0] in EXAPUNKS_data.codes:
        # check case of copy
        if instr[0] == 'COPY':
            if(check_copy_code(instr)):
                num1 = to_int(instr[1][0])
                print(copy(num1, instr[1][1])) # if true then all the inputs are good
    
        # check valid code not copy
        # if true then all inputs are good
        else :
            if check_code(instr): 
                #all inputs were good, now convert them to ints 
                num1 = to_int(instr[1][0])
                num2 = to_int(instr[1][1])
                if instr[0] == 'ADDI':
                    addi(num1, num2, instr[1][2])
                elif instr[0] == 'SUBI':
                    subi(num1, num2, instr[1][2])
                elif instr[0] == 'MULI':
                    muli(num1, num2, instr[1][2])
                elif instr[0] == 'DIVI':
                    divi(num1, num2, instr[1][2])
                elif instr[0] == 'MODI': 
                    modi(num1, num2, instr[1][2])
                else:
                    print('wrong instruction')
    print(EXAPUNKS_data.regs)


