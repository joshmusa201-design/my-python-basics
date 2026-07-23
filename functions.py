print ("hello world")

def joshu_musa(insert):
    if  insert % 3 == 0 and insert % 5 == 0:
        print ("joshu_musa")
    elif insert % 5 == 0:
        print ("musa")
    elif insert % 3 == 0:
        print ("joshu")
    elif insert % 3 != 0 and insert % 5 != 0:
        print ("invalid")
    

joshu_musa(15)
