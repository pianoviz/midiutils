import os
import unittest
from pathlib import Path

from midiutils.midi_preprocessor import MidiPreprocessor
from midiutils.types import NoteEvent


class TestMidiProcessor(unittest.TestCase):
  def setUp(self) -> None:
    self.mid_path = os.path.join(
      os.path.dirname(__file__), "resources/cut_liszt.mid"
    )

  def test_extract_notes(self):
    mp = MidiPreprocessor()
    note_events = mp.get_midi_events(midi_path=Path(self.mid_path))
    assert isinstance(note_events[0], NoteEvent)
