import random
feet_in_mile = 5200
meters_in_kilometer = 1000
beattles = ["John Lennon","Paul McCartney","George Harrison","Ringo Star"]
def get_file_ext(filename):
    return filename[filename.index(".")+1:]
def roll_dice(num):
    return random.randint(1,num)