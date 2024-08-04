class Logger():
    def __init__(self):
        self.messages = dict()
        self.timestamp = 0

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages or self.messages[message] <= timestamp:
            self.timestamp = timestamp
            self.messages[message] = timestamp + 10
            return True
        else:
            return False

    def clean(self, timestamp: int) -> bool:
        if self.timestamp < timestamp:
            self.messages.clear()
            self.timestamp = 0
            return True
        else:
            return False

    def loggerSize(self) -> int:
        return len(self.messages)