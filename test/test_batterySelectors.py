import unittest

from src.batterySelector import getMaxJoltage, getMaxJoltageNew
class TestBatterySelectors(unittest.TestCase):
    def test_getMaxJoltage(self):
        assert getMaxJoltage(811111111111119) == 89
        assert getMaxJoltage(987654321111111) == 98
        assert getMaxJoltage(234234234234278) == 78
        assert getMaxJoltage(818181911112111) == 92

    def test_getMaxJoltageNew(self):
        assert getMaxJoltageNew(811111111111119) == "811111111119"
        assert getMaxJoltageNew(987654321111111) == "987654321111"
        assert getMaxJoltageNew(234234234234278) == "434234234278"
        assert getMaxJoltageNew(818181911112111) == "888911112111"


if __name__ == '__main__':
    unittest.main() 