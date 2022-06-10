from abc import abstractmethod, ABC


class ICommand(ABC):
    @abstractmethod
    def __call__(self) -> None:
        ...
