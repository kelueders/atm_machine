from atm_machine4_v2 import read_data

def test_read_data():
    expected = [
        ["Kate", "Bob", "Fred", "Ted"],
        ["123", "789", "345", "134"],
        [40.00, 20.00, 70.00, 20.00]
    ]
    assert read_data('P4ATMdata.txt') == expected