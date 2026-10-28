print("not True and False =", not True and False)
# (not True) and False -> False and False -> False

print("True or False and False =", True or False and False)
# True or (False and False) -> True or False -> True

print("not (5 > 3) =", not (5 > 3))
# 5 > 3 is True, and not True flips it to False

print("10 == 10 and 4 != 4 =", 10 == 10 and 4 != 4)
# 10 == 10 is True, but 4 != 4 is False, and and needs both sides True -> False

print("not False or not True =", not False or not True)
# (not False) or (not True) -> True or False -> True, since or only needs one side True