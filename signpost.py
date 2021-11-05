from settings import *
from factory import *


class SignPostState:
    def start(self):
        raise NotImplementedError

    def end(self):
        raise NotImplementedError

    def enter(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError


class SignPost:
    def __init__(self):
        self.signPostState = SignPostStartState(self)

    def changeState(self, newState: SignPostState):
        if self.signPostState != None:
            self.signPostState.exit()
        self.signPostState = newState
        self.signPostState.enter()

    def startState(self):
        self.signPostState.start()

    def endState(self):
        self.signPostState.end()


class SignPostStartState(SignPostState):
    def __init__(self, signPost: SignPost):
        self.signPost = signPost

    def start(self):
        print("Sign is already in start state, SignPostStartState")

    def end(self):
        self.signPost.changeState(SignPostEndState(self.signPost))

    def enter(self):
        print("Sign is in start state, SignPostStartState")
        return True

    def exit(self):
        pass


class SignPostEndState(SignPostState):
    def __init__(self, signPost: SignPost):
        self.signPost = signPost

    def start(self):
        self.signPost.changeState(SignPostStartState(self.signPost))

    def end(self):
        print("Sign is already in end state, SignPostEndState")

    def enter(self):
        print("sign is now in end state, SignPostEndState")

    def exit(self):
        pass
