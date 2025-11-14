import threading
import pyautogui
import math
import time

def circular_mouse_motion(center_x, center_y, radius, duration=5, steps=100):
	start_time = time.time()
	while time.time() - start_time < duration:
		for i in range(steps):
			angle = 2 * math.pi * i / steps
			x = int(center_x + radius * math.cos(angle))
			y = int(center_y + radius * math.sin(angle))
			pyautogui.moveTo(x, y)
			time.sleep(duration / steps)
		
		if time.time() - start_time >= duration:
			break


def click_after_n_seconds(seconds):
   time.sleep(seconds)
   pyautogui.click()


if __name__ == "__main__":
	screen_width, screen_height = pyautogui.size()
	center_x, center_y = screen_width // 2, screen_height // 2
	radius = min(screen_width, screen_height) // 4
	t = threading.Thread(target=circular_mouse_motion, args=(center_x, center_y, radius, 5, 120))
	t.start()
	t.join()

