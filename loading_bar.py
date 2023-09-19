import math

def loading_bar(progress, length):
    percent = 100 * (progress / float(length))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")
