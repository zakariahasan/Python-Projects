with open("/Volumes/Z/T1/Lab-3-2_configuration.txt","r") as f:

    line = f.readline()
    cnt = 1

    while line:
        x, y = f.readline().split("#")
        line = f.readline()
        cnt += 1

        with open("/Volumes/Z/T1/Lab-3-2_configuration_new.txt", "a") as f2:
            f2.write(y)
           

 
