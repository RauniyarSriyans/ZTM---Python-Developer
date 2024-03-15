import sys
import os
from PIL import Image

# grab the first and second arguments
# first is the target folder where you get the images 
# second is the destination folder where converted images are stored

source = sys.argv[1]
destination = sys.argv[2]

# check if destination exists, if not, create a new one
if not os.path.exists(destination):
    os.makedirs(destination)

for filename in os.listdir(source):
    img = Image.open(f'{source}{filename}')
    clean_name = os.path.splitext(filename)
    img.save(f'{destination}{clean_name[0]}.png', 'png')
    print
