from datetime import datetime as dt
from datetime import timedelta as delta
from sqlalchemy import Column, String,Text ,DateTime, Float, Integer, ForeignKey, Boolean, func, update
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship
from sqlalchemy.sql.type_api import STRINGTYPE
from sqlalchemy_utils import UUIDType
from pytz import timezone
import ulid
from common.database import Base, get_ulid, session,engine


class SyuppinItem(Base):
    __tablename__ = 'a_syuppin_item'
    mysql_charset = 'utf8mb4',
    mysql_collate = 'utf8mb4_unicode_ci'

    id = Column('id', Integer, primary_key=True)
    item_name = Column('item_name', String(256), nullable=True)
    price = Column('price', String(64),nullable=True)
    seller_name = Column('seller_name', String(50), nullable=True)
    image_url1 = Column('image_url1', Text, nullable=True)   
    url = Column('url', Text)
    site = Column('site', String(20), nullable=False)

    
Base.metadata.create_all(engine)
