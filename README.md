# Particle Dynamics Simulator

A simulator for particle dynamics. Uses techniques adopted from: <https://www.cs.cmu.edu/~baraff/sigcourse/>.

## Setup
Project requires **python 3.8+**

Option 1: Use a virtual environment

1. `python -m venv .env` (`python3` for mac)
1. `source .env/bin.activate` (activate virtual environment, adjust for your platform)
1. `pip install -r requirements.txt`

Other Options. 

1. Don't use a virtual environment - run `pip install -r requirements.txt` globally
1. Manually install the necessary packages on your global python installation (`numpy`, `matplotlib`, etc.)
1. Download a python distribution that already has the necessary requirements.
    *  Example: https://github.com/microsoft/coding-pack-for-python

## Running

* The project has launch configurations predefined for visual studio code. You can chose them using the debugging tab.
* Or, you can run things with `python -m simulator` (this will execute the `__main__.py` file in the root package)