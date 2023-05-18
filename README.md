# DAGs - directed acyclic graphs

## Why? Running tests takes longer the more you have- this is especially common in DevOps pipelines

>  **Note**
> This is cool! Are you looking to make complex Playwright tests faster? See [Playwright example branch](https://github.com/KarmaComputing/dag-directed-acyclic-graph-example/tree/playwright).

Often in DevOps pipelines, test pipelines get longer and longer to run- especially if tests
take too long to run.

Solution? State interdependent tasks, then parallelise them using DAGs!


> Hint: In addition to this, make your you're failing fast- don't make developers wait 30mins
  to be told about a lint issue- run *some* quick win tests early.


- Read `main.py`

Condider the following graph (<small>Taken extract from `main.py`</small>):

```
graph = {222: [333], 333: [111], 555: [], 777: []}

```

The above graph means task `333` is dependant on task `222`, and task `111` is dependant on task `333` also. Tasks `555`, and `777` have zero depdendancies. 

What's harder to spot (for me) is actually tasks `111`, `555`, and `777` are not dependant on eachother *at-all*- that's where the `TopologicalSorter` comes in to automatically work out which tests can be ran in parallel! 

The `TopologicalSorter` can work out the optimal arangement as the dependencies get more complex (you still need to state the dependencies correctly though)


## Usage:

Run:

```
python3 -i main.py
```

Output example:
```
Running tests as fast as possible
Starting to run tests (111, 555, 777) in parallel
Running test_111
Running test_555
Running test_777
Starting to run tests (333,) in parallel
Running test_333
1111
Starting to run tests (222,) in parallel
Running test_222
```


# See also

- `dot` bash utility from `graphviz` and https://graphviz.org/doc/info/lang.html for alternate syntax and image generation


# Links / further reading

- https://en.wikipedia.org/wiki/Directed_acyclic_graph
- https://stackoverflow.com/questions/54903222/implementing-a-dag-in-python
