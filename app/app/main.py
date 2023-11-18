from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from app.models import FormTemplate

import uvicorn
import logging
import re

logger = logging.getLogger(__name__)

app = FastAPI()

# MongoDB connection setup
MONGO_URI = "mongodb://mongo:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["forms"]
collection = db["form_templates"]

class FormData(BaseModel):
    data: dict

@app.post("/save_form_template")
async def save_form_template(form_template: FormTemplate):
    logger.info("Received request to save_form_template")
    template_data = form_template.dict()

    # Save form template in MongoDB
    await collection.insert_one(template_data)
    logger.info("Saved form template successfully")
    return {"message": "Form template saved successfully"}

@app.post("/get_form")
async def get_form_data(formData: FormData):
    logger.info("Received request to get_form_data")
    received_data = formData.data

    # Search for a matching form template in the database
    matching_template = await find_matching_template(received_data)

    if matching_template:
        logger.info("Found matching template")
        return {"template_name": matching_template.template_name}
    else:
        logger.info("No matching template found")
        # Perform dynamic field type identification
        field_types = {}

        for key, value in received_data.items():
            # Pass both value and key as arguments to identify_field_type
            field_types[key] = identify_field_type(value, key)

        logger.info("Identified field types")
        return {"fields": field_types}

async def find_matching_template(received_data: dict) -> FormTemplate:
    logger.info("Finding matching template")
    async for template in collection.find({}):
        fields_match = True

        for key, value in template['fields'].items():
            if key not in received_data or value['field_type'] != identify_field_type(received_data[key], value['field_type']):
                fields_match = False
                break

        if fields_match:
            logger.info("Matching template found")
            return FormTemplate(**template)

    logger.info("No matching template found")
    return None

def identify_field_type(value, field_type):
    logger.info("Identifying field type")
    if field_type == "email":
        return "email" if re.match(r"[^@]+@[^@]+\.[^@]+", value) else "text"
    elif field_type == "phone":
        return "phone" if re.match(r"\+\d{10,14}", value) else "text"
    elif field_type == "date":
        return "date" if re.match(r"\d{4}-\d{2}-\d{2}|\d{2}\.\d{2}\.\d{4}", value) else "text"
    else:
        return "text"



if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0", port=80)
    except Exception as e:
        logger.exception("Unhandled exception: %s", e)
