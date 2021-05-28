import main as GSM
import random, string
#Function 1-2: tests data that should be rejected

#Comment 1: test if non-integers are entered
def test_data_verification_nonintegers():
    l = random.choice(string.ascii_letters)
    assert GSM.data_verification(l) == False

#Comment 2: test if negative numbers are entered
def test_data_verification_negatives():   
    n = random.randrange(-50,-1)
    assert GSM.data_verification(n) == False

#Function 3-4: test data that is accepted by the code

#Comment 3: tests if positive integers are entered
def test_data_verification_int_datatype():
    i = random.randrange(0,50)
    assert GSM.data_verification(i) == float(i)

#Comment 4: test if float data is entered
def test_data_verification_float():
    f = round(random.uniform(1,50), 2)
    assert GSM.data_verification(f) == f