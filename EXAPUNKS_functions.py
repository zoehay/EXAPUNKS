import EXAPUNKS_data as exadata


#print(instructions, end= '')                
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
    if instr[0] in exadata.code:
        #check case of copy
        if instr[0] == 'copy':
            check_copy_code(instr)
        else :
            check_code(instr)


def check_reg_or_num(arg):
    if arg in exadata.code or type(arg) is int:
        return True
    else:
        return False

def check_copy_code():
    pass
    # check len of 2
    # check rest of inputs 
    

def check_code(instr):
    #check len stuff first 
    #check rest of inputs
    if check_reg_or_num(instr[1][0]) and check_reg_or_num(instr[1][1]):
        if instr[1][2] in exadata.regs:
            return True
        else:
            return ValueError(f'not a valid register destination')
    else:
        raise ValueError(f'invalid input argument')

#COPY R/N R
def copy(num,reg):
    '''Copy the value of the first operand into the second operand'''
    exadata.regs[reg] = num
    return exadata.regs[reg]

#ADDI R/N R/N R
def addi(num1,num2,reg):
    '''Add the value of the first operand to the value of the second operand and
        store the result in the third operand'''
    exadata.regs[reg] = num1 + num2
    return exadata.regs[reg]

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