import math



def loading_bar(num_bars, names, progress, length):
    names = names
    percent = []
    bar = []
    for lbar in num_bars:
        percent.append(100 * (progress[lbar] / float(length[lbar] + 1)))
        bar.append('█' * int(percent[lbar]) + '-' * (100 - int(percent[lbar])))

    print(f"""
        \r|{bar[0]}| {percent[0]:.2f}% {names[0]}
          |{bar[1]}| {percent[1]:.2f}% {names[1]}
          |{bar[2]}| {percent[2]:.2f}% {names[2]}
          """, end="\r")

