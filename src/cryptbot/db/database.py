# db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from ..config.config import Config

# Create engines
default_engine = create_engine(Config.SQLITE_DATABASE_PATH)
knowledge_base_engine = create_engine(Config.DUCKDB_DATABASE_PATH)

# Create session makers
DefaultSession = sessionmaker(bind=default_engine)
KnowledgeBaseSession = sessionmaker(bind=knowledge_base_engine)

# Base classes
DefaultBase = declarative_base()
KnowledgeBaseBase = declarative_base()
