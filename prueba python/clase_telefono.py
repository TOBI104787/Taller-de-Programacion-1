class telefono:
    def __init__ (self):
        pass
    def llamar(self):
        print("llamar")
    def colgar(self):
        print("colgar")
class camara:
    def __init__ (self):
        pass
    def foto(self):
        print("foto")
    def flash(self):
        print("flash")
class reproductor:
    def __init__ (self):
        pass
    def repro_video(self):
        print("video")
    def repro_audio(self):
        print("audio")
class smartphone(telefono, camara, reproductor):
    def __del__ (set):
        print("apagado")
telefono = smartphone()
telefono.llamar()