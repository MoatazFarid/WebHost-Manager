#functions module
# -*- coding: utf-8 -*-

import HostManagerdb

def login_Auth(user,password):
    if user == "admin" and password == "admin":
        return true
    else:
        return false

def addnewUser():
    OwnerName = raw_input("Owner Name : ")
    OwnerEmail = raw_input("Owner Email : ")
    OwnerPhone = raw_input("Owner Phone : ")

    st =HostManagerdb.newUser(OwnerName,OwnerPhone,OwnerEmail)
    if st == 1:
        print "New User Added Successfully"
    else:
        print "Failed To create User"

def addnewHost():
    userID = raw_input("user ID : ")
    websiteName = raw_input("Enter Website Name : ")
    websiteStorgae = raw_input("Enter Website storage : ")
    websiteBandwidth = raw_input("Enter Website bandwidth : ")
    websiteHostStart = raw_input("Enter Website Host Start date : ")
    websiteHostEnd = raw_input("Enter Website Host End date : ")
    websiteHoststate = raw_input("Enter Website Host state : ")
    websiteHostFinAmount = raw_input("Host Price = ")
    websiteHostFinState = raw_input("Host Paid/Not-Paid : ")

    st = HostManagerdb.newHost(userID,websiteName,websiteStorgae,websiteBandwidth,websiteHostStart,websiteHostEnd,websiteHostFinState,websiteHoststate,websiteHostFinAmount)
    if st == 1:
        print "New Host Added Successfully"
    else:
        print "Failed To create Host"
