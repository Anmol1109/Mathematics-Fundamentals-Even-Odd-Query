N = int(raw_input())
arr = map(int,raw_input().split())
for _ in xrange(int(raw_input())):
    x, y = map(lambda x : int(x) - 1,raw_input().split())
    print "Even" if arr[x] % 2 == 0 and (x == y or (x < y and arr[x + 1] != 0)) else "Odd"
