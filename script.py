import random
import datetime
back = ['bent-over row', 'lying row', ]
quadriceps = ['lunge', 'side lunge', 'walking lunge', 'rear lunge', 'split squat',
              'front squat', 'step ups']
chest = ['bench press', 'fly', 'pullover']
hamstrings = ['straight-leg deadlift', 'straight-back stiff-leg deadlift']
deltoid = ['arnold press', 'front raise', 'shoulder press']
calves = ['standing calf raise', 'single leg calf raise']
biceps = ['curl', 'seated curl', 'incline curl']
abdominal = ['push crunch', 'crunch', 'jack-knife', 'reverse crunch']
triceps = ['kickback', 'lying tricep extension', 'incline tricep extension']


def random_exercise_generator(lst):
    ran_num = random.randint(1, len(lst))
    return lst[ran_num - 1]


back_exercise = random_exercise_generator(back)
quadriceps_exercise = random_exercise_generator(quadriceps)
chest_exercise = random_exercise_generator(chest)
hamstrings_exercise = random_exercise_generator(hamstrings)
deltoid_exercise = random_exercise_generator(deltoid)
calves_exercise = random_exercise_generator(calves)
biceps_exercise = random_exercise_generator(biceps)
abdominal_exercise = random_exercise_generator(abdominal)
triceps_exercise = random_exercise_generator(triceps)

name = input("Name: ")
date = datetime.datetime.now()

print(f"Client's name: {name.title()}")
print(f"Todays date: {date}")
print("******* Workout Generator *******")
print(f"Back: {back_exercise}")
print(f"Quads: {quadriceps_exercise}")
print(f"Chest: {chest_exercise}")
print(f"Hams: {hamstrings_exercise}")
print(f"Delts: {deltoid_exercise}")
print(f"Bis: {biceps_exercise}")
print(f"Abs: {abdominal_exercise}")
print(f"Tris: {triceps_exercise}")
print("**********************************")
