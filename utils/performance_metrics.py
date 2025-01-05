"""This module calculates the performance metrics"""

import random
import time
import os
import tracemalloc
from collections import defaultdict

import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons


def create_array(x):  # pylint: disable=C0116
    return [random.randint(-1000, 1000) for _ in range(x)]


def is_search_function(func):
    """
    Checks if a function is a search function by looking
    if it is part of the 'searching' folder
    """
    search_folder = "searching/"
    for root, _, files in os.walk(search_folder):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    if func.__name__ in f.read():
                        return True
    return False


def is_traversing_function(func):
    """
    Checks if a function is a traversing function by looking
    if it is part of the 'traversing' folder
    """
    traversing_folder = "traversing/"
    for root, _, files in os.walk(traversing_folder):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    if func.__name__ in f.read():
                        return True
    return False


def create_graph(size):
    """Creates a random graph to test traversing functions"""
    graph = defaultdict(list)
    for i in range(size):
        for _ in range(random.randint(1, 4)):
            neighbor = random.randint(0, size - 1)
            if neighbor != i:
                graph[i].append(neighbor)
    return graph


def analyze_functions_performance(functions, sizes, plot_graph=True):
    """Run the algorithms and trace their time and space performance"""

    performance_data = {
        func.__name__: {"size": [], "time": [], "space": []} for func in functions
    }

    for size in sizes:
        array = create_array(size)
        graph = create_graph(size)
        start_node = 0
        target_node = size - 1

        for func in functions:
            if is_search_function(func):
                target = random.randint(-2000, 2000)
                tracemalloc.start()
                start_time = time.time()
                func(array.copy(), target)
                end_time = time.time()
                _, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
            elif is_traversing_function(func):
                try:
                    tracemalloc.start()
                    start_time = time.time()
                    func(graph, start_node, target_node)
                    end_time = time.time()
                    _, peak = tracemalloc.get_traced_memory()
                    tracemalloc.stop()
                except RecursionError: # TODO: think about representing this in graph
                    end_time = time.time()
                    peak = -1
                    print(
                        f"RecursionError caught while running {func.__name__} "
                        f"with a graph size of {size}. This is likely due to "
                        f"traversing a looping graph."
                    )
            else:
                tracemalloc.start()
                start_time = time.time()
                func(array.copy())
                end_time = time.time()
                _, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()

            performance_data[func.__name__]["time"].append(end_time - start_time)
            performance_data[func.__name__]["space"].append(peak)
            performance_data[func.__name__]["size"].append(size)

    if plot_graph:
        plot_performance(performance_data, functions)

    return performance_data


def plot_performance(performance_data, functions):
    """This function plots the performance graphs with interactive buttons"""

    _, ax1 = plt.subplots(figsize=(12, 6))
    plt.subplots_adjust(left=0.2)

    ax2 = ax1.twinx()

    lines = {}
    for func in functions:
        sizes = performance_data[func.__name__]["size"]
        times = performance_data[func.__name__]["time"]
        spaces = performance_data[func.__name__]["space"]

        line_time = ax1.plot(
            sizes, times, label=f"{func.__name__} Time", linestyle="-", visible=False
        )
        line_space = ax2.plot(
            sizes, spaces, label=f"{func.__name__} Space", linestyle="--", visible=False
        )
        lines[f"{func.__name__} Time"] = line_time
        lines[f"{func.__name__} Space"] = line_space

    ax1.set_title("Performance Metrics")
    ax1.set_xlabel("Array Size")
    ax1.set_ylabel("Time - solid line (seconds)", color="b")
    ax2.set_ylabel("Space - dashed line (bytes)", color="g")

    rax = plt.axes([0.45, 0.85, 0.15, 0.15])
    labels = [func.__name__ for func in functions]
    visibility = [False] * len(labels)
    check = CheckButtons(rax, labels, visibility)

    def click(label):
        time_label = f"{label} Time"
        space_label = f"{label} Space"
        for line in lines[time_label]:
            line.set_visible(not line.get_visible())
        for line in lines[space_label]:
            line.set_visible(not line.get_visible())
        plt.draw()

    check.on_clicked(click)
    plt.show()
