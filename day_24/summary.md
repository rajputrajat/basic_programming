# dict, tuple, assert

## dictionary type (map)

* type is 'dict'
* dict variable is defined as below:

```python
    var_1 = {0: 'data1', 1: 'data 2', 3: 'data 3'}
    var_2 = {
        'ankit': 'faridabad',
        'amit': 'ghaziabad'
    }
```

* values are accessed by using square brackets

```python
    where_does_amit_live = var_2['amit']
```

* accessing keys in for loop

```python
    for k in var_2.keys():
        print(k)
```

* accessing values in for loop

```python
    for v in var_2.values():
        print(v)
```

* accessing both key, values in for loop

```python
    for k, v in var_2.items():
        print(k, v)
```

## Tuple data type

* tuple is basic data-type in python which resembles a list
* tuple values are enclosed in parenthesis => ()

```python
    a_tuple = (1, 2, 3, 4)
```

* tuple is immutable => tuple variable cannot be modified
* generally used while returning multiple values from functions

## assert function

* one of the most useful tools of a programmer
* we pass a 'True' condition in assert function
* in case that condition is indeed 'True', nothing happens
* in case that condition is 'False', program crashes saying 'Assertion failed'

```python
    a = [1, 2, 3]
    assert(a == [1, 2, 3])
    a.append(5)
    assert(a == [1, 2, 3, 5])
    a.append(6)
    assert(a != [1, 2, 3, 5])
```
