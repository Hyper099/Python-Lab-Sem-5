names = ["Amy", "Jonathan", "Riya", "Christopher", "Bob"]

fil_names = list(filter( lambda x: len(x) > 5, names))

print(fil_names)