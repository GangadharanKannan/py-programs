a = {
    "name":"ganga",
    "age": 21
}

print(a)
print(a["name"])
print(a.get("age"))

a["blood-group"] = "O+ve"
print(a)

print(a.keys())
print(a.values())
print(a.items())

print(a.pop("age"))
print(a)

a.clear()
print(a)