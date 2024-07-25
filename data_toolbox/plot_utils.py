
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd


def create_dual_y_axis_plot_matplotlib(x, y1, y2, y1_label='Y1 Axis', y2_label='Y2 Axis', x_label='X Axis', title='Dual Y Axis Plot'):
    """
    Creates a dual Y-axis plot using Matplotlib.

    Args:
        x (list or array-like): The data for the X axis.
        y1 (list or array-like): The data for the first Y axis.
        y2 (list or array-like): The data for the second Y axis.
        y1_label (str): The label for the first Y axis. Default is 'Y1 Axis'.
        y2_label (str): The label for the second Y axis. Default is 'Y2 Axis'.
        x_label (str): The label for the X axis. Default is 'X Axis'.
        title (str): The title of the plot. Default is 'Dual Y Axis Plot'.

    Returns:
        fig, ax1, ax2: Matplotlib figure and axes objects for further customization.
    """
    
    # Determine the size of the figure based on the length of the data
    fig_width = max(10, len(x) / 10)  # Ensure a minimum width of 10
    fig_height = 6  # Fixed height for better aspect ratio
    
    # Create a figure and a set of subplots
    fig, ax1 = plt.subplots(figsize=(fig_width, fig_height))

    # Plot the first Y-axis data
    ax1.plot(x, y1, color='blue', label=y1_label)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label, color='blue')
    ax1.tick_params('y', colors='blue')

    # Create a second Y-axis sharing the same X-axis
    ax2 = ax1.twinx()
    ax2.plot(x, y2, color='red', label=y2_label)
    ax2.set_ylabel(y2_label, color='red')
    ax2.tick_params('y', colors='red')

    # Add legends
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper left')
    ax1.tick_params(axis='x', rotation=45)

    # Adjust layout
    plt.tight_layout()
    
    # Set the title
    plt.title(title)

    # Show the plot
    plt.show()

    return fig, ax1, ax2


def create_dual_y_axis_plot_plotly(x, y1, y2, y1_label='Y1 Axis', y2_label='Y2 Axis', x_label='X Axis', title='Dual Y Axis Plot'):
    """
    Creates a dual Y-axis plot using Plotly.

    Args:
        x (list or array-like): The data for the X axis.
        y1 (list or array-like): The data for the first Y axis.
        y2 (list or array-like): The data for the second Y axis.
        y1_label (str): The label for the first Y axis. Default is 'Y1 Axis'.
        y2_label (str): The label for the second Y axis. Default is 'Y2 Axis'.
        x_label (str): The label for the X axis. Default is 'X Axis'.
        title (str): The title of the plot. Default is 'Dual Y Axis Plot'.

    Returns:
        fig (go.Figure): A Plotly Figure object representing the dual Y-axis plot.
    """
    
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x, 
        y=y1, 
        mode='lines+markers',
        name=y1_label,
        yaxis='y1'
    ))

    fig.add_trace(go.Scatter(
        x=x, 
        y=y2, 
        mode='lines+markers',
        name=y2_label,
        yaxis='y2'
    ))

    fig.update_layout(
        title=title,
        xaxis=dict(title=x_label),
        yaxis=dict(
            title=y1_label,
            titlefont=dict(color='blue'),
            tickfont=dict(color='blue')
        ),
        yaxis2=dict(
            title=y2_label,
            titlefont=dict(color='red'),
            tickfont=dict(color='red'),
            overlaying='y',
            side='right'
        ),
        legend=dict(x=0.1, y=1.1)
    )

    return fig


def boxplot_by_column(data: pd.DataFrame, group_col: str, check_col: str):
    """
    Draws a boxplot for the specified column, grouped by another column.

    Args:
        data (pd.DataFrame): The input data frame containing the data.
        group_col (str): The column name to group by (e.g., date).
        check_col (str): The column name for which the boxplot is to be drawn.

    Notes:
        - The figure width is automatically adjusted based on the length of x-axis labels to ensure they fit within the 
          plot. The width adjustment factor is determined by the length of the longest label.
        - If any x-axis label exceeds a certain length (default is 10 characters), the labels are rotated 90 degrees
          to improve readability.
    """
    # Create subplots
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Draw the boxplot
    data.boxplot(column=check_col, by=group_col, ax=ax1)
    ax1.set_xlabel(group_col.capitalize())
    ax1.set_ylabel(check_col.capitalize())
    ax1.set_title(f'Boxplot of {check_col.capitalize()} by {group_col.capitalize()}')

    # Get current x-tick labels
    labels = [item.get_text() for item in ax1.get_xticklabels()]

    # Calculate maximum label length
    max_label_length = max(len(label) for label in labels)

    # Adjust figure size based on the maximum label length
    fig_width = 10 + max_label_length * 0.2 
    fig.set_size_inches(fig_width, 6)

    # Rotate x-axis labels if any label is particularly long
    max_label_length = max(len(label) for label in labels)
    if max_label_length > 10:  
        plt.xticks(rotation=90)
        
    # Remove the default 'Boxplot' title
    plt.suptitle('')
    plt.show()