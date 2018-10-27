import array as arr

class Note(object):

    def __init__(self, note_name="", dist_btwn=0):
        self.note_name = note_name
        self.dist_btwn = dist_btwn

    def distance(self):
        return self.dist_btwn

    def string_num(self):
        return self.str_num

    def set_dist(self, x):
        self.dist_btwn = x

    def set_string_num(self, x):
        self.str_num = x


class Strings(object):
    midpoint_list = [17.1, 15.9, 14.25, 13.25, 12.75, 11.7, 11,
                     10.35, 9.75, 9.2, 8.65, 8.1, 7.75, 7.0, 6.85, 6.1, 6.25, 5.85, 5.4]

    open_E = arr.array()
    open_A = arr.array()
    open_D = arr.array()
    open_G = arr.array()
    open_B = arr.array()
    open_e = arr.array()


    def create_note(self, x, y):
        new_note = Note(x, y)
        return new_note

    def populate_array():
        musical_notes = ['E', 'F', 'G', 'A', 'B', 'C', 'D']
        notes_list = []

