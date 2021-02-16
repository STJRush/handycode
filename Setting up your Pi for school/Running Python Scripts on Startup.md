## How to run stuff on startup

In the terminal go to

```bash
sudo nano /etc/rc.local
```

Then on the last line, add your script

```python
python3/home/pi/myscript.py &
```

The & symbol stops your program being a cul de sac and lets the pi keep going. It won't wait for it to complete the program.

Nano is an ancient text editor used by Moses to code his way out of the red sea using hax. It's pretty old. When you open things in nano, you need to hit CTRL+O to save and then CTRL+X to exit.

## HERE BE DRAGONS!!! DANGERZONE
That & is very important especially if you put a loop into your program. A loop can stop the pi booting up and you could end up locked out of your pi altogether.

It's a good idea also to have a
```python
sleep(30)
```
in your code right after from time import sleep because your pi might need a while to get out of bed on startup. I've found when I don't add this, nothing happens on startup. Maybe the program ran but it hadn't connected to the internet yet so didn't run properly.
