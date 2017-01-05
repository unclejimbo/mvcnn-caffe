import caffe
import os
import sys
import re
import numpy as np

n_views = 80 # change this if you are not using 80 views per model"
n_classes = 40 # change this if you are not using 40 class dataset
model = "./mvcnn_caffenet_simple/deploy.prototxt" # change this to your model defiintion
weights = "./mvcnn_caffenet_simple/caffenet_train_iter_15000.caffemodel" # change this to your trained model
mean_file = "./modelnet40v2/mean.binaryproto" # change this to your mean file
label_name_file = "./modelnet40v2/label_name.txt" # change this to your label_name file

def predict(images, net, transformer):
    if (len(images) != n_views):
        sys.exit("Error: expecting ", n_views, " images in a batch")

    votes = np.zeros(n_views)
    for img in images:
        net.blobs['data'].data[...] = transformer.preprocess('data', img)
        net.forward()
        scores = net.blobs['prob'].data[0].flatten()
        prediction = np.argmax(scores)
        votes[prediction] += 1
    return np.argmax(votes)

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        sys.exit("Usage: python classify_model_simple.py /path/to/image_directory/")

    files = os.listdir(sys.argv[1])
    if (len(files) % n_views != 0):
        sys.exit("Error: num of input images should be divisible by " + str(n_views))

    # Import label-name correspondence
    label_name = {}
    with open(label_name_file) as f:
        for line in f:
            (label, name) = line.split()
            label_name[int(label)] = name

    # Net
    net = caffe.Net(model, weights, caffe.TEST)

    # Convert image mean
    mean_blob = caffe.proto.caffe_pb2.BlobProto()
    mean_bin = open(mean_file, 'rb').read()
    mean_blob.ParseFromString(mean_bin)
    mean = np.array(caffe.io.blobproto_to_array(mean_blob))
    # have to manually slice mean size because caffe assume mean size to be the same as input dims,
    # during training both mean and image sizes could automatically get cropped to network input dims,
    # however when testing only image size could be cropped automatically by deployment input layer
    mean = mean[0, :, 14:-15, 14:-15]

    # Transform data
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2, 0, 1))
    transformer.set_mean('data', mean)
    transformer.set_raw_scale('data', 255)
    transformer.set_channel_swap('data', (2, 1, 0))

    # Load images and predict
    count = 0;
    right = 0;
    for i in range(len(files) / n_views):
        images = []
        for j in range(i*n_views, (i+1)*n_views):
            img = caffe.io.load_image(os.path.join(sys.argv[1], files[j]))
            images.append(img)

        # Extract label from file name
        pos = re.search("\d", files[j])
        name = files[j][:pos.start()-1]
        pred_label = predict(images, net, transformer)
        pred_name = label_name[int(pred_label)]
        print("label: " + name + ", " + "prediction: " + pred_name)
        count += 1
        if name == pred_name:
            right += 1

    print("Accuracy: " + str(right / float(count)))
