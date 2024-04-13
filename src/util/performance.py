from typing import Callable, Any
from time import perf_counter, perf_counter_ns
from nguyenpanda.swan import Color
import time

def perf(precision: int = 4, unit: str = 's') -> Callable:

    def decorator(func: Callable) -> Callable:

        if unit == 'ns':
            timer = perf_counter_ns
            unit_str = 'nanoseconds'
        else:
            timer = perf_counter
            unit_str = 'seconds'

        def wrapper(*args, **kwargs):
            start = timer()
            result = func(*args, **kwargs)
            end = timer()
            print(f'Function '
                  f'{Color['c']}{func.__name__}{Color.reset} '
                  f'took {Color['c']}{end - start:.{precision}f}{Color.reset} {unit_str}')
            return result

        return wrapper

    return decorator

@perf(precision=1, unit='s')
def test(n=1):
    time.sleep(n)

if __name__ == '__main__':

    test(2)
