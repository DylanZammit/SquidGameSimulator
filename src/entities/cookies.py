from dataclasses import dataclass


@dataclass(frozen=True)
class Cookie:
    shape: str
    alpha: float
    beta: float


@dataclass(frozen=True)
class Circle(Cookie):
    shape: str = 'Circle'
    alpha: float = 6
    beta: float = 4


@dataclass(frozen=True)
class Triangle(Cookie):
    shape: str = 'Triangle'
    alpha: float = 8
    beta: float = 2


@dataclass(frozen=True)
class Star(Cookie):
    shape: str = 'Star'
    alpha: float = 4
    beta: float = 6


@dataclass(frozen=True)
class Umbrella(Cookie):
    shape: str = 'Umbrella'
    alpha: float = 2
    beta: float = 8
