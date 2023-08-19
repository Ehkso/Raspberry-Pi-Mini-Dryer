# Raspberry-Pi-Mini-Dryer
A quick little python program I wrote for my Raspberry Pi Zero W (wiring not included).
I was bored, so I decided to code something real quick before the Pi heats up and gets even slower (this happens quite a lot).
It's a motion-activated fan, but I told the kids it's for cooling down my food when I'm eating so I don't need to blow on it.

Being motion-activated and a fan, it requires a PIR sensor and a fan (but you can use some other sort of output such as an LED), plus wires and whatever.
I do not have any resistors, but for something this small I don't think it's that big a deal. As a matter of fact, I don't really have anything for making circuits -
no breadboard, neither male nor female jumper cables, no solder, nothing. I'd attach a picture of how I set it up, but I don't like putting pictures into READMEs.

The code is pretty straightforward, and I have comments included but I'm gonna pull out one of the bigger comment blocks because it's rambling so
it'd be better placed here to keep the code ramble-free.

## max_timer variable:
The reason why this doesn't actually start counting down until the first time the fan is used is because my pi (zero w) has a
tendency to run extremely slowly. This would've been way faster to code on my computer and then just ported over. This is just to let you
know that you can of course have the max_timer outside this function and begin counting from the moment this program starts, I'm just
trying to account for expected lag. Note to self: buy a good sd card rather than using what comes in the rpi starter kit.

## dryer() while loop:
The reason why I don't use any while loops within the max_timer loop is because creating nested while loops
would make the rate at which max_timer decrements vary (at a much higher rate than what we'll have to accept from
simple executions), meaning we'd basically have a countdown where at some times it's basically paused and
at other times it counts down faster than you can say "slow down please"

Anyway I think that's it, there's really nothing to the wiring but just in case this (somehow) happens to be the first thing someone came across when they wanted to learn
how to make a circuit:
When you just have red/black wires, the red wire connects to the pin you've set (generally your outputs, correlating to GPIO.OUT in RPi.GPIO) and the black wire connects to ground.
When you have red/black/yellow wires, that generally means that red connects to power, black connects to ground, and yellow connects to your pin (generally inputs, GPIO.IN).
Obviously if whatever you're using is telling you otherwise, it's of higher importance so follow that instead. My PIR sensor connects to 5v but if yours connects to 3v then don't
blow your tech and then call me up telling me I owe you a replacement, I'm already broke I don't need debts.

Hope you found this fun and refreshing and whatnot, and happy tech-ing.
