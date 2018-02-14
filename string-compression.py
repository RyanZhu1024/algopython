import itertools


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        i, j = 0, 0
        index = 0
        while j < len(chars):
            if chars[j] == chars[i]:
                j += 1
            else:
                count = j - i
                if count == 1:
                    chars[index] = chars[i]
                    index += 1
                else:
                    countStr = str(count)
                    chars[index: index + len(countStr)] = itertools.chain([chars[i]], [x for x in countStr])
                    index += len(countStr)
                i = j
        if j > i:
            count = j - i
            if count == 1:
                chars[index] = chars[i]
                index += 1
            else:
                countStr = str(count)
                chars[index: index + len(countStr) + 1] = itertools.chain([chars[i]], [x for x in countStr])
                index += (len(countStr) + 1)
        return index

print(Solution().compress(["a","a","b","b","c","c","c"]))