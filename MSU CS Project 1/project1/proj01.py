"""
Python practice project using one of the Project Guidelines assigned
to the Michigan State University project list.

Developed by: Jarred Parr

Version: 1.0
"""

class proj01:

    """Calculate the wind chill for Farenheight and MP/H"""
    def chillCalculatorF(self, temp, speed):

        if (temp > 50):
            print "Wind chill is not a factor for temperatures over 50 degrees(F)"

        if (speed < 0 or speed > 200):
            print "Speed either too high, or too low."

        print (0.6215(temp) - (35.75(speed)**0.16) + (0.4275(temp)(speed)**0.16) + 35.74)

    """Calculate wind chill for Celsius and KM/H"""
    def chillCalculatorC(self, temp, speed):

        if (temp > 10):
            print "Wind chill is not a factor for temperatures over 10 degrees(C)"

        if (speed < 0 or speed > 200):
            print "Speed either too high, or too low."

        print (0.6215(temp) - (11.37(speed) ** 0.16) + (0.3965(temp)(speed) ** 0.16) + 13.12)

if __name__ == '__main__':

    choice = 0
    chillCalc = proj01()

    choice = int(input("Please make a selection: "))

    print "\nWelcome to the Wind Chill Calculator!"
    print "\n1. Calculate wind chill for Farenheight and MPH"
    print "\n2. Calculate wind chill for Celsius and KMH"
