# ShimCalc

ShimCalc is a simple python script that determines the best possible combinations of shims to time a muzzle device.

-----

#### Requirements

Python 3.X

-----

#### Inputs

The required inputs (found in **inputs.py**) are:

* **shims** - A list of available shims to stack up;

* **threads_per_inch** - Threads per inch of the barrel/muzzle device thread;

* **degrees** - How many degrees of additional counter-clockwise rotation are needed to get the muzzle device timed, based on where the muzzle device times without any shims.

* **orientations** - Number of possible install orientations (1 = only one way to time, 2 = no defined "top" or "bottom");

* **max_height** - Maximum height for the stack of shims.

-----

#### Outputs

Running ShimCalc.py will print a list in the console/terminal with the following values:

* **Angle** - Nominal/target degrees of rotation for the muzzle device from the starting point (can be ignored);

* **Shims** - A list of shims to use for that possible install option;

* **Error** - Estimation of how far off in degrees the install option will be from the nominal target.


    Angle: 30.0
    Shims: 0.003
    Error: -0.24º


    Angle: 390.0
    Shims: 0.002 + 0.003 + 0.004 + 0.03
    Error: -3.12º


    Angle: 750.0
    Shims: 0.002 + 0.002 + 0.003 + 0.003 + 0.004 + 0.004 + 0.008 + 0.008 + 0.01 + 0.03
    Error: 4.08º
    

-----

#### Notes

This calculator does not take into account deformation of the shims from compressive forces, on the assumption that the amount of torque generally used for installation will not cause significant deformation.  That, and the code would get super complexificated.