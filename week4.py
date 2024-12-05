mydic = {"aisyah":"berr","ali":"berg"}

print(mydic["aisyah"])

mydic2 = {"banana":100, "Apple":350}
mydic3 = {1:2,3:4,2:3.45}
menu = {"nasi lemak": 3.00, "milo ais":1.50}
mytrans = {"one":"satu", "two":"dua"}

print("RM" ,menu["nasi lemak"])
print(menu)

del menu["milo ais"]
print(menu)
menu["nasi lemak"] -= 2.5
print(menu)

menu2 = menu.copy

menu2 = menu
print(menu2)
menu2["nasi lemak"] += 2.5
print(menu)
print(menu2)