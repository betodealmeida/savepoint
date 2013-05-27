import sys
import inspect
import os.path
import cPpickle as pickle


class SavePoint(object):

    def __init__(self, path):
        # where we'll store the modified scope
        self.path = path

    def __enter__(self):
        # get caller globals()
        caller = inspect.currentframe(1)

        if os.path.exists(self.path):
            # update scope from savepoint
            with open(self.path) as fp:
                updated = pickle.load(fp)
            caller.f_globals.update(updated)

            # skip `with` body (http://stackoverflow.com/a/12594789/807118)
            sys.settrace(lambda *args, **keys: None)
            caller.f_trace = self.trace

        # store the original scope, so we'll store only the diff when we leave
        self.original_scope = caller.f_globals.copy()

    def trace(self, frame, event, arg):
        raise

    def __exit__(self, type, value, traceback):
        # get caller globals()
        caller = inspect.currentframe(1)

        # calculate what has changed
        updated = {}
        for k, v in caller.f_globals.items():
            if k not in self.original_scope or self.original_scope[k] != v:
                updated[k] = v

        # store diff scope
        if updated:
            with open(self.path, 'w') as fp:
                pickle.dump(updated, fp)

        return True
