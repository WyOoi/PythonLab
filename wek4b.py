mydic = {"aisyah":"berr","ali":"berg"}

print(mydic["aisyah"])

mydic2 = {"banana":100, "Apple":350}
mydic3 = {1:2,3:4,2:3.45}
menu = {"tomyam": 3.00, "nasi lemak":1.50, "milo ais":1.50, "mee goreng":5.50, "ayam goreng":2.50}
mytrans = {"one":"satu", "two":"dua"}

print(menu)
menu_sort = list(menu.keys())
menu_sort.sort()
print(menu_sort)

sort_comb = {i: menu[i] for i in menu_sort}
print(sort_comb)