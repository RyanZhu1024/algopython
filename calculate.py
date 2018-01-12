def calcualte(digits, target):
    candidates = '+-*/'
    return dfs(digits, target, candidates, [])

def dfs(digits, target, candidates, cur):
    if len(cur) == len(digits) - 1:
        return validate(digits, target, cur)
    for c in candidates:
        cur += [c]
        if dfs(digits, target, candidates, cur):
            return True
        cur.pop()
    return False

def validate(digits, target, cur):
    signs = ''.join(cur) + ' '
    exp = ''.join(i for j in zip(digits, signs) for i in j)
    return eval(exp) == target

print(calcualte('321', 0))
