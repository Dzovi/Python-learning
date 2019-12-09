# If statements

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are male and tall.")
elif is_male and not(is_tall):
    print("You are male but not tall.")
elif is_tall and not(is_male):
    print("You are tall but not male.")
else:
    print("You are not male or tall.")