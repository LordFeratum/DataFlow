# DataFlow

DataFlow is a framework to process your data easily. DataFlow lets you to create a flow to transform your data.

# How to use

First, you need to create a flow to be able to manage your transformation steps. And then, apply every transform function you need.

``` python
from dataflow import Flow, Enum, Promise

Flow.from_enumerable([1, 2, 3, 4])\
>> Enum.map(lambda x: x * 2)\
>> Promise.as_list

# 2, 4, 6, 8
```

# Async Support

From v0.3 DataFlow has async/await support for Python >=3.5. The inclusion of Python3.5 forced me to drop the support
of lazyness in AsyncEnum. From Python3.6 this support will become to life again.

``` python
from asyncio import get_event_loop

loop = get_event_loop()

async def by_two(n):
    return n * 2

Flow.from_enumerable([1, 2, 3, 4], loop)\
>> Enum.map(lambda x: x * 2)\
>> AsyncEnum.map(by_two)\
>> Enum.map(lambda x: x * 2)\
>> AsyncEnum.map(by_two)\
>> Promise.as_list

# [16, 32, 48, 64, 80]
```

# Enum Module

In Enum module you can find functions wich works with enumerates.

## Enum.map

This function takes another function and apply that function to every element on your flow.

``` python
Flow.from_enumerate([1, 2, 3])\
>> Enum.map(lambda x: x * 2)\
>> Promise.as_list

# [2, 4, 6]
```

## Enum.flat_map

This function takes another function and apply that function, but returns a flattened list.

``` python
Flow.from_enumerate([1, 2, 3])\
>> Enum.flat_map(lambda x: [x, x*2])\
>> Promise.as_list

# [1, 2, 3, 6, 4, 8]
```

## Enum.filter

This function takes another function to filter the elements of your flow. This functions only allos flow your elements that evaluate True for that function.

``` python
Flow.from_enumerable([1, 2, 3])\
>> Enum.filter(lambda x: x >= 2)\
>> Promise.as_list

# [2, 3]
```

## Enum.grouper

This function takes an integer and gather your data into sets of that length. If a set can be completed, then a fillvalue will be used. Defaults to None.

``` python
Flow.from_enumerable([1, 2, 3, 4, 5])\
>> Enum.grouper(2)\
>> Promise.as_list

# [[1, 2], [3, 4], [5, None]]
```

## Enum.reduce

This functions takes another funtion that remember the last accumulated value and returns the new accumulated value. You can specify the initial accumulated value. Empty list by default

``` python
Flow.from_enumerable([1, 2, 3])\
>> Enum.reduce(lambda acc, data: acc + data, 0)\
>> Promise.as_int

# 6
```

## Enum.dropwhile

This function takes another function that drops elements until the condition returns False.

``` python
Flow.from_enumerable([1, 2, 3, 4])\
>> Enum.dropwhile(lambda x: x < 3)\
>> Promise.as_list

# [3, 4]
```

## Enum.takewhile

This functions is the inverted version of Enum.dropwhile. That functions take elements of the iterable until
the condition is False.

``` python
Flow.from_enumerable([1, 2, 3, 4])\
>> Enum.takewhile(lambda x: x < 3)\
>> Promise.as_list

# [1, 2]
```

## Enum.sort

This function sort any collection of items. You can set the key to sort by and if you what it reversed or not.

``` python
from operator import itemgetter

Flow.from_enumerable([('A', 1), ('B', 0), ('C', 3), ('D', 2)])\
>> Enum.sort(key=itemgetter(1), reverse=True)\
>> Promise.as_list

# [('C', 3), ('D', 2), ('A', 1), ('B', 0)]
```

# AsyncEnum

AsyncEnum module gives you support to transform data with asynchronous functions. The implemented methods are:
* AsyncEnum.map
* AsyncEnum.flat_map
* AsyncEnum.filter
* AsyncEnum.reduce
* AsyncEnum.dropwhile
* AsyncEnum.takewhile


# String module

In the String module you can find functions to manipulate strings.

## String.split

It allows you to split your string flow into a smaller pieces. By default it splits by whitespace.

``` python
Flow.from_enumerable("One Two Three Four Five Six Seven")\
>> String.split(" ")\
>> Enum.filter(lambda x: len(x) >= 4)\
>> Promise.as_list

# ["Three", "Four", "Seven"]
```

## String.join

It allows to join a list of strings into and unique string. This functions allows you to choose the string for concate. Default as empty string.

``` python
Flow.from_enumerable("Hello world!")\
>> String.split(" ")\
>> String.join("-")\
>> Promise.resolve

# Hello-world!
```

# Promise module

This module is in charge to return a valid data structure from a flow.

## Promise.as_list

Returns the data from the flow as a list.

## Promise.as_int

Returns the data from the flow as integer.

## Promise.as_float

Returns the data from the flow as float.

## Promise.resolve

Returns the data from the flow without any casting.

## Promise.for_each

This functions take a function as argument and apply that function to every element of your flow. This method does not return anything.


# How can I create my own modules?

Easy, you just need to create a python class with all methods statics. All the methods must returns a function that get the data flow as argument and return a new Flow element.

``` python
class MyModule:
    @staticmethod
    def per_two(data):
        new_data = [element * 2 for element in data]
	return Flow(new_data)

    @staticmethod
    def multiply(n):
        def _multiplier(data):
	    new_data = [element * n for element in data]
	    return Flow(new_data)
	return _multiplier


Flow.from_enumerable([1, 2, 3])\
>> MyModule.per_two\
>> MyModule.multiply(2)\
>> Promise.as_list

# [4, 8, 12]
```

With async/await support:

``` python
class MyAsyncModule:
    @staticmethod
    def multiply(n):
        async def _multiply(data):
	    data = [await awesome_multiplier(datum, n) for datum in data]
	    return Flow(data)
	return _multiply
```
