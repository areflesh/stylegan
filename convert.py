from PIL import Image
import os 
dir="./raw_images"
for i in os.listdir(dir):
    im = Image.open(dir+"/"+i)
    if im.format!="JPEG":
        rgb_im = im.convert('RGB')
        rgb_im.save(dir+'/'+os.path.splitext(i)[0]+'.jpg')
        os.remove(dir+"/"+i)
