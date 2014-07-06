from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
job = Table('job', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=40)),
    Column('desc', String(length=200)),
    Column('completed', Boolean, default=ColumnDefault(False)),
    Column('date', DateTime),
    Column('building', String(length=15)),
    Column('room', String(length=5)),
    Column('type', String(length=15)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['job'].columns['building'].create()
    post_meta.tables['job'].columns['room'].create()
    post_meta.tables['job'].columns['type'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['job'].columns['building'].drop()
    post_meta.tables['job'].columns['room'].drop()
    post_meta.tables['job'].columns['type'].drop()
