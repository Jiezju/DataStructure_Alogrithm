'''

accounts = [
    ["John", "johnsmith@mail.com", "john00@mail.com"], 
    ["John", "johnnybravo@mail.com"], 
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
    ["Mary", "mary@mail.com"]
]

Output = [
    ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
    ["John", "johnnybravo@mail.com"], 
    ["Mary", "mary@mail.com"]
]
'''

def accountsMerge(accounts):

    from collections import defaultdict
    emails_accounts_map = defaultdict(list) # email:account

    for i, account in enumerate(accounts):
        for j in range(1, len(accounts)):
            email = accounts[j]
            emails_accounts_map[email].append(i)

    visited = [False] * len(accounts)

    res = []

    def dfs(i, emails):
        if visited[i] == True:
            return
        
        visited[i] = True

        for email in accounts[i][1:]:
            emails.add(email)

            for nbr in emails_accounts_map[email]:
                dfs(nbr, emails)



    for i, account in enumerate(accounts):        
        name = account[0]
        emails = set()
        dfs(i, emails)

        res.append([[name] + list(emails)])

    return res
