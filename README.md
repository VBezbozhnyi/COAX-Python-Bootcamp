# Vitalii Bezbozhnyi - COAX-Python-Bootcamp task

Tasks: https://gist.github.com/DevIhor/fd23135bc324d6cee0bb7270ca84c01d

Pre-requisites:

- python 3.9.2
- ffmmpeg

### Task 1

Initial string is saved as string variable 's'. I used **hash()** function that is already available in python to hash
the input string.
Additionally I used hashlib to use MD5 and SHA1 algorithms.

### Task 2

Example video link is stored in string variable. **moviepy** library is used to download and convert video to GIF
format.
**random** lib is to add some fun and change output file name each time.
**os** lib is used to get absolute path to the output GIF file.
Reason to use **moviepy** - public library that can do the job.

P.S. Didn't have **ffmpeg**. Installed it to make script work.

### Task 3

Used variable to add/remove notes because have no experience to work with csv files on the fly.
Why Pandas - used it before to write convert files and wanted to learn a bit how to work with DataFrames.

P.S. After some time I just decided to check how far I can dive into this madness.
