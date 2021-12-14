def shift(num, i, side):
    if side == "right":
        # 101
        # 001
        num = num >> i 
    if side == "left":
        # 10100
        num = num << i
    print(num)

shift(4, 2, "right")
shift(4, 2, "left")