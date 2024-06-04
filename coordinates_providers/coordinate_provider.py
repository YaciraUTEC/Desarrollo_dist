from abc import ABC, abstractmethod

class CoordinateProvider(ABC):
    @abstractmethod
    def get_coordinates(self, city, country):
        pass
