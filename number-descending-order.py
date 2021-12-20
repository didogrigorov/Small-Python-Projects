def descending_order(num):
    # Bust a move right here

    if num < 0:
        print(0)
    else:
        nums = str(num)
        newnum = nums[::-1]
        newnums = str(newnum)
        print(newnums)

descending_order(0)
