from romans import to_roman


class TestRomans(object):
    def test_one(self):
        assert to_roman(1) == 'I'

    def test_two_three(self):
        assert to_roman(2) == 'II'
        assert to_roman(3) == 'III'

    def test_four(self):
        assert to_roman(4) == 'IV'

    def test_five(self):
        assert to_roman(5) == 'V'

    def test_six_seven_eight(self):
        assert to_roman(6) == 'VI'
        assert to_roman(7) == 'VII'
        assert to_roman(8) == 'VIII'

    def test_nine(self):
        assert to_roman(9) == 'IX'

    def test_ten(self):
        assert to_roman(10) == 'X'

    def test_twenty_fifteen(self):
        assert to_roman(2015) == 'MMXV'
