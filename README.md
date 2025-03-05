# midiutils

Code to preprocess the midi file. Normally, midi files are represented in the
number of ticks that occur after the previous note. This code converts the midi
file into a list of notes with the start time and end time of each note.

## Installation

```bash
pip install midiutils
```

from source, clone the repository and run the following command
```bash
pip install -e .       # for normal installation
pip install -e .[dev]  # for development installation
```

## Usage

```python
from midiutils import MidiPreprocessor
processor = MidiPreprocessor()
events = processor.get_midi_events('data/cut_liszt.mid', max_note_length=50)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for details.


