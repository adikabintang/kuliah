# State Design Pattern
https://sourcemaking.com/design_patterns/state

## Intent
- Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
- An object oriented state machine
- wrapper + polymorphic wrappee + collaboration

## Example
In vending machine, the bahavior can change its behavior at runtime based on condition. When currency is deposited and a selection is made, the machine will either deliver a product and no change, deliver a product and change, deliver no product due to insufficient currency on deposit, or deliver no product due to inventory depletion.

##