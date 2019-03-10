def main():
    # print results
    print(fib(15))
    print(cache_decor)
    pass

# func to save data about
def fib(n):
    if n < 2:
        return n
    if n in cache_decor:
        return cache_decor[n]
    ans = fib(n - 1) + fib(n - 2)
    cache_decor[n] = ans
    return ans

# defining cache decorator
cache_decor = {}
if __name__ == '__main__':
    main()
