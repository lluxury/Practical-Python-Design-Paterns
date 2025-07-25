# chain_of_responsibility_alt.py
class Dispatcher(object):
    def __init__(self, handlers=[]):
        self.handlers = handlers

        def handle_request(self, request):
            for handler in self.handlers:
                request = handler(request)
            return request