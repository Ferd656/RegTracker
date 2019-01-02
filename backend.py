# -*- coding: utf-8 -*-

"""

    backend.py
    created by: Ferdinand Feoli
    developer's profile: https://sites.google.com/view/ferdsprofile/
    coded using Python 3.7 syntax
    built using Python 3.6 and pyinstaller 3.3

    This module contains the main functions of the program.

    Available functions:
        - create_readme()
        - html_open()
        - html_log()
        - html_readme()
        - regedit_open()
        - db_open()
        - donate()
        - explains_delay()
        - entry_validation()
        - store_key_info()
        - print_results()
        - get_listbox_selection()
        - mainprocess()
        - close_protocol()

"""

# External modules needed  - - - - - - -
import os
import pyperclip
import webbrowser
from winreg import *
from tkinter import *
from subprocess import *
from datetime import datetime
from tkinter import messagebox
import sqlite_functions as sql_f
# - - - - - - - - - - - - - - - - - - - -

# Module variables  - - - - - - - - - - - - - - - - - - - -

# UNUSED:	print(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

myname = "RegTracker"

mypath = os.getcwd()

d = chr(92)

Hkeys = {'HKEY_CLASSES_ROOT': HKEY_CLASSES_ROOT,
         'HKEY_CURRENT_USER': HKEY_CURRENT_USER,
         'HKEY_LOCAL_MACHINE': HKEY_LOCAL_MACHINE,
         'HKEY_USERS': HKEY_USERS,
         'HKEY_PERFORMANCE_DATA': HKEY_PERFORMANCE_DATA,
         'HKEY_CURRENT_CONFIG': HKEY_CURRENT_CONFIG,
         'HKEY_DYN_DATA': HKEY_DYN_DATA}
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def create_readme():
    """
        This function creates 'readme.txt' file.

        args:
            none.
    """
    readme = open("readme.txt", "w+")

    rdmstr = ["================================== " + myname + " ==================================", " ",
              "    Hello registry hackers, this program was created in order to provide a",
              "    tool for those who have the need of making any system changes via",
              "    registry.",
              "    Make a change in your system and " + myname + " will help you to",
              "    find out wich was the key whose values were modified within",
              "    that change.",
              "    The program works obtaining the last modified keys in the registry",
              "    within a user-defined time range, giving the possibility of tracking",
              "    the key you need.", " ",
              "    All data related to " + myname + "'s scans will be porperly stored so you",
              "    can consult it any time.",
              "    Use " + myname + "'s graphic interface to perform the scans and query the",
              "    resulting data.",
              "    This program uses SQLite DB Browser for advanced queries.",
              "    Visit DB Browser webpage at: https://sqlitebrowser.org/",
              "    Keep in mind that the depth of the scans will go as far as your",
              "    rights over the registry.", " ",
              "    Do you want to know more about me?",
              "    Please visit my page: https://sites.google.com/view/ferdsprofile/", " ",
              "_+88_",
              "_+880_",
              "_++88_",
              "_++88_",
              "__+880_________________________++_",
              "__+888________________________+88_",
              "__++880______________________+88_",
              "__++888_____+++88__________+++8_",
              "__++8888__+++8880++88____+++88_",
              "__+++8888+++8880++8888__++888_",
              "___++888++8888+++888888++888_",
              "___++88++8888++8888888++888_",
              "___++++++888888888888888888_",
              "____++++++88888888888888888_",
              "____++++++++000888888888888_",
              "_____+++++++000088888888888_",
              "______+++++++00088888888888_",
              "_______+++++++088888888888_",
              "_______+++++++088888888888_",
              "________+++++++8888888888_",
              "________+++++++0088888888_",
              "________++++++0088888888_",
              "________+++++0008888888_",
              "________###############_",
              " ",
              "Visit Developer's GitHub profile for this pyoject's full documentation and sourcecode:",
              "https://github.com/Ferd656"]

    for rstr in rdmstr:

        readme.write(rstr + chr(10))

    readme.close()


def html_open(htmlfile):
    """
        This function opens an HTML file in default browser.

        args:
            htmlfile=
                (string) contains the path of the HTML file to open.
    """
    try:
        webbrowser.open(htmlfile)
    except Exception as e4:
        messagebox.showerror("Error", myname + " could not open " +
                             htmlfile + ". Restarting the program may " +
                             "fix the problem.\n\n" +
                             "  - Exception detail:"
                             "\n\n" + str(e4))


def html_log():
    """
        This function creatles the Log.html file using Log.csv,
        then, the Log.html file is opened by the html_open() function.

        args:
            none.
    """

    filepath = mypath + d + "Log.csv"

    if os.path.isfile(filepath):

        htmllog = open("Log.html", "w+")
        html_content = ["<!DOCTYPE html>",
                        "<html>",
                        "<head>",
                        "<center><font color='#000066' face='arial' size='14'><b>Process Log</b></font></center>"
                        "    <script type='text/javascript' src='http://mbostock.github.com/d3/d3.js'></script>",
                        "</head>",
                        "<body>",
                        "<font color='#003366'>",
                        "NOTE:",
                        "<br>",
                        ">>>>>>>> Keep in mind that the depth of the scans will go as far as your rights over the ",
                        "registry. Some exceptions may raise due to matter of perrmissions.",
                        "<br>",
                        ">>>>>>>> If no data is loaded, log file may be damaged, in that case run again the process",
                        "to generate a new log.",
                        "<br>",
                        "</font>",
                        "    <div id='viz'></div>",
                        "    <script type='text/javascript'>",
                        "    d3.text('Log.csv', function(datasetText) {",
                        "    var parsedCSV = d3.csv.parseRows(datasetText);",
                        "    var sampleHTML = d3.select('#viz')",
                        "        .append('table')",
                        "        .style('border-collapse', 'collapse')",
                        "        .style('border', '2px black solid')",
                        "        .selectAll('tr')",
                        "        .data(parsedCSV)",
                        "        .enter().append('tr')",
                        "        .selectAll('td')",
                        "        .data(function(d){return d;})",
                        "        .enter().append('td')",
                        "        .style('border', '1px black solid')",
                        "        .style('padding', '5px')",
                        "        .on('mouseover', function(){d3.select(this).style('background-color', 'aliceblue')})",
                        "        .on('mouseout', function(){d3.select(this).style('background-color', 'white')})",
                        "        .text(function(d){return d;})",
                        "        .style('font-size', '12px');",
                        "    });",
                        "    </script>",
                        "</body>",
                        "</html>"]

        for cntnt in html_content:

            htmllog.write(cntnt + chr(10))

        htmllog.close()

        html_open("Log.html")

    else:
        messagebox.showwarning("Unable to load", filepath + " file not found.\n" +
                               "Click the 'Run' button to generate " +
                               "new results.")


def html_readme():
    """
        This function creatles the readme.html file,
        then, the readme.html file is opened by the html_open() function.

        args:
            none.
    """
    imgref = mypath + d + r"bin\images\Donate.png"
    htmlreadme = open("readme.html", "w+")
    html_content = ["<!DOCTYPE html>",
                    "<head>",
                    "<font color='#000066' size='10'>",
                    "<center>",
                    "    = = = = = = = = = = " + myname + " = = = = = = = = = =",
                    "</center>",
                    "</font>",
                    "</head>", "<br> ",
                    "<body>",
                    "<font face='arial'>",
                    "<center>",
                    "<br>    Hello registry hackers, this program was created in order to provide a",
                    "<br>    tool for those who have the need of making any system changes via registry.", "<br> ",
                    "<br>    Make a change in your system and " + myname + " will help you to",
                    "<br>    find out wich was the key whose values were modified within that change.", "<br> ",
                    "<br>    The program works obtaining the last modified keys in the registry",
                    "<br>    within a user-defined time range, giving the possibility of tracking",
                    "<br>    the key you need.", "<br> ",
                    "<br>    All data related to " + myname + "'s scans will be porperly stored so you",
                    "<br>    can consult it any time.", "<br> ",
                    "<br>    Use " + myname + "'s graphic interface to perform the scans and query the",
                    "<br>    resulting data.", "<br> ",
                    "<br>    This program uses SQLite DB Browser for advanced queries.",
                    "<br>    Visit DB Browser webpage at: <a href='https://sqlitebrowser.org/' target='_blank'>" +
                    "https://sqlitebrowser.org/</a> ", "<br> ",
                    "<br>    Keep in mind that the depth of the scans will go as far as your",
                    "<br>    rights over the registry.", "<br> ",
                    "<br>    Do you want to know more about me?",
                    "<br>    Please visit my page:",
                    "<br>    <a href='https://sites.google.com/view/ferdsprofile/' target='_blank'>" +
                    "Developer's profile</a> ", "<br> ",
                    "<br>    Feel free to make a voluntary donation", "<br> ",
                    "<br>    ",
                    "    <a href = 'https://paypal.me/Feoli' target='blank'>",
                    "        <img src = '" + imgref + "' alt = 'Donate' style = 'width:241;height:128px;'>",
                    "    </a>", "<br> ",
                    "<br>_+88_______________________________",
                    "<br>_+880______________________________",
                    "<br>_++88______________________________",
                    "<br>_++88______________________________",
                    "<br>__+880_________________________++__",
                    "<br>__+888________________________+88__",
                    "<br>__++880______________________+88___",
                    "<br>__++888_____+++88__________+++8____",
                    "<br>__++8888__+++8880++88____+++88_____",
                    "<br>__+++8888+++8880++8888__++888______",
                    "<br>___++888++8888+++888888++888_______",
                    "<br>___++88++8888++8888888++888________",
                    "<br>___++++++888888888888888888________",
                    "<br>____++++++88888888888888888________",
                    "<br>____++++++++000888888888888________",
                    "<br>_____+++++++000088888888888________",
                    "<br>______+++++++00088888888888________",
                    "<br>_______+++++++088888888888_________",
                    "<br>_______+++++++088888888888_________",
                    "<br>________+++++++8888888888__________",
                    "<br>________+++++++0088888888__________",
                    "<br>________++++++0088888888___________",
                    "<br>________+++++0008888888____________",
                    "<br>________###############____________", "<br> ",
                    "<br>    Visit <a href='https://github.com/Ferd656' target='_blank'>" +
                    "Developer's GitHub profile</a> for this project's full documentation and sourcecode.",
                    "</center>",
                    "</font>",
                    "</body>",
                    "</html>"]

    for cntnt in html_content:

        htmlreadme.write(cntnt + chr(10))

    htmlreadme.close()

    html_open("readme.html")


def regedit_open(root):
    """
        This function opens the registry editor.
        An error message will be shown if an exception raises.

        args:
            root=
                (tkinter window object) the object reference for
                interactions with interface.
    """
    try:
        root.withdraw()
        call(['regedit'], shell=True)
        root.deiconify()
    except Exception as e3:
        messagebox.showerror("Error",
                             myname + u" could not open RegEdit\n\n" +
                             "  - Exception detail:\n\n" + str(e3))


def db_open(root):
    """
        This function opens the program's database using DB Browser.
        An error message will be shown if an exception raises.

        args:
            root=
                (tkinter window object) the object reference for
                interactions with interface.
    """
    try:
        database_path = mypath + d + "data" + d + "STORAGE.db"

        if os.path.isfile(database_path):

            # os.chdir(mypath + d + "bin" +d)
            # os.system(mypath + d + "bin" +d + "DBBrowser.exe " + database_path)
            root.withdraw()
            call(mypath + d + "bin" + d + "DBBrowser.exe " + database_path, shell=True)
            root.deiconify()

        else:
            messagebox.showwarning("Unable to load", "DataBase file not found.\n" +
                                   "Click the 'Run' button to generate " +
                                   "new data.")

    except Exception as e4:
        messagebox.showerror("Error",
                             myname + u" could not open BD Browser\n\n" +
                             "  - Exception detail:\n\n" + str(e4))


def donate():
    """
        This function opens PayPal's url for payments
        You can make a voluntary donation to the developer
        through there.

        args:
            none.
    """
    webbrowser.open("https://paypal.me/Feoli")


def explains_delay():
    """
        Swhows a messagebox explaining the function of the
        ''delay seconds'' defined by the user.

        Seconds must be > 0 and < 1000000

        args:
            none.
    """
    messagebox.showinfo(myname, "The program will ignore those keys wich " +
                        "last time modified is\na certain number of seconds before " +
                        "the time the main process starts running.\n\n" +
                        "Using the following entry you can define those seconds to " +
                        "the program.")


def entry_validation(entry, var):
    """
        This function validates the delay value defined in entry and will correct
        it if necessary.

        args:
            entry=
                (tkinter entry widget) the widget wich this function will interact with.
            var=
                (string) the value to be validated
    """
    lst = [".", ",", "-", " "]
    flag = False
    if len(var) > 0:
        for i in lst:
            if i in var:
                var = var.replace(i, "")
                flag = True

        if not var.isdigit():
            var = "60"
            flag = True

        elif var == "0":
            var = "60"
            flag = True

        elif int(var) > 1000000:
            var = "1000000"
            flag = True

        if flag:
            entry.delete(0, END)
            entry.insert(INSERT, var)


def store_key_info(root, widget, dbpath, log, dt_now, keyname, key):
    """
        This function sends key and subkeys information to the database using
        db_insert() function from sqlite_functions module.

        To know wich information is stored, consult the docstring of db_create_table()
        function or db_insert() function in sqlite_functions module.

        args:
            dbpath=
                (string) the path where the database is stored
            log=
                (textiowrapper) object where the log message will be stored.
            dt_now=
                (float) contains the value of the datetime value in seconds of the
                excecution of mainprocess() minus delay.
            keyname=
                (string) contains the name of the key/subkey.
            key=
                (winreg handler object) registry keyobject.
    """
    seconds = (QueryInfoKey(key)[2]/10000000)-11644473600

    if seconds >= dt_now or keyname in Hkeys:

        sql_f.db_insert(dbpath, keyname, seconds,
                        datetime.fromtimestamp(seconds).strftime("%A, %B %d, %Y %H:%M:%S"))

    for i in range(QueryInfoKey(key)[0]):

        subkey = EnumKey(key, i)

        kn = keyname + d + subkey

        try:

            k = OpenKeyEx(key, subkey, 0, KEY_READ)

        except Exception as e2:

            log.write(u"\nUnable to access " + kn + ",Exception," + str(e2))
            k = ""

        if k != "":

            if keyname in Hkeys:
                status_str = "{0:.2f}%".format(((i+1)/QueryInfoKey(key)[0])*100)

                log.write(u"\nComputing " + keyname + ",Ok," + status_str)

                widget.delete('1.0', END)
                widget.insert(INSERT, "   Status:" + " "*90 + "Computing " +
                              keyname + " " + status_str)
                root.update()

            store_key_info(root, widget, dbpath, log, dt_now, kn, k)

            CloseKey(k)


def print_results(root, widget, path):
    """
        This function printd inside the interface listbox, the top
        50 results of the scan, queried by db_get_top50() function of
        sqlite_functions module.

        args:
            root=
                (tkinter window object) the object reference for
                interactions with interface.
            widget=
                (TKTreectrl multilistbox widget) the widget that will
                recieve and store the list of top results of the scan
                to show them to the user.
            path=
                (string) the path where the database is stored
    """
    result_list = sql_f.db_get_top50(path)

    if len(result_list) > 50:
        for i in range(50):
            widget.insert("END", result_list[i])

    else:
        for i in range(len(result_list)):
            widget.insert("END", result_list[i])

    root.update()

    return len(result_list)


def get_listbox_selection(item, listbox):
    """
        This function will store the selected item in the listbox
        to the clipboard. It will be triggered by double-click
        on the listbox.

        args:
            item=
                (integer) the integer index of the selected item in
                the listbox.
            listbox=
                (TKTreectrl multilistbox widget) thw widget that
                contains the list of top results of the scan.
    """
    if str(listbox.get(item)) != "()":
        try:
            pyperclip.copy(str(listbox.get(item)))

            messagebox.showinfo(myname, "Item copied to the clipboard")

        except Exception as e4:
            messagebox.showwarning(myname, "Could not get item\n\n" +
                                   "  - Exception detail:\n\n" + str(e4))


def mainprocess(root, monitor, listbox, delay=60):
    """
        This function will iterate through registry main keys:
            -   HKEY_CLASSES_ROOT
            -   HKEY_CURRENT_USER
            -   HKEY_LOCAL_MACHINE
            -   HKEY_USERS
            -   HKEY_PERFORMANCE_DATA
            -   HKEY_CURRENT_CONFIG
            -   HKEY_DYN_DATA
        storing their last modified datetime in database using
        the store_key_info() function.

        args:
            root=
                (tkinter window object) the object reference for
                interactions with interface.
            monitor=
                (tkinter text widget) the widget that will recieve
                scan status information to show it to the user.
            listbox=
                (TKTreectrl multilistbox widget) the widget that will
                recieve and store the list of top results of the scan
                to show them to the user.
            delay=
                (integer) number of seconds defined by user, that
                will be substracted from this function's execution
                date time seconds.

                Those registry keys or subkeys wich last modification
                datetime is less than the result of the substraction
                mentioned above, will be ignored by store_key_info()
                function, in order to optimize execution times.
    """
    listbox.delete(0, END)
    monitor.insert(INSERT, "   Status:" + " "*100 +
                   "- -       click 'Run' button to start       - -")
    root.update()
    try:
        dt_now = datetime.now().timestamp() - delay

        dbpath = "data" + d

        log = open('Log.csv', 'w+')

        log.write("DESCRIPTION,STATUS,DETAIL")

        sql_f.db_drop_table(dbpath)

        sql_f.db_create_table(dbpath)

        for Hkey in Hkeys:

            try:
                store_key_info(root, monitor, dbpath, log, dt_now, Hkey, Hkeys[Hkey])
            except Exception as e:
                log.write(u"\nAn error occurred computing " + Hkey + ",Exception," + str(e))

        log.close()

        sql_f.db_table_sort(dbpath)

        monitor.delete('1.0', END)
        monitor.insert(INSERT, "   Status:" + " "*90 +
                       "- -       Task finished       - -")
        root.update()

        q_results = print_results(root, listbox, dbpath)

        if q_results > 50:
            selection = messagebox.askyesno(myname,
                                            "Process finished successfully!\n\n" +
                                            "The process stored more than 50 results, \n" +
                                            "however only 50 results were printed in the \n" +
                                            "output listbox.\n\n" +
                                            "Would you like to open the database using DB Browser" +
                                            "\nsoftware to see complete results?")

            if selection:
                db_open(root)

        selection = messagebox.askyesno(myname,
                                        "Process finished successfully!\n\n" +
                                        "Would you like to load the process log?")

        if selection:
            html_log()

    except Exception as main_e:
        messagebox.showerror("Error",
                             "An error occurred durind the main process execution.\n\n" +
                             "  - Exception detail:\n\n" + str(main_e))


def close_protocol(root):
    """
        This function will aplly the WM_DELETE_WINDOW protocol
        when the Exit buttom is not being used to close the
        window.

        args:
            root=
                (tkinter window object) the object reference for
                interactions with interface.
    """
    if messagebox.askokcancel(myname, "Do you want to quit?"):
        root.destroy()
