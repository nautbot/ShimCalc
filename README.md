# ShimCalc
A python script to assist with muzzle device timing

-----

ShimCalc is a simple python script that determines the best possible combinations of shims to time a muzzle device.

Inputs (configured in the "inputs.py" file) are:

* **shims** - A list of available shims to stack up;

* **threads_per_inch** - Threads per inch of the barrel/muzzle device thread;

* **degrees** - How many degrees of additional counter-clockwise rotation are needed to get the muzzle device timed, based on where the muzzle device times without any shims.

The script will provide three outputs - minimum shims needed with no full rotations, timed with one additional full rotation and with two full rotations, as well as how far off in degrees each option is from perfectly timed.
