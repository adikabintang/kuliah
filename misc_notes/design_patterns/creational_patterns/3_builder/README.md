
Tutorial: https://sourcemaking.com/design_patterns/builder

# Builder Design Pattern
## Intent
- Separate the construction of a complex object from its representation so that the same construction process can create different representations.
- parse a complex representation, create on of several targets.
- Builder pattern affords finer control over the construction process. Unlike 'abstract factory' pattern that constructs products in one shot, the builder pattern constructs the product step by step under the control of the "director".
- Often, designs start out using Factory Method and evolve toward abstract factory, prototype, or builder as the designer doscovers where more flexibility is needed.

From [medium](https://medium.com/educative/the-7-most-important-software-design-patterns-d60e546afb0e):
- The difference between 'abstract factory' pattern and builder pattern is the builder pattern creates an object step by step whereas the abstract factory pattern returns the object in one go.

## Use Case Example
Construction process in fast food restaurants:

![image](https://sourcemaking.com/files/v2/content/patterns/Builder_example1.png)

image source: https://sourcemaking.com/files/v2/content/patterns/Builder_example1.png
