import threading
from time import perf_counter_ns


def factorial(n: int) -> int:

    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result



def _timed_factorial(n: int, slot: int, starts: list[int], ends: list[int]):
    starts[slot] = perf_counter_ns()
    factorial(n)
    ends[slot] = perf_counter_ns()



def run_multithread_round(nums: list[int]) -> tuple[int, int]:
    starts = [0] * len(nums)
    ends = [0] * len(nums)
    threads = []

    for i, n in enumerate(nums):
        t = threading.Thread(target=_timed_factorial, args=(n, i, starts, ends))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_time = max(ends) - min(starts)
    avg_task_time = sum(e - s for e, s in zip(ends, starts)) // len(nums)
    return total_time, avg_task_time



def run_singlethread_round(nums: list[int]) -> tuple[int, int]:
    per_task = []
    starts, ends = [], []
    for n in nums:
        t0 = perf_counter_ns()
        factorial(n)
        t1 = perf_counter_ns()
        starts.append(t0)
        ends.append(t1)
        per_task.append(t1 - t0)
    total_time = max(ends) - min(starts)
    avg_task_time = sum(per_task) // len(nums)
    return total_time, avg_task_time



if __name__ == "__main__":
    numbers = [50, 100, 200]
    rounds = 10

    print("====================================================")
    print("> MULTITHREADING EXECUTION <")
    print("====================================================")
    mt_times = []
    for i in range(1, rounds + 1):
        T, avg_task = run_multithread_round(numbers)
        mt_times.append(T)
        print(f"Round {i:02d}: T(ns) = {T} | AvgTask(ns) = {avg_task}")
    mt_avg_T = sum(mt_times) // rounds
    print(f"Average of T (Multithreading): {mt_avg_T} ns\n")

    print("====================================================")
    print("> NO MULTITHREADING EXECUTION<")
    print("====================================================")
    st_times = []
    for i in range(1, rounds + 1):
        T, avg_task = run_singlethread_round(numbers)
        st_times.append(T)
        print(f"Round {i:02d}: T(ns) = {T} | AvgTask(ns) = {avg_task}")
    st_avg_T = sum(st_times) // rounds
    print(f"Average of T (No Multithreading): {st_avg_T} ns\n")

    print("====================================================")
    print("SUMMARY COMPARISON")
    print("====================================================")
    print(f"Multithreading Average T : {mt_avg_T} ns")
    print(f"No Multithreading Average T : {st_avg_T} ns")
    if mt_avg_T < st_avg_T:
        print("Multithreading was faster than single thread.")
    else:
        print("Multithreading was slower than single thread.")