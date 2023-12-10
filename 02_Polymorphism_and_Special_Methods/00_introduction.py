'''
Polymorphism: the ability to define a generic type of behavior that will
              behave differently when applied to different types

Python is very polymorphic in nature
    >>> Duck typing -> if it walks and quack like a duck then it is a duck.
        "Duck typing is a concept related to dynamic typing, where the type
        or the class of an object is less important than the methods it defines"

        example, when we iterate over a collection, then obj just need to support
        the iterable protocol, it does not matter if it is list, tupple, dictionary
        or generator.

        so to get an iterator, that itself can be anything as long as it implements
        the iterator protocol.

    >>> Operators (+, -. *, /) are also polymorphic as we can use operators between
    two ints, or two real/complex values

    >>> We can add support of polymorphism to our own class for the '+' operator by
    implementing __add__ method
    
'''