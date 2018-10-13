import array as arr

# class Note(object):
#
#     def __init__(self):
#         self.note_name = ""
#         self.dist_btwn = 0
#         self.str_num = 0
#
#     def distance(self):
#         return self.dist_btwn
#
#     def string_num(self):
#         return self.str_num
#
#     def set_dist(self, x):
#         self.dist_btwn = x
#
#     def set_string_num(self, x):
#         self.str_num = x

midpoint_list = []
musical_notes = ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E']

open_E = arr.array()
open_A = arr.array()
open_D = arr.array()
open_G = arr.array()
open_B = arr.array()
open_e = arr.array()

for i in range(0, 12):
    open_E[i] = i
    open_A[i] = i + 5
    open_D[i] = i + 10
    open_G[i] = i + 15
    open_B[i] = i + 19
    open_e[i] = i + 24
