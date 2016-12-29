import os, sys, re

def run(train, val, test, step = 1):
    train_text = open(train, 'w')
    val_text = open(val, 'w')
    test_text = open(test, 'w')

    name_label = {}
    with open('./label_name.txt') as f:
        for line in f:
            (label, name) = line.split()
            name_label[name] = label

    count = 0
    images = os.listdir('./bakedata/train')
    for img in images:
        s = re.search('\d', img)
        name = img[:s.start()-1]
        label = name_label[name]
        if count < 80:
            line = img + ' ' + str(label) + '\n'
            train_text.write(line)
        count += 1
        if count == int(step) * 80:
            count = 0

    count = 0
    images = os.listdir('./bakedata/val')
    for img in images:
        s = re.search('\d', img)
        name = img[:s.start()-1]
        label = name_label[name]
        if count < 80:
            line = img + ' ' + str(label) + '\n'
            val_text.write(line)
        count += 1
        if count == int(step) * 80:
            count = 0

    count = 0
    images = os.listdir('./bakedata/test')
    for img in images:
        s = re.search('\d', img)
        name = img[:s.start()-1]
        label = name_label[name]
        if count < 80:
            line = img + ' ' + str(label) + '\n'
            test_text.write(line)
        count += 1
        if count == int(step) * 80:
            count = 0

if __name__ == '__main__':
    if (len(sys.argv) == 4):
        run(sys.argv[1], sys.argv[2], sys.argv[3])
    elif (len(sys.argv) == 5):
        run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print('Usage:')
        print('    python create_data_text.py your_train.txt your_validation.txt your_test.txt [sample_step=1]')
