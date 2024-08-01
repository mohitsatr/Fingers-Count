
import os ,glob
DIR_FINGERS = os.path.join(os.getcwd(), 'Fingers_data','fingers')



def rename_data(partition_path):
  path = os.path.join(DIR_FINGERS, partition_path)
  i = 0
  for file in sorted(glob.glob(os.path.join(path, '*'))):
    name = file.split(".png")[0][-2:]
    os.rename(file,os.path.join(path,f"{name[0]}_{name[1]}_{i}.png"))
    i += 1

rename_data("train") 
rename_data("test")



