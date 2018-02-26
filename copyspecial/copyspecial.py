#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess as sb # change from commands to subprocess for Python 3.x

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def zip_to(paths, zippath):
  # print the command going to be run
  print("Command I\'m going to do:zip -j %s %s" % (zippath, " ".join(paths)))
  
  # attempt to run the call via the subprocess module
  # if it fails catch CalledProcessError and fail
  try:
    sb.check_call(["zip", "-j", zippath] + paths)
  except sb.CalledProcessError:
    print("Error: could not create zip file!")




def copy_to(paths, dir_name):
  # for simplicity, if the directory name's path already exists then just remove it
  if os.path.exists(dir_name):
    sb.call(["rm", "-rf", dir_name])

  # make the directory, this assumes that the directory doesn't exist!!!
  os.mkdir(dir_name)

  # copy each filepath to the directory
  for f_path in paths:
    shutil.copy(f_path, dir_name)



def get_special_paths(dir_name, todir, tozip):
  # note that the following will only get files in the current directory
  # this approach will need to be modified if we want to descend into other directories
  # that will need the isdir function in os.path
  special_paths = [os.path.abspath(x) for x in os.listdir(dir_name) if re.search(r'__\w+__\.\w+', x) is not None]
  
  # check if todir and tozip are set
  # if so then call respective function
  # otherwise just print list
  if len(todir) > 0:
    copy_to(special_paths, todir)
  elif len(tozip) > 0:
    zip_to(special_paths, tozip)
  else:
    print('\n'.join(special_paths))


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.

  # I changed the if statement checking for --tozip, the original version could cause some problems
  # For example, someone could accidently specify a command:
  # python3 copyspecial.py --todir ./test
  # Then args is None but the if statement checking --tozip still runs

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if len(args) > 0 and args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  get_special_paths(args[0], todir, tozip)
  
if __name__ == "__main__":
  main()
