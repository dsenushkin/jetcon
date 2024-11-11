
from typing import Callable, Any

from jetcon.node import JetNode
from jetcon.build import build
from jetcon.cast import cast, to_dict
from jetcon.read import read
from jetcon.merge import merge
from jetcon.save import save


# yet another interface for interacting with nodes
class JetConfig:
    def __init__(self) -> None:
        raise RuntimeError(f"Class {JetConfig.__name__} cannot be instansiated. "
                           "Use .from_*() methods to create config tree.")

    @staticmethod
    def read(
        path: str
    ) -> JetNode:
        return read(path, compose=True, reset=True)

    @staticmethod
    def build(
        cfg: JetNode
    ) -> JetNode:
        return build(cfg)

    @staticmethod
    def cast(
        cfg: JetNode,
        factory: Callable
    ) -> Any:
        return cast(cfg, factory)

    @staticmethod
    def to_dict(
        cfg: JetNode
    ) -> dict:
        return to_dict(cfg, recursive=True)

    @staticmethod
    def merge(
        dst: JetNode,
        src: JetNode
    ) -> JetNode:
        return merge(dst, src)

    @staticmethod
    def save(
        cfg: JetNode,
        path: str
    ) -> None:
        return save(cfg, path=path)
