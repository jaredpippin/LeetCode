class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        for i in range(0,len(candies)):
            print("Extra:",candies[i] + extraCandies)
            for j in range(0,len(candies)):
                print(candies[j])
                if (candies[i] + extraCandies >= candies[j]):
                    result[i] = True
                else:
                    print("False!")
                    result[i] = False
                    break
        return result