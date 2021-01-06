import html

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import requests
from lxml import etree
import xlrd


class major:
    def __init__(self, name, url):
        self.name = name
        self.url = url


class school:
    def __init__(self, name, tag):
        self.name = name
        self.tag = tag


def createMajorList(loc, tag):
    majors = []
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    for i in range(sheet.nrows):
        name = sheet.cell_value(i, 0)
        url = sheet.cell_value(i, 1) + tag
        m = major(name, url)
        majors.append(m)
    return majors


wb = xlrd.open_workbook("schools.xlsx")
sheet = wb.sheet_by_index(0)
schools = []
for i in range(sheet.nrows):
    name = sheet.cell_value(i, 0)
    tag = sheet.cell_value(i, 1)
    s = school(name, tag)

    schools.append(s)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ce597dcf9dcd138b8cd0828a7dbe7437'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', schools=schools)


@app.route("/about")
def about():
    return render_template('sfsu-accountancy.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/ucd")
def ucdMajor():
    loc = ('ucd.xlsx')  # list of sfsu majors'
    return render_template('ucd-major.html', title='University of California, Davis', majors=createMajorList(loc, ""))


@app.route("/ucr")
def ucrMajor():
    return render_template('ucr-major.html', title='University of California, Riverside')


@app.route("/ucla")
def uclaMajor():
    loc = ('ucla.xlsx')  # list of sfsu majors'
    return render_template('ucla-major.html', title='University of California, Los Angeles',
                           majors=createMajorList(loc, ""))


@app.route("/ucmerced")
def ucmMajor():
    loc = ('ucm.xlsx')  # list of sfsu majors'
    return render_template('ucm-major.html', title='University of California, Merced', majors=createMajorList(loc, ""))


@app.route("/uci")
def uciMajor():
    loc = ('uci.xlsx')  # list of sfsu majors'
    return render_template('uci-major.html', title='University of California, Irvine',
                           majors=createMajorList(loc, "#requirementstext"))


@app.route("/ucsb")
def ucsbMajor():
    loc = ('ucsb.xlsx')  # list of sfsu majors'
    return render_template('ucsb-major.html', title='University of California, Santa Barbara',
                           majors=createMajorList(loc, ""))

@app.route("/ucsc")
def ucscMajor():
    loc = ('ucsc.xlsx')  # list of sfsu majors'
    return render_template('ucsc-major.html', title='University of California, Santa Cruz',
                           majors=createMajorList(loc, ""))

@app.route("/ucb")
def ucbMajor():
    loc = "ucb.xlsx"
    return render_template('ucb-major.html', title='University of California, Berkeley',
                           majors=createMajorList(loc, "#majorrequirementstext"))


@app.route("/sfsu")  # sfsu majors
def sfsuMajor():
    class major:
        def __init__(self, name, disciplines, urls):
            self.name = name
            self.disciplines = disciplines
            self.urls = urls

    sfsuMajors = ('sfsu.xlsx')  # list of sfsu majors
    majors = []
    wb = xlrd.open_workbook(sfsuMajors)
    sheet = wb.sheet_by_index(0)

    for i in range(sheet.nrows):
        name = sheet.cell_value(i, 0)
        disciplines = sheet.cell_value(i, 1).split("; ")
        urls = sheet.cell_value(i, 2).split("; ")

        for i in range(0, len(urls)):
            urls[i] = urls[i] + "#degreerequirementstext"
            m = major(name, disciplines, urls)

        majors.append(m)
    return render_template('sfsu-major.html', title='SFSU Majors', majors=majors)


@app.route("/ucsd")  # sfsu majors
def ucsdMajor():
    class major:
        def __init__(self, name, disciplines, urls):
            self.name = name
            self.disciplines = disciplines
            self.urls = urls

    loc = ('ucsd.xlsx')  # list of sfsu majors
    majors = []
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    count = 13436

    for i in range(sheet.nrows):
        name = sheet.cell_value(i, 0)
        disciplines = sheet.cell_value(i, 1).split("; ")
        urls = sheet.cell_value(i, 2).split("; ")

        m = major(name, disciplines, urls)
        majors2 = majors.copy()

        majors.append(m)
    return render_template('ucsd-major.html', title='University of California, San Diego', majors=majors)

@app.route("/syracuse")  # sfsu majors
def syrMajor():
    class major:
        def __init__(self, name, disciplines, urls):
            self.name = name

            self.disciplines = disciplines
            self.urls = urls

    loc = ('syr.xlsx')  # list of sfsu majors
    majors = []
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)


    majors.append(m)
    return render_template('sfsu-major.html', title='SFSU Majors', majors=majors)

if __name__ == '__main__':  # used to be able to run Flaskblog.py through terminal
    app.run(debug=True) 
