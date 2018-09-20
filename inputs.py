# list of all shims we have to play with
#    pre-populated with all sizes from Brownells™ part# 084-000-459WB shim kit - ain't that handy?
shims = [.002, .002, .003, .003, .004, .004, .008, .008, .010, .015, .030]

# threads per inch of our muzzle & device threads
threads_per_inch = 28

# when installed without shims, how much further does the muzzle device need to tightened to time?
degrees = 30

# how many ways can we mount the muzzle device?
#    1 = there's only one "this way is up" installation
#    2 = "symmetric" e.g. muzzle brake without a "top" or "bottom"
orientations = 1

# max height for the stack of shims
#    rifle muzzle threads are usually .600" long, and we still need to leave some meat to hold onto
max_height = .125
