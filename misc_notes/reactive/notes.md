This is just some notes taken when learning reactive from here: 
- https://gist.github.com/staltz/868e7e9bc2a7b8c1f754
- https://kirkshoop.github.io/introductionToRxcpp/#63 

# What is reactive programming
**Reactive programming is programming with asynchronous data streams**

### Streams
- A stream is a sequence of ongoing events in time
- Anything can be a stream: variables, user inputs, properties, caches, data structures, etc.
- We capture these emitted events only asynchronously by defining *a function that will execute when a value is emitted* and another *function that will execute when an error is emitted*, for example.
- **Subscribing**: listening to the stream
- **Observers**: the function defined to observe the stream and react according to what we want it to do
- **Observable**: the stream/subject that is observed. 