#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
from urllib import request
import subprocess as sb

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

# helper function to sorted in read_urls return statement
def jpg_sort(elem):
  # get the second word in jpg files ending with -wordchars-wordchars.jpg
  # group the second such wordchar group
  jpg_group = re.search(r'\S*-\w+-([\w]+)\.jpg', elem)

  # return the wordchar group if the file extension described above is present
  # else just return the original element back
  return jpg_group.group(1) if jpg_group is not None else elem


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""

  # +++your code here+++
  # note that the following code assumes that the server name is properly formatted
  # the regex could allow "......." or even _+3dvs*,,,com to pass
  server = re.search(r'\w+_(\S+)', filename).group(1)
  img_urls = []

  # I wanted to demonstrate how set operations can be used to remove duplicate elements
  with open(filename) as fin:
    img_urls = set([ 'http://' + server + x for x in re.findall(r'GET\s(\S*)\s', fin.read()) ])

  # return the sorted list of only unique URLs
  # return sorted(list(img_urls)) # this naive sort only works with animal_code.google.com
  return sorted(list(img_urls), key=jpg_sort) # this sort is needed for place_code.google.com
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++

  # for simplicity, if the directory name's path already exists then just remove it
  if os.path.exists(dest_dir):
    sb.call(["rm", "-rf", dest_dir])

  # now make the directory
  os.mkdir(dest_dir)

  # get each url and attempt to read each from the specified URL
  # some of the URLs don't exist
  # hence the picture will not be complete 
  # I've printed out status and error messages so the user can know
  for index in range(0, len(img_urls)):
    print(os.path.join(dest_dir, 'img' + str(index)))
    try:
      request.urlretrieve(img_urls[index], os.path.join(dest_dir, 'img' + str(index)))
    except IOError:
      print("Problem reading URL %s to image img%d" % (img_urls[index], index))

  # write beginning tags to the file
  with open(os.path.join(dest_dir, 'index.html'), 'w') as fout:
    fout.write(
'''
<verbatim>
<html>
<body>
'''
    )

    # each image gets its specified tag
    # normally I would not have put the if statement in
    # however some of the URLs don't exist
    for index in range(0, len(img_urls)):
      if os.path.exists(os.path.join(dest_dir, 'img' + str(index))):
        fout.write('<img src="%s"></img>' % ('img' + str(index)))

    # write closing tags to file
    fout.write(
'''
</body>
</html>
'''
    )



def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
