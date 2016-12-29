import os
from skimage import io, util

train_dir = './bakedata/train/'
val_dir = './bakedata/val/'
test_dir = './bakedata/test/'

label = 0
dirs = os.listdir('./rawdata')
for d in dirs:
    path = os.path.join('./rawdata', d, 'train')
    print(path)
    images = os.listdir(path)
    print('found ' + str(len(images)) + ' images')
    count = 0
    for img_name in images:
        if count < 720: # train : val = 9 : 1
            img = io.imread(os.path.join(path, img_name))
            img = util.pad(img, ((16,16),(16,16),(0,0)),'edge')
            io.imsave(os.path.join(train_dir, img_name), img)
        else:
            img = io.imread(os.path.join(path, img_name))
            img = util.pad(img, ((16,16),(16,16),(0,0)),'edge')
            io.imsave(os.path.join(val_dir, img_name), img)
        count += 1
        if count == 800:
            count = 0;

    path = os.path.join('./rawdata', d, 'test')
    print(path)
    images = os.listdir(path)
    print('found ' + str(len(images)) + ' images')
    for img_name in images:
        img = io.imread(os.path.join(path, img_name))
        img = util.pad(img, ((16,16),(16,16),(0,0)),'edge')
        io.imsave(os.path.join(test_dir, img_name), img)

    label += 1
