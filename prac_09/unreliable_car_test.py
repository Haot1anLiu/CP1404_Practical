from unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("Old Faithful", 100, 10)
reliable_car = UnreliableCar("Modern Machine", 100, 90)

for i in range(1, 10):
    print("{} drove {}km".format(unreliable_car.name, unreliable_car.drive(i)))
    print("{} drove {}km".format(reliable_car.name, reliable_car.drive(i)))


print(unreliable_car)
print(reliable_car)