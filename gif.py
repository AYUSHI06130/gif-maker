import imageio.v3 as iio 

filenames = ['image-1.jpg','image-2.jpg']
images = []
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('my.gif', images, duration=500, loop=0)