
from downloader import Downloader

if __name__ == "__main__":
    
   downloader = Downloader()
   url = downloader.run()
   song = downloader.execute(url)
   


