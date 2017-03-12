#!/usr/bin/env python
import os
import shutil

print("1:"+'\x1b[1;48;2;80;200;120m'+"  Emerald  "+ '\x1b[0m')
print("2:"+'\x1b[1;48;2;231;34;52m'+ "   Ruby    "+ '\x1b[0m')
print("3:"+'\x1b[1;48;2;79;142;241m'+" Sapphire  "+ '\x1b[0m')
print("4:"+'\x1b[1;48;2;44;202;255m'+" Torquiose "+ '\x1b[0m')
print("9:"+'Square')
name=int(input("Choose one of the color scheme:"))
scheme = ""
if name == 1:
  scheme = "emerald"
elif name == 2:
  scheme = "ruby"
elif name == 3:
  scheme = "sapphire"
elif name == 4:
  scheme = "torquise"
elif name == 9:
  scheme = "square"
else:
  print("No Such Scheme Exists Yet")
  quit()
print(scheme.upper() +" scheme will be applied")
schemename="places_"+scheme
nautilaus = "./"+schemename+"/system-file-manager.svg"
foldernew = "./"+schemename+"/folder-new.svg"
print(schemename)
print(nautilaus)
os.chdir("./scalable")
os.unlink("places")
os.symlink(schemename,"places")
shutil.copy(nautilaus,"./apps")
shutil.copy(foldernew,"./actions")
