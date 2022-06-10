from typing import Any

from src.ioc.ioc_container import IOCBaseContainer
from src.ioc.ioc_exception import IocException

ioc_base_container = IOCBaseContainer()


def ioc_resolve(key: str, *args, **kwargs) -> Any:
    try:
        return ioc_base_container["IoC.Resolve"](key, *args, **kwargs)
    except IocException as e:
        raise e
    except Exception as e:
        raise IocException(f"An unexpected exception occurred with key: {key} and args: {args}, and kwargs: {kwargs}: {e}")
