from abc import ABCMeta, abstractmethod


class LikeBase(metaclass=ABCMeta):
    @abstractmethod
    def like(self, model):
        pass

