import EXAPUNKS_functions
from EXAPUNKS_functions import *

# dictionary of registers and list of codes
regs = {'X': 0,  'T': 0, 'F': 0}
codes = ['copy', 'addi', 'subi', 'multi', 'divi', 'modi']

instructions = '''COPY 70 X
ADDI X 1 X
COPY 3 T
MULI T X T
SUBI T 1 T'''
l_instr =[]

