import contextlib
import os
import sys


class LoggingContexManager:
    def __enter__(self):
        print('LoggingContexManager.__enter__()')
        return "You are in a with-block"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("LoggingContexManager.__exit__()", 'normal exit detect')
        else:
            print(f"LoggingContexManager.__exit__({exc_type}, {exc_val}, {exc_tb})", 'normal exit detect')

        return True
        # return False


# with LoggingContexManager() as x:
#     print(x)

# with LoggingContexManager() as x:
#     raise ValueError('Something has gone wrong')

# try:
#     with LoggingContexManager() as x:
#         raise ValueError('Something has gone wrong')
# except ValueError:
#     print("*** ValueError detected ***")


# @contextlib.contextmanager
# def logging_context_manager():
#     print('logging_context_manager: enter')
#     try:
#         yield "You are in a with-block"
#         print('logging_context_manager: normal exit')
#     except Exception:
#         print("logging_context_manager: exceptional exit", sys.exc_info())  # sys.exc_info - zwraca info except info
#         raise  # wyrzuca na zewnatrz bledy
#
#
# with logging_context_manager() as x:
#     raise ValueError('Something has gone wrong')


@contextlib.contextmanager
def nest_test(name):
    print('Entering', name)
    yield name
    print('Exiting', name)


# with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
#     print('Body')

# with nest_test('outer') as n1:
#     with nest_test('inner, nested in' + n1):
#         print('Body')

@contextlib.contextmanager
def propagator(name, propagate):
    try:
        yield
        print(name, 'exited normally')
    except Exception:
        print(name, 'received an exception')
        if propagate:
            raise


# with propagator('outer', False), propagator('inner', False):
#     raise TypeError('Cannot convert lead into gold')


f = open(os.path.join('../README.MD'), 'r')
with f as g:
    print(f is g)