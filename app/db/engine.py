# Creates a database engine

import json
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert

from app.db import settings
from app.db.models import metadata_table

def create_db_uri():
    return settings.SQLALCHEMY_DATABASE_URI

def create_engine_and_session():
    engine = create_engine(
        url=create_db_uri()
        )
    return engine


def insert_metadata(user_id: str, 
                    contract_name: str, 
                    metadata: dict,
                    contract_url: Optional[str], 
                    ):
    engine = create_engine_and_session()
    stmt = insert(metadata_table).values(
        user_id=user_id,
        contract_name=contract_name,
        metadata=json.dumps(metadata),
        contract_url=contract_url
    )
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()