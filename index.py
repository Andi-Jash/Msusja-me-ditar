user_dict = {}

num_entry = int(input("Shkruaj numrin e nxenseve: "))
for x in range(num_entry):
    key = input("Enter key: ")
    value = input("Enter value: ")

    try:
        value = int(value)
    except ValueError:
        pass
    user_dict[key] = value

shuma = sum(user_dict.values())
mesatarja =int( shuma / len(user_dict))
print("Piket minimale jane", min(user_dict.values()))
print("Piket maksimale jane", max(user_dict.values()))
print(f"Piket mesatare jane {mesatarja}")

kan_kaluar = {}
nuk_kan_kaluar = {}
for key, value in user_dict.items():
    if value >= 60:
        kan_kaluar[key] = value
    else:
        nuk_kan_kaluar[key] = value
for i in kan_kaluar:
    print(i, kan_kaluar[i])
for i in nuk_kan_kaluar:
    print(i, nuk_kan_kaluar[i])