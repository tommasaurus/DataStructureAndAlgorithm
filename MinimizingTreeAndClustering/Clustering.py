# CS3100 - Spring 2024 - Programming Assignment 3
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
# Your Computing ID: rck9ng
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################

import heapq as pq

class Clustering:
    def __init__(self):
        return

     # This is the method that should compute the maximum possible
     # spacing for the clustering. It takes as input an integer k
     # and the nxn array of distances. 
     #
     # @return the maximum possible spacing of the clustering 
    def compute(self, k, distances):
        nodes = [i for i in range(0,len(distances))]
        minimal_spanning_tree = []
        current_node = 0
        
        visited = []
        done = set()
        done.add(current_node)
        r = current_node
        while len(minimal_spanning_tree) < len(nodes) - 1:
            for c, each in enumerate(distances[current_node]):
                if each != 0:
                    pq.heappush(visited, (distances[r][c], r, c))
            next_length = len(done) + 1
            while len(done) < next_length:                
                minimum_edge = pq.heappop(visited)
                print(minimum_edge)
                minimum_distance = minimum_edge[0]                
                col = minimum_edge[2]
                if col not in done:
                    print(col)
                    done.add(col)
                    r = col
                    minimal_spanning_tree.append(minimum_distance)
        
        for i in range(k-2):
            minimal_spanning_tree.remove(max(minimal_spanning_tree))
        
        # for r in nodes:
        #     if r != len(nodes) - 1:            
        #         for c in range(r+1,len(nodes)):
        #             if c != r:
        #                 pq.heappush(visited, (distances[r][c], r, c))
        #         next_length = len(done) + 1
        #         while len(done) < next_length:                
        #             minimum_edge = pq.heappop(visited)
        #             print(minimum_edge)
        #             minimum_distance = minimum_edge[0]                
        #             col = minimum_edge[2]
        #             if col not in done:
        #                 print(col)
        #                 done.add(col)
        #                 minimal_spanning_tree.append(minimum_distance)

        # while len(minimal_spanning_tree) < len(nodes) - 1:
        #     minimum_edge = pq.heappop()
        #     minimum_distance = minimum_edge[0]
        #     row = minimum_edge[1]
        #     col = minimum_edge[2]


        # visited = []
        # while len(minimal_spanning_tree) < len(nodes) - 1:    
        #     added_nodes = set()

        #     for each in distances[current_node] and each != 0:
        #         visited.append(each)
        #     minimum_edge = min(visited)
        #     current_node += 1
        return max(minimal_spanning_tree)

# matrix_data = """0 200 444 789 229 435 454 694 262 531
# 200 0 207 793 663 391 438 515 870 229
# 444 207 0 64 993 345 196 455 651 956
# 789 793 64 0 622 320 381 952 114 535
# 229 663 993 622 0 208 389 109 504 982
# 435 391 345 320 208 0 81 206 235 802
# 454 438 196 381 389 81 0 990 145 622
# 694 515 455 952 109 206 990 0 923 976
# 262 870 651 114 504 235 145 923 0 307
# 531 229 956 535 982 802 622 976 307 0"""
# cluster = [[0, 18, 21, 23, 5],
#             [18, 0, 54, 30, 31],
#             [21, 54, 0, 15, 32],
#             [23, 30, 15, 0, 15],
#             [5, 31, 32, 15, 0]]

# matrix = [list(map(int, row.split())) for row in matrix_data.strip().split('\n')]
# tree = compute(0,2, matrix)
# print(tree)
