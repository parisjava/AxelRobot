#make a python script to scan through a simple text file and store each line into
# data structure


def read_in(x):
    f = open(x, "r")

    if f.mode == 'r':
        contents = f.read()
        print(contents)

    fl = f.readlines()

    for j in fl:
        print(j)
        #append them to data structure of choice here

    f.close()

def store_in_tuple():

def store():

def main():
    read_in("midpoints.txt")
if __name__ == "__main__":
    main()

