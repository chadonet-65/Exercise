class Robot:
    def __init__(self,name,build_year):
        self.__name = name
        self.__build_year = build_year

    def hi(self):
        if self.__name:
            print("Hello I am ",self.__name)
        else:
            print("Hello I am a robot s n")
        if self.__build_year:
            print("I have a ",self.__build_year)
        else:
            print("I do not have a age of construction")
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_build_year(self,build_year):
        self.__build_year = build_year
    def get_build_year(self):
        return self.__build_year
if __name__ == "__main__":
    x = Robot("Marvin",45)
    x.set_name("Henri")
    x.hi()