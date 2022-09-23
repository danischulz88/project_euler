import numpy as np

with open("dados.txt") as file:
    lines=file.readlines()
    lines=[int(line.rstrip()) for line in lines]
    print(lines)

    result=0
    for x in lines:
        result+=x
        
    print(result)

    result_fd=str(result)[:10]
    print(result_fd)

