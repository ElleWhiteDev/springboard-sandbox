from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import *
from forms import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    """Render home page"""
    return render_template("home.html")


@app.route('/phones')
def list_phones():
    """Renders directory of employees and phone numbers  (from dept)"""
    emps = Employee.query.all()
    return render_template('phones.html', emps=emps)


@app.route("/snacks/new", methods=["POST", "GET"])
def add_snack():
    """Snack add form; handle adding"""
    form = AddSnackForm()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        flash(f"Created new snack! Name is {name} and price is ${price}")
        return redirect("/")
    else:
        return render_template("add_snack_form.html", form=form)


@app.route("/employees/new", methods=["GET", "POST"])
def add_employee():
    """Add new employee form"""
    form = EmployeeForm()
    depts = db.session.query(Department.dept_code, Department.dept_name).all()
    form.dept_code.choices = depts

    if form.validate_on_submit():
        name = form.name.data
        state = form.state.data
        dept_code = form.dept_code.data

        emp = Employee(name=name, state=state, dept_code=dept_code)
        db.session.add(emp)
        db.session.commit()

        return redirect("/phones")
    else:
        return render_template("add_employee_form.html", form=form)


@app.route("/employees/<int:id>/edit", methods=["GET", "POST"])
def edit_employee(id):
    emp = Employee.query.get_or_404(id)
    form = EmployeeForm(obj=emp)
    depts = db.session.query(Department.dept_code, Department.dept_name).all()
    form.dept_code.choices = [(d[0], d[1]) for d in depts]

    if form.validate_on_submit():
        emp.name = form.name.data
        emp.state = form.state.data
        emp.dept_code = form.dept_code.data
        db.session.commit()
        return redirect("/phones")
    else:
        return render_template("edit_employee_form.html", form=form)
