from app.cfg import settings
import databases
import ormar
import sqlalchemy


database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Devices(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'devices'

    id: int = ormar.Integer(primary_key=True, autoincrement=False)
    dev_id: int = ormar.String(max_length=256, unique=False, nullable=False)
    dev_type: str = ormar.String(max_length=256, unique=False, nullable=False)


class Endpoints(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'endpoints'

    id: int = ormar.Integer(primary_key=True, autoincrement=False)
    dev_id: int = ormar.String(max_length=256, unique=False, nullable=False)
    comment: str = ormar.String(max_length=256, unique=False, nullable=False)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
