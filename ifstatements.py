is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male or not(is_tall):
    print("You are a short male")
elif not(is_male) or is_tall:
    print("You are not a male but you are tall")
else:
    print("You are neither male nor tall")