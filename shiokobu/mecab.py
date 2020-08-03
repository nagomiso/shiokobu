from typing import Any, Dict, NamedTuple, Optional, Union

from natto import MeCab as BaseMeCab


class _MeCabArgs(NamedTuple):
    options: Optional[Union[Dict[str, str], str]]
    kwargs: Dict[str, Any]


class MeCab(BaseMeCab):
    def __init__(
        self, options: Optional[Union[Dict[str, str], str]] = None, **kwargs
    ) -> None:
        self.__args = _MeCabArgs(options, kwargs)
        if type(options) is _MeCabArgs:
            super().__init__(getattr(options, "options"), **getattr(options, "kwargs"))
        else:
            super().__init__(options, **kwargs)

    def __reduce_ex__(self, proto):
        return self.__class__, (self.__args,)
