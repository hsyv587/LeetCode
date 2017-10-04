class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        currDir = ''
        res = ''
        path += '/'
        for i in range(len(path)):
            if path[i] == '/':
                if currDir:
                    if currDir == '..' and stack:
                        del stack[-1]
                    elif currDir != '.' and currDir != '..':
                        stack.append(currDir)
                    currDir = ''
            else:
                currDir += path[i]
        for i in range(len(stack)):
            res += '/'
            res += stack[i]
        if not res:
            return '/'
        return res
        