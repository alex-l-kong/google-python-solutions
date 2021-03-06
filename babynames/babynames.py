#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++

  ret_list = [] # the list to return

  with open(filename, 'r') as fin:
    date_match = re.findall(r'Popularity in (\d\d\d\d)', fin.read()) # extract group from line describing year survey taken
    fin.seek(0) # reset to the beginning of the file
    name_match = re.findall(r'<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', fin.read()) # extract groups describing name and respective ranking

    # this method adds both the boy and girl information in one pass
    # elem[0] is the ranking, elem[1] is the boy's name, elem[2] is the girl's name
    my_dict = {}
    for elem in name_match:
      my_dict[elem[1]] = elem[0]
      my_dict[elem[2]] = elem[0]

    ret_list.append(date_match[0]) # the date is the first element

    # sorted will sort the dict in alphabetical order
    # that way when we append to the list we will do so in alphabetical order
    for key in sorted(my_dict):
      ret_list.append('{} {}'.format(key, my_dict[key]))

  return ret_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('Usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  while len(args) > 0:
    print(args)
    info = extract_names(args[0])

    # part 1, printing the list information as a string
    var = '\n'.join(info)
    print(var)

    # part 2, writing to a file with .summary prefix
    with open(args[0] + '.summary', 'w') as fout:
      fout.write(var)

    del args[0]
  
if __name__ == '__main__':
  main()
