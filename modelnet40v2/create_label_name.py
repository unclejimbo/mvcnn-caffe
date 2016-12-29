import os

ln_file = open('label_name.txt', 'w')
words = os.listdir('./rawdata')
label = 0
for word in words:
    ln_file.write(str(label) + ' ' + word + '\n')
    label += 1
