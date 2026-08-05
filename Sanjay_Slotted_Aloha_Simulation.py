import random

def slotted_aloha():
    print("=" * 50)
    print("       SLOTTED ALOHA SIMULATION")
    print("=" * 50)

    stations = int(input("Enter number of stations: "))
    slots = int(input("Enter number of time slots: "))
    probability = float(input("Enter transmission probability (0-1): "))

    success = 0
    collision = 0
    idle = 0

    attempts = [0] * stations
    successful = [0] * stations

    print("\nSlot\tTransmitting Stations\tStatus")
    print("-" * 55)

    for slot in range(1, slots + 1):

        transmitting = []

        for station in range(stations):
            if random.random() < probability:
                transmitting.append(station)
                attempts[station] += 1

        if len(transmitting) == 0:
            idle += 1
            status = "Idle"

        elif len(transmitting) == 1:
            success += 1
            successful[transmitting[0]] += 1
            status = "Success"

        else:
            collision += 1
            status = "Collision"

        station_list = [x + 1 for x in transmitting]
        print(f"{slot}\t{station_list}\t\t{status}")

    print("\n" + "=" * 50)
    print("SIMULATION RESULT")
    print("=" * 50)

    print("Total Slots        :", slots)
    print("Successful Slots   :", success)
    print("Collision Slots    :", collision)
    print("Idle Slots         :", idle)

    throughput = success / slots
    print("Throughput         :", round(throughput, 3))
    print("Efficiency         :", round(throughput * 100, 2), "%")

    print("\nPer Station Statistics")
    print("-" * 50)
    print("Station\tAttempts\tSuccess")

    for i in range(stations):
        print(f"{i+1}\t{attempts[i]}\t\t{successful[i]}")

    print("-" * 50)
    print("Total Attempts :", sum(attempts))
    print("=" * 50)
    print("Simulation Completed Successfully")

if __name__ == "__main__":
    slotted_aloha()