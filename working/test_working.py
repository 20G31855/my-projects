import pytest
from working import convert


def main():
    test_ValueError()
    test_DigitInput()
    test_IntegerInput()


def test_ValueError():
    with pytest.raises(ValueError):
        assert convert("09:60 AM to 05:60 PM")== ValueError


def test_DigitInput():
    assert convert("09:30 AM to 05:30 PM")== ("09:30 to 17:30")


def test_IntegerInput():
    assert convert("9 AM to 5 PM")==("09:00 to 17:00")



if __name__ == "__main__":
    main()