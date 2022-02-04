#from re import X
#from tempfile import TemporaryFile 
#import EXAPUNKS_functions
#from codecs import register
#from EXAPUNKS_functions import *
#from EXAPUNKS_functions import regs, copy, addi
import EXAPUNKS_functions as exafunc
import EXAPUNKS_data as exadata

#unit function testing
#words[0] should be instruction, check if valid instruction 
#if valid, call instruction and use shared function to validate 


# test codes behavior with good inputs

def test_copy():
    assert exafunc.copy(70, exadata.regs['X']) == 70

def test_addi():
    assert exafunc.addi(exadata.regs['X'], 1, exadata.regs['X']) == exadata.regs['X'] + 1
 
def test_subi():
    assert exafunc.subi(exadata.regs['X'], 1, exadata.regs['T']) == exadata.regs['X'] -1

def test_muli():
    assert exafunc.muli(exadata.regs['T'], exadata.regs['X'], exadata.regs['T']) == exadata.regs['T'] * exadata.regs['X']

def test_divi():
    assert exafunc.divi(exadata.regs['T'], exadata.regs['X'], exadata.regs['T']) == exadata.regs['T'] / exadata.regs['X']

def test_modi():
    assert exafunc.modi(exadata.regs['X'], 2, exadata.regs['T']) == exadata.regs['X'] % 2


# input testing

    # test invalid code
def test_invalid_code_gernerates_exception():
    try:
        exafunc.copy('hello', 1, exadata.regs['X'])
    except ValueError:
        assert True 

# test invalid input to copy


# pass valid code with invalid inputs should 

def test_valid_code_invalid_input_generates_exception():
    try:
        exafunc.addi(exadata.regs['X'], 'a', exadata.regs['X'])
    except ValueError:
        assert True


    # test
def test_valid_code_valid_input_invalid_reg_generates_exception():
    try:
        exafunc.addi(exadata.regs['X'], 2, 3)
    except ValueError:
        assert True




# pass empty should throw error 


