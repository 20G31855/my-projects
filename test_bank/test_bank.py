from bank import value


def main():
    test_hello()
    test_how_are_you()
    test_any_other_input()



def test_hello():
    assert value("hello")== 0


def test_how_are_you():
    assert value("how are you")== 20


def test_any_other_input():
    assert value("python is annoying sometimes") == 100


if __name__ == "__main__":
    main()