from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from ..models import Department, Group


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class GroupForm(FlaskForm):
    """
    Form for admin to add or edit a group
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class StudentAssignForm(FlaskForm):
    """
    Form for admin to assign departments and groups to students
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    group = QuerySelectField(query_factory=lambda: Group.query.all(),
                             get_label="name")
    submit = SubmitField('Submit')
