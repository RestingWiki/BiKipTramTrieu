from abc import ABC, abstractmethod

class IEvent(ABC):

    @abstractmethod
    def active_event(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
