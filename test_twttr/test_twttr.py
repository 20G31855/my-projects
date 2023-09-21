from twttr import shorten


def main():
    test_vowel_removal()
    test_numbers()

def test_vowel_removal():
    assert shorten("love")== "lv"
    assert shorten("LOVE")== "LV"
    assert shorten("love")== "lv"
    assert shorten("LovE")== "Lv"

def test_numbers():
    assert shorten("1234")== "1234"


if __name__ == "__main__":
    main()