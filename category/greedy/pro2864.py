def solution(input):
    import re

    in1, in2 = input.split(" ")
    # 5 -> 5, 6 -> 5 when get min value
    patern_chage_6 = re.compile("6")
    min = int(patern_chage_6.sub("5", in1)) + int(patern_chage_6.sub("5", in2))

    # 5 -> 6, 6 -> 6 when get max value
    patern_chage_5 = re.compile("5")
    max = int(patern_chage_5.sub("6", in1)) + int(patern_chage_5.sub("6", in2))
    return str(min) + " " + str(max)
