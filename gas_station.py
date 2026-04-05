n , k , l = map(int , input().split())

gas_station_distances = list(map(int , input().split()))
gas_station_distances.append(l)

vehicle_location = 0
index_gas_station = []
location_index = 0

if vehicle_location + k < gas_station_distances[0]:
    print(-1)
    exit()

for i in range(n+1):

    if gas_station_distances[i] > vehicle_location + k:
        index_gas_station.append(i)
        vehicle_location = gas_station_distances[i-1]

        if vehicle_location + k < gas_station_distances[i]:
            print(-1)
            exit()




print(len(index_gas_station))
print(*index_gas_station)