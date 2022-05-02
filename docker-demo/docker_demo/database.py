from databases import Database

from docker_demo.settings import settings


database = Database(settings.database_url)
