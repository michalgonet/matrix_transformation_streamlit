import numpy as np


def translation_matrix_2d(tx: float, ty: float) -> np.ndarray:
    """Transformation matrix for 2D translation"""
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])


def scaling_matrix_2d(sx: float, sy: float) -> np.ndarray:
    """Transformation matrix for 2D scaling"""
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])


def rotation_matrix_2d(theta: float) -> np.ndarray:
    """Transformation matrix for 2D rotation along (0,0)"""
    return np.array([
        [np.cos(np.radians(theta)), -np.sin(np.radians(theta)), 0],
        [np.sin(np.radians(theta)), np.cos(np.radians(theta)), 0],
        [0, 0, 1]
    ])


def apply_2d_transformation(original_coordinates, transformation_matrix: np.ndarray) -> list:
    new_vertexes = []
    x_coords, y_coords = zip(*original_coordinates)
    for x, y in zip(x_coords, y_coords):
        point = np.array([x, y, 1])
        point = np.dot(transformation_matrix, point)
        new_vertexes.append(point[:-1])
    return new_vertexes
