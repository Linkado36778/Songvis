import spotipy 
import webbrowser
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
from transcription import transcrever_comando

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-modify-playback-state user-read-playback-state"
))

def ler_comando():
    comando = transcrever_comando()
    
    if "open spotify" in comando:
        conectar_spotify()

    else:
        #executar_comando(comando)
        pass

def conectar_spotify():
    webbrowser.open("spotify:")


def executar_comando(comando):
    if "play" in comando:
        nome_musica = comando.replace("play", "").strip()
        tocar_musica(nome_musica)


def tocar_musica(nome):
    resultado = sp.search(q=nome, type="track", limit=1)
    tracks = resultado["tracks"]["items"]
    
    if tracks:
        uri = tracks[0]["uri"]
        sp.start_playback(uris=[uri])
        print(f"Tocando: {tracks[0]['name']} - {tracks[0]['artists'][0]['name']}")
    else:
        print("Música não encontrada")