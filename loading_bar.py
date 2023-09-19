import math
import os

def loading_bar(name, progress, length):
    name = name
    percent = 100 * (progress / float(length))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end=f" {name}")