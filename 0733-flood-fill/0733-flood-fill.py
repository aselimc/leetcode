class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = [(sr, sc)]
        old_color = image[sr][sc]
        image[sr][sc] = color
        visited = [(sr, sc)]
        while queue:
            sr, sc = queue.pop(0)
            if sr-1 >= 0:
                if image[sr-1][sc] == old_color:
                    image[sr-1][sc] = color
                    if (sr-1, sc) not in visited:
                        queue.append((sr-1, sc))
                        visited.append((sr-1, sc))
            if sr+1 <= len(image)-1:
                if image[sr+1][sc] == old_color:
                    image[sr+1][sc] = color
                    if (sr+1, sc) not in visited:
                        queue.append((sr+1, sc))
                        visited.append((sr+1, sc))
            if sc-1 >= 0:
                if image[sr][sc-1] == old_color:
                    image[sr][sc-1] = color
                    if (sr, sc-1) not in visited:
                        queue.append((sr, sc-1))
                        visited.append((sr, sc-1))
            if sc+1 <= len(image[0])-1:
                if image[sr][sc+1] == old_color:
                    image[sr][sc+1] = color
                    if (sr, sc+1) not in visited:
                        queue.append((sr, sc+1))
                        visited.append((sr, sc+1))
        return image