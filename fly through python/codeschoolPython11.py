performances = {}

schedule_file = open('schedule.txt', 'r')

for line in schedule_file:
    (show, time) = line.split(' - ')
    print(show, time)
    performances[show] = time.strip()
schedule_file.close() 
print(performances)