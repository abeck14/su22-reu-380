import queue
from queue import Queue


class CMQueue:
    """
        This class was developed with the intention to create a Queue for the
        cloudmesh jobs that will be developed for the NLP, COVID, and
        Earthquake prediction projects that are occurring in REU2022
        at the Biocomplexity Institute.
        Developer: Jackson Miskill
    """

    # initialize the queue object, assuming that this is a FIFO queue.
    def __init__(self, queuename):
        self.queuename = queue.Queue()

    # add items to the queue
    def add(self, name, command):
        self.queuename.put([name, command])

    # remove the first element of the queue to be started as a job
    def remove(self, name):
        self.queuename.get(name)

    # figure out in what position a specific job is in the queue
    def status(self, name):
        for element in self.queuename:
            if self.queuename[element] == name:
                return "Job is in the", element, "position"

    # list the elements left in the queue
    def list(self):
        for element in self.queuename:
            print(element)
