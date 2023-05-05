from graphlib import TopologicalSorter
from tests import (
    test_111,
    test_222,
    test_333,
    test_555,
    test_666,
    test_777,
)  # noqa: E501
import multiprocessing


"""

You might imagine that the unique numbers refer to tests.

This code automatically works out which tests can run in parallel

"""

# Note that graph values must be iterables (if you pass a
# string e.g. "333" that won't work because TopologicalSorter
# will treat that as "3", "3", and "3" ).
# To overcome that, put the values (depenants) as lists with single
# elements. e.g. ["333"]
graph = {222: [333], 333: [111], 555: [], 777: []}

ts = TopologicalSorter(graph)


def test(ts):
    ts.prepare()
    while ts.is_active():
        node_group = ts.get_ready()
        yield node_group
        ts.done(*node_group)


# Function to run a test based on it's number
def run_test(test_number: int):
    eval(f"test_{test_number}()")


print("Running tests as fast as possible")

for group in test(ts):
    # run those tests in parallel e.g. call test_111() , test_222() in parallel using multiprocessing perhaps?
    # Use a multiprocessing Pool to run the test in parallel
    print(f"Starting to run tests {group} in parallel")
    with multiprocessing.Pool() as pool:
        pool.map(run_test, group)
