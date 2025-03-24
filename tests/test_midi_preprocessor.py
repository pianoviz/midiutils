import os
import unittest
from pathlib import Path

from mido import Message

from midiutils.midi_preprocessor import MidiPreprocessor
from midiutils.types import NoteEvent


class TestMidiProcessor(unittest.TestCase):
  def setUp(self) -> None:
    self.mid_path = os.path.join(
      os.path.dirname(__file__), "resources/cut_liszt.mid"
    )

  def test_extract_notes(self) -> None:
    mp = MidiPreprocessor()
    note_events = mp.get_midi_events(midi_path=Path(self.mid_path))
    assert isinstance(note_events[0], NoteEvent)

  def test_overlapping_notes(self):
    # Test with overlapping notes
    preprocessor = MidiPreprocessor()
    test_track = [
      Message("note_on", channel=0, note=60, velocity=64, time=0),
      Message("note_on", channel=0, note=60, velocity=64, time=100),
      Message("note_off", channel=0, note=60, velocity=0, time=100),
      Message("note_off", channel=0, note=60, velocity=0, time=100),
    ]
    preprocessor._preprocess_track(test_track, "right")
    events = preprocessor.events
    print(f"Extracted events: {len(events)}")
    for event in events:
      print(f"Note: {event.note}, Start: {event.start}, End: {event.end}")

    # Verify results
    assert len(events) == 2, f"Expected 2 events, got {len(events)}"
    assert (
      events[0].start == 0 and events[0].end == 200
    ), "First event incorrect"
    assert (
      events[1].start == 100 and events[1].end == 300
    ), "Second event incorrect"
