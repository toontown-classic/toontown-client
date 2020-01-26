# toontown-client

Toontown 2003 client repository for startup files and the original game installer for running on MacOS

# Running on Mac OS

You will need to run the Toontown_MacOS executable provided in this repository,
this executable is modified in a way where it will run with wine on MacOS.
Drag the Toontown_MacOS.exe file from this repo to your Toontown installation folder after installing Toontown from the original 2003 executable, Then edit the start.py file and replace the following line:

## Before

```python
os.system('Toontown.exe null http://127.0.0.1/toontown http://127.0.0.1 http://127.0.0.1 0 "-OGL -windowed -allow_hw_midi -show_fps"')
```

## After

```python
os.system('Toontown_MacOS.exe null http://127.0.0.1/toontown http://127.0.0.1 http://127.0.0.1 0 "-OGL -windowed -allow_hw_midi -show_fps"')
```

Finally to launch the game, open a new terminal window and cd into the
Toontown installation directory where the executable is located and run the following:

```
wine cmd start.bat
```
