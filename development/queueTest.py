from CMQueue import CMQueue

q = []
q = CMQueue(q)

names = []
commands = []

for i in range(0, 10):
    job = "Job", i
    names.append(job)
    commands.append(i)

for i in range(0, len(names)):
    q.add(names[i], commands[i])
    print('Added names and commands')
print()
print('The current queue:', q)
print()

for i in range(0, len(names)):
    q.remove(names[i])
    q.status()
    q.list()