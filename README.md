# srt_tools
Tools for script creation and data plotting for the MIT Small Radio Telescope (SRT). These scripts complement the official [SRT software](https://www.haystack.mit.edu/edu/undergrad/srt/SRT%20Software/SRT_software_exec.html).

## Requirements
The only requirements are Python's libraries Numpy and Matplotlib. On a Debian based system you can install them typing on terminal:

```
sudo apt install python-numpy python-matplotlib
```

Or in any system with [pip](https://pip.pypa.io/en/stable/):

```
sudo pip install numpy matplotlib
```

## Installation
Clone or download the repository and then run in the root folder:

```
sudo python setup.py install
```

Or you can install it directly with pip (you need to have [git](https://git-scm.com/) installed):

```
sudo pip install git+https://github.com/francocalan/srt_tools.git
```

## Usage

This repository provides two types of scripts: scripters and plotters. All the scripts are well documented and the detail of their usage can be read running in terminal `<script_name> -h`. Here we provide a quick overview of their usage.

### Scripters
Scripters generate .cmd script files that the SRT software can read to run automatic tests. Currently there are three types of test implemented:

* `srt_observation_scripter.py`: runs an observation test, that is, moves the telescope to a defined source and measure it for a fixed number of seconds (defined by the argument `--delay`). The default script with no arguments produces an observation of the Sun for 11 seconds:

```
: azel 200 30
: freq 1420 1
: noisecal
: record 
:11 Sun
: roff
: stow
```

* `srt_beamwidth_scripter.py`: run a beamwidth test. Moves the telescope to source and scan it in either the azimuth (az) or the elevation (el) angle (defined by the argument `--axis`). The default script with no arguments scans the sun in the azimuth angle between -15 and 15 degrees with 1 degree of spacing:
```
: azel 200 30
: freq 1420 1
: noisecal
: Sun
: record 
:11 offset -15 0
:11 offset -14 0
...
:11 offset 14 0
:11 offset 15 0
: roff
: stow
```

* `srt_skymap_scripter.py`: run a skymap test. Scans the sky around a defined number of coordinates (defined by the arguments `--az1`, `az2`, `--el1`, and `--el2`). The default script with no arguments scans the sky from az=[190, 170] and el=[2, 88] with 5 degree of spacing in both axis:
```
: azel 200 30
: freq 1420 1
: noisecal
: record 
:11 azel 190 2
:11 azel 190 7
...
:11 azel 165 7
:11 azel 165 2
: roff
: stow
```

Notice that az1>az2, this is valid as the script can wrap around azimuth angles at 360°, although this is not valid for elevation angles.

All scripts include a calibration phase at the beginning, with the default calibration position at (200, 30), which can be changed with the arguments `--cal_az` and `--cal_el`. Also, by default the scripts are set to frequency 1420[MHz] and mode 1 (see the SRT software help for the modes definitions).

### Plotters
Plotters plot the data recorded by the SRT by parsing the .rad files generated by the SRT software. There are three types of plots, one for each scripter test. All plotter are run as: `<plotter_script.py> rad_file.rad` 

* `srt_observation_plotter.py`: plot an observation test. Example:



* `srt_beamwidth_plotter.py`: plot a beamwidth test. Example:



* `srt_skymap_plotter.py`: plot a skymap test. Example:



