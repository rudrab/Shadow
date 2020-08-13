#!/usr/bin/env python3
import os
import shutil
import sys


def denv():
  de = "gnome"
  print("Choose your desktop environments")
  print("1: Cinnamon")
  print("2: Gnome-3")
  print("3: Mate")
  print("4: Pantheon")
  print("5: Unity")
  print("6: KDE ")
  name = int(input("Enter 1/2/3 etc to choose your de:"))
  if name == 1:
    de = "cinnamon"
  elif name == 2:
    de = "gnome"
  elif name == 3:
    de = "mate"
  elif name == 4:
    de = "pantheon"
  elif name == 5:
    de = "unity"
  elif name == 6:
    de = "kde"
  else:
    print('\x1b[1;48;2;205;0;0m' + "Not Supported" + '\x1b[0m')
    print("Check Carefully")
    sys.exit()
  print("You have chosen " + de.upper() + " Desktop Environment")
  den = "index.theme_" + de
  os.unlink("index.theme")
  os.symlink(den, "index.theme")
  return de


def color():
  print("Now choose your favourite color scheme")
  print("1:" + '\x1b[1;48;2;80;200;120m' + "  Emerald  " + '\x1b[0m')
  print("2:" + '\x1b[1;48;2;230;91;0m' + "  Garnet   " + '\x1b[0m')
  print("3:" + '\x1b[1;48;2;231;34;52m' + "   Ruby    " + '\x1b[0m')
  print("4:" + '\x1b[1;48;2;79;142;241m' + " Sapphire  " + '\x1b[0m')
  print("5:" + '\x1b[1;48;2;44;202;255m' + " Torquiose " + '\x1b[0m')
  print("9:" + 'Square')
  name = int(input("Enter 1/2/3 etc to choose your color scheme:"))
  scheme = ""
  if name == 1:
    scheme = "emerald"
  elif name == 2:
    scheme = "garnet"
  elif name == 3:
    scheme = "ruby"
  elif name == 4:
    scheme = "sapphire"
  elif name == 5:
    scheme = "turquoise"
  elif name == 9:
    scheme = "square"
  else:
    print("No Such Scheme Exists Yet")
    quit()
  return scheme


def main():
  print('\x1b[1;48;2;185;0;0m' + "CAREFULNESS ASSUMED!\n" +
        'i.e. You may face some weird icon if you choose \n' +
        'MATE when you don\'t have MATE icon or MINT installed!' + '\x1b[0m')

  den = denv()
  scheme = color()
  print(scheme.upper() + " scheme will be applied")
  schemename = "places_" + scheme
  nautilaus = "./" + schemename + "/system-file-manager.svg"
  foldernew = "./" + schemename + "/folder-new.svg"
  print(schemename)
  print(nautilaus)
  os.chdir("./scalable")
  os.unlink("places")
  os.symlink(schemename, "places")
  shutil.copy(nautilaus, "./apps")
  shutil.copy(foldernew, "./actions")
  os.chdir(schemename)
  os.unlink("folder.svg")
  os.unlink("folder-symbolic.svg")
  fname = "folder_" + den + ".svg"
  fname2 = "folder-symbolic_" + den + ".svg"
  print(den)
  print(os.getcwd())
  os.symlink(fname, "folder.svg")
  os.symlink(fname2, "folder-symbolic.svg")


main()
