import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyByOBOCNBGcTv8Dj0AfEGy0ym4C65Y2Pkg",
    "databaseURL": "https://authdemo-9f37b.firebaseio.com/",
    "authDomain": "authdemo-9f37b.firebaseapp.com",
    "projectId": "authdemo-9f37b",
    "storageBucket": "authdemo-9f37b.appspot.com",
    "messagingSenderId": "242925489903",
    "appId": "1:242925489903:web:a2be4821aa5ab8cbaf151a",
    "measurementId": "G-NJGLV08EGS"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def signup_account(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Sign up successfully")
    except:
        print("Email already exist!")


def login_account(email, password):
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Log in success!")
        return True
    except:
        print("Invalid email or password!")
        return False
