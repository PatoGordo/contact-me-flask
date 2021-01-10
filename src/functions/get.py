from ..services.firebase import db

def getData():
  contacts = []
  all_contacts = db.child("contacts").get()
  for contact in all_contacts.each():
    contacts.append(contact.val())

  return { "status": 200, "Message": "Get data successfully", "results": contacts }
