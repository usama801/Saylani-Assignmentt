cities = {
    "Multan": {
            "Country" : "Pakistan",
            "Population" :  233916,
            "Fact" : "Also Known as City of Saints"
            },
    
    "Hyderabad": {
            "Country" : "Pakistan",
            "Population" : 1732693,
            "Fact" : "The city is famous for its winds which moderate the otherwise hot climate."
            },
    
    "Karachi": {
            "Country" : "Pakistan",
            "Population" : 15741000,
            "Fact" : "There are plenty of things to do in Karachi from the beaches to the best local sights, from great food to the soothing environment."
            }
         }
i = 1

for key, value in cities.items():    
    print(i,"City Details \n")
    print(key,value,"\n")
    i = i + 1

