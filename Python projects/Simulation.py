import simpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the simulation environment
class Car(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        while True:
            print('Start parking and charging at %d' % self.env.now)
            charge_duration = 5
            yield self.env.process(self.charge(charge_duration))

            print('Start driving at %d' % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)

# Create the simulation environment and start the simulation
env = simpy.Environment()
car = Car(env)
env.run(until=15)


