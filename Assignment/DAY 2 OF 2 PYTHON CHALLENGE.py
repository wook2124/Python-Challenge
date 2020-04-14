days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", "Wed" in days)

print("The fourth item in 'days' is:", days[3])

days.append("Sat")
print(days)

days.remove("Mon")
print(days)
