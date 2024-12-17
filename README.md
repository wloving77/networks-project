# Getting Setup:

1. Install professors `.ovm` or `.utm` image depending on host machine (Should be in your email)
2. Install `p4-utils` once inside the VM, clone p4 utils then run `./install.sh` in the root of the repo.
3. Put behavioral-model-v2 scripts on your PYTHON_PATH
    - This is essential for connecting to the switch for the p4 performance numbers, simply add these lines to your .bashrc:
    - export PYTHONPATH=/home/sdn/behavioral-model/tools/:$PYTHONPATH
    - export PYTHONPATH=/home/sdn/behavioral-model/targets/simple_switch:$PYTHONPATH
3. Clone this repo, navigate to either `src/telemety/endhost` or `src/telemety/p4` and check the README.md's there. 
4. I also recommend making a virtual environment in python so everything is in one place, there is a requirements.txt file in this directory that has everything you should need.