import itertools

import inputs

pitch = 1/inputs.threads_per_inch

target_1 = inputs.degrees / 360 * pitch
target_2 = inputs.degrees / 360 * pitch + pitch
target_3 = inputs.degrees / 360 * pitch + pitch * 2

result_1 = []
result_2 = []
result_3 = []

error_1 = None
error_2 = None
error_3 = None

for L in range(0, len(inputs.shims)+1):
    for combo in itertools.combinations(inputs.shims, L):
        if not result_1 or abs(target_1 - sum(combo)) < error_1:
            result_1 = combo
            error_1 = abs(target_1 - sum(combo))
        if not result_2 or abs(target_2 - sum(combo)) < error_2:
            result_2 = combo
            error_2 = abs(target_2 - sum(combo))
        if not result_3 or abs(target_3 - sum(combo)) < error_3:
            result_3 = combo
            error_3 = abs(target_3 - sum(combo))

if result_1:
    print('{} - error = {}º'.format(result_1, error_1 / pitch * 360))
if result_2:
    print('{} - error = {}º'.format(result_2, error_2 / pitch * 360))
if result_3:
    print('{} - error = {}º'.format(result_3, error_3 / pitch * 360))
