"""
dir_list = os.listdir("logs")
curr_index = 0
for i in range(len(dir_list)):
    temp = int(dir_list[i].replace(" ","").replace("contour-file-","").replace(".txt",""))
    if temp > curr_index:
        curr_index = temp
"""