from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import  SQLAlchemy
from models import db_session, table, Employee
from schema import schema, Department
from flask import render_template,request, redirect, flash
from sqlalchemy import *


app = Flask(__name__)
app.debug = True
db = SQLAlchemy(app)


@app.route("/employee")
def listAllEmployee():
    employees = db_session.query(Employee).all();

    table.border = True
    return render_template("employeelist.html", myEmployee=employees)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()