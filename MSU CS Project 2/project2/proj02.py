"""
MSU CSE 231 Project 2

--This assignment focuses on the design, implementation and testing of a Python program to solve
an arithmetic puzzle using repetition and selection.--

Developed on: 12/30/16
Developed by: Jarred Parr

Version: 1.0
"""

class proj02:

    def addUntilComplete(self):

        a = int(input("Input an integer: "))
        while (a < 0):
            a = int(input("ERROR, ENTER A POSITIVE NUMBER: "))

        numberArr = [int(i) for i in str(a)]
        total = sum([int(i) for i in str(a)])
        output = list(n for n in numberArr + ' +')
        return output + " = " + total

if __name__ == '__main__':

    p = proj02()

    p.addUntilComplete()
