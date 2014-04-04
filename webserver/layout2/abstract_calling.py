import sys, os
import errno
from multiprocessing import Process, Queue


for i in xrange(7):
    sys.path.append("../../JendasWork/{}_task/".format(i+1))

from pascals_triangle import plot_pascals_triangle as Jendaspascal



def worker(result, target, kwargs):
    result.put(target(**kwargs))


class SubprocessTimeout():
    """
    Provides timeout even in child processes.
    """
    def __init__(self, target=None, kwargs={}):

        self.result  = Queue()
        self.process = Process(target=worker, args=(self.result, target, kwargs))

    def run(self):
        self.process.start()

    def join(self, timeout):

        self.process.join(timeout)

        if self.process.is_alive():
            self.process.terminate()
            raise Exception("Timer expired!")
        else:
            return self.result.get()



def isfloat(s):

    try:
        float(element)
        return True
    except ValueError:
        return False


def convertArguments(arguments):
    """
    Converts all kinds of different data types,
    stored in dictionary, from string to python
    internal representation of given data type.
    """
    for key in arguments:
        value = arguments[key][0]

        if value.isdigit():
            arguments[key] = int(value)
        elif isfloat(value):
            arguments[key] = float(value)


def evaluateFunction(owner, funName, arguments):
    """
    Evaluate function of given owner and 
    given arguments.
    """
    convertArguments(arguments)

    if owner + funName in globals():
        fun = globals()[owner + funName]
        p   = SubprocessTimeout(target=fun, kwargs=arguments)
        p.run()
        return p.join(15)
    else:
        raise Exception("Function name '%s' not found!" % (owner + funName))
    