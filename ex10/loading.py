import time
import sys

def update_percent(count, nb):

    percent = int(count * 100 / nb)
    if percent < 0:
        percent = 0

    return percent

def update_visual(count, visual, nb):

    frequency = int(nb / 10)
    if count % frequency == 0:
            visual = visual.replace(">", "=", 1)
            visual = visual.replace(" ", ">", 1)

    return visual

def update_time_left(elapsed_time, count, nb):

    time_for_one_elem = elapsed_time / count
    elem_left = nb - count
    time_left = elem_left * time_for_one_elem

    return time_left

def ft_progress(lst, nb):

    count = 0
    visual = "          "
    start_time = time.time()

    for i in lst:
        yield i
        count += 1

        visual = update_visual(count, visual, nb)
        percent = update_percent(count, nb)
        
        now = time.time()
        elapsed_time = now - start_time

        time_left = update_time_left(elapsed_time, count, nb)

        print("\rETA:", f"{time_left:.2f}",  "[" + str(percent) + "%]" + "[" + visual + "]", str(count) + "/" + str(nb), "| elapsed time", f"{elapsed_time:.2f}" + "s", end='', flush=True)
        
        

def main():
    args = sys.argv[1:]

    if len(args) != 2:
        return
    listy = range(int(args[0]))
    ret = 0
    for elem in ft_progress(listy, int(args[0])):
        ret += (elem + 3) % 5
        time.sleep(float(args[1]))
    print("")
    print(ret)



if __name__=="__main__":
    main()
