import sys
import psutil


class Fib:
    def __init__(self):
        self.fib_array = [0, 1]

    def fibonacci(self, n):
        print(psutil.cpu_percent(interval=0.1), psutil.virtual_memory()._asdict()['percent'])
        if n < 0:
            print("Incorrect input")
            # First Fibonacci number is 0
        elif n == 1:
            return 0
        # Second Fibonacci number is 1
        elif n == 2:
            return 1
        else:
            return self.fibonacci(n-1)+self.fibonacci(n-2)

    def fibonacci_dp(self, n):
        print(psutil.cpu_percent(interval=0.1), psutil.virtual_memory()._asdict()['percent'])
        if n < 0:
            print("Incorrect input")
        elif n <= len(self.fib_array):
            return self.fib_array[n-1]
        else:
            temp_fib = self.fibonacci_dp(n-1)+self.fibonacci_dp(n-2)
            self.fib_array.append(temp_fib)
            return temp_fib

    @staticmethod
    def fibonacci_dp_opt_memory(n):
        print(psutil.cpu_percent(interval=0.1), psutil.virtual_memory()._asdict()['percent'])
        a = 0
        b = 1
        if n < 0:
            print("Incorrect input")
        elif n == 0:
            return a
        elif n == 1:
            return b
        else:
            for i in range(2, n):
                c = a + b
                a = b
                b = c
            return b


if __name__ == '__main__':
    print(sys.getrecursionlimit())
    print(Fib().fibonacci_dp(50))