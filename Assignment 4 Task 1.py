person_info = {"first_name": str(input("Enter First name Of person :- ")),
               "last_name" : str(input("Enter Last name Of person :- ")),
               "age": int(input("Enter age Of person :- ")),
               "city": str(input("Enter the city Of person :- "))
               }
print("\n Person Info Without Qualification Key/Value.\n")
print(person_info,"\n")

person_info["qualification"] = "Graduate"
print(" Person Info including Qualification Key/Value before Updating.\n")
print(person_info,"\n")

qualification = {"qualification" : "high academic level"}
person_info.update(qualification)
print(" Person Info After Updating Qualification key.\n")
print(person_info,"\n")


del person_info["qualification"]
print(" Person Info After Deleting Qualification Key.\n")
print(person_info)
