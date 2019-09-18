file_1="/Volumes/Z/Lab4-1.txt"
file_2="/Volumes/Z/T1/Edited_file.txt"

with open(file_1,'r') as f:
    for line in f.readlines():
        line.strip(" ")
        x, y= line.split('#')
        print(y)
        with open(file_2,'a')as f2:
            f2.writelines(y)
