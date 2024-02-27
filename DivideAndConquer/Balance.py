# CS3100 - Spring 2024 - Programming Assignment 2
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

class Balance:

    def __init__(self):
        return
        


    # This is the method that should run the computation
    # of the balance score for the bookshelf.  You should
    # write an additional recursive method that compute
    # calls.  Your method may have different return values.
    #
    # @return The balance score for the bookshelf.
    
    def compute(self, bookshelf):
        sorted_list, B_L, B_R, balance_score = self.divideAndConquer(bookshelf)
        return balance_score
    
    def divideAndConquer(self, bookshelf):
        if len(bookshelf) <= 1:
            return bookshelf, 0, 0, 0

        middle = len(bookshelf)//2
        left, left_B_L, left_B_R, left_balance = self.divideAndConquer(bookshelf[:middle])
        right, right_B_L, right_B_R, right_balance = self.divideAndConquer(bookshelf[middle:])

        merged, current_step_B_L, current_step_B_R = self.merge(left, right)
        B_L = left_B_L + right_B_L + current_step_B_L
        B_R = left_B_R + right_B_R + current_step_B_R

        balance_score = abs(B_L - B_R)
        return merged, B_L, B_R, balance_score

    def merge(self, left, right):
        B_L = B_R = 0
        sorted_list = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                smaller_item = left[left_index]
                B_L += len(right) - right_index
                left_index += 1
            elif left[left_index] == right[right_index]:
                if left[-1] != left[left_index]:
                    temp_index = left_index
                    while left[temp_index] == right[right_index]:
                        temp_index += 1
                    B_R += len(left) - temp_index
                smaller_item = right[right_index]
                right_index += 1
            else:
                smaller_item = right[right_index]
                B_R += len(left) - left_index
                right_index += 1

            sorted_list.append(smaller_item)

        while left_index < len(left):
            sorted_list.append(left[left_index])
            left_index += 1 
            
        while right_index < len(right):
            sorted_list.append(right[right_index])
            right_index += 1
            
        return sorted_list, B_L, B_R
# test = [10,37,79,10,71,62,14,76,54,80,25,44]

# def calculate_balance_score(books):#     
#     def balance_left(scores):
#         bl = [0] * len(scores)
#         for i in range(len(scores)):
#             bl[i] = sum(scores[j] < scores[i] for j in range(i))
#         return bl

#     def balance_right(scores):
#         br = [0] * len(scores)
#         for i in range(len(scores) - 1, -1, -1):
#             br[i] = sum(scores[j] < scores[i] for j in range(i + 1, len(scores)))
#         return br

#     bl = balance_left(books)
#     br = balance_right(books)

#     return abs(sum(bl) - sum(br))

# # mylist = [10,2,8,4,12]1
# # print(calculate_balance_score(mylist))
# if __name__ == "__main__":
#     mylist = [9,9,9,9,9]
#     myList1 = [10,2,8,4,12]
#     test = [10,37,79,10,71,62,14,76,54,80,25,44]
#     # print(mergesort(list), B_L, B_R)
#     # test = [10,37,79,10,71,62]
#     books = Balance()
#     print( Balance.compute(books, myList1))
#     print(calculate_balance_score(test))