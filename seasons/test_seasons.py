from seasons import check_birthday, minuites_lived

def main():
    test_1()
    test_2()


def test_1():
    assert check_birthday("2002-03-24") == "Eleven million, two hundred ninety-nine thousand, six hundred eighty minuites"
    assert check_birthday('2000-06-22') == "Twelve million, two hundred twenty-one thousand, two hundred eighty minuites"

def test_2():
    assert minuites_lived(23, 1, 2000) == "Invalid Date"

if __name__ == "__main__":
    main()