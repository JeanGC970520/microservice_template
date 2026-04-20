from typing import Protocol


class ExampleRepository(Protocol):
    def save(self, data): ...
