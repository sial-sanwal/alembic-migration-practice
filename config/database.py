from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL="postgresql://neondb_owner:npg_W9Hcd3BNuftA@ep-tiny-union-a8pp7989-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
engine= create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)