## Clock stuck behind
If you clock is stuck behind, in the terminal enter these lines one at a time

    timedatectl set-local-rtc 0
    timedatectl set-ntp 1
    timedatectl status
  
  
## Windows snapping closed and or chrome all messed up into nonsenical tiles

In the terminal type 

    sudo apt-get install --reinstall pcmanfm





# To summarise bookworm installs:

## Installing:
Install Python packages with apt where possible:

    sudo apt install python3-packagename

Use a virtual environment where apt packages are not available:


    python -m venv --system-site-packages [path/to/venv]
    [path/to/venv]/bin/python -m pip install packagename

## Updating:

Update both system and virtual environment packages


    sudo apt update && sudo apt upgrade
    [path/to/venv]/bin/python -m pip install --upgrade packagename

## Running:
Run Python scripts with:

 [path/to/venv]/bin/python myscript.py
