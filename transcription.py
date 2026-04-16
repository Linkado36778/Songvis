import whisper
from soundMic import gravar_por_tecla

model = whisper.load_model("base")
gravacao = gravar_por_tecla()
result = model.transcribe(gravacao, language="en", fp16=False)
print(result["text"])