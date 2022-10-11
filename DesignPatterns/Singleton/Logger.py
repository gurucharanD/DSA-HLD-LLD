# Double Checked Locking singleton pattern
import threading


class Logger:

	# resources shared by each and every
	# instance

	__singleton_instance = None

	# define the classmethod
	@classmethod
	def instance(cls):

		# check for the singleton instance
		if not cls.__singleton_instance:
			with threading.Lock():
				if not cls.__singleton_instance:
					cls.__singleton_instance = cls()

		# return the singleton instance
		return cls.__singleton_instance
