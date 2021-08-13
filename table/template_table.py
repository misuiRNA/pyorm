from sqlalchemy import Column, Integer, JSON, Boolean

from base.base_table import Base


class TemplateTable(Base):
    __tablename__ = "simple_template_model"

    id = Column(Integer(), name="id", primary_key=True)
    is_deleted = Column(Boolean(), nullable=False, default=False)
    status = Column(Integer(), default=int(0))
    doc_type_id = Column(Integer(), comment="文档类型")
    config = Column(JSON(), default={})
