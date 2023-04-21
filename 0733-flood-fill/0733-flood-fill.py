class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if (image[sr][sc] == color):
            return image
        
        def dfs(image, sr,sc,oldColor,newColor):
            if (sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != oldColor):
                return
            image[sr][sc] = newColor
            dfs(image, sr-1, sc, oldColor, newColor)
            dfs(image, sr+1, sc, oldColor, newColor)
            dfs(image, sr, sc-1, oldColor, newColor)
            dfs(image, sr, sc+1, oldColor, newColor)
            
        dfs(image, sr, sc, image[sr][sc], color)
        return image
        