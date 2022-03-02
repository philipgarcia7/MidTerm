"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

import re
import CourseClass as cc


def main():
    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]
    c1 = cc.Course(name, crn, seats, status)
    for s in students:
        r1 = cc.Register(s,crn)
    for s in students:
        r1 = cc.Register(s,crn)
        if c1.get_status() == "open":
            c1.update_seat_count()
            print("Student Name:", r1.get_name())
            print("Course Name:", c1.get_name())
            print("CRN:", c1.get_crn())
            print("Seat Count:", c1.get_seats())
            print()

        else:
            print("Sorry ", r1.get_name(), ", registration is closed for ", c1.get_name(), sep="")


main()
