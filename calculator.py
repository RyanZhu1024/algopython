def calculate(s):
    if s is None or len(s) == 0:
        return 0
    number, sign, res = 0, 1, 0
    st = []
    for c in s:
        if c.isdigit():
            number = number * 10 + int(c)
        elif c == '-':
            res += (number * sign)
            sign = -1
            number = 0
        elif c == '+':
            res += (number * sign)
            sign = 1
            number = 0
        elif c == '(':
            st.append(res)
            st.append(sign)
            number = 0
            sign = 1
            res = 0
        elif c == ')':
            res += (number * sign)
            res *= st.pop()
            res += st.pop()
            sign = 1
            number = 0
    if number != 0:
        res += sign * number
    return res

print(calculate("2"))