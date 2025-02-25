from main import Bank

bankObj = Bank()

def test_getAmount():
    assert bankObj.getAmount() == 0

def test_deposit():
    bankObj.deposit(1000)
    assert bankObj.getAmount() == 1000