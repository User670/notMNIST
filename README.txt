Each file contains the raw pixel values of all pictures from one folder.

The file format is simple: there are 28x28x[number of images] bytes, each byte is a pixel (unsigned 8-bit integer, 0-255), the first 28x28 bytes belongs to the first image, the next 28x28 pixels belong to the next image, and so on.

The number of images in each file/folder can be found in the JSON file. The reason there is a difference is because 1. there are a few bad files that can't be read, and 2. the J folder came with one less file than every other folder.