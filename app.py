import streamlit as st

import algebra
import classes
import const
import utils
import plotting


def main():
    st.sidebar.title('Matrix Transformations')
    choice = st.sidebar.radio('Navigation', ['Translation', 'Scaling', 'Rotation'])
    st.info("Interactive Matrix Transformation")

    if choice == 'Translation':
        handle_translation()
    elif choice == 'Scaling':
        handle_scaling()
    elif choice == 'Rotation':
        handle_rotation()


def handle_translation():
    st.write("Set the initial coordinates")
    vertices = [utils.input_coordinates(i) for i in range(3)]

    st.write("Set the translation vector (tx, ty).")
    tx = st.number_input('TX', min_value=None, max_value=None, value=const.TRANSLATE_X)
    ty = st.number_input('TY', min_value=None, max_value=None, value=const.TRANSLATE_Y)

    t = algebra.translation_matrix_2d(tx, ty)
    apply_transformation(vertices, t, "TRANSLATION")


def handle_scaling():
    st.write("Set the initial coordinates")
    vertices = [utils.input_coordinates(i) for i in range(3)]

    st.write("Set the scaling vector (sx, sy).")
    sx = st.number_input('SX', value=const.SCALING_X)
    sy = st.number_input('SY', min_value=None, max_value=None, value=const.SCALING_Y)

    t = algebra.scaling_matrix_2d(sx, sy)
    apply_transformation(vertices, t, "SCALING")


def handle_rotation():
    st.write("Set the initial coordinates")
    vertices = [utils.input_coordinates(i) for i in range(3)]

    st.write("Set the rotation angle (degree).")
    theta = st.number_input('THETA', value=const.THETA)

    t = algebra.rotation_matrix_2d(theta)
    apply_transformation(vertices, t, "ROTATION")


def apply_transformation(vertices, transformation_matrix, title):
    new_coordinates = algebra.apply_2d_transformation(vertices, transformation_matrix)

    original_triangle = classes.Triangle(vertex_1=vertices[0],
                                         vertex_2=vertices[1],
                                         vertex_3=vertices[2]
                                         )
    transformed_triangle = classes.Triangle(vertex_1=new_coordinates[0],
                                            vertex_2=new_coordinates[1],
                                            vertex_3=new_coordinates[2]
                                            )

    vectors = st.checkbox("Show Vectors", value=False)
    annotations = st.checkbox("Show Annotations", value=False)
    triangles = classes.Transformation(original=original_triangle, transformed=transformed_triangle)
    plt = plotting.plot_transformation(triangles, vectors, annotations)
    st.write(title)
    st.pyplot(plt)


if __name__ == "__main__":
    main()
