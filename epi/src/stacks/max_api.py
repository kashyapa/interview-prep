#!/usr/bin/env python




class max_stack:
    max_cache = []
    max_count = {}

    def __init__(self):
        self.st = []

    def max_val(self):
        return max_stack.max_cache[-1] if len(max_stack.max_cache) > 0 else -float('inf')

    def pop(self):
        val = self.st.pop()
        if val in max_stack.max_count:
            max_stack.max_count[val] -= 1

        if max_stack.max_count[val] == 0:
            max_stack.max_cache.pop()
            del(max_stack.max_count[val])
        print(self.st)
        return val

    def push(self, n):
        if n > self.max_val():
            max_stack.max_cache.append(n)
            max_stack.max_count[n] = 1
        elif n == max_stack.max_cache[-1]:
            max_stack.max_count[n] += 1

        self.st.append(n)
        print(self.st)


if __name__ == "__main__":
    stack = max_stack()
    stack.push(1)
    stack.push(3)
    stack.push(-1)
    stack.push(10)
    stack.push(23)
    stack.push(5)

    print(stack.max_val())
    stack.push(23)
    stack.push(16)
    print(stack.max_val())
    stack.pop()
    print(stack.max_val())
    stack.pop()
    print(stack.max_val())
    stack.pop()
    print(stack.max_val())
    stack.pop()
    print(stack.max_val())
    stack.pop()
    print(stack.max_val())
    stack.pop()
    print(stack.max_val())
    stack.pop()
    print(stack.max_val())
    stack.pop()
    print(stack.max_val())
    stack.pop()
    print(stack.max_val())
