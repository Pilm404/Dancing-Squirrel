import requests
from PIL import Image
from io import BytesIO
from ascii_magic import AsciiArt
import os
import time
import threading


clean_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class DancingSquirrel:
    def __init__(self, gif_url, columns=80, frame_delay=0.1):
        self.gif_url = gif_url
        self.columns = columns
        self.frame_delay = frame_delay
        self.ascii_frames = []
        self.is_running = False
        self._load_gif()

    def _load_gif(self):
        response = requests.get(self.gif_url)
        if response.status_code != 200:
            return

        gif_data = BytesIO(response.content)
        gif = Image.open(gif_data)

        for i in range(gif.n_frames):
            gif.seek(i)
            frame = gif.convert('RGB')
            frame = frame.resize((80, 80))
            ascii_art = AsciiArt.from_pillow_image(frame)
            ascii_text = ascii_art.to_ascii(columns=self.columns)
            self.ascii_frames.append(ascii_text)

    def _animate(self):
        while self.is_running:
            for frame in self.ascii_frames:
                if not self.is_running:
                    break
                clean_screen()
                print(frame)
                time.sleep(self.frame_delay)

    def run(self):
        if not self.ascii_frames:
            print("ERROR")
            return
        self.is_running = True
        threading.Thread(target=self._animate, daemon=True).start()

    def stop(self):
        self.is_running = False



if __name__ == '__main__':
    squirrel = DancingSquirrel("https://media.tenor.com/smLZ8pqP42UAAAAi/dancing-squirrel-dancing.gif", 100)
    squirrel.run()
    try:
        input("Prees Enter to exit\n")
    finally:
        squirrel.stop()
