import os
import ctypes
import time
from PIL import Image, ImageDraw, ImageSequence

class IconInnovator:
    def __init__(self, icon_path, animation_frames=10, animation_interval=0.5):
        self.icon_path = icon_path
        self.animation_frames = animation_frames
        self.animation_interval = animation_interval
        self.animated_icons = []

    def create_animated_icon(self):
        original_icon = Image.open(self.icon_path)
        width, height = original_icon.size

        for i in range(self.animation_frames):
            frame = Image.new('RGBA', (width, height))
            draw = ImageDraw.Draw(frame)
            draw.rectangle([i, i, width - i, height - i], outline=(255, 0, 0, 255))
            frame.paste(original_icon, (0, 0), original_icon)
            self.animated_icons.append(frame)

        temp_icon_path = "animated_icon.ico"
        self.animated_icons[0].save(
            temp_icon_path,
            save_all=True,
            append_images=self.animated_icons[1:],
            duration=self.animation_interval * 1000,
            loop=0
        )

        return temp_icon_path

    def set_desktop_icon(self, icon_path):
        # This requires admin privileges
        ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)
        key = r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Icons'
        value_name = '29'  # Recycle Bin full - just for demonstration
        with ctypes.windll.advapi32.RegOpenKeyExW(0x80000002, key, 0, 0xF003F) as handle:
            ctypes.windll.advapi32.RegSetValueExW(handle, value_name, 0, 1, icon_path, len(icon_path))

    def animate_icon(self):
        animated_icon_path = self.create_animated_icon()
        self.set_desktop_icon(animated_icon_path)
        time.sleep(self.animation_interval * self.animation_frames)
        os.remove(animated_icon_path)
        print("Animation complete.")

if __name__ == "__main__":
    icon_path = "path_to_your_icon.ico"
    icon_innovator = IconInnovator(icon_path)
    icon_innovator.animate_icon()