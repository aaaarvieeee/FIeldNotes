from abc import ABC, abstractmethod


class TrigReading(ABC):
    @abstractmethod
    def __init__(self, Vert, Horiz, SD, HD, Target):
        self.Vert = Vert
        self.Horiz = Horiz
        self.SD = SD
        self.HD = HD
        self.Target = Target
