from abc import ABC, abstractmethod


class Pizza:
    def setDough(self, dough: str):
        self.dough = dough

    def setSauce(self, sauce: str):
        self.sauce = sauce
    
    def setTopping(self, topping: str):
        self.topping = topping
    
    def __str__(self):
        return "Pizza{" + \
                "dough='" + self.dough + '\'' + \
                ", sauce='" + self.sauce + '\'' + \
                ", topping='" + self.topping + '\'' + \
                '}'

class PizzaBuilder(ABC):
    @abstractmethod
    def buildDough(self):
        pass

    @abstractmethod
    def buildSauce(self):
        pass

    @abstractmethod
    def buildTopping(self):
        pass

    @abstractmethod
    def getResult(self) -> Pizza:
        pass

class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    
    def buildDough(self):
        self.pizza.setDough('cross')

    def buildSauce(self):
        self.pizza.setSauce("mild")

    def buildTopping(self):
        self.pizza.setTopping("ham+pineapple")
    
    def getResult(self) -> Pizza:
        return self.pizza
    
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder
    
    def constructPizza(self):
        self.builder.buildDough()
        self.builder.buildSauce()
        self.builder.buildTopping()
    
builder = HawaiianPizzaBuilder()
director = PizzaDirector(builder)

director.constructPizza()
pizza = builder.getResult()
print(pizza)

 
    