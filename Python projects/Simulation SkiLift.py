# Skilift simulation mit Trassenlänge 2000m und 15 Liften, Geschwindigkeit 5m/s, Ankunft der Skifahrer Normalverteilt mit Mittelwert 120s und Standardabweichung 30s

import simpy
import numpy as np

class SkiLift:
    def __init__(self, env, num_lifts, track_length, speed):
        self.env = env
        self.num_lifts = num_lifts
        self.track_length = track_length
        self.speed = speed
        self.lift_process = env.process(self.run())

    def run(self):
        while True:
            travel_time = self.track_length / self.speed
            for i in range(self.num_lifts):
                print(f'Lift {i+1} starts at {self.env.now}')
                yield self.env.timeout(travel_time)
                print(f'Lift {i+1} ends at {self.env.now}')

def skier_arrival(env):
    while True:
        arrival_time = np.random.normal(120, 30)
        yield env.timeout(arrival_time)
        print(f'Skier arrives at {env.now}')

env = simpy.Environment()
ski_lift = SkiLift(env, num_lifts=15, track_length=1500, speed=3.5)
env.process(skier_arrival(env))
env.run(until=3600)