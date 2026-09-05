class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets