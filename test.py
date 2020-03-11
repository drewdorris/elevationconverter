import math
import subprocess
import os
import re
import glob
from PIL import Image

Image.MAX_IMAGE_PIXELS = 1000000000;

def irlToMC(num):
    if num < 1:
        return -1 * math.sqrt(-.25 * num);
    if num < 469:
        return (num / 6.1) + 63;
    if num > 468:
        return (20 * math.log(num)) + math.sqrt(.6 * num);

def handleImage(file):
    result = subprocess.run(['gdalinfo', '-json', file], stdout=subprocess.PIPE);
    decoded = result.stdout.decode('utf-8');
    max = re.search('.*maximum.*\n', decoded).group().replace('\"maximum\":', '').replace('\n', '').replace(',', '').replace(' ', '');
    min = re.search('.*minimum.*\n', decoded).group().replace('\"minimum\":', '').replace('\n', '').replace(',', '').replace(' ', '');
    maxRealigned = irlToMC(float(max));
    minRealigned = irlToMC(float(min));

    imageName = 'testing.png';
    subprocess.call(['gdal_translate', '-of', 'PNG', '-scale', min, max, str(minRealigned), str(maxRealigned), '-co', 'worldfile=yes', file, imageName]);
    img = Image.open(imageName);

    img.save('images/' + imageName);
    print('Image saved: ' + imageName);

for file in glob.glob('./*.img'):
    handleImage(file);
