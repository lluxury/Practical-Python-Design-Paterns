# observer.py  
class ConcreteObserver(object):

    def update(self, observed):
        print("Observing: {}".format(observed))


class Observable(object):

    def __init__(self):
        self.callbacks = set()
        self.changed = False

    def register(self, callback):
        self.callbacks.add(callback)

    def unregister(self, callback):
        self.callbacks.discard(callback)

    def unregister_all(self):
        self.callbacks = set()

    def poll_for_change(self):
        if self.changed:
            self.update_all

    def update_all(self):
        for callback in self.callbacks:
            callback(self)  