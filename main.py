"""Playground for benchmarking and testing the algorithms"""
import json

from utils.performance_metrics import analyze_functions_performance

from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from searching.binary_search import binary_search
from traversing.breadth_first_search import breadth_first_search
from traversing.depth_first_search import depth_first_search, iterative_deepening_dfs

def run_experiments() -> None:
    """
    This function benchmarks the algorithms
    """
    functions = [
        merge_sort,
        quick_sort,
        binary_search,
        breadth_first_search,
        depth_first_search,
        iterative_deepening_dfs
        ]

    sizes = [int(1000*x) for x in range(1,2*10,2)]

    performance_data = analyze_functions_performance(functions, sizes, plot_graph=True)

    print(json.dumps(performance_data, indent=4))


def run_tests():
    """
    This function should run tests for correctness
    """
    raise NotImplementedError # TODO: add correctness tests (merge with experiments?)


def main():
    """This function runs the tests and benchmarks"""
    #run_tests()
    run_experiments()


if __name__ == "__main__":
    main()
