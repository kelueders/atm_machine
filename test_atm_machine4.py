from atm_machine4 import read_file

def test_read_file_kate():
    assert read_file('123') == ['Kate', '123', 40.0]

def test_read_file():
    assert read_file('345') == ['Fred', '345', 70.0]