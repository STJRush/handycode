## Clock stuck behind
If you clock is stuck behind, in the terminal enter these lines one at a time

    timedatectl set-local-rtc 0
    timedatectl set-ntp 1
    timedatectl status
  
  
## Windows snapping closed

In the terminal type 

    sudo apt-get full-upgrade
