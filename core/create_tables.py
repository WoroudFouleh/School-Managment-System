from core.database import engine
from core.base import Base

print(" Creating tables...")
Base.metadata.create_all(bind=engine)
print(" Tables created successfully!")
