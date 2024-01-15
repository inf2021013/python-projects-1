import random
import string

def create_file(file_name, num_items):
    # Open File:
    f = open(file_name, "w")
    for i in range(num_items):
        # Random integer form 0 to 1.000.000:
        num = random.randint(0, 1000000)
        # Random strings for s1, s2 and s3:
        s1 = ''.join((random.choice(string.ascii_letters) for x in range(10)))
        s2 = ''.join((random.choice(string.ascii_letters) for x in range(10)))
        s3 = ''.join((random.choice(string.ascii_letters) for x in range(10)))
        # Write in given file name:
        f.write(str(num) + "\n")
        f.write(s1 + "\n")
        f.write(s2 + "\n")
        f.write(s3 + "\n")
    f.close()

# Creating file:
create_file("my_file.txt",100)