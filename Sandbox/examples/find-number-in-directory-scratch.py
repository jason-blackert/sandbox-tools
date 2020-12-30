import os

if __name__ == "__main__":

    dir_list = os.listdir(".")
    curr_index = 0
    for i in range(len(dir_list)):
        print(i, dir_list[i])
