from abc import ABC
from abc import abstractmethod

class Fighter(ABC):
    @abstractmethod
    def toString(self):
        pass

    @abstractmethod    
    def isVulnerable(self):
        pass

