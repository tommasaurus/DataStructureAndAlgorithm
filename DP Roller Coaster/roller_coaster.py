# CS3100 - Spring 2024 - Programming Assignment 4
#################################
# Collaboration Policy: You may discuss the problem and the overall
# strategy with up to 4 other students, but you MUST list those people
# in your submission under collaborators.  You may NOT share code,
# look at others' code, or help others debug their code.  Please read
# the syllabus carefully around coding.  Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID:  rck9ng
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
class RollerCoaster:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.memo = []
        self.longest_path_start_node = None
        return

    class Node:
        def __init__(self, value, path_length=1, child=None, coordinates = []):
            self.value = value  
            self.path_length = path_length  
            self.child = child  
            self.coordinates = coordinates

        def path(self):            
            path = [self.value]
            current = self
            while current.child is not None:
                current = current.child
                path.append(current.value)
            return path

    def exists(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.columns

    def dfs(self, r, c, terrain):
        if self.memo[r][c] is not None:
            return self.memo[r][c]

        current_node = self.Node(terrain[r][c], coordinates=[r,c])
        max_path_length = 1

        for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            nr, nc = r + dx, c + dy
            if self.exists(nr, nc) and terrain[nr][nc] < terrain[r][c]:
                candidate_node = self.dfs(nr, nc, terrain)
                candidate_path_length = 1 + candidate_node.path_length
                if candidate_path_length > max_path_length:
                    max_path_length = candidate_path_length
                    current_node.child = candidate_node
                    current_node.path_length = max_path_length

        self.memo[r][c] = current_node
        return current_node

    # @return the length of the longest drop of the coaster
    def compute(self, terrain):
        self.rows = len(terrain)
        self.columns = len(terrain[0])
        self.memo = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        

        longest_path_start_node = None
        longest_path_length = 0

        for row in range(self.rows):
            for col in range(self.columns):
                start_node = self.dfs(row, col, terrain)
                if start_node.path_length > longest_path_length:
                    longest_path_length = start_node.path_length
                    longest_path_start_node = start_node
        
        self.longest_path_start_node = longest_path_start_node
        return longest_path_length

    # Get the terrain values in the coaster's main drop path, in order from highest to lowest elevation
    #
    # @return the ordered list of terrain values in the coaster's main drop
    def getCoasterPath(self):
        if self.longest_path_start_node:
            return self.longest_path_start_node.path()
        return []

    # Get the row,column starting point for the coaster's main drop path 
    #
    # @return an int[] with the first element being the row and the second being the column
    def getCoasterStart(self):
        if self.longest_path_start_node:
            return self.longest_path_start_node.coordinates
        return []

# terrain = [
#     [82, 90, 81, 42, 84, 30, 97, 9, 40, 66, 41, 75, 76, 56, 33, 4, 76, 94, 56, 36],
#     [55, 77, 79, 15, 95, 48, 7, 40, 42, 40, 50, 100, 62, 28, 30, 44, 26, 62, 43, 55],
#     [18, 0, 76, 12, 40, 21, 43, 96, 87, 48, 80, 20, 51, 14, 31, 11, 68, 6, 95, 83],
#     [89, 40, 45, 95, 29, 36, 95, 58, 80, 36, 26, 99, 41, 58, 51, 80, 95, 59, 98, 72],
#     [72, 10, 19, 31, 85, 10, 61, 96, 51, 23, 99, 40, 33, 74, 2, 81, 57, 20, 77, 4],
#     [45, 58, 18, 58, 30, 79, 34, 22, 68, 87, 10, 92, 100, 2, 51, 54, 49, 37, 42, 88],
#     [43, 99, 33, 41, 74, 61, 68, 68, 22, 68, 89, 3, 100, 79, 92, 33, 47, 44, 18, 33],
#     [46, 85, 47, 14, 47, 13, 1, 56, 6, 59, 39, 40, 1, 71, 71, 53, 88, 48, 77, 37],
#     [58, 58, 58, 76, 55, 74, 78, 56, 39, 25, 67, 16, 100, 66, 91, 25, 16, 82, 95, 59],
#     [52, 97, 63, 30, 81, 70, 89, 49, 86, 42, 62, 28, 67, 78, 57, 68, 9, 69, 7, 87],
#     [1, 11, 58, 55, 31, 10, 33, 9, 50, 1, 36, 54, 28, 14, 56, 64, 98, 12, 70, 27],
#     [25, 30, 25, 67, 20, 1, 96, 44, 65, 36, 52, 57, 99, 54, 53, 74, 30, 59, 90, 8],
#     [44, 42, 3, 49, 46, 4, 36, 40, 50, 70, 29, 65, 57, 54, 43, 84, 83, 86, 55, 38],
#     [88, 63, 70, 50, 55, 66, 34, 28, 95, 59, 14, 74, 36, 27, 50, 59, 93, 89, 43, 3],
#     [92, 63, 76, 9, 95, 69, 61, 53, 64, 12, 62, 57, 98, 22, 59, 43, 73, 12, 95, 65],
#     [69, 52, 24, 79, 52, 18, 23, 26, 94, 68, 21, 49, 74, 11, 21, 24, 89, 97, 39, 52],
#     [9, 62, 57, 18, 17, 62, 18, 59, 70, 83, 93, 80, 57, 95, 24, 41, 68, 79, 40, 8],
#     [38, 56, 65, 2, 56, 51, 46, 31, 1, 93, 69, 90, 55, 91, 39, 53, 2, 66, 91, 61],
#     [48, 1, 38, 94, 41, 51, 38, 26, 89, 67, 72, 68, 66, 29, 39, 15, 8, 18, 80, 74],
#     [36, 59, 51, 78, 55, 38, 2, 9, 17, 5, 43, 63, 16, 23, 92, 5, 16, 41, 36, 32]
# ]


# roller_coaster = RollerCoaster()
# # terrain = [
# #     [66, 78, 41,  3, 77],
# #     [ 4, 90, 41,  8, 68],
# #     [12, 11, 29, 24, 53],
# #     [ 0, 51, 58,  9, 28],
# #     [97, 99, 96, 58, 92]
# # ]
# longest_path_length = roller_coaster.compute(terrain)
# print(roller_coaster.getCoasterPath())
# print("Length of the longest path:", longest_path_length)
# print(roller_coaster.getCoasterStart())