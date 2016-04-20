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

def addnewDomain():
    userID = raw_input("user ID : ")
    DomainName = raw_input("Enter Domain name : ")
    DomainStart = raw_input("Enter Domain Start date : ")
    DomainEnd = raw_input("Enter Domain End date : ")
    DomainFinState = raw_input("Domain Paid/Not-Paid : ")
    DomainFinAmount = raw_input("Domain Price = ")

    st = HostManagerdb.newDomain(userID,DomainName,DomainStart,DomainEnd,DomainFinState,DomainFinAmount)
    if st == 1:
        print "New Domain Added Successfully"
    else:
        print "Failed To create Domain"

def PrintAllUsers():
    ar = HostManagerdb.getAllUsers()
    for row in ar:
        print "++===============++"
        print "User Id : %s"%(row[0])
        print "User Name : %s"%(row[1])
        print "User Phone : %s"%(row[2])
        print "User Email  : %s"%(row[3])
        print "++===============++"

def PrintDomainsAndUserId():
    ar = HostManagerdb.getAllDomains()
    for row in ar:
        print "++===============++"
        print "User Id : %s"%(row[0])
        print "User Domain : %s"%(row[1])
        print "++===============++"

def PrintDomainDetails(arg):
    ar = HostManagerdb.getDomainData(arg)
    for row in ar:
        print "++===============++"
        print "User Id : %s"%(row[0])
        print "User Domain : %s"%(row[1])
        print "Domain Start Date : %s"%(row[2])
        print "Domain End Date : %s"%(row[3])
        print "Domain paid state : %s"%(row[4])
        print "Domain price : %s"%(row[5])
        print "++===============++"
