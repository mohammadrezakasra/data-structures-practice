secret_police_count  = int(input())
secret_police_name = set()
for i in range(secret_police_count):
    secret_police_name.add(input())

secret_police_data_count = int(input())
secret_police_data = []
for i in range(secret_police_data_count):
    secret_police_data.append(input())


ans = 0
temp_set = set()
for i in secret_police_data:
    temp_set.add(i)
    if len(temp_set) == secret_police_count:
        ans +=1
        temp_set = set()
        temp_set.add(i)

print(ans)
