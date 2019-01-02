# -*- coding: utf-8 -*-

"""

    sqlite_functions.py
    created by: Ferdinand Feoli
    developer's profile: https://sites.google.com/view/ferdsprofile/
    coded using Python 3.7 syntax
    built using Python 3.6 and pyinstaller 3.3

    This module contains the functions for interaction with the database.
    The database creation comes implicit in all the functions of this module.

    Available functions:
        - db_drop_table()
        - db_create_table()
        - db_table_sort()
        - db_insert()
        - db_get_top50()

"""

# External modules needed  - - - - - - -
import sqlite3 as sql3
# - - - - - - - - - - - - - - - - - - - -


def db_drop_table(path):
    """
        Drops REGEDITINFO table if exists.

        args:
            path=
                (string) the directory where the database should be stored
    """
    conn = sql3.connect(path+"STORAGE.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS REGEDITINFO")
    conn.commit()
    conn.close()


def db_create_table(path):
    """
        Creates REGEDITINFO table and its columns:
            - KEY: (String) Column to store the registry key/subkey name.
            - NUM_DATE: (Float) Column to store the value in seconds of the
            key/subkey's last modification date time.
            - NUM_DATE: (DateTime) Column to store the value of the
            key/subkey's last modification date time
            in the following format: A,B d,Y H:M:S

        args:
            path=
                (string) the directory where the database should be stored
    """
    conn = sql3.connect(path+"STORAGE.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE REGEDITINFO (KEY TEXT, NUM_DATE REAL, LAST_MODIFIED DATETIME)")
    conn.commit()
    conn.close()


def db_table_sort(path):
    """
        Sorts REGEDITINFO table by descending NUM_DATE.

        args:
            path=
                (string) the directory where the database should be stored
    """
    conn = sql3.connect(path+"STORAGE.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS TEMP")
    cur.execute("CREATE TABLE TEMP AS SELECT * FROM REGEDITINFO ORDER BY NUM_DATE DESC")
    cur.execute("DROP TABLE REGEDITINFO")
    cur.execute("ALTER TABLE TEMP RENAME TO REGEDITINFO")
    conn.commit()
    conn.close()


def db_insert(path, key, num_date, last_modified):
    """
        Stores key/subkey information passed as arguments by
        store_key_info() function from backend module in REGEDITINFO table.

        args:
            path=
                (string) the directory where the database should be stored
            key=
                (string) contains the name of the key/subkey.
            num_date=
                (float) contains the value in seconds of the
                key/subkey's last modification date time.
            last_modified=
                (datetime) (DateTime) contains the value of the
                key/subkey's last modification date time
                in the following format: A,B d,Y H:M:S
    """
    conn = sql3.connect(path+"STORAGE.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO REGEDITINFO VALUES (?,?,?)", (key, num_date, last_modified))
    conn.commit()
    conn.close()


def db_get_top50(path):
    """
        Executes a query taht gets the top50 results stored in the database.

        args:
            path=
                (string) the directory where the database should be stored
    """
    conn = sql3.connect(path+"STORAGE.db")
    cur = conn.cursor()
    cur.execute("SELECT KEY, LAST_MODIFIED FROM REGEDITINFO LIMIT 51")

    lst = cur.fetchall()

    conn.close()

    return lst
