
from downloader import Downloader

if __name__ == "__main__":
    
   try:
      downloader = Downloader()
      data = downloader.run()
   except Exception as error:
      print(error)



