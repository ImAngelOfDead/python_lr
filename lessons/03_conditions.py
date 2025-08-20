age = int(input("Сколько тебе лет? "))

if age < 12:
    print("pizduk")
elif 12 <= age < 18:
    print("vse ravno pizduk")
elif 18 <= age < 65:
    print("ne pizduk")
else:
    print("pesok ebuchi ")
