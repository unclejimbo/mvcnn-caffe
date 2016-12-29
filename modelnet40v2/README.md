1. Please download the rendered images provided by mvcnn authors at the [GitHub repo](https://github.com/suhangpro/mvcnn).
2. Unzip it and rename the directory as 'rawdata'.
3. Use bake_data.py to pad the image and prepare training data.
4. Use create_label_name.py to create a text file assigning label and name.
5. Use create_data_text.py to create the text files containing image names for training, validation and testing.
6. Use create_leveldb.sh to convert images into leveldb files.
7. Use compute_image_mean in caffe tools to compute the mean of training images.
8. Go ahead and train a network.
