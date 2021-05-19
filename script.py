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
cardio = ['skaters', 'jump jacks', 'burpees', 'jump rope', 'mountain climbers',
          'high knees', 'fanny kickers', 'jump squats']


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
cardio_exercise = random_exercise_generator(cardio)

name = input("Name: ")
date = datetime.datetime.now()

workout_text = []

workout_text.append(f"Client's name: {name.title()}")
workout_text.append(f"Todays date: {date}")
workout_text.append(f"# Workout Generator")
workout_text.append(f"Back: {back_exercise}")
workout_text.append(f"Quads: {quadriceps_exercise}")
workout_text.append(f"Chest: {chest_exercise}")
workout_text.append(f"Hams: {hamstrings_exercise}")
workout_text.append(f"Delts: {deltoid_exercise}")
workout_text.append(f"Calves: {calves_exercise}")
workout_text.append(f"Bis: {biceps_exercise}")
workout_text.append(f"Abs: {abdominal_exercise}")
workout_text.append(f"Tris: {triceps_exercise}")
workout_text.append(f"Cardio: {cardio_exercise}")
workout_text.append(f"**********************************")

with open("workout.md", 'w') as f:
    for text in workout_text:
        f.write("%s\n" % text)


