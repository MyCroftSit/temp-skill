from mycroft import MycroftSkill, intent_file_handler


class Temp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('temp.intent')
    def handle_temp(self, message):
        self.speak_dialog('temp')


def create_skill():
    return Temp()

