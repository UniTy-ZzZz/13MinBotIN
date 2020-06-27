import time
import os
import math
import sys

time.sleep(3)
print("")
print("")
print("[*] Initialiti g Services...")
time.sleep(0.40)
print("Insert Full Number :")
num = input("124(NumFinder) >")
def america():
    AM = "America"
    print("[+] Number From " + AM)
def japan():
    AM = "Japan"
    print("[+] Number From " + AM)
def italy():
    AM = "Italy"
    print("[+] Number From " + AM)
def india():
    AM = "India"
    print("[+] Number From " + AM)
def algeria():
    AM = "Algeria"
    print("[+] Number From " + AM)
def argentina():
    AM = "Argentina"
    print("[+] Number From " + AM)
def australia():
    AM = "Australia"
    print("[+] Number From " + AM)
def austria():
    AM = "Austria"
    print("[+] Number From " + AM)
def belgium():
    AM = "Belgium"
    print("[+] Number From " + AM)
def brazil():
    AM = "Brazil"
    print("[+] Number From " + AM)
def france():
    AM = "France"
    print("[+] Number From " + AM)
def greece():
    AM = "Greece"
    print("[+] Number From " + AM)
def germany():
    AM = "Germany"
    print("[+] Number From " + AM)
def united_kingdom():
    AM = "United Kingdom"
    print("[+] Number From " + AM)
def vietnam():
    AM = "Vietnam"
    print("[+] Number From " + AM)
if "+1" in num:
    america()
elif "+81" in num:
    japan()
elif "+39" in num:
    italy()
elif "+91" in num:
    india()
elif "+213" in num:
    algeria()
elif "+54" in num:
    argentina()
elif "+61" in num:
    australia()
elif "+43" in num:
    austria()
elif "+32" in num:
    belgium()
elif "+55" in num:
    brazil()
elif "+33" in num:
    france()
elif "+30" in num:
    greece()
elif "+49" in num:
    germany()
elif "+44" in num:
    united_kingdom()
elif "+84" in num:
    vietnam()
else:
    print("[-] Number Not Exist or not definied in Nation {" + num + "}")
