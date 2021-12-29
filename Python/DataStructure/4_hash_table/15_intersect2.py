'''
两个Array求交集(允许重复)
'''


def intersect(nums1, nums2):
    dic = {}

    for ele in nums1:
        dic[ele] = dic.setdefault(ele, 0) + 1

    res = []
    for ele in nums2:
        if ele in dic and dic[ele] >= 1:
            res.append(ele)
            dic[ele] -= 1

    return res


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersect(nums1, nums2))
