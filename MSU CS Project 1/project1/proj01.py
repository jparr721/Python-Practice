import sys

"""
Python practice project using one of the Project Guidelines assigned
to the Michigan State University project list.

Developed by: Jarred Parr

Version: 1.0
"""

class proj01:


    """Calculate the wind chill for Farenheight and MP/H"""
    def chillCalculatorF(self, temp, speed):
        #Check if the temp isn't too high
        if temp > 50:
            print "Wind chill is not a factor for temperatures over 50 degrees(F)"
        #Check if wind speed is valid
        if speed < 0 or speed > 200:
            print "Speed either too high, or too low."

        #Same error here
        result = 0.6215*temp - (35.75*speed**0.16) + (0.4275*temp*speed**0.16) + 35.74
        return result

    def chillCalculatorC(self, temp, speed):
        #Check if the temp is too high
        if (temp > 10):
            print "Wind chill is not a factor for temperatures over 10 degrees(C)"
        #Check if wind speed is valid
        if (speed < 0 or speed > 200):
            print "Speed either too high, or too low."

        #Result not callable, ERROR IS HERE
        result = 0.6215*temp - (11.37*speed ** 0.16) + (0.3965*temp*speed ** 0.16) + 13.12
        return result

    def welcomeScreen(self):

        choice = 0
        print "\n\n Welcome to the Wind Chill Calculator!"
        print "\n1. Calculate wind chill for Farenheight and MPH"
        print "\n\n2. Calculate wind chill for Celsius and KMH"

        choice = int(input("\nPlease make a selection: "))

        if choice == 1:
            tempF = int(input("\nPlease enter your temperature(in F): "))
            speedMPH = int(input("\nPlease enter your wind speed(in MPH): "))

            print "\n\nThinking..."
            print "The wind chill temperature index (in F and MPH) is: "
            print round(calc.chillCalculatorF(tempF, speedMPH), 2)

        if choice == 2:
            tempC = int(input("\nPlease enter your temperature(in C): "))
            speedKPH = int(input("\nPlease enter your wind speed(in KPH): "))

            print "\n\nThinking..."
            print "The wind chill temperature index (in C and KPH) is: "
            print round(calc.chillCalculatorC(tempC, speedKPH), 2)

    def programRestart(self):
        print "\nWould you like to make another calculation?"
        print "\n 1. Yes"
        print "\n 2. No, exit the program"

        choice = int(input("\n\n Please make a selection: "))

        if choice == 1:
            calc.welcomeScreen()
            return True
        if choice == 2:
            return False
            sys.exit()



if __name__ == '__main__':

    calc = proj01()
    running = True

    while(running):
        print "----------------------------------------------------------------------------"
        print "----------------------------------------------------------------------------"
        print "-----------LOADING--LOADING--LOADING--LOADING--LOADING--LOADING-------------"
        print "----------------------------------------------------------------------------"
        print "----------------------------------------------------------------------------"
        calc.welcomeScreen()
        calc.programRestart()
        print "\nRun Again? 1. Yes  2. No"
        choice = int(input("Enter your selection: "))

        if choice == 1:
            running = True
        elif choice == 2:
            running = False

    print "\n\n\nThanks for using my program! -Jarred"