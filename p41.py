
s, n = input().split()
s = sorted(s)
n = int(n)

for r in range(1, n + 1):
    def combine(start, result):
        if len(result) == r:
            print(result)
            return

        for i in range(start, len(s)):
            combine(i + 1, result + s[i])

    combine(0, "")
