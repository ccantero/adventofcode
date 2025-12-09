import unittest

from src.invalidIDs import getListOfNSubstrings, isNotLegitID, getInvalidIdsFromRange, isNotLegitIDNew
class TestInvalidIDs(unittest.TestCase):
    def test_isNotLegitID(self):
        assert isNotLegitID(11) == True
        assert isNotLegitID(22) == True
        assert isNotLegitID(10) == False
        assert isNotLegitID(100) == False
        assert isNotLegitID(1010) == True
    
    def test_isNotLegitIDNew(self):
        assert isNotLegitIDNew(11) == True
        assert isNotLegitIDNew(22) == True
        assert isNotLegitIDNew(10) == False
        assert isNotLegitIDNew(100) == False
        assert isNotLegitIDNew(1010) == True
        assert isNotLegitIDNew(111) == True
        assert isNotLegitIDNew(565656) == True
        assert isNotLegitIDNew(446446) == True
        assert isNotLegitIDNew(38593859) == True
        assert isNotLegitIDNew(2121212121) == True
        assert isNotLegitIDNew(824824824) == True
        
    def test_getInvalidIdsFromRange(self):
        assert getInvalidIdsFromRange("1-10") == []
        assert getInvalidIdsFromRange("59593-59595") == []
        assert getInvalidIdsFromRange("11-22") == [11, 22]
        assert getInvalidIdsFromRange("95-115") == [99,111]
        assert getInvalidIdsFromRange("998-1012") == [999, 1010]
        assert getInvalidIdsFromRange("1188511880-1188511890") == [1188511885]
        assert getInvalidIdsFromRange("222220-222224") == [222222]
        assert getInvalidIdsFromRange("1698522-1698528") == []
        assert getInvalidIdsFromRange("446443-446449") == [446446]
        assert getInvalidIdsFromRange("565653-565659") == [565656]
        assert getInvalidIdsFromRange("38593856-38593862") == [38593859]
        assert getInvalidIdsFromRange("2121212118-2121212124") == [2121212121]
        


    def test_getListOfNSubstrings(self):
        assert getListOfNSubstrings("121212",3) == ['12', '12', '12']

if __name__ == '__main__':
    unittest.main() 