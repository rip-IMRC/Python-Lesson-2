class India:
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language in India")
    def type(self):
        print("India is a developing country")
class USA:
    def capital(self):
        print("Washington, D. C. is the capital of USA")
    def language(self):
        print("English is the primary language in USA")
    def type(self):
        print("USA is a developed country")
obj_Ind=India()
obj_USA=USA()
for country in (obj_Ind, obj_USA):
    country.capital()
    country.language()
    country.type()