from sqlalchemy import Column, Integer, Boolean, String
from config.my_session import Base


class MarkTaskGroupTable(Base):
    __tablename__ = "simple_template_mark_task_group"

    id = Column(Integer(), name="id", primary_key=True)
    name = Column(String(255), name="name", nullable=False)
    is_deleted = Column(Boolean(), nullable=False, default=False)
    doc_type_id = Column(Integer, name="doc_type_id", comment="文档类型")


