import time
import random
import socket

class AUV:
    def __init__(self):
        self.depth = 0
        self.speed = 0
        self.temperature = 0
        self.salinity = 0
        self.pressure = 0
        self.battery = 100
        self.location = (0, 0)
        self.destination = (0, 0)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 10000)

    def update_sensors(self):
        self.depth = random.uniform(0, 100)
        self.speed = random.uniform(0, 10)
        self.temperature = random.uniform(0, 30)
        self.salinity = random.uniform(0, 40)
        self.pressure = random.uniform(0, 100)
        self.battery -= random.uniform(0, 1)

    def navigate(self):
        if self.location == self.destination:
            self.destination = (random.uniform(-180, 180), random.uniform(-90, 90))
        else:
            x = self.destination[0] - self.location[0]
            y = self.destination[1] - self.location[1]
            self.location = (self.location[0] + x / 100, self.location[1] + y / 100)

    def transmit_data(self):
        data = f"Depth: {self.depth:.2f} m\nSpeed: {self.speed:.2f} m/s\nTemperature: {self.temperature:.2f} C\nSalinity: {self.salinity:.2f} ppt\nPressure: {self.pressure:.2f} atm\nBattery: {self.battery:.2f}%\nLocation: {self.location}\nDestination: {self.destination}"
        self.sock.sendto(data.encode(), self.server_address)

    def run(self):
        while self.battery > 0:
            self.update_sensors()
            self.navigate()
            self.transmit_data()
            print(f"Depth: {self.depth:.2f} m")
            print(f"Speed: {self.speed:.2f} m/s")
            print(f"Temperature: {self.temperature:.2f} C")
            print(f"Salinity: {self.salinity:.2f} ppt")
            print(f"Pressure: {self.pressure:.2f} atm")
            print(f"Battery: {self.battery:.2f}%")
            print(f"Location: {self.location}")
            print(f"Destination: {self.destination}")
            time.sleep(1)

auv = AUV()
auv.run()
