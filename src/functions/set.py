from ..services.firebase import db

def setData(name, message, email):
  data = {"name": name,"message": message,"email": email}
  db.child("contacts").push(data)

  return data