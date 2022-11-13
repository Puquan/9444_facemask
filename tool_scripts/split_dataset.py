import os
import shutil

image_dir = os.listdir('./images')
label_dir = os.listdir('./labels')

image_dir.sort()
label_dir.sort()

    
pivot1 = int(len(image_dir) * 0.8)
pivot2 = int(len(image_dir) * 0.9)



for i in range(pivot1):
    img_path = os.path.join('./images', image_dir[i])
    label_path = os.path.join('./labels', label_dir[i])
    shutil.copy(img_path, './train/images')
    shutil.copy(label_path, './train/labels')
    print('copy ' + img_path + ' to ./train/images')
    
    
    
for i in range(pivot1,pivot2):
    img_path = os.path.join('./images', image_dir[i])
    label_path = os.path.join('./labels', label_dir[i])
    shutil.copy(img_path, './valid/images')
    shutil.copy(label_path, './valid/labels')
    print('copy ' + img_path + ' to ./valid/images')
    
    
for j in range(pivot2,len(image_dir)):
    img_path = os.path.join('./images', image_dir[i])
    label_path = os.path.join('./labels', label_dir[i])
    shutil.copy(img_path, './test/images')
    shutil.copy(label_path, './test/labels')
    print('copy ' + img_path + ' to ./test/images')
