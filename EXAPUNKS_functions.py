



#print(instructions, end= '')                
def read_lines(instrutions):
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
    if instr[0] in codes:
        #check case of copy
        if instr[0] == 'copy':
            check_copy(instr)
        else :
            check_other


def check_reg_or_num(arg):
    if arg in codes or type(arg) is int:
        return True
    else:
        return False

def check_copy():
    # check len of 2
    # check rest of inputs 
    

def check_code(instr):
    #check len stuff first 

    #check rest of inputs
    if check_reg_or_num(instr[1][0]) and check_reg_or_num(instr[1][1]):
        if instr[1][2] in regs:
            return True
        else:
            return ValueError(f'not a valid register destination')
    else:
        raise ValueError(f'invalid input argument')