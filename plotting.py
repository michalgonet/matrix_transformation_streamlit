import matplotlib.pyplot as plt

import const
import classes


def plot_transformation(
        transformation: classes.Transformation,
        vectors: bool,
        annotations: bool,
) -> plt:
    """
    Funtion for show transformations of triangle
    Parameters
    ----------
    transformation:
        The transformation object contains original and transformed coordinates
    vectors:
        Boolean value for showing/hide vectors on plot
    annotations:
        Boolean value for showing/hide vertices annotations

    Returns
    -------
    Function return matplotlib.pyplot object

    """
    # Prepare the required data
    original_coordinates = [transformation.original.vertex_1,
                            transformation.original.vertex_2,
                            transformation.original.vertex_3
                            ]

    transformed_coordinates = [transformation.transformed.vertex_1,
                               transformation.transformed.vertex_2,
                               transformation.transformed.vertex_3
                               ]

    x_coords, y_coords = zip(*original_coordinates)
    new_x_coords, new_y_coords = zip(*transformed_coordinates)

    # Customized the plot
    fig, ax = plt.subplots()
    fig.set_facecolor(const.PLOT_BG_COLOR)
    ax.set_facecolor(const.PLOT_FG_COLOR)
    ax.xaxis.label.set_color(const.PLOT_TICK_COLOR)
    ax.yaxis.label.set_color(const.PLOT_TICK_COLOR)
    ax.tick_params(axis='x', colors=const.PLOT_TICK_COLOR)
    ax.tick_params(axis='y', colors=const.PLOT_TICK_COLOR)
    ax.locator_params(axis='x', nbins=const.NUMBER_OF_TICKS)
    ax.locator_params(axis='y', nbins=const.NUMBER_OF_TICKS)

    # Plot the original triangle
    plt.plot(x_coords, y_coords, marker='o', linewidth=2, color=const.PLOT_ORG_COLOR)
    ax.fill(x_coords, y_coords, color=const.PLOT_ORG_COLOR, alpha=const.PLOT_ALPHA)

    # Plot the transformed triangle
    plt.plot(new_x_coords, new_y_coords, marker='o', linewidth=2, color=const.PLOT_TRANSFORMED_COLOR)
    ax.fill(new_x_coords, new_y_coords, color=const.PLOT_TRANSFORMED_COLOR, alpha=const.PLOT_ALPHA)

    if annotations:
        # Annotate the original vertices
        for (x, y), pos in zip(original_coordinates, const.ANNOTATION_POS):
            plt.annotate(f'({x},{y})', (x, y), textcoords="offset points", xytext=pos, ha='center', color='white',
                         size=7)

        # Annotate the transformed vertices
        for (x, y), pos in zip(transformed_coordinates, const.ANNOTATION_POS):
            plt.annotate(f'({round(x, 1)},{round(y, 1)})', (x, y), textcoords="offset points", xytext=pos, ha='center',
                         color='white', size=7)

    if vectors:
        # Plot vectors from the origin to original vertices
        for (x, y) in original_coordinates:
            plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=const.PLOT_VECTOR_ORG_COLOR)

        # Plot vectors from the origin to transformed vertices
        for (x, y) in transformed_coordinates:
            plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=const.PLOT_VECTOR_TRANSFORMED_COLOR)

    # Set plot limits, labels, and grid
    plt.axis('square')
    plt.xlim(const.X_LIMIT)
    plt.ylim(const.Y_LIMIT)
    plt.yticks(fontsize=const.TICK_FONT_SIZE)
    plt.xticks(fontsize=const.TICK_FONT_SIZE)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()

    return fig
