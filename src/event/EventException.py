class EventException(Exception):

    def __init__(self, message: str = 'error occurred'):
        self.message = message
        super().__init__(self.message)


class SkillEventException(EventException):

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class NoSkillException(EventException):

    def __init__(self, message: str = 'error in skill'):
        self.message = message
        super().__init__(message)
