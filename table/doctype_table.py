from sqlalchemy import Column, Integer, String
from sqlalchemy import text
from sqlalchemy.dialects import mysql
from config.my_session import Base


class DocTypeTable(Base):
    __tablename__ = "doc_type"

    id = Column(Integer(), name="id", primary_key=True)
    name = Column(String(255), name="name", nullable=False)
    desc = Column(String(255))
    create_time = Column(mysql.TIMESTAMP(), server_default=text('CURRENT_TIMESTAMP'), comment="创建时间")
    last_update_time = Column(mysql.TIMESTAMP(),
                              server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                              comment="上次更新时间")

