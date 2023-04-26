import time

class FlushPrint:
	def flushprint(text: str, speed: float):
		for chars in text:
			print(chars, end="", flush = True)
			time.sleep(speed)
		print()