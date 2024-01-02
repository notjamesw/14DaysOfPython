from droneblocks.DroneBlocksTello import DroneBlocksTello

tello = DroneBlocksTello()

tello.connect()

print(f"You have {tello.get_battery()}% left in your battery")
print(f"The current temp is {tello.get_temperature()} degrees")
tello.display_smile()