from sqlalchemy import Column, Integer, Boolean, String
from config.my_session import Base


class MarkTaskTable(Base):
    __tablename__ = "simple_template_mark_task"

    id = Column(Integer(), name="id", primary_key=True)
    is_deleted = Column(Boolean(), nullable=False, default=False)
    group_id = Column(Integer, name="group_id", comment="组id")
