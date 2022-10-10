# Intro
We hacked a car and decided to play mario kart with it.

This was a hack for HackRU Spring 2022. The authors of this hack are Cyrus Majd, Yousef Attia, and Nick Gottwerth.

# Tools
We used an OBDII to USB adapter and shoved it into my 2021 Toyota Tacoma to read data flowing through the CAN bus. Thanks to our unfortunate financial situation as college students, we bought the cheapest knockoff ELM327 device we could find on Amazon for this hack. It cost 15 bucks and there's got to be like a thousand clones all being sold by random vendors. We also used Python, C, MelonDS, help from https://github.com/norly/elmcan, and a very legally obtained copy of the Mario Kart DS ROM.

# The Hack
We plugged in the ELM327 into the OBDII port and immediately had to troubleshoot how exactly we were going to read data from the car. We had to interpret the data through a serial connection. The data also was not just automatically flowing from the car and into our computer, instead we had to lookup commands supported by the ELM327 device that we could use to then pull in data from the car one chunk at a time. 

![Registering the ELM327 as an input device](https://github.com/Cyrus-Majd/carHacking/tree/master/assets/images/1.jpg)

![Reading in our first packet of raw data through the serial connection](https://github.com/Cyrus-Majd/carHacking/tree/master/assets/images/2.jpg)

![Our first group photo, a few hours into HackRU](https://github.com/Cyrus-Majd/carHacking/tree/master/assets/images/3.jpg)

The CAN bus, which is the communications line we were trying to tap into, is always busy with traffic, with status messages being sent out by hundreds of internal devices within the car. Our ELM327 device only had a buffer space of 32 bytes, so we coulnt read in a whole lot of information at any given time manually. We needed some kind of driver that would read in the contents of the buffer of the ELM device, dump it, and then read in new data immediately afterwards. Because the OBDII port on our vehicle operates at a 384kHZ baud rate, our drivers needed to operate very quickly. We fiddled with this for a while until we found a tool that helped us finish the job. The tool can be found here: https://github.com/norly/elmcan. 

![Reading in the largest chunk of data we could, hitting the buffer limit](https://github.com/Cyrus-Majd/carHacking/tree/master/assets/images/4.jpg)

![We have no idea whats happening lol](https://github.com/Cyrus-Majd/carHacking/tree/master/assets/images/5.jpg)

[Getting canutils to work for the first time with the elmcan drivers](https://youtu.be/LXCfOl-7LPU)

[Interpreting candump data for the first time](https://youtube.com/shorts/Jfq8_UJvQLQ)

Now that we could read in data, we needed to identify which device IDs corresponded to different components in the car. We found schematics online that indicated the device ID of the steering column for our testing vehicle, a 2005 Mercedes e320. 

Then it was just a matter of isolating the data packets being sent over the canbus with that specific device ID and interpreting the data. When we isolated the stream of data, we moved the steering wheel around while examining the bytes change with each new data packet. We took notes on which bytes corresponded to the angle of the steering wheel, which side the steering wheel was on (whether it was steering right or left), and if there have been full revolutions.

As a fun exploratory thing, we actually tried reading in data from the seatbelts and wondered if we could do anything with that, but we ultimately decided against the idea. Nonetheless, [here's some testing we did with that.](https://youtube.com/shorts/mxOtgQowX4I)

Anyways putting all of this data together, we devised a "driver" (no pun intended, haha) which then would interpret this data into mario kart commands. We basically had set up an emulator that was running mario kart in a new window and wrote a python program to convert steering wheel commands into right and left commands in mario kart. For mario's gas, we just had the code constantly hold down the accelerator. Who hits the brakes in mario kart anyways?

[Here's the video we submitted at HackRU.](https://www.youtube.com/watch?v=eoyW9eIAbho) We actually submitted it just on the deadline!

Now our project was good, but not flawless. There were a ton of bugs and stuff we needed to patch up. We also were invited to give a presentation of our project to the other students and computer science clubs. So we brought up the project in the next Rutgers Security Club meeting. Our club is full of amazing talent, and our members quickly volunteered to work on the project. We work really well as a team. Here's some pics of [Yousef and Rajat](https://github.com/Cyrus-Majd/carHacking/tree/master/assets/images/6.jpg), some of [Manav and Arnav](https://github.com/Cyrus-Majd/carHacking/tree/master/assets/images/7.jpg), and one of [me and Adam](https://github.com/Cyrus-Majd/carHacking/tree/master/assets/images/8.jpg). Here's [one of the whole gang!](https://github.com/Cyrus-Majd/carHacking/tree/master/assets/images/9.jpg) After a ton of tinkering and a few hours of work, we hit success! Here's a video of my roomate Wesley [trying it out](https://youtu.be/wawf_0Af980). Huge props to this guy for everything he's done to help us in the project!

Here's [our presentation to the Rutgers students](https://youtu.be/Vj0rI6NxBhY), and [here's those same students trying it out for themselves!](https://youtu.be/aJ4rJ2TC5D0)

Anyways, our hack turned out to be a huge success. We won a nice prize in HackRU and plan to take this hack further come fall 2022. We plan to apply what we learned on another vehicle, with hopes that we can actually end up controlling the vehicle remotely with some kind of game controller. Think IRL GTA, but in our computer science building's parking lot. Stay tuned! :)

# The Hack Continued
The new objective is to drive the car, with a controller. At this point the team has developed a pretty good understanding of the CAN bus and how it can be used to take control of vehicles. We are currently researching what we can do and trying new stuff all the time. Here's a list of resources/research papers that are guiding us throughout this process;

- https://ioactive.com/pdfs/IOActive_Adventures_in_Automotive_Networks_and_Control_Units.pdf
- https://illmatics.com/remote%20attack%20surfaces.pdf
- https://github.com/jaredthecoder/awesome-vehicle-security/blob/master/README.md
- https://www.giac.org/paper/gcia/9927/hacking-bus-basic-manipulation-modern-automobile-bus-reverse-engineering/133228

We have made some good progress since our mario kart demonstration. We tried our hacking skills on an old 2008 Honda CRV. Our objective was to actually send commands to the vehicle. If successful, this would be the first time we are actually controlling parts of the car. After a few attempts, we managed to achieve this result:
https://www.youtube.com/watch?v=M2VccjgLOjM. We could actually control the tachometer on the vehicle!

We will take this further, but with a 2021 Toyota Tacoma. The Honda CRV is 100% not street legal given that it is way past due for inspection and registration renewal. lol

We will update this page as we discover new stuff!
