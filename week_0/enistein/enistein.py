def main():
#Receive the mass and convert it to int
    mass = int(input("please enter the mass : (kg)"))
    print(energy(mass))

# Calculate the amount of energy and display it as int
def energy(mass):
    celeritas = 300000000**2
    energy = int(mass*celeritas)
    return (f"the energy is {energy} j")

main()
