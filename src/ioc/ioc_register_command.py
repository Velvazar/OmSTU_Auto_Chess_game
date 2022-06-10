from src.base.icommand import ICommand
from src.ioc.idependencies_container import IDependenciesContainer
from src.ioc.ioc_exception import IocException
from src.ioc.istrategy import IStrategy


class IOCBaseRegisterCommandResolver(IStrategy):
    def __init__(self, container: IDependenciesContainer):
        self.__container = container

    def __call__(self, key: str, strategy: IStrategy) -> ICommand:
        try:
            return IOCBaseRegisterCommand(self.__container, key, strategy)
        except IndexError:
            raise IocException("IoC.Register requires two args: key(str) and strategy(IStrategy)")


class IOCBaseRegisterCommand(ICommand):
    def __init__(self, container: IDependenciesContainer, key: str, strategy: IStrategy):
        self.container = container
        self.key = key
        self.strategy = strategy

    def __call__(self) -> None:
        self.container[self.key] = self.strategy
