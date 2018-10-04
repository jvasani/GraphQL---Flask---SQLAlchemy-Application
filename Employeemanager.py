from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from models import Employee
import paginate
import paginate_sqlalchemy
import sqlalchemy_paginate
import flask_paginate
from models import db_session, Employee
from flask_json import *
from flask import render_template
from schema import schema
from flask_paginate import Pagination, get_page_parameter


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

app.debug = True
db = SQLAlchemy(app)

app.config['JSON_ADD_STATUS'] = False


@app.route("/employees")
@app.route("/employees/<int:index>")
def listAllEmployee():
    page = request.args.get('page', 1, type=int)
    employees = db_session.query(Employee.EmpID, Employee.EmployeeName, Employee.Department,
                                 Employee.Salary).all() # type: object

    page = request.args.get(get_page_parameter(), type=int, default=1)

    pagination = Pagination(page=page)
    print page

    empdata = []
    elist = {}

    for row in employees[:50]:
        data = list(row)
        #result.update(json.dumps(data, ensure_ascii=False, indent=4))
        elist["id"] = data[0]
        elist["name"] = data[1]
        elist["department"] = data[2]
        elist["salary"] = data[3]

        empdata.append(json.dumps(elist, skipkeys=False, ensure_ascii=True,
                                  check_circular=True, allow_nan=True, cls=None,
                                  indent=None, separators=None, encoding='utf-8',
                                  default=None, sort_keys=False) )

    print json.dumps(empdata)
    return render_template("employeelist.html", allEmployee=json.dumps(empdata), pagination=pagination)



app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        graphiql=True,
        schema=schema  # for having the GraphiQL interface
    )
)


@app.teardown_appcontext
def shutdown_session():
    db_session.remove()


if __name__ == '__main__':
    app.run()
