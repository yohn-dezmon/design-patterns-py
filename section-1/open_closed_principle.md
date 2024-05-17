# Open Closed Principle

when you add new functionality to a class, add it by via extension NOT via modification.

basically: define base classes that you then use to define more specific classes. That way you keep your modifications within the extended classes.

Extension:
- literally extending existing classes in java with `extend` keyword
- or using an interface/trait and writing implementations in classes...

Modification:
- after you've written a class and tested it, don't modify it... uhh what? lol.
- modification does not scale


Open Closed Principle:
- open for extension
- closed for modification 

State explosion:
- filtering by two criteria gives us 3 possible methods (and that's just with `and`)


Design Patterns --> Enterprise Patterns.

Enterprise Patterns:
- specification.  
- we'll implement it there

2 classes.
1. specification
2. filter 


# Combinator

- a structure which combines other structures  

