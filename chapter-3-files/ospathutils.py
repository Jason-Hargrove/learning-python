#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    
    # Check for item existence and type
    print("Item exists:", str(path.exists("textfile.txt")))
    print("Itme is a file:", path.isfile("textfile.txt"))
    print("Item is a dir:" , path.isdir("textfile.txt"))

    
    # Work with file paths
    print("Item's path:", path.realpath("textfile.txt"))
    print("Item's path and name:", path.split(path.realpath("textfile.txt")))

    
    # Get the modification time

    
    # Calculate how long ago the item was modified

  
if __name__ == "__main__":
    main()
