from app.cfg import settings
import databases


database = databases.Database(settings.database_url)
