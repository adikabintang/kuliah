"""
Allow an object to alter its behavior when its internal state changes.
The object will appear to change its class.
https://sourcemaking.com/design_patterns/state/python/1
"""
import abc

class Context:
    """
    Define the interface of interest to clients.
    Maintain an instance of a ConcreateState subclass
    that defines the current state.
    """
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()
    
class State(metaclass=abc.ABCMeta):
    """
    Define an interface for encapsulating the behavior 
    associated with a particular state of the context.
    """

    @abc.abstractmethod
    def handle(self):
        pass
    
class ConcreateStateA(State):
    """
    Implement a behavior associated with a state of
    the context.
    """
    def handle(self):
        pass

class ConcreateStateB(State):
    def handle(self):
        pass

def main():
    concreate_state_a = ConcreateStateA()
    context = Context(concreate_state_a)
    context.request()

if __name__ == "__main__":
    main()