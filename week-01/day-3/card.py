# A simple script that prints an ASCII terminal business card using f-strings

name = "Saba"
track = "ALPHA - Agentic AI"
city = "Tehran"
motto = "Small commits , big progress.."

width = 44

print("+" + "-" * width + "+")
print(f"| Name  : {name:<34} |")
print(f"| Track : {track:<34} |")
print(f"| City  : {city:<34} |")
print(f"| Motto : {motto:<34} |")
print("+" + "-" * width + "+")

