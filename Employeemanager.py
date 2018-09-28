from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from models import db_session, Employee
from flask_json import *
from flask import render_template
from sqlalchemy import *
from schema import schema


app = Flask(__name__)
app.debug = True
db = SQLAlchemy(app)

app.config['JSON_ADD_STATUS'] = False


@app.route("/employee")
def listAllEmployee():
    employees = db_session.query(Employee.EmpID, Employee.EmployeeName, Employee.Department, Employee.JobTitle,
                                 Employee.Salary)  # type: object

    emp = {}

    for id in employees[:5]:
        for name in id:
            for dept in id:
                for salary in id:
                    emp["id"] = id[0]
                    emp["Name"] = name
                    emp["Department"] = dept
                    emp["Salary"] = salary
                    empdata = (json.dumps(emp, ensure_ascii=False, indent=4))
                    #print empdata
                    return render_template("employeelist.html", allEmployee=empdata)




app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        graphiql=True,
        schema=schema  # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()