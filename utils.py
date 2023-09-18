import streamlit as st

import const


def input_coordinates(vertex_num):
    x, y = st.columns(2)
    x_coord = x.number_input(f'X {vertex_num}', min_value=-20, max_value=20,
                             value=const.VERTICES[vertex_num - 1][0])
    y_coord = y.number_input(f'Y {vertex_num}', min_value=-20, max_value=20,
                             value=const.VERTICES[vertex_num - 1][1])
    return x_coord, y_coord
