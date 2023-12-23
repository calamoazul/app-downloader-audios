
#Clase para gestionar errores de desacarga

class DownloadError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message