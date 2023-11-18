from pydantic import BaseModel
from typing import Dict

# Create models
class FormField(BaseModel):
    field_type: str

# Модель для описания шаблона формы
class FormTemplate(BaseModel):
    template_name: str
    fields: Dict[str, FormField]
