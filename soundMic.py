import sounddevice as sd
import soundfile as sf
import numpy as np

SAMPLE_RATE = 16000
CHANNELS = 1

def gravar_por_tecla():
    print("Pressione ENTER para começar a gravar...")
    input()
    
    frames = []

    def callback(indata, frame_count, time_info, status):
        frames.append(indata.copy())

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS,
                        dtype='float32', callback=callback):
        print("Gravando... pressione ENTER para parar")
        input()

    audio = np.concatenate(frames, axis=0)
    sf.write("comando.wav", audio, SAMPLE_RATE)
    print("Salvo em comando.wav")
    return "comando.wav"

gravar_por_tecla()