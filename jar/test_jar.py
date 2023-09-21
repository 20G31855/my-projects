from jar import jar

def test_init():
    jar = jar(4)
    assert jar.capacity == 4
    assert jar.size == 0
    jar1 = jar(3)
    assert jar1.capaciy == 12


def test_str():
    jar = jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = jar()
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(3)
    assert jar.size == 9


def test.withdraw():
    jar = jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3
    jar.withdraw(1)
    assert jar.size == 2