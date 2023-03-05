from parallel_processing_script import ParallelProcessing
from parallel_processing_script import get_logger
import time 
import sys
class MyParallelProcessing(ParallelProcessing):
    def process(self, name: str) -> None:
        """
        Process to run in parallel (overrides abstract method).
        """
        logger = get_logger()
        logger.info(f"Executing process: {name}...")
        time.sleep(5)


def main() -> None:
    n_jobs = int(sys.argv[1])  # Number of jobs to run in parallel.
    params_list = [("A",), ("B",), ("C",), ("D",), ("E",), ("F",)]

    mpp = MyParallelProcessing(n_jobs=n_jobs)

    # Executing processes in parallel:
    mpp.run(args_list=params_list)


if __name__ == '__main__':
    main()