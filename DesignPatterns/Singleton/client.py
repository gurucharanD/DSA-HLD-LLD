# logger implementation using singleton design pattern
from Logger import Logger

logger1 = Logger()
print(Logger.__singleton_instance)

logger2 = Logger()
print(Logger.__singleton_instance)

