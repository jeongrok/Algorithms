# People who study epidemiology use models to analyze the spread of disease.
# In this problem, we use a simple model.
#
# When a person has a disease, they infect exactly  other people but only on the very next day.
# No person is infected more than once. We want to determine when a total of more than  people have had the disease.

cut = int(input())
a = int(input())
b = int(input())

infected = a
infected_last = a
result = 0

while infected <= cut:
    result += 1
    infected += infected_last * b
    infected_last *= b

print(result)