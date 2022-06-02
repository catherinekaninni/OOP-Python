class Student:
    school="AkiraChix"
    def __init__(self,firstname,lastname,age,country):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country
    
    def greet(self):
        return f"Hello {self.firstname} welcome to {self.school} you are from {self.country}"
    def fullname(self):
            name=f"{self.firstname} {self.lastname}"
            return name
    def year_of_birth(self):
        year_of_birth=self.age
        return year_of_birth
    def initials(self):
        t=f"{self.firstname} {self.lastname}"
        z=t.upper()
        return z
    


        
    

        