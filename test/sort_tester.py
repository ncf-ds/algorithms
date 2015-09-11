import unittest
from copy import copy
from random import randrange

class IntHolder:
    def __init__(self,val,serial):
        self.val = int(val)
        self.serial = serial

    def __eq__(self,other):
        return self.val == other.val

    def __neq__(self,other):
        return self.val != other.val

    def __cmp__(self,other):
        return self.val.__cmp__(other.val)

    def __hash__(self):
        return self.val

class SortTester(unittest.TestCase):
    def multiplicities(self,items):
        d = dict()
        for i in items:
            if not i in d:
                d[i] = 0
            d[i] += 1
        return d

    def assertSorted(self,orig,items):
        self.assertEqual(len(orig),len(items))
        for i in range(1,len(items)):
            self.assertTrue(items[i] >= items[i-1])
        self.assertEqual(self.multiplicities(orig),self.multiplicities(items))
    def trySorting(self,items):
        srt = copy(items)
        self.sort(srt)
        self.assertSorted(items,srt)
        return srt

    def test_inorder(self):
        for i in range(1,100):
            for d in [-1,1,-2,2]:
                items = range(1,i,d)
                self.trySorting(items)

    def test_random(self):
        for n in range(500):
            for i in range(3):
                items = [ randrange(1000) for x in range(n) ]
                self.trySorting(items)

    #override to disable stability test
    def isStable(self):
        return True

    def test_stability(self):
        if self.isStable():
            for n in range(40,200):
                items = [ IntHolder(randrange(20),i) for i in range(n) ]
                srt = self.trySorting(items)
                for i in range(1,len(srt)):
                    if srt[i].val == srt[i-1].val:
                        self.assertTrue( srt[i].serial > srt[i-1].serial )
