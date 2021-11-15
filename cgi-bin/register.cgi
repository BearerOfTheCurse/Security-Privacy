#!/usr/bin/env python3
import cgi
import subprocess
import re

PATH_TO_MACHINE = "./etovucca"


def render_register():
    print("Content-Type: text/html")
    print("Cache-Control: no-store, must-revalidate")
    print()
    print()
    print("<link rel='stylesheet' href='https://spar.isi.jhu.edu/teaching/443/main.css'>")
    print("<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>")
    print("<link rel='stylesheet' type='text/css' href='../style/vm.css' />")
    print('<h2 id="dlobeid-etovucca-voting-machine">A WONDERFUL E-Voting Machine</h2><h1 id="voter-registration">Voter Registration</h1><br><form><label for="name">Voter Name</label><br> <input type="text" id="name" name="name"><br> <label for="county">County</label><br> <input type="text" id="county" name="county"><br> <label for="zipc">ZIP Code</label><br> <input type="number" id="zipc" name="zipc"><br> <label for="dob">Date of Birth</label><br> <input type="date" id="dob" name="dob"><br> <input type="submit" value="Submit"></form>')
    print('<p>All fields must be filled~</p>')
    print('<a href="./home.cgi">Return to Homepage</a><br>')


def register_voter():
    validName = form.getvalue('name') != None and re.match(
        "^[A-Za-z]+$", form.getvalue('name'))
    validCounty = form.getvalue('county') != None and re.match(
        "^[A-Za-z]+$", form.getvalue('county'))
    validZip = form.getvalue('dob') != None
    validDob = form.getvalue('zipc') != None and re.match(
        "^[0-9]+$", form.getvalue('zipc'))
    if validName and validCounty and validZip and validDob:
        voter_id = int(subprocess.check_output([PATH_TO_MACHINE, 'add-voter', form.getvalue(
            'name'), form.getvalue('county'), form.getvalue('zipc'), form.getvalue('dob')]))
        if voter_id != 0:
            print("<b>Voter registered. ID: {}</b>".format(voter_id))
        else:
            print("<b>Error in registering voter. Please try again.</b>")
    else:
        print("<script>alert('Invalid or missing entries>_<')</script>")


render_register()
form = cgi.FieldStorage()
if len(form) != 0:
    register_voter()
