#sqlite database module
# -*- coding: utf-8 -*-
import sqlite3


def init():

    conn = sqlite3.connect('m_database.db')
    print "Opened database successfully";
    try :
        #dropping existing tables
        conn.execute("DROP TABLE ADMINS;")
        conn.execute("DROP TABLE USERS;")
        conn.execute("DROP TABLE HOSTING;")
        conn.execute("DROP TABLE DOMAIN;")
    except:
        print "e100 no tables exists"

    #CREATE tables
    print "Creating admins Table"
    conn.execute('''CREATE TABLE ADMINS
           (adminId INT PRIMARY KEY     NOT NULL,
           name           TEXT    NOT NULL,
           password            TEXT     NOT NULL
           );''')
    print "Table created successfully";

    print "Creating users Table"
    conn.execute('''CREATE TABLE USERS
           (userId INT PRIMARY KEY     NOT NULL,
           name           TEXT    NOT NULL,
           phone            TEXT     NOT NULL,
           email        TEXT
           );''')
    print "Table created successfully";

    print "Creating hosting Table"
    conn.execute('''CREATE TABLE HOSTING
           (userId INT     NOT NULL,
           website           TEXT    NOT NULL,
           storage            TEXT     NOT NULL,
           bandwidth            TEXT     NOT NULL,
           startDate            TEXT     NOT NULL,
           endDate            TEXT     NOT NULL,
           paidState            INT     NOT NULL,
           hostingState            TEXT     NOT NULL,
           price         REAL,
           PRIMARY KEY (userId, website));''')
    print "Table created successfully";

    print "Creating domain Table"
    conn.execute('''CREATE TABLE DOMAIN
           (userId INT     NOT NULL,
           domain           TEXT    NOT NULL,
           startDate            TEXT     NOT NULL,
           endDate            TEXT     NOT NULL,
           paidState            INT     NOT NULL,
           price         REAL,
           PRIMARY KEY (userId, domain));''')
    print "Table created successfully";
    conn.close()


def newAdmin(f_name,f_pass):
    id = noOfAdmins() + 1;
    conn = sqlite3.connect('m_database.db')
    print "Opened database successfully";
    c = conn.cursor()
    # c.execute('INSERT INTO USERS (userId,name,phone,email) VALUES ( id,name,phone,email)')
    # print "data inste"
    c.execute('''INSERT INTO ADMINS (adminId,name,password) VALUES ( ?,?,?)''',(id,f_name ,f_password) )
    conn.commit()
    conn.close()
    return 1

def newUser(vname,vphone,vemail):
    id = noOfUsers() + 1;
    conn = sqlite3.connect('m_database.db')
    print "Opened database successfully";
    c = conn.cursor()
    # c.execute('INSERT INTO USERS (userId,name,phone,email) VALUES ( id,name,phone,email)')
    # print "data inste"
    c.execute('''INSERT INTO USERS (userId,name,phone,email) VALUES ( ?,?,?,?)''',(id,vname,vphone,vemail) )
    conn.commit()
    conn.close()
    return 1

def newDomain(id,domain,start,end,paidS,price):
    conn = sqlite3.connect('m_database.db')
    c = conn.cursor()
    print "Opened database successfully";
    c.execute("INSERT into Domain values (?,?,?,?,?,?)"%(id,domain,start,end,paidS,price))
    conn.commit()
    conn.close()
    return 1

def newHost(id,website,storage,bandwidth,start,end,paidS,hostS,price):
    conn = sqlite3.connect('m_database.db')
    c = conn.cursor()
    c.execute("INSERT into Domain values (?,?,?,?,?,?)"%(id,website,storage,bandwidth,start,end,paidS,hostS,price))
    conn.commit()
    conn.close()
    return 1

def getAllUsers():
    conn = sqlite3.connect('m_database.db')
    c = conn.cursor()
    out = c.execute("SELECT * FROM USERS")
    out = out.fetchall();
    conn.close()
    return out

def noOfUsers():
    conn = sqlite3.connect('m_database.db')
    c = conn.cursor()
    out = c.execute("SELECT count(*) FROM USERS")
    out = out.fetchone();
    conn.close()
    return out[0]

def noOfAdmins():
    conn = sqlite3.connect('m_database.db')
    c = conn.cursor()
    out = c.execute("SELECT count(*) FROM ADMINS")
    out = out.fetchone();
    conn.close()
    return out[0]

def noOfDomains():
    conn = sqlite3.connect('m_database.db')
    c = conn.cursor()
    out = c.execute("SELECT count(*) FROM DOMAIN")
    out = out.fetchone();
    conn.close()
    return out[0]

def noOfHosts():
    conn = sqlite3.connect('m_database.db')
    c = conn.cursor()
    out = c.execute("SELECT count(*) FROM HOSTING")
    out = out.fetchone();
    conn.close()
    return out[0]

def dropTables():
    conn = sqlite3.connect('m_database.db')
    c = conn.cursor()
    print "Opened database successfully";
    try :
        #dropping existing tables
        c.execute("DROP TABLE ADMINS;")
        c.execute("DROP TABLE USERS;")
        c.execute("DROP TABLE HOSTING;")
        c.execute("DROP TABLE DOMAIN;")
        conn.commit()
        print "Tables Droped Successfully "
    except:
        print "e100 no tables exists"
    finally:
        conn.close()

def getUserData(f_userId):
    conn = sqlite3.connect('m_database.db')
    c = conn.cursor()
    out = c.execute("SELECT * FROM USERS WHERE userId = ?",(f_userId))
    out = out.fetchall();
    conn.close()
    return out

#get user id
def getUserID(userName):

    conn = sqlite3.connect('m_database.db')
    print "Opened database successfully";
    res = conn.execute("SELECT userId from USERS where name = ?",(userName))
    conn.close()
    return res[0]
