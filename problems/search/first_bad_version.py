def isBadVersion(version):
    pass

def first_bad_version(n):
    if not n:
        return -1
    left , right = 1, n
    while left + 1 <= right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid
    return right
