# Run *complex* playwright tests in parallel using DAGs - directed acyclic graphs

## Why? Running tests takes longer the more you have- especially common in Playwright tests and DevOps pipelines

Often in DevOps pipelines, test suite pipelines get longer and longer to run- especially if tests
take too long to run.

This becomes a problem especially is tests must run in a certain order- and you're watiing a long time if other, non-dependant tests are ran sequentially.

Solution? State interdependent taks, then parrellise those that can be ran in parallel!

> Hint: In addition to this, make sure you're failing fast- don't make developers wait 30mins
  to be told about a lint issue- run *some* quick win tests early.


- Read `main.py`

Condider the following graph (<small>Taken extract from `main.py`</small>):

```
graph = {222: [333], 333: [111], 555: [], 777: []}

```

The above graph means task `333` is dependant on task `222`, and task `111` is dependant on task `333` also. Tasks `555`, and `777` have zero depdendancies. 

What's harder to spot (for me) is actually tasks `111`, `555`, and `777` are not dependant on eachother *at-all*- that's where the `TopologicalSorter` comes in to automatically work out which tests can be ran in parallel! 

The `TopologicalSorter` can work out the optimal arangement as the dependencies get more complex (you still need to state the dependencies correctly though)

## Install

Install playwright dependencies.
```
npm install
```

## Usage:

Run:

```
python3 main.py
```

Output example:

> Notice that test `@five` is held back because we've said it's
  dependant on test `@one` and `@three`:
```
$ python3 -i main.py
Running tests as fast as possible
Starting to run tests ('@one', '@two', '@three', '@four') in parallel
Running test @one
Running test @two
Running test @three
Running test @four
...
...
Starting to run tests ('@five',) in parallel
Running test @five
```

# Why not just use [Playwright Parallelism and sharding](https://playwright.dev/docs/test-parallel)?

If your tests are truly (and *can*) be truly independant of eachother, you've no need for this, but if you
want to simulate interdependant tests *without* suffering extreemly long pipeline durations, expressing
their interdependencies in a DAG (see `main.py` `graph` for an example).

> Note because of this approach, we actually turn *off* Playwrights built-in parallelism (see `playwright.config.ts` where `fullyParallel: false` and `workers` set to `1`),
 and workers by replacing that with python's `multiprocessing` so you still get the speed 
 benefits, with the added benefit of using a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph) to
 express test dependencies using `graphlib`'s [`TopologicalSorter`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter).

# See also

- `dot` bash utility from `graphviz` and https://graphviz.org/doc/info/lang.html for alternate syntax and image generation


# Links / further reading

- https://en.wikipedia.org/wiki/Directed_acyclic_graph
- https://stackoverflow.com/questions/54903222/implementing-a-dag-in-python
