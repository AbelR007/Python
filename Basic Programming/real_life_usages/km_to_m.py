# Converting KM to Metres
# =================================================
def convert_km_to_m(km):
    return km * 1000

x = int(input("Enter km : "))
print(f"Converting {x} km to {convert_km_to_m(x)} m")
