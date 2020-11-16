import os
import subprocess
os.system('ls -l')

subprocess.run(["ls", "-l"]) # Run command
subprocess.run(["ls", "-l"], stdout=subprocess.PIPE) # This will run the command and return any output
subprocess.run(shlex.split("ls -l")) # You can also use the shlex library to split the command
