from graphlib import TopologicalSorter

"""

I have 4 tests, which are each identified by a unique number:

- 111
- 222
- 333
- 444

Every test is dependant on 111 and 333.
No other tests are dependant.

You might imagine that the unique numbers refer to tests.

This code automatically works out which tests can run in parallel

"""

graph = {
    "111": "333",
    "222": {"111", "333"},
    "333": {"111"},
    "444": {"111", "333"},
    "555": {"111": "333"},
    "666": {"7", "8", "9", "10"},
}

# After running this code, un-comment the graph
# variable below.
# Notice the only different is that we've not made
# 666 dependany on 111.
# Run the script again, and watch the different output.

"""
graph = {
    "111": "333",
    "222": {"111", "333"},
    "333": {"111"},
    "444": {"111", "333"},
    "555": {"111": "333"},
    "666": {"7", "8", "9", "10", "111"},
}
"""

ts = TopologicalSorter(graph)


def test(ts):
    ts.prepare()
    while ts.is_active():
        node_group = ts.get_ready()
        yield node_group
        ts.done(*node_group)


for group in test(ts):
    print(f"We can run in parallel: {group}")
