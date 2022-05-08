from abc import ABC, ABCMeta, abstractmethod

class EmotionalState(metaclass =ABCMeta):
    @abstractmethod
    def say_hello(self):
        pass

    @abstractmethod
    def say_goodbye(self):
        pass


class HappyState(EmotionalState):
    def say_goodbye(self):
        return "Bye, friend! See you again!!!"

    def say_hello(self):
        return "Hello, friend!"


class SadState(EmotionalState):
    def say_goodbye(self):
        return "Bye. HUUHUHUHU!!!!"

    def say_hello(self):
        return "HUHU, Hello. Just lose my bike"


class Person:
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def say_goodbye(self):
        return self.state.say_goodbye()

    def say_hello(self):
        return self.state.say_hello()



if __name__ == "__main__":
	print(25*"-")
	person = Person(HappyState())
	print(person.say_hello())
	print(person.say_goodbye())

	print(25*"-")

	person.set_state(SadState())
	print(person.say_hello())
	print(person.say_goodbye())
