import time
def string_print1(string_,time_,color_):
    print(" ")
    for i in range(len(string_)):
        print(f"{color_}{string_[i]}",end="", flush=True)
        time.sleep(time_)
def string_print2(string_,time_,color_):

    for i in range(len(string_)):
        print(f"{color_}{string_[i]}",end="", flush=True)
        time.sleep(time_)
