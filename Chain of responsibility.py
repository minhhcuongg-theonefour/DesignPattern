from abc import ABCMeta, abstractclassmethod

class IHandler(metaclass=ABCMeta):
    def handle(self, request):
        "Interface"

    def processRequest(self, request):
        "Interface"

class AbstractHandler(IHandler):

	def __init__(self, next_):

		self._next = next_

	def handle(self, request):

		handled = self.processRequest(request)

		if not handled:
			self._next.handle(request)

	def processRequest(self, request):

		raise NotImplementedError('First implement it !')


class FirstHandler(AbstractHandler):

	def processRequest(self, request):

		if 'a' <= request <= 'e':
			print("{} handling request '{}'".format(self.__class__.__name__, request))
			return True


class SecondHandler(AbstractHandler):

	def processRequest(self, request):

		if 'e' < request <= 'l':
			print("{} handling request '{}'".format(self.__class__.__name__, request))
			return True

class ThirdHandler(AbstractHandler):

	def processRequest(self, request):

		if 'l' < request <= 'z':
			print("{} handling request '{}'".format(self.__class__.__name__, request))
			return True

class DefaultHandler(AbstractHandler):

	def processRequest(self, request):

		print("{} telling you that request '{}' has no handler right now.".format(self.__class__.__name__, request))
		return True


class User:

	def __init__(self):

		a = None
		self.handler = FirstHandler(SecondHandler(ThirdHandler(DefaultHandler(a))))

	def agent(self, user_request):

		for request in user_request:
			self.handler.handle(request)


if __name__ == "__main__":

	user = User()

	string = input("Nhap chuoi:")
	requests = list(string)
	user.agent(requests)
