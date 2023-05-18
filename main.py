from graphlib import TopologicalSorter
import multiprocessing
import subprocess


"""

You might imagine that the unique numbers refer to tests.

This code automatically works out which tests can run in parallel

"""

# Note that graph values must be iterables (if you pass a
# string e.g. "333" that won't work because TopologicalSorter
# will treat that as "3", "3", and "3" ).
# To overcome that, put the values (depenants) as lists with single
# elements. e.g. ["333"]
#
# Here we pretend that test named @five is dependant on tests
# names @one and @three
graph = {"@one": [], "@two": [], "@three": [], "@four": [], "@five": ["@one", "@three"]}

ts = TopologicalSorter(graph)


def test(ts):
    ts.prepare()
    while ts.is_active():
        node_group = ts.get_ready()
        yield node_group
        ts.done(*node_group)


# Function to run a test based on it's number
def run_test(test_name: int):
    print(f"Running test {test_name}")
    subprocess.run(
        f"npx playwright test --grep {test_name} --headed",
        shell=True,
    )


print("Running tests as fast as possible")

for group in test(ts):
    # run those tests in parallel e.g. call test_111() , test_222() in parallel using multiprocessing perhaps?
    # Use a multiprocessing Pool to run the test in parallel
    print(f"Starting to run tests {group} in parallel")
    with multiprocessing.Pool() as pool:
        pool.map(run_test, group)
