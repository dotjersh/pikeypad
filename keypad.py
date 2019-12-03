
import RPi.GPIO as GPIO
import time

class keypad():
    # CONSTANTS
    KEYPAD = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ["*",0,"#"]
    ]

    ROW         = [26,19,13,6]
    COLUMN      = [22,27,17]

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def getKey(self):
        # Set all columns as output low
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)

        # Set all rows as input
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i

        # if rowVal is not 0 then no button was pressed and we can exit
        if rowVal <0 :
            self.exit()
            return

        # Convert columns to input
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Switch the i-th row found from scan to output
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)

        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 2.
        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal=j

        # if colVal is not 0 thru 2 then no button was pressed and we can exit
        if colVal <0:
            self.exit()
            return

        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[rowVal][colVal]

    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

if __name__ == '__main__':
    # Initialize the keypad class
    kp = keypad()
    keypadDigits= " "
    # Loop while waiting for a keypress
    digit = None
    tempdigit = None
try:
    while digit == None and digit!= "*" and digit != "#":
            while len(keypadDigits)<= 3:
                 digit = kp.getKey()
                 if digit is not None and digit != "#" and digit != "*":
                        temp = str(digit)
                        keypadDigits = keypadDigits + temp
                        time.sleep(0.5)
                 if keypadDigits != " " and (digit == "#" or digit == "*"):
                       digit = int(keypadDigits)
                       break
    print(keypadDigits)
    # Print the result
    if digit == "#" or digit == "*":
            print (digit)
    else:
            exit(0)
except KeyboardInterrupt:
                pass

GPIO.cleanup()
