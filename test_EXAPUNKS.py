#from re import X
#from tempfile import TemporaryFile 

from EXAPUNKS_functions import *
#from EXAPUNKS_functions import regs, copy, addi

#unit function testing
#words[0] should be instruction, check if valid instruction 
#if valid, call instruction and use shared function to validate 


# test codes behavior with good inputs

def test_copy():
    assert copy(70, regs['X']) == 70

def test_addi():
    assert addi(regs['X'], 1, regs['X']) == regs['X'] + 1
 
def test_subi():
    assert subi(regs['X'], 1, regs['T']) == regs['X'] -1

def test_muli():
    assert muli(regs['T'], regs['X'], regs['T']) == regs['T'] * regs['X']

def test_divi():
    assert div(regs['T'], regs['X'], regs['T']) == regs['T'] / regs['X']

def test_modi():
    assert modi(regs['X'], 2, regs['T']) == regs['X'] % 2


# input testing

    # test invalid code
def test_invalid_code_gernerates_exception():
    try:
        copy('hello', 1, reg['X'])
    except ValueError:
        assert True 

# test invalid input to copy


# pass valid code with invalid inputs should 

def test_valid_code_invalid_input_generates_exception():
    try:
        addi(regs['X'], 'a', regs['X'])
    except ValueError:
        assert True


    # test
def test_valid_code_valid_input_invalid_reg_generates_exception():
    try:
        addi(regs['X'], 2, 3)
    except ValueError:
        assert True




# pass empty should throw error 


