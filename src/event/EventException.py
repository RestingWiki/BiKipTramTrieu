class EventException(Exception):

    def __init__(self, message: str = 'error occurred'):
        self.message = message
        super().__init__(self.message)


class SkillEventException(EventException):

    def __init__(self, _type: str):
        super().__init__(_type)
