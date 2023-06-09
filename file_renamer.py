import os
_src = "/path/to/directory/"
_ext = ".png"
for i,filename in enumerate(os.listdir(_src)):
    if filename.endswith(_ext):
        os.rename(filename, _src+str(i).zfill(3)+_ext)