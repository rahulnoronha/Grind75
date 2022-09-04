class Solution:
    def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        curr_colour = image[sr][sc]
        height = len(image)
        width = len(image[0])
        def dfs(sr,sc):
            if(0<=sr<height and 0<=sc<width and image[sr][sc]==curr_colour and image[sr][sc]!=color):
                image[sr][sc] = color
                dfs(sr, sc-1)
                dfs(sr,sc+1)
                dfs(sr+1,sc)
                dfs(sr-1,sc)
            else:
                return
        dfs(sr,sc)
        return image
    
print(Solution.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))
print(Solution.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0))