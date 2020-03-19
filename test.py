import math
import subprocess
import os
import re
import glob
import json
import yaml
import time
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
    fileType = 'unknown';
    if 'one_meter' in file:
        fileType = '1m';
    elif 'nem19' in file:
        fileType = '1_9arc';
    elif 'imgn' in file:
        fileType = '30m'
    print(fileType);
    
    result = subprocess.run(['gdalinfo', '-json', file], stdout=subprocess.PIPE);
    decoded = result.stdout.decode('utf-8');
    jsonStuff = json.loads(decoded);

    left = 0;
    top = 0;
    right = 0;
    bottom = 0;
    
    for i in jsonStuff['wgs84Extent']['coordinates']:
        index = 0;
        for j in i:
            for k in j:
                if index == 0:
                    left = k;
                elif index == 1:
                    top = k;
                elif index == 4:
                    right = k;
                elif index == 5:
                    bottom = k;
                index += 1;
    if left == 0 or top == 0 or right == 0 or bottom == 0:
        print('Oh no something went wrong no!!!');
        return;

    width = 0;
    for i in jsonStuff['size']:
        width = i;
        break;
    inte = 0;
    max = jsonStuff['bands'][0]['maximum'];
    min = jsonStuff['bands'][0]['minimum'];
    maxRealigned = irlToMC(max);
    minRealigned = irlToMC(min);

    imageNameNoFile = fileType + ';' + str(int(left * 10000)).replace('.', '') + ';' + str(int(top * 10000)).replace('.', '');
    imageName = imageNameNoFile + '.png';
    subprocess.call(['gdal_translate', '-of', 'PNG', '-scale', str(min), str(max), str(minRealigned), str(maxRealigned), '-co', 'worldfile=yes', file, imageName]);
    img = Image.open(imageName);

    img.save('images/' + imageName);
    print('Image saved: ' + imageName);

    yaml_data = {
        imageNameNoFile: {
            'left': left,
            'top': top,
            'right': right,
            'bottom': bottom,
            'width': width,
            'type': fileType,
        }
    }

    with open('example.yml','r') as yamlfile:
        cur_yaml = yaml.safe_load(yamlfile);
        cur_yaml['images'].update(yaml_data);

    if cur_yaml:
        with open('example.yml','w') as yamlfile:
            yaml.safe_dump(cur_yaml, yamlfile);

    os.remove(imageName);
    os.remove(imageName + '.aux.xml');
    os.remove(imageNameNoFile + '.wld');

while True:
    for file in glob.glob('./*.img'):
        handleImage(file);
        os.remove(file);
    time.sleep(30);
