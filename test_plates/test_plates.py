from plates import is_valid
def main():
    test_max_min_characters()
    test_start_with_two_letters()
    test_no_extras()
    test_no_number_in_middle()
    test_cannot_start_with_zero()


def test_max_min_characters():
    assert is_valid("w") == False
    assert is_valid ("asdsdsw")== False
def test_start_with_two_letters():
    assert is_valid("1sdd") == False
    assert is_valid("w2kk") == False
    assert is_valid("22ss") == False
def test_no_extras():
    assert is_valid("wwd#dd") == False
def test_no_number_in_middle():
    assert is_valid("sdc3d") == False
def test_cannot_start_with_zero():
    assert is_valid("ddd04") == False


if __name__ == "__main__":
    main()