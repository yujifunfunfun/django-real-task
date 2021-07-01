from sqlalchemy import Column, String,Text ,DateTime, Float, Integer, ForeignKey, Boolean, func, update
from common.database import Base, get_ulid, session,engine


class UrlList(Base):
    __tablename__ = 'url_list'
    mysql_charset = 'utf8mb4',
    mysql_collate = 'utf8mb4_unicode_ci'
    id = Column('id', Integer, primary_key=True)
    url_list = Column('url', Text)
  

Base.metadata.create_all(engine)
