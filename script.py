import random

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

def randomize(lst):
    return random.randint(1, len(lst)-1)

exercise1 = randomize(back)


print(exercise1)

