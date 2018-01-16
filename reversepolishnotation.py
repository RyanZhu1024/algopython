class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st= []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                st.append(int(t))
            else:
                r, l = st.pop(), st.pop()
                if t == '+':
                    st.append(l + r)
                elif t == '-':
                    st.append(l - r)
                elif t == '*':
                    st.append(l * r)
                else:
                    print(l,r)
                    st.append(l // r)
                print(st[-1])
        return st.pop()

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))