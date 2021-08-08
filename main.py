import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import argparse

def sub_task1(index:int):
    print("doing job1 {0}".format(index))
    time.sleep(0.5)

def sub_task2(index:int):
    print("doing job2 {0}".format(index))
    time.sleep(0.5)

def main_task(index):
    sub_task1(index)
    sub_task2(index)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Practice ThreadPoolExecutor")
    parser.add_argument("--max_workers", type=int, required=True)
    args = parser.parse_args()

    executor = ThreadPoolExecutor(max_workers=args.max_workers)

    start_time = datetime.now()
    print("start {0}".format(start_time))
    for index in range(10):
        executor.submit(main_task, index=index)
    executor.shutdown()
    
    end_time = datetime.now()
    print("end {0}".format(end_time))
    print("execution time {0}".format(end_time - start_time ))