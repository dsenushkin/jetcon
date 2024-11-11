from __future__ import annotations
from adict import adict     # type: ignore
from typing import Any, Callable


class JetNode(adict):
    def __init__(
        self,
        cfg: dict = {},
        recursive: bool = True
    ) -> None:
        self._built = False
        # create nodes recursively
        if recursive:
            for key, value in cfg.items():
                if isinstance(value, dict):
                    cfg[key] = JetNode(value)

                if isinstance(value, list):
                    _value = []
                    for _v in value:
                        if isinstance(_v, dict):
                            _v = JetNode(_v)
                        _value.append(_v)
                    cfg[key] = _value

        # use adict constructor
        super().__init__(cfg)

    @staticmethod
    def read(
        path: str
    ) -> JetNode:
        from jetcon.read import read
        return read(path, reset=True, compose=True)

    def build(
        self
    ) -> Any:
        from jetcon.build import build
        return build(self, recursive=True)

    def cast(
        self,
        factory: Callable
    ) -> Any:
        from jetcon.cast import cast
        return cast(self, factory=factory)

    def to_dict(
        self
    ) -> dict:
        from jetcon.cast import to_dict
        return to_dict(self, recursive=True)

    def merge(
        self,
        node: JetNode
    ) -> JetNode:
        from jetcon.merge import merge
        return merge(self, node)

    def save(
        self,
        path: str
    ) -> None:
        from jetcon.save import save
        return save(self, path=path)
