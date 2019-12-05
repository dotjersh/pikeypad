# Sample Raspberry Pi Keypad

Contributers:
- Tinotenda Nyakurerwa
- Josh Grift

This document contains information on how the we were able to use a 3x4 matrix keypad(shown below) for the first time. 

![key_pad_back](https://github.com/dotjersh/pikeypad/raw/master/key_pad_back.png)
![key_pad_front](https://github.com/dotjersh/pikeypad/raw/master/key_pad_front.png)

## Packages Needed
- RPi.GPIO
- Time 

## Circuit overview
The circuit used was composed of a Raspberry Pi and 3x4 keypad matrix. The keypad was connected directly to the Pi and no other materials were used. The packages used were the RPi.GPIO package to allow control of the GPIO on the Raspberry Pi. The time package was also used, this package was needed to allow the program time to process the value of the key pressed. The software figures out which key has been pressed by first scanning through all the keypad rows for an input then once the row value is found the row value is stored, the software then proceeds to loop through all the columns to find the column value of the pressed key. A combination of the column and row value were then used to provide the value of the key pressed.

## Problem & Challenges
Our goal was to read in multiple values from the keypad. However, because we had not used the pull-up and pull-down resistors, the value of the keys just kept on randomly changing when only one key had been pressed. We found a tutorial [online](https://crumpspot.blogspot.com/2013/05/using-3x4-matrix-keypad-with-raspberry.html?m=1) and managed to get the keypad from taking in just one key value at a time, to being able to take an infinite number of key values and stopping only if the user presses the "*" or "#" key. This then presented us with a new problem of having the keypad only taking in one key value and printing that infinitely despite other keys being pressed, this issue was fixed by importing the time package and using the sleep() function after the program gets the key press, this then provided the program with ample time to process each key value. We also modified the original code by implementing a try except block, this is to allow the user to escape using the normal command line escape of Ctrl-C in the event that they are unable to stop the program or something unexpected happens and the program does not run as intended.

## Instructional Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/Cx3d5uxPOOs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Helpful Links
- https://crumpspot.blogspot.com/2013/05/using-3x4-matrix-keypad-with-raspberry.html?m=1
- This link helped us with the initial understanding of how keypad worked: https://tutorials-raspberrypi.com/connecz-raspberry-pi-kecpad-code-lock/
- This link led us to the forum that led us to finding the code that was used: https://www.raspberrypi.org/forums/viewtopic.php?t=34235

