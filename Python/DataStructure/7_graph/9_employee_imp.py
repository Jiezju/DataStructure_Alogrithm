'''
Employee Importance
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1

Output: 11
'''

def getImportance(employees, em_id):
    return dfs(employees, em_id)

def dfs(employees, em_id):

    for employee in employees:
        if employee[0] == em_id:
            if employee[2] != []:
                for ele in employee[2]:
                    return employee[1] + dfs(employees, ele)
            else:
                return employee[1]
