# Pyannote configuration
import os

HF_TOKEN = os.environ["HF_TOKEN"]

# Diarization settings
MIN_SILENCE_GAP = 3.0  # seconds
INTRO_DURATION = 60.0  # seconds for teacher calibration
