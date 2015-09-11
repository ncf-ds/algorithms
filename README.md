#Work for Fall 2015 'Algorithms for Data Science'

## Unit Testing

`test/sort_tester.py` contains the `SortTester` class, which can be subclassed to
test given sort implementations.  It tries the implementation with lists of various
lengths, in random, ascending, and descending order.  It also includes a test for sort
stability, which can be disabled (see below).

Subclasses need to define the `sort` method, which should take a list and sort it in place.
If the sort to be tested is unstable, override the `isStable` method, to return `False`.

See `test/test_sorted.py` for an example using the built-in `sorted` function.  Run it with:

    ./test/test_sorted.py

