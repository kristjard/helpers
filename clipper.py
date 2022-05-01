# import math
# import os
# import matplotlib.pyplot as plt
#
# # Config:
# images_dir = '/home/kristjan/Documents/schola/lõputööasjad/dev_kristjan/results/est_infer/retrained_g300-600_raw/vis'
# result_grid_filename = './grid.jpg'
# result_figsize_resolution = 40 # 1 = 100px
#
# images_list = sorted(os.listdir(images_dir))
# images_count = len(images_list)
# print('Images: ', images_list)
# print('Images count: ', images_count)
#
# # Calculate the grid size:
# grid_size = math.ceil(math.sqrt(images_count))
#
# # Create plt plot:
# fig, axes = plt.subplots(grid_size, grid_size, figsize=(result_figsize_resolution, result_figsize_resolution))
#
# current_file_number = 0
# for image_filename in images_list:
#     x_position = current_file_number % grid_size
#     y_position = current_file_number // grid_size
#
#     plt_image = plt.imread(images_dir + '/' + images_list[current_file_number])
#     axes[x_position, y_position].imshow(plt_image)
#     print((current_file_number + 1), '/', images_count, ': ', image_filename)
#
#     current_file_number += 1
#
# plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
# plt.savefig(result_grid_filename)

import sys
from PIL import Image

# images = [Image.open(x) for x in ['infered_1_vis.png', 'infered_2_vis.png', 'infered_3_vis.png', 'infered_4_vis.png',
#                                   'infered_5_vis.png', 'infered_6_vis.png', 'infered_7_vis.png', 'infered_8_vis.png',
#                                   'infered_9_vis.png', 'infered_10_vis.png', 'infered_11_vis.png', 'infered_12_vis.png',
#                                   'infered_13_vis.png', 'infered_14_vis.png', 'infered_15_vis.png', 'infered_16_vis.png',]]
images = [Image.open(x) for x in ['infered_10_vis.png', 'infered_11_vis.png', 'infered_14_vis.png', 'infered_15_vis.png',]]
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (4096, 4096))

x_offset = 0
y_offset = 2048
count = 1
for im in images:
  print(count)
  #im = im.resize((1024, 1024))


  new_im.paste(im, (x_offset, y_offset))
  x_offset += im.size[0]
  if count % 2 == 0:
    y_offset -= im.size[0]
    x_offset = 0

  print(x_offset, y_offset)
  count += 1

print(new_im.size)
new_im.save('vljnd_orto2.jpg')

