# Cursor Finish Sound

A simple Python package that plays a gentle notification sound and/or speaks the current folder name using text-to-speech.

## Installation

0. go to the main folder of your repo, open your terminal (should be in the main folder, so you can identify later which agent in which project has finished creating), write

```
git clone https://github.com/eliaspfeffer/cursorfinishsound.git
```

press Enter

1. Make sure you have Python 3.x installed
2. Install system dependencies (on Ubuntu/Debian):

   ```bash
   sudo apt-get install espeak python3-pip
   ```

3. Install the Python package dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add this sentence to cursor->settings (gearwheel in agent-window)->"Rules for AI"->

```
Always play cursorfinishsound/soundname.py when you have finished the last job, before you stop generating.
```

(You can use sound.py instead of soundname.py to play a simple sound instead of saying the name of the repository folder.)

## Usage

You can use this package in two ways:

### 1. Play a gentle notification sound

```python
from cursorfinishsound import sound
sound.play_gentle_notification()
```

### 2. Speak the current folder name

```python
from cursorfinishsound import soundname
soundname.say_folder_name()
```

### 3. Adjust volumne for soundname.py

you can adjust how loud the robot voice says the folder name. See this line in soundname.py:

```
subprocess.run(['espeak', '-a', '50', parent_folder], check=True)
```

## Integration with other projects

To use this in your project, as explained above already:

1. Clone this repository into your project:

   ```bash
   git clone https://github.com/yourusername/cursorfinishsound.git
   ```

2. Install the dependencies as shown above (create a virutal environment if not already happened)
