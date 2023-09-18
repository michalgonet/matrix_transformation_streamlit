from dataclasses import dataclass


@dataclass(frozen=True)
class Triangle:
    vertex_1: tuple[float, float]
    vertex_2: tuple[float, float]
    vertex_3: tuple[float, float]


@dataclass(frozen=True)
class Transformation:
    original: Triangle
    transformed: Triangle
