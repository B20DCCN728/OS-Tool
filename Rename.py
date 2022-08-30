import os, codecs
import pathlib as Campus

path_folder = r"C:\Users\PC\OneDrive\Documents\Selenium\Campus_Profile\data"
list_dir = os.listdir(path=path_folder) 

for i in range(0, 1049):
    oldpath = Campus.Path(f"C:\\Users\\PC\\OneDrive\\Documents\\Selenium\\Campus_Profile\\data\\{list_dir[i]}")
    newpath = Campus.Path(f"C:\\Users\\PC\\OneDrive\\Documents\\Selenium\\Campus_Profile\\data\\Profile {str(i + 1)}")
    oldpath.rename(newpath)
