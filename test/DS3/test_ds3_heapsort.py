import sys
sys.path.append("test")
import sort_tester
import unittest
sys.path.append("grp-DS3")
from heapsort import heapsort

class InsertionTest(sort_tester.SortTester):
    # This needs to be here for an unstable sort;
    # SortTester defines this to return True
    def isStable(self):
        return False

    #TestSorts expects in-place sort
    def sort(self,items):
        heapsort(items)

if __name__ == '__main__':
    unittest.main()
