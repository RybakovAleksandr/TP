from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        return 'You have created a Windows button.'

class MacButton(Button):
    def paint(self):
        return 'You have created a Mac button.'
    
class LinuxButton(Button):
    def paint(self):
        return 'You have created a Linux button.'

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsCheckbox(Checkbox):
    def paint(self):
        return 'You have created a Windows checkbox.'

class MacCheckbox(Checkbox):
    def paint(self):
        return 'You have created a Mac checkbox.'
    
class LinuxCheckbox(Checkbox):
    def paint(self):
        return 'You have created a Linux checkbox.'
    
class GUIFactory(ABC):
    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass

class WindowsFactory(GUIFactory):
    def createButton(self) -> Button:
        return WindowsButton()
    
    def createCheckbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory (GUIFactory):
    def createButton(self) -> Button:
        return MacButton()
    
    def createCheckbox(self) -> Checkbox:
        return MacCheckbox()
    
class LinuxFactory (GUIFactory):
    def createButton(self) -> Button:
        return LinuxButton()
    
    def createCheckbox(self) -> Checkbox:
        return LinuxCheckbox()

class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.createButton()
        self.checkbox = factory.createCheckbox()
    
    def paint(self):
        return self.button.paint(), self.checkbox.paint()


app1 = Application(WindowsFactory())
print(app1.paint())

app2 = Application(MacFactory())
print(app2.paint())

app3 = Application(LinuxFactory())
print(app3.paint())