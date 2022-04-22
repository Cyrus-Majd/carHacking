# Intro
We hacked a car and decided to play mario kart with it.

This was a hack for HackRU Spring 2022. The authors of this hack are Cyrus Majd, Yousef Attia, and Nick Gottwerth.

# Tools
We used an OBDII to USB adapter and shoved it into my 2021 Toyota Tacoma to read data flowing through the CAN bus. Thanks to our unfortunate financial situation as college students, we bought the cheapest knockoff ELM327 device we could find on Amazon for this hack. It cost 15 bucks and there's got to be like a thousand clones all being sold by random vendors. We also used Python, C, MelonDS, help from https://github.com/norly/elmcan, and a very legally obtained copy of the Mario Kart DS ROM.

# The Hack
We plugged in the ELM327 into the OBDII port and immediately had to troubleshoot how exactly we were going to read data from the car. We had to interpret the data through a serial connection. The data also was not just automatically flowing from the car and into our computer, instead we had to lookup commands supported by the ELM327 device that we could use to then pull in data from the car one chunk at a time. 

The CAN bus, which is the communications line we were trying to tap into, is always busy with traffic, with status messages being sent out by hundreds of internal devices within the car. Our ELM327 device only had a buffer space of 32 bytes, so we coulnt read in a whole lot of information at any given time manually. We needed some kind of driver that would read in the contents of the buffer of the ELM device, dump it, and then read in new data immediately afterwards. Because the OBDII port on our vehicle operates at a 384kHZ baud rate, our drivers needed to operate very quickly. We fiddled with this for a while until we found a tool that helped us finish the job. The tool can be found here: https://github.com/norly/elmcan. 

Now that we could read in data, we needed to identify which device IDs corresponded to different components in the car. We found schematics online that indicated the device ID of the steering column for our testing vehicle, a 2005 Mercedes e320. 
