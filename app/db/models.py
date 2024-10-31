import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

# Creates sql alchemy model for the metadata
from sqlalchemy import Table, MetaData


metadata_obj = MetaData()

metadata_table = Table(
    'contract_metadata', 
    metadata_obj,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('user_id', String),
    Column('contract_url', String),
    Column('contract_name', String),
    Column('metadata', String),
)
