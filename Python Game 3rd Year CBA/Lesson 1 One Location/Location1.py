print("You get to the (b)each")

choice = input("""
- Go to the (m)mountains
- Go to the (f)orest
""")

if choice == "m":
    print("You start climbing up...")
elif choice == "f":
    print("You wander into the trees...")
else:
    print("What? That's not an option")
