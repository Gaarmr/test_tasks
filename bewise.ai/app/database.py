from databases import Database

from .settings import settings


database = Database(settings.database_url)
