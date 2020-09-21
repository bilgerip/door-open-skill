from mycroft import MycroftSkill, intent_file_handler


class DoorOpen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('open.door.intent')
    def handle_open_door(self, message):
        self.speak_dialog('open.door')


def create_skill():
    return DoorOpen()

