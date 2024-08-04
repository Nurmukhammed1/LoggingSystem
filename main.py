from logger import Logger

logger = Logger()

print(logger.shouldPrintMessage(1, "foo"))  # True
print(logger.shouldPrintMessage(2, "bar"))  # True
print(logger.shouldPrintMessage(3, "foo"))  # False
print(logger.shouldPrintMessage(8, "bar"))  # False
print(logger.shouldPrintMessage(10, "foo")) # False
print(logger.shouldPrintMessage(11, "foo")) # True

print(logger.loggerSize())  # 2
print(logger.clean(11))     # False
print(logger.clean(12))     # True