class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        def convert(string):
            addy = list(string.split('.'))
            return addy
        def intersperse(lst, item):
            result = [item] * (len(lst) * 2 - 1)
            result[0::2] = lst
            return result
        new = convert(address)
        new = intersperse(new,'[.]')
        result = ''
        return result.join(new)
        