import pyrebase

class UpdateDB:
    
    config = {
    "apiKey": "AIzaSyBOc7fqbr_KhBYxsiAoxj_4sSR1zp3tatw",
    "authDomain": "past-papers-87cef.firebaseapp.com",
    "databaseURL": "https://past-papers-87cef.firebaseio.com",
    "projectId": "past-papers-87cef",
    "storageBucket": "past-papers-87cef.appspot.com",
    "serviceAccount": "/Users/ibraaheem/workspace/personal/temp/paperbot/backend/utils/past-papers-87cef-firebase-adminsdk-6p4e4-76ea8284ad.json"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    def send(self, data):
        self.db.child("papers").set(data)