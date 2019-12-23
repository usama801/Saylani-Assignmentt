class Car():
    def __init__(self,model,color,company_name,speed,fuel_capacity):
        self.model = model
        self.color = color
        self.company_name = company_name
        self.speed = speed
        self.fuel_capacity = fuel_capacity


    def Change_Car_Color(self,changed_color):
        self.color = changed_color

    def Change_Car_Model_Company(self,changed_model,changed_company):
        self.model = changed_model
        self.company_name = changed_company

    def Change_Car_Speed(self,changed_speed):
        self.speed = changed_speed

#Before Updating Car

Car1 = Car('A5','Black','Audi',500,120)
print("\tBEFORE UPDATING \n\nModel Name :-",Car1.model,"\nColor :- ",Car1.color,"\nCompany :- ",Car1.company_name,"\nSpeed :- ",Car1.speed," Km/h\nFuel Capacity :- ",Car1.fuel_capacity," Litre\n\n")

# After Updating Car

Car1.Change_Car_Color('White')
Car1.Change_Car_Model_Company('1.8','Corolla')
Car1.Change_Car_Speed(220)
print("\tAFTER UPDATING \n\nModel Name :-",Car1.model,"\nColor :- ",Car1.color,"\nCompany :- ",Car1.company_name,"\nSpeed :- ",Car1.speed," Km/h\nFuel Capacity :- ",Car1.fuel_capacity," Litre\n\n")

#Another 4 Objects of Car Class

Car2 = Car('Mehran','Blue','Suzuki',180,30)
Car3 = Car('Cultus','White','Suzuki',180,40)
Car4 = Car('Civic','Gun Metallic','Honda',320,70)
Car5 = Car('Alto','Half White','Suzuki',140,20)

print("\tCAR 2 \n\nModel Name :-",Car2.model,"\nColor :- ",Car2.color,"\nCompany :- ",Car2.company_name,"\nSpeed :- ",Car2.speed," Km/h\nFuel Capacity :- ",Car2.fuel_capacity," Litre\n\n")
print("\tCAR 3 \n\nModel Name :-",Car3.model,"\nColor :- ",Car3.color,"\nCompany :- ",Car3.company_name,"\nSpeed :- ",Car3.speed," Km/h\nFuel Capacity :- ",Car3.fuel_capacity," Litre\n\n")
print("\tCAR 4 \n\nModel Name :-",Car4.model,"\nColor :- ",Car4.color,"\nCompany :- ",Car4.company_name,"\nSpeed :- ",Car4.speed," Km/h\nFuel Capacity :- ",Car4.fuel_capacity," Litre\n\n")
print("\tCAR 5 \n\nModel Name :-",Car5.model,"\nColor :- ",Car5.color,"\nCompany :- ",Car5.company_name,"\nSpeed :- ",Car5.speed," Km/h\nFuel Capacity :- ",Car5.fuel_capacity," Litre\n\n")
