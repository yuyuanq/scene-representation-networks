from PIL import Image
import glob
import os

dir_path = r'E:\PycharmProjects\scene-representation-networks\logs\my_cars_2_test\gt_comparisons\000000'

if not os.path.exists('output'):
    os.mkdir('output')

# Create the frames
frames = []
imgs = glob.glob(os.path.join(dir_path, "*.png"))
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# Save into a GIF file that loops forever
frames[0].save('./output/000000.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               loop=0)
