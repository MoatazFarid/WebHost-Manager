#!/usr/bin/env python

import HostManagerdb

OwnerName=""
OwnerPhone = ""
OwnerEmail = ""

def getData():
    # getting data from user
    # websiteName = raw_input("Enter Website Name : ")
    OwnerName = raw_input("Owner Name : ")
    OwnerEmail = raw_input("Owner Email : ")
    OwnerPhone = raw_input("Owner Phone : ")
    # websiteHostStart = raw_input("Enter Website Host Start date : ")
    # websiteHostEnd = raw_input("Enter Website Host End date : ")
    # websiteHostFinAmount = raw_input("Host Price = ")
    # websiteHostFinState = raw_input("Host Paid/Not-Paid : ")
    # DomainStart = raw_input("Enter Domain Start date : ")
    # DomainEnd = raw_input("Enter Domain End date : ")
    # DomainEnd = raw_input("Enter Domain End date : ")
    # DomainFinAmount = raw_input("Domain Price = ")
    # DomainFinState = raw_input("Domain Paid/Not-Paid : ")

#saving data to db
#conn = sqlite3.connect('m_database.db')

#HostManagerdb.init()
getData()

HostManagerdb.createUser(OwnerName,OwnerPhone,OwnerEmail)

rs = HostManagerdb.getAllUsers();
printUsers(rs)
