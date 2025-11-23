import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TRANSFORMERS_NO_TF'] = '1'

from rest_framework.views import APIView
from rest_framework.response import Response
from transformers import pipeline
import tempfile
import logging
import traceback

# Lazy-loaded pipeline so startup is cheaper and errors can be surfaced
_HF_ASR_PIPE = None
def get_asr_pipeline():
    global _HF_ASR_PIPE
    if _HF_ASR_PIPE is None:
        # This may raise if model or dependencies (ffmpeg) are missing — caller will handle it
        _HF_ASR_PIPE = pipeline("automatic-speech-recognition", model="openai/whisper-small")
    return _HF_ASR_PIPE

class Transcribe(APIView):
    """A class for transcribing audio files."""
    def post(self, request):
        audio_file = request.FILES.get("audio")
        if not audio_file:
            return Response({"error": "No audio file provided."}, status=400)
        tmp = tempfile.NamedTemporaryFile(suffix=".webm", delete=False)
        try:
            try:
                for chunk in audio_file.chunks():
                    tmp.write(chunk)
                tmp.flush()
                tmp.close()  # release lock so pipeline/ffmpeg can read
            except Exception as e:
                # problem writing uploaded file
                try:
                    os.unlink(tmp.name)
                except Exception:
                    pass
                return Response({"message": "Failed to save uploaded file.", "error": str(e)}, status=500)
            try:
                asr = get_asr_pipeline()
            except Exception as e:
                # pipeline couldn't be created (missing model or deps)
                logging.exception("ASR pipeline initialization failed")
                try:
                    os.unlink(tmp.name)
                except Exception:
                    pass
                return Response({"message": "ASR pipeline initialization failed.", "error": repr(e), "traceback": traceback.format_exc()}, status=500)
            try:
                result = asr(tmp.name)
            except Exception as e:
                # surface the real error to the client for easier debugging
                logging.exception("Transcription failed")
                try:
                    os.unlink(tmp.name)
                except Exception:
                    pass
                return Response({"message": "Transcription failed.", "error": repr(e), "traceback": traceback.format_exc()}, status=500)
            return Response({"message": "Audio has been transcribed.", "transcription": result}, status=200)
        finally:
            try:
                if os.path.exists(tmp.name):
                    os.unlink(tmp.name)
            except Exception:
                pass
