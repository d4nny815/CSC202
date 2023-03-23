# Given integer n, returns True or False based on reachability of goal
# See the write up for "rules" for bears
def bears(n: int) -> bool:
    """Given integer n, returns True or False based on reachability of goal.
    1. If n is even, then you may give back n/2 bears.
    2. If n is divisible by 3 or 4, then you may multiply the last two digits of n and give back this many bears.
    3. If n is divisible by 5, then you may give back 42 bears.
    bears(250) is True"""
    if n == 42:
        return True
    if n < 42:
        return False
    if n % 2 == 0 and bears(n // 2):
        return True
    if n % 3 == 0 and bears(n - (n % 10) * ((n % 100) // 10)):
        return True
    if n % 4 == 0 and bears(n - (n % 10) * ((n % 100) // 10)):
        return True
    if n % 5 == 0 and bears(n - 42):
        return True
    return False

if __name__ == "__main__":
    print(bears(250))
