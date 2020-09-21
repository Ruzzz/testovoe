"""empty message

Revision ID: cb1379febdd1
Revises: 
Create Date: 2020-07-03 12:54:40.225014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb1379febdd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('balance', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    op.create_table('animals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('breed', sa.String(), nullable=True),
    sa.Column('alias', sa.String(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], name=op.f('fk_animals_owner_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_animals'))
    )
    op.create_index('ix_animals_owner_id', 'animals', ['owner_id'], unique=False)
    op.create_table('lot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('animal_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['animal_id'], ['animals.id'], name=op.f('fk_lot_animal_id_animals')),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], name=op.f('fk_lot_owner_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_lot')),
    sa.UniqueConstraint('owner_id', 'animal_id', name=op.f('uq_lot_owner_id'))
    )
    op.create_table('bet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('lot_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lot_id'], ['lot.id'], name=op.f('fk_bet_lot_id_lot')),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], name=op.f('fk_bet_owner_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bet')),
    sa.UniqueConstraint('owner_id', 'lot_id', name=op.f('uq_bet_owner_id'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bet')
    op.drop_table('lot')
    op.drop_index('ix_animals_owner_id', table_name='animals')
    op.drop_table('animals')
    op.drop_table('user')
    # ### end Alembic commands ###