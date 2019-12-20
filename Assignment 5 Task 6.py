def BoughtItems(boughted_items):
    print("The Items you bought are : ",boughted_items)

items = []
i = 1
start = True

print("Type exit if you have done Shopping.")
while start:
    print("Enter ",i," Item")
    bought_item = input()
    if bought_item == 'exit':
        break
    else:
        items.append(bought_item)
        i = i + 1
        
BoughtItems(items)
