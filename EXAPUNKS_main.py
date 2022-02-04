import EXAPUNKS_functions as exafunc
import EXAPUNKS_data as exadata
import sys
#from EXAPUNKS_functions import *
#from EXAPUNKS_functions import *

# dictionary of registers and list of codes
#regs = {'X': 0,  'T': 0, 'F': 0}
#codes = ['copy', 'addi', 'subi', 'multi', 'divi', 'modi']

instructions = '''COPY 647 X
MODI X 7 T
DIVI X T X
MULI T T T
MULI X T X
MULI T T T
ADDI X T X
DIVI T 9 T
ADDI X 3 X
ADDI T X T
ADDI T X X
SUBI X T T
SUBI X T X
SUBI X T X'''

list_instructions = exafunc.read_lines(instructions)
print(list_instructions)

for instruction in list_instructions:
    exafunc.validate_instructions(instruction)
    print('processing:', instruction)

print(sys.argv[0])