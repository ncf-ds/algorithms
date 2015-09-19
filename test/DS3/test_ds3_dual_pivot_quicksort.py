#!/usr/bin/env python
import sort_tester
import unittest
import sys
sys.path.append("grp-DS3")
from dual_pivot_quicksort import dual_pivot_quicksort

class InsertionTest(sort_tester.SortTester):
    # This needs to be here for an unstable sort;
    # SortTester defines this to return True
    def isStable(self):
        return False

    #TestSorts expects in-place sort
    def sort(self,items):
        dual_pivot_quicksort(items, 0, len(items)-1)

if __name__ == '__main__':
    unittest.main()
