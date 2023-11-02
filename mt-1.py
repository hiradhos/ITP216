class Dessert():
    def __init__(self, name_param = "ice cream"):
        self.name = name_param
    def get_name(self):
        return self.name
    def set_name(self, new_name = "ice cream"):
        self.name = new_name
    def __str__(self):
        return f"The dessert type is {self.name}."

class IceCream(Dessert):
    def __init__(self, name_param, flavor_param = "Vanilla"):
        super().__init__(name_param)
        self.flavor = flavor_param
    def get_flavor(self):
        return self.flavor
    def set_flavor(self, new_flavor = "Vanilla"):
        self.flavor = new_flavor
    def __str__(self):
        return f"The dessert type is {self.name} and its flavor is {self.flavor}"

def main():
    dessert_object = Dessert()
    print(dessert_object.get_name())
    dessert_object.set_name("cookie")
    print(dessert_object.get_name())
    print(dessert_object)
    print()
    icecream_object = IceCream("ice cream")
    print(icecream_object.get_name())
    print(icecream_object.get_flavor())
    icecream_object.set_name("cookie")
    icecream_object.set_flavor("Chocolate")
    print(icecream_object)

if __name__ == "__main__":
    main()