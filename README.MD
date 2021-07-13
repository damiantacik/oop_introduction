# OOP introduction


## Concept
1. Create cars
2. Car
    - brand
    - engine
    - max speed
    - speed_up()
    - slow_down()
    - start_engine()
    - stop_engine()
   
## OOP dictionary
1. Class -> schema, pattern for creating object
2. Object -> instance of class (egzemplarz)
3. self -> reference to the object
4. method -> function in class
5. fields/attributes -> variables in class/object
6. ```__init__``` -> special method (dunder -> double underscores), initialize object
7. ```__new__``` -> constructor (create an object of class)
8. Base class/ parent class, super class -> 
9. Child class, inherited class ->


## OOP Main rules:
1. Abstraction
2. Inheritance
3. Polymorphism
4. Encapsulation


## Inheritance
- copy all fields and methods from parent class

# Context Manager (Protocol) (PEP 343)

```python

def __enter__(self):
    pass

def __exit__(self, exc_type, exc_val, exc_tb):
    pass

```

```python
with expression as x:
    body
```

1. expression -> object context manager
2. '__enter__' -> bound to x
3. evaluate body
4. '__exit__' if exception -> pass to '__exit__'

## '__enter__':
1. Return any value, commonly use object of context-manager

## '__exit__':
1. Never raise exception
2. Pass exception out to with-block use '__exit__' return False
3. If no pass exception return True

## contextlib (Standard Library)
1. module for working with context-managers

```python

@contexlib.contextmanager
def my_context_manager():
    #  <Enter>
    try:
        yield value
        #  <Normal Exit>
    except:
        #  <Exceptional Exit>
        raise
```

## Multiple context-managers

```python
with cm1() as a, cm2() as b:
    #  Body
    pass

with cm1() as a:
    with cm2() as b:
        # Body
        pass
    