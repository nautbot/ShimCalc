import itertools
import sys

import inputs

# validate inputs, because I'm an idiot
if not inputs.shims:
    print('No available shims for calculation.')
    sys.exit()
if inputs.degrees <= 0 or 360 >= inputs.degrees:
    print('Invalid angle - enter and angle between 0 and 360 degrees.')
    sys.exit()
if inputs.threads_per_inch <= 0:
    print('Invalid threads per inch - enter a value greater than zero.')
    sys.exit()
if inputs.orientations <= 0:
    print('Invalid muzzle device orientations - enter a value greater than or equal to one.')
    sys.exit()

# local variables
pitch = 1 / inputs.threads_per_inch
orientations = []
cnt = 0

# build list of possible muzzle device orientations
while True:
    orientation = {
        'Angle': inputs.degrees + cnt * 360 / inputs.orientations,
        'Shims': [],
        'Error': None
    }
    if orientation['Angle'] * pitch / 360 > inputs.max_height:
        break
    orientations.append(orientation)
    cnt += 1

# test all possible shim combinations for best fit at given muzzle device orientation
for L in range(0, len(inputs.shims)+1):
    for combo in itertools.combinations(inputs.shims, L):
        for orientation in orientations:
            error = orientation['Angle'] * pitch / 360 - sum(combo)
            if not orientation['Shims'] or abs(error) < abs(orientation['Error']):
                orientation['Shims'] = combo
                orientation['Error'] = error

# sort by lowest (absolute) error
orientations = sorted(orientations, key=lambda i: abs(i['Error']))

# output
for orientation in orientations:
    if orientation['Shims'] and abs(orientation['Error'] / pitch * 360) < inputs.degrees:
        print('Angle: {}\nShims: {}\nError: {}º\n\n'.format(
            orientation['Angle'],
            ' + '.join(str(x) for x in orientation['Shims']),
            round(orientation['Error'] / pitch * 360, 3)
        ))
