import pyautogui
import math
import time

def circular_clicks(center_x, center_y, radius, num_clicks=12):
	"""
	Perform clicks in a circular pattern around a center point.
	
	Args:
		center_x: X coordinate of circle center
		center_y: Y coordinate of circle center
		radius: Radius of the circle
		num_clicks: Number of clicks to perform around the circle
	"""
	print(f"Starting circular clicks at center ({center_x}, {center_y}) with radius {radius}")
	print(f"Will perform {num_clicks} clicks in a circular pattern\n")
	
	for i in range(num_clicks):
		angle = 2 * math.pi * i / num_clicks
		
		x = int(center_x + radius * math.cos(angle))
		y = int(center_y + radius * math.sin(angle))
		
		pyautogui.moveTo(x, y, duration=0.3)
		pyautogui.click()
		
		print(f"Click {i+1}/{num_clicks} at position ({x}, {y})")
		time.sleep(0.5)
	
	print("\nCircular clicks completed!")


if __name__ == "__main__":
	print("PyAutoGUI Circular Clicks Program")
	print("=" * 40)
	
	screen_width, screen_height = pyautogui.size()
	print(f"Screen size: {screen_width}x{screen_height}\n")
	
	center_x, center_y = screen_width // 2, screen_height // 2
	radius = min(screen_width, screen_height) // 4
	
	time.sleep(3)
	
	circular_clicks(center_x, center_y, radius, num_clicks=12)

