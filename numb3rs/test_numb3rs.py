from numb3rs import validate

def main():
    test_true()
    test_false()
    test_invalid_input()


def test_true():
    assert validate("1.1.1.1") == True

def test_false():
    assert validate("300.1.1.1") == False

def test_invalid_input():
    assert validate("cat") == False

if __name__ == "__main__":
    main()