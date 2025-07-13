#Chad Collard
#Chapter 14 Lab 1
#Vehicle project
#7/12/2025

import vehicle

my_car = vehicle.Vehicle('Ford', '2020', 'Fusion')

print(my_car)
print()
my_car.accelerate()
print(f"Current Speed: {my_car.get_speed()} mph")
my_car.accelerate()
print(f"Current Speed: {my_car.get_speed()} mph")
print()
my_car.decelerate()
print(f"Current Speed: {my_car.get_speed()} mph")
my_car.decelerate()
print(f"Current Speed: {my_car.get_speed()} mph")
print()
print(my_car)


