README
-The Hash file, hashes.txt, stores the filenames, hashes, and dates/times of every file in the system. It excludes files from dev, proc, run, sys, tmp, var/lib, and var/run directories.
-The file is in the form of a semicolon separated file, not as a comma separated file because for some reason some of the files had commas in their names which through off name processing.
-Every time I run the .py script, it opens the hashes.txt files, reads every line, and stores the filename and its corresponding hash into a dictionary.
-I then use os.walk to read through all system files and cross reference each file with the dictionary in order to see if there is a new file, missing file, or altered file. Each of these kinds of files are printed to the screen.
-After completion, the number of missing, new, and altered files is printed to the screen.
