from src.ioc.idependencies_container import IDependenciesContainer
from src.ioc.ioc_exception import IocException
from src.ioc.ioc_register_command import IOCBaseRegisterCommandResolver
from src.ioc.ioc_resolve_command import IOCBaseResolveResolver
from src.ioc.istrategy import IStrategy


class IOCBaseContainer(IDependenciesContainer):
    def __init__(self):
        self.__store = {}
        self.__not_found_strategy = lambda key: raise_exception(IocException(f"Dependency {key} is missing"))
        self.__store["IoC.Resolve"] = IOCBaseResolveResolver(self)
        self.__store["IoC.Register"] = IOCBaseRegisterCommandResolver(self)
        self.__store["IoC.BaseContainer"] = lambda: self

    def __getitem__(self, key: str) -> IStrategy:
        try:
            return self.__store[key]
        except KeyError:
            return self.__not_found_strategy(key)
        except IocException as e:
            raise e

    def __setitem__(self, key: str, strategy: IStrategy):
        self.__store[key] = strategy


def raise_exception(ex):
    raise ex
