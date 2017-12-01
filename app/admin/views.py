from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import DepartmentForm, StudentAssignForm, GroupForm
from .. import db
from ..models import Department, Student, Group


def check_admin():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)


# Department Views


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')

        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))

    return render_template(title="Delete Department")


# Group Views


@admin.route('/groups')
@login_required
def list_groups():
    check_admin()
    """
    List all groups
    """
    groups = Group.query.all()
    return render_template('admin/groups/groups.html',
                           groups=groups, title='Groups')


@admin.route('/groups/add', methods=['GET', 'POST'])
@login_required
def add_group():
    """
    Add a group to the database
    """
    check_admin()

    add_group = True

    form = GroupForm()
    if form.validate_on_submit():
        group = Group(name=form.name.data,
                      description=form.description.data)
        try:
            # add group to the database
            db.session.add(group)
            db.session.commit()
            flash('You have successfully added a new group.')
        except:
            # in case group name already exists
            flash('Error: group name already exists.')

        # redirect to the groups page
        return redirect(url_for('admin.list_groups'))

    # load group template
    return render_template('admin/groups/group.html', add_group=add_group,
                           form=form, title='Add Group')


@admin.route('/groups/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_group(id):
    """
    Edit a group
    """
    check_admin()

    add_group = False

    group = Group.query.get_or_404(id)
    form = GroupForm(obj=group)
    if form.validate_on_submit():
        group.name = form.name.data
        group.description = form.description.data
        db.session.add(group)
        db.session.commit()
        flash('You have successfully edited the group.')

        # redirect to the groups page
        return redirect(url_for('admin.list_groups'))

    form.description.data = group.description
    form.name.data = group.name
    return render_template('admin/groups/group.html', add_group=add_group,
                           form=form, title="Edit Group")


@admin.route('/groups/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_group(id):
    """
    Delete a group from the database
    """
    check_admin()

    group = Group.query.get_or_404(id)
    db.session.delete(group)
    db.session.commit()
    flash('You have successfully deleted the group.')

    # redirect to the groups page
    return redirect(url_for('admin.list_groups'))

    return render_template(title="Delete Group")


# Student Views

@admin.route('/students')
@login_required
def list_students():
    """
    List all students
    """
    check_admin()

    students = Student.query.all()
    return render_template('admin/students/students.html',
                           students=students, title='Students')


@admin.route('/students/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_student(id):
    """
    Assign a department and a group to an student
    """
    check_admin()
    student = Student.query.get_or_404(id)

    # prevent admin from being assigned a department or group
    if student.is_admin:
        abort(403)

    form = StudentAssignForm(obj=student)
    if form.validate_on_submit():
        student.department = form.department.data
        student.group = form.group.data
        db.session.add(student)
        db.session.commit()
        flash('You have successfully assigned a department and group.')

        # redirect to the group page
        return redirect(url_for('admin.list_students'))

    return render_template('admin/students/student.html',
                           student=student, form=form,
                           title='Assign Student')
