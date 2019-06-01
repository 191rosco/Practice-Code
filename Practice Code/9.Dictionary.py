#Dictionary Practice

#Easy
#write a program to create a dictionary with 5 key-value pairs.

Motorbike_colors = {"CG125":"Blue", "DR600":"White/Blue", "DT125":"Black", "NXC125":"Grey", "TT600":"Red"}
Motorbike_colors["DR600"]

#Medium
#Update the value of a key.

Motorbike_colors["DT125"] = "Black/Blue"
Motorbike_colors["DT125"]

#Hard
#Copy this dictionary to another dictionary and clear the first dictionary.

Car_colors = {"allroad":"Black", "Combo":"Silver"}
print(Car_colors)
Car_colors = Motorbike_colors.copy()
print(Car_Colors)
Motorbike_colors.clear()
Motorbike_colors

#End
