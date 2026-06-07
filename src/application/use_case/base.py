from abc import abstractmethod
from typing import Protocol


class UseCase[In, Out](Protocol):
    @abstractmethod
    async def __call__(self, data: In) -> Out: ...
