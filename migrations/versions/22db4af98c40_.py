"""empty message

Revision ID: 22db4af98c40
Revises: 
Create Date: 2017-12-09 02:47:24.033273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22db4af98c40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.Column('isbn', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_students_email'), 'students', ['email'], unique=True)
    op.create_index(op.f('ix_students_first_name'), 'students', ['first_name'], unique=False)
    op.create_index(op.f('ix_students_last_name'), 'students', ['last_name'], unique=False)
    op.create_index(op.f('ix_students_username'), 'students', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_username'), table_name='students')
    op.drop_index(op.f('ix_students_last_name'), table_name='students')
    op.drop_index(op.f('ix_students_first_name'), table_name='students')
    op.drop_index(op.f('ix_students_email'), table_name='students')
    op.drop_table('students')
    op.drop_table('groups')
    op.drop_table('departments')
    op.drop_table('books')
    # ### end Alembic commands ###