import subprocess
proc = subprocess.Popen(['candump','can0,238:FF'],stdout=subprocess.PIPE)
#works in python 3.0+
#for line in proc.stdout:

# VALUE OF N: 160 is the middle. anything less is LEFT. anything greater is RIGHT.
for line in iter(proc.stdout.readline,''):
    s = line.rstrip().decode("UTF-8")
    n = int(s[28:30],16)
    print(n)


