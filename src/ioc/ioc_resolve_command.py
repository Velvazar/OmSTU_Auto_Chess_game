from typing import Any

from src.ioc.idependencies_container import IDependenciesContainer
from src.ioc.istrategy import IStrategy


class IOCBaseResolveResolver(IStrategy):
    def __init__(self, container: IDependenciesContainer):
        self.__container = container

    def __call__(self, *args: Any, **kwargs: Any) -> IStrategy:
        key = args[0]
        return self.__container[key](*args[1:], **kwargs)
