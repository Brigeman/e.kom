import requests

# URL for form
save_form_url = "http://localhost/save_form_template"

# URL for get
get_form_url = "http://localhost/get_form"

# test
save_data = {
    "template_name": "TestForm",
    "fields": {
        "email": {"field_type": "email"},
        "phone": {"field_type": "phone"},
        "text_field": {"field_type": "text"},
        "date_field": {"field_type": "date"}
    }
}

# test
get_data = {
    "data": {
        "email": "test@example.com",
        "phone": "+1234567890",
        "text_field": "This is a text field",
        "date_field": "2023-11-19"
    }
}

# Executing a POST request to save a form
save_response = requests.post(save_form_url, json=save_data)
print("Save Form Response:", save_response.json())

# Executing a POST request to retrieve a form
get_response = requests.post(get_form_url, json=get_data)
print("Get Form Response:", get_response.json())
