import array as arr
import collections

def musical_notes_array():
    midpoint_list = [17.1, 15.9, 14.25, 13.25, 12.75, 11.7, 11, 10.35, 9.75, 9.2, 8.65, 8.1]
    accumulated_dist = []
    musical_notes = ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B']

    open_E = arr.array('i', [x for x in range(12)])
    open_A = arr.array('i', [x + 5 for x in range(12)])
    open_D = arr.array('i', [x + 10 for x in range(12)])
    open_G = arr.array('i', [x + 15 for x in range(12)])
    open_B = arr.array('i', [x + 19 for x in range(12)])
    open_e = arr.array('i', [x + 24 for x in range(12)])
    mid_list = arr.array('d', midpoint_list)

    d = collections.OrderedDict()

    for itm in range(12):
        d[itm] = [open_E[itm], midpoint_list[itm], musical_notes[itm]]

    for itm in range(12):
        d[itm+12] = [open_A[itm], midpoint_list[itm], musical_notes[itm]]

    for itm in range(12):
        d[itm+24] = [open_D[itm], midpoint_list[itm], musical_notes[itm]]

    for itm in range(12):
        d[itm+36] = [open_G[itm], midpoint_list[itm], musical_notes[itm]]

    for itm in range(12):
        d[itm+48] = [open_B[itm], midpoint_list[itm], musical_notes[itm]]

    for itm in range(12):
        d[itm+60] = [open_e[itm], midpoint_list[itm], musical_notes[itm]]

    print(d)
    print(open_E)
    print(open_A)
    print(open_D)
    print(open_G)
    print(open_B)
    print(open_e)
    print(mid_list)
    return d


def main():
    musical_notes_array()

if __name__ == '__main__':
    main()

