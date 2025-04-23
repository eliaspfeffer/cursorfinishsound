# Cursor Finish Sound

A simple Python package that plays a gentle notification sound and/or speaks the current folder name using text-to-speech.

## Installation

1. Make sure you have Python 3.x installed
2. Install system dependencies (on Ubuntu/Debian):

   ```bash
   sudo apt-get install espeak python3-pip
   ```

3. Install the Python package dependencies:
   ```bash
   pip install -r requirements.txt
   ```

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

## Integration with other projects

To use this in your project:

1. Clone this repository into your project:

   ```bash
   git clone https://github.com/yourusername/cursorfinishsound.git
   ```

2. Install the dependencies as shown above (create a virutal environment if not already happened)

3. Import and use the functions in your code as needed

4. Open cursor settings and add "Always play sound.py when you have finished the last job, before you stop generating.". Or change it to "soundname.py" instead of "sound.py", to make it say the folder name in case you work on multiple cursor editors at once, so you know which cursor agent has finished in which cursor window.
