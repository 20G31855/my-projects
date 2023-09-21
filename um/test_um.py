from um import count


def main():
    test_um()
    test_um_with_right_boundary()
    test_um_with_left_boundary()
    test_multiple_inputs()



def test_um():
    assert count("um")== 1


def test_um_with_right_boundary():
    assert count("hum")== 0


def test_um_with_left_boundary():
    assert count("umi") == 0


def test_multiple_inputs():
    assert count("um, hum, yummy, um") == 2


if __name__ == "__main__":
    main()