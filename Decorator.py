from abc import ABCMeta, abstractclassmethod


class IText(metaclass=ABCMeta):

    def __init__(self, text):      
        self.text =  text

    @abstractclassmethod
    def text_method():
        "Interface"

class WriteText(IText):

    def text_method(self):
        return self.text


class Decorator(IText):
    def __init__(self, wtext):
        super().__init__(text)
        self._wtext = wtext

    def text_method(self):
        return self._wtext.text_method()


class InDam(Decorator):

    def text_method(self):
        return "{} + In dam".format(self._wtext.text_method())


class InNghieng(Decorator):

    def text_method(self):
        return "{} + In Ngieng".format(self._wtext.text_method())


class InGachNang(Decorator):

    def text_method(self):
        return "{} + In gach ngang".format(self._wtext.text_method())


text = WriteText("Bach")
print( text.text_method())

text1 = InDam(text)
text2 = InNghieng(text1)
text3 = InGachNang(text2)
print(text3.text_method())

text3 = InGachNang(text)
print(text3.text_method())