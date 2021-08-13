from sqlalchemy import Column, Integer, String, Boolean

from base.base_table import Base


class DocTypeTable(Base):
    __tablename__ = "doc_type"

    id = Column(Integer(), name="id", primary_key=True)
    is_deleted = Column(Boolean(), nullable=False, default=False)
    name = Column(String(255), name="name", nullable=False)
    desc = Column(String(255))

