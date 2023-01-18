# DAGs - directed acyclic graphs



- Read `main.py`

Condider the following graph (<small>Taken extract from `main.py`</small>):

```
graph = {
    "111": "333",
    "222": {"111", "333"},
    "333": {"111"},
    "444": {"111", "333"},
    "555": {"111": "333"},
    "666": {"7", "8", "9", "10"},
}
```

The above graph will produce the following output when ran:

```
We can run in parallel: ('3', '8', '10', '9', '7')
We can run in parallel: ('111', '666')
We can run in parallel: ('333', '555')
We can run in parallel: ('222', '444')
```

Now consider this different graph (with the only different is that we've now made
666 dependant on 111:

```
graph = {
    "111": "333",
    "222": {"111", "333"},
    "333": {"111"},
    "444": {"111", "333"},
    "555": {"111": "333"},
    "666": {"7", "8", "9", "10", "111"},
}

```

Will produce the following output:

```
We can run in parallel: ('3', '10', '9', '7', '8')
We can run in parallel: ('111',)
We can run in parallel: ('333', '555', '666')
We can run in parallel: ('222', '444')
```

## Usage:

Run:
```
python3 -i main.py
```

Edit code (edit `graph`)


Run again:
```
python3 -i main.py
```



# Links / further reading

- https://en.wikipedia.org/wiki/Directed_acyclic_graph
- https://stackoverflow.com/questions/54903222/implementing-a-dag-in-python
