import subprocess

proc = subprocess.Popen(['candump','can0,238:FF'],stdout=subprocess.PIPE)
#works in python 3.0+
#for line in proc.stdout:

prev = (-1, -1)

# VALUE OF N: 160 is the middle. anything less is LEFT. anything greater is RIGHT.    for line in iter(proc.stdout.readline,''):
for line in iter(proc.stdout.readline,''):
	s = line.rstrip().decode("UTF-8")
	n = int(s[28:30],16)
	sign = int(s[25:27],16)
	turn = 'l' if sign & 0x8 else 'r'
	mag = ((sign & 0x7) << 8) | n
	if (sign, n) != prev:
		print(f"sign:{sign}, val:{n}, turn:{turn}, mag:{mag}")
		prev = sign, n
