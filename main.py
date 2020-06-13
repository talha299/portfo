"""
free templates are:
https://cruip.com/
https://www.creative-tim.com/bootstrap-themes/ui-kit?direction=asc&sort=price
http://www.mashup-template.com/templates.html
"""


"""
http://www.mashup-template.com/templates.html  --download free templates from here, in video he download the see images: 1-template.png
make virtual environment by on terminal like this: D:python -m venv p19-building-a-portfolio/
now activate the scripts by this: D:.\p19-buiding-a-portfolio\Scripts\ activate   -> see images: 2-make virtual environment plus activate the scripts.png
virtual environment files: see images:  3-virtual environment files.png
create folder "templates" for html files bcz we use flask and in flask we use render_template to run the html file in the python file
and create folder "static" to place images of free download templates and css files and js files
downloaded free templates files move into these folders and delete some files which is not in the image, see images: 4-template download files.png
change the url of the file like: static/assets, please do on terminal see images: 5-do on terminal.png
as you see images: 5-do on terminal.png, do degug mode on like that: see images: 6-debug-mode-on.png
"""

from flask import Flask, render_template, url_for, request, redirect   #  request for fetch data from contact-form,  redirect for thankyou.html
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

"""
and then run the url see images: 7-first_run_after_terminal_installation.png
"""

"""
change code in html page, change url for images,css,js,assets folder like ./static/  instead of ./
"""

"""
for other pages
@app.route("/about.html")
def my_about():
    return render_template("about.html")


@app.route("/components.html")
def my_components():
    return render_template("components.html")


@app.route("/contact.html")
def my_contact():
    return render_template("contact.html")


@app.route("/work.html")
def my_work():
    return render_template("work.html")


@app.route("/works.html")
def my_works():
    return render_template("works.html")


but it is not a correct way, everytime we make a html file then we need to add the code like this, it is not a good way so for it make it dynamic
"""

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


"""
comment out the components.html file from all html pages bcz we don't need it like: <!--   <li><a href="./components.html" title="">05 : Components</a></li>   -->
"""

"""
now work on contact.html page, people who contact me, save it in the database
contact.html: form action=submit_form method=post   -> submit_form bcz of @app.route("submit_form") (note: you can change this name) bcz when form sent then action takes place and changes in url and our url changes to 127.0.0.1:5000/submit_form
post=information not show in url,  get= information show in url

"""


"""
@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    return "form Submitted hurrey"
"""
"""
after above see images: 8-contact-form(1).png, 8-contact-form(2).png
add the name in the form like input name="email" etc see images: 8-contact-form(3).PNG
after form sent see network part, see images: 8-contact-form-network(4.1).PNG, 8-contact-form-network(4.2).PNG
"""


"""
make a thankyou.html, copy the contact.html data into thankyou.html file,  and cut the form part in thankyou.html
"""
"""
@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        # data = request.form["email"]   #  one way and there is also another way
        data = request.form.to_dict()  #  all data of form sent in dictionary
        # print(data)  #  {"email":"ta@gmail.com", "subject":"fdf", "message":"jfdsdsj"}
        return redirect("/thankyou.html")
    else:
        return "Something went wrong. Please try again!"

after above see images: 8-contact-form(5.1).png, 8-contact-form(5.2).png
optional: add name of user in thankyou.html like {{}} Thank you...,  but we not do now

now we save it in the database, bcz before it is just save in memory. Anytime i close/refresh the server this information is lost.
first we save the data in a file and file place it our laptop, name it database.txt
and write in a file like email,subject,message  see images: 8-contact-form-save-in-a-file(6.1).PNG
"""

def write_to_file(data):
    with open("database.txt", mode="a") as database:   #  a for append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"{email},{subject},{message}\n")

# add it later for csv(comma separated values)
import csv
def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:   #  a for append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",")  #  csv.writer has 4 parameters and 3 of them are optional, you can check by yourself, delimeter is for how to separate the data
        #  if you have not headers in a file(header mean: email,subject,message the first row of the file) then you can also do by using writeheader()
        csv_writer.writerow([email,subject,message])

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        # data = request.form["email"]   #  one way and there is also another way
        data = request.form.to_dict()  #  all data of form sent in dictionary
        # print(data)  #  {"email":"ta@gmail.com", "subject":"fdf", "message":"jfdsdsj"}
        write_to_file(data)

        # add it later to data save in excel/csv file, previos code you see in 8-contact-form-save-in-a-file(6.1-6.5).PNG
        # make a new file database.csv, and make a function write_to_csv  -> csv file see images: 8-contact-form-save-in-a-csv(7.1).PNG
        # see images: 8-contact-form-save-in-a-csv(7.1-7.6).PNG
        write_to_csv(data)

        return redirect("/thankyou.html")
    else:
        return "Something went wrong. Please try again!"


"""
may be i lost my laptop, or my laptop is not turn on anymore, in this case i lost my data, database use for to store large
amount of data it looks like the excel sheet but even more powerful
Database: it is collection of data, and what is meant by data, there are many forms of them, there can be numbers, there can be dates
Database allow us to organize this data in a useful way
DBMS(Database Management System): it is a collection of programs which allow us to access databases and work with data
there are two types:
relational database  -- (there are postgresql, mysql, oracle, sqlite etc)  : for these we mostly need sql to communicate
non relational database  -- (there are mongodb, redis, couchdb, riak etc)   : in mongodb we need mongodb query language to communicate
but both used for to communicate database with server
see images: 9-contact-form-save-in-database(1).PNG

http://127.0.0.1:5000/index.html or localhost:5000/index.html , if i give url to any person then he not used it, bcz this url
points to my localhost, localhost simply means your computer
we create our url like 000webhost which i used in my final year project
https://pythonanywhere.com  -> make an account and select free account/beginner account
email: umersultan29959@gmail.com, password: talha7636, username: talha299
create a github account and upload all files there, create a repository
email: umersultan29959@gmail.com, password: talha7636, username: talha299
see images: 9-contact-form-save-in-database(2.1-python everywhere after login).PNG ,
9-contact-form-save-in-database(3.1-github after login).PNG, 9-contact-form-save-in-database(3.2-github after login).PNG,
9-contact-form-save-in-database(3.3-github after login).PNG
now open the new terminal: go on that folder where this project is available like like it is current page of D drive, and on
terminal make the project clone: git clone https://github.com/talha299/portfo.git
see images: 9-contact-form-save-in-database(3.4-github after login).PNG, 9-contact-form-save-in-database(3.5-github after login).PNG,
9-contact-form-save-in-database(3.6-github after login).PNG
see on previous terminal: make the requiremnt file like see images: 10-make-requirements-txt(1).png
what is inside in requirements.txt -> in which we have the requirements to run our website: see iamges: 10-make-requirements-txt(2).png,
when i upload these project files into pythonanywhere(static, templates, database.csv, requirements.txt, main.py) -> then from reqirements.txt file he automatically
installed these things for us
bcz if we upload all files on pythonanywhere then there is load more on it, so from requirements.txt he automatically install these
now copy files from here and paste in portfo see images: 


"""

"""
create logos for free for your project:  https://hatchful.shopify.com/
"""
