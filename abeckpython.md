# Current Knowledge of Python

### By Alex Beck

## Prior Python Experience:

* Took CS 1110: Introduction to Programming in the Fall 2021 semester

## Built-in Python Functions

### `print()`

The print function is used to print strings on the screen. The parameters
`sep` and `end` can be used to input characters between different
parts of what's being printed and at the end of each line, respectively.
Below here is an example:

```python
print('Hello', 'World', sep='_', end='0')
```

The following output is produced:

`Hello_World0`

### `input()`

The input allows the user input a string to answer a prompt. Below here 
is an example:

```python
origin = input('Where are you from? ')
print('What is it like in', origin + '?')
```

The following output is produced when the input is `'Virginia'`.

```
Where are you from? >? Virginia
What is it like in Virginia?
```

### Typecasting

In Python, values can be assigned to a variable where it has the potential
to change. Every value has a certain type, the most common ones being
`int()`, `float()`, and `str()`. Typecasting is the process of reshaping
the value into a new type.

`int` values are whole numbers with no decimal places. `float` values are 
any numerical values that can have decimal places. If a `float` is 
typecasted, it'll always round down to the lowest integer. This
can be shown in the following example.

```python
print(int(8.9))
```

The following output is produced.

`8`

When a `str` value is typecasted into either an `int` or `float`,
a error is produced. However, it can work the other way around. 
The `type()` function denotes the type of each value in the input. 
All of this can be shown in this example:

```python
print(8.9)
print(type(8.9))
print(str(8.9))
print(type(str(8.9)))
```

The following output is produced:

```
8.9
<class 'float'>
8.9
<class 'str'>
```

### Operators

Basic mathematical operations can be done with Python using the following
operators: 
* `+` for addition
* `-` for subtraction
* `*` for multiplication
* `**` for exponents
* `/` for division
* `//` for integer division
* `%` for modulus (remainder)


In terms of value types:

* `int` and `int` values always produce `int` values
* `int` and `float` values always produce `float` values.
* `float` and `float` values always produce `float` values.

This can be shown in the example below.

```python
print(2+2)
print(type(2+2))
print(2+2.1)
print(type(2+2.1))
print(2.1+2.1)
print(type(2.1+2.1))
```

Where the following output is produced.

```
4
<class 'int'>
4.1
<class 'float'>
4.2
<class 'float'>
```

The only exception is that `/` always produce `float` values, and `//`
and `%` always produce `int` values. This can be shown in the following
example.

```python
print(4/2)
print(type(4/2))
print(8//5)
print(type(8//5))
```

Where the following output is produced.

```
2.0
<class 'float'>
1
<class 'int'>
```

The operators `+` and `*` can work for strings by concatenating them
and multiplying them, respectively. This can be shown in the following
exanple.

```python
print('Hello')
print('Hello'+'world')
print('Hello'*5)
```

Where the following output is the produced.

```
Hello
Helloworld
HelloHelloHelloHelloHello
```

### Boolean Operators and Types

Values can be compared using the following comparison operators:

* `<` for less than
* `<=` for less than and equal to
* `==` for equal to
* `!=` for not equal to
* `>=` for greater than and equal to
* `>` for greater than

The operator `=` cannot be used for boolean expressions. Rather, it is
only used as an assignment operator for variables.


Booleans only produce two outputs which are `True` and `False`. This
can be shown in the following example.

```python
print(8>=2)
print(9!=9)
print(type(9!=9))
```

Where the following output is produced. Note that booleans have their
own type of value.

```
True
False
<class 'bool'>
```

Multiple booleans can be compared with each other using the following
logical operators:

* `and` for when all things are `True`
* `or` for when any of the things are `True`
* `not` for when the comparison is `False`

This can be shown in the following example.

```python
print(8>=2 and 9!=9)
print(8>=2 or 9!=9)
print(not 9!=9)
```

Where the following output is produced.

```
False
True
True
```




