'''
两个Array求交集 unique
'''


def intersectionSet(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)

    return list(s1 & s2)


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersectionSet(nums1, nums2))
