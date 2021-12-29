'''
subdomain
'''


def subdomainVisits(cpdomains):
    dic = {}
    result = []
    for addr in cpdomains:
        temp = addr.split()
        num = int(temp[0])
        domains = temp[1].split('.')

        for i in range(len(domains)):
            key = '.'.join(domains[i:])
            dic[key] = dic.setdefault(key, 0) + num

    for k, v in dic.items():
        ele = str(v) + ' ' + k
        result.append(ele)

    return result


if __name__ == '__main__':
    cp = ["9001 scholar.google.com"]
    print(subdomainVisits(cp))
