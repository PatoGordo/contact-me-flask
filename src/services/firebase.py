import pyrebase

config = {
  "apiKey": "AIzaSyCeLPgM8XD0RyPA3c4CdmO-Eg8y2LuY4xM",
  "authDomain": "contact-me-pg.firebaseapp.com",
  "databaseURL": "https://contact-me-pg-default-rtdb.firebaseio.com",
  "storageBucket": "contact-me-pg.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()