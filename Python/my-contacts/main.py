from fastapi import FastAPI, HTTPException
from uuid import uuid4
from pydantic import BaseModel

from src.lib.managedb import Managebd

class ContactModel(BaseModel):
    id: str = str(uuid4())
    name: str
    phone: str

app = FastAPI()
md = Managebd()

@app.get("/")
def root():
    return {'Message': 'Server Online'}

@app.get("/api/contacts")
def get_all_contacts():
    return md.read_contact()

@app.get("/api/contacts/{id_contact}")
def get_contact(id_contact: str):
    contacts = md.read_contact()
    for contact in contacts:
        if contact["id"] == id_contact:
            return contact
    raise HTTPException(
        status_code=404,
        detail=f'Contact {id_contact} not found'
    )
    
@app.post("/api/contacts")
def add_contact(new_contact: ContactModel):
    contacts = md.read_contact()
    contacts.append(new_contact.dict())
    md.write_contact(contacts)
    
    return {
        "Success": True,
        "Message": "Added new contact",
        "id": new_contact
    }
    
    
@app.put("/api/contacts/{id_contact}")
def update_contact(id_contact: str, new_contact: ContactModel):
    contacts = md.read_contact()
    
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts[index] = new_contact.dict()
            
            if new_contact.name == "":
                contacts[index]["name"] = contact["name"]
                
            if new_contact.phone == "":
                contacts[index]["phone"] = contact["phone"]
                
            # Escribir los cambios en la base de datos
            md.write_contact(contacts)
            
            # Devolver un mensaje de éxito
            return {
                "Success": True,
                "Message": "Contact updated"
            }
    # Si no se encuentra el contacto con el ID proporcionado, lanzar una excepción
    raise HTTPException(
        status_code=404,
        detail="Contact not found"
    )


@app.delete("/api/contacts/{id_contact}")
def remove_contact(id_contact: str):
    contacts = md.read_contact()
    for index, contact in enumerate(contacts):
        if contact["id"] == id_contact:
            contacts.pop(index)
            
            md.write_contact(contacts)
        
            return {
                "Success": True,
                "Message": "Delete contact"
            }
        
    raise HTTPException (
        status_code=404,
        detail="Contact NOT Found"
    )