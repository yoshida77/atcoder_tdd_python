import signed_difficulty


def test_convert_0to2():
    output_value = signed_difficulty.convert("1.0")
    assert output_value == "1-"


def test_convert_3to6():
    output_value = signed_difficulty.convert("12.5")
    assert output_value == "12"


def test_convert_7to9():
    output_value = signed_difficulty.convert("15.8")
    assert output_value == "15+"
