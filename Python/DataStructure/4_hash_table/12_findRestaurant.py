'''
假设Andy和Doris各有一个喜欢餐厅的清单，存储格式为string。
请你帮她们找到她们都喜欢的餐厅：假设存在多对，要求两个餐厅的Index相加最小
'''


def findRestaurant(A, B):
    dic = {}
    res = []

    for i, rest in enumerate(A):
        dic[rest] = i

    for i, rest in enumerate(B):
        if rest in dic:
            res.append([rest, abs(dic[rest] + i)])

    index_diff = 1000
    result = None
    for ele in res:
        if ele[1] < index_diff:
            index_diff = ele[1]
            result = [ele[0]]

    return result


if __name__ == '__main__':
    A = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    B = [
        "Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse",
        "Shogun"
    ]
    print(findRestaurant(A, B))
