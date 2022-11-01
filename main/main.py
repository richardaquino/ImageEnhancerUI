from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class SentiSnap(MDApp):
    Window.size = (310, 580)

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("forgot.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("terms.kv"))

        return screen_manager

    def signup(self):
        signup = self.root.get_screen('signup')

        signupEmail = signup.ids.signup_email.text
        signupFullname = signup.ids.signup_fullname.text
        signupMobile = signup.ids.signup_mobile.text
        signupBirthday = signup.ids.signup_birthday.text
        signupPassword = signup.ids.signup_password.text

        # if signupEmail.split() == [] or signupUsername.split() == [] or signupPassword.split() == []:
        #     cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
        #     self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
        #                            buttons=[cancel_btn_username_dialogue])
        #     self.dialog.open()
        # if len(signupUsername.split()) > 1:
        #     cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
        #     self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
        #                            size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
        #     self.dialog.open()
        # else:
        print(signupEmail, signupFullname, signupMobile, signupBirthday, signupPassword)

    def login(self):
        login = self.root.get_screen('login')
        print(login.ids.login_username.text)
        print(login.ids.login_password.text)

    def close_username_dialog(self, obj):
        self.dialog.dismiss()

    def splash(self, *args):
        screen_manager.current = "login"

    def on_start(self):
        Clock.schedule_once(self.splash, 5)


if __name__ == "__main__":
    SentiSnap().run()
