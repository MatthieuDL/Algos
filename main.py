"""Playground for benchmarking and testing the algorithms"""
import json

from utils.performance_metrics import analyze_functions_performance

from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from searching.binary_search import binary_search


def run_experiments() -> None:
    """
    This function benchmarks the algorithms
    """
    functions = [
        merge_sort,
        quick_sort,
        binary_search
        ]

    sizes = [int(1000*x) for x in range(1,2*10,2)]
    
    # TODO: add graph initializers and 'traverse function' performance metrics
    performance_data = analyze_functions_performance(functions, sizes, plot_graph=True)

    print(json.dumps(performance_data, indent=4))


def run_tests():
    """
    This function should run tests for correctness
    """
    raise NotImplementedError


if __name__ == "__main__":
    run_experiments()
