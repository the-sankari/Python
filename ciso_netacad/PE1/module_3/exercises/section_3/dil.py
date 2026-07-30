"""Print a decorative love heart with names inside."""

import math


def make_heart(name1: str = "A1 ", name2: str = "A2") -> str:
	# Build the heart shape dynamically using a smooth mathematical curve.
	width = 60
	height = 32
	canvas = [[" "] * width for _ in range(height)]
	center_x = width // 2
	center_y = height // 2 + 2
	scale = 1.2

	for angle in [i / 100 for i in range(0, 628)]:
		x = int(round(16 * (math.sin(angle) ** 3) * scale))
		y = int(round((13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * scale))
		for dx in (-1, 0, 1):
			for dy in (-1, 0, 1):
				px = center_x + x + dx
				py = center_y - y + dy
				if 0 <= px < width and 0 <= py < height:
					canvas[py][px] = "*"

	# Centered text lines placed inside the heart.
	name_line = f"{name1}  ♥  {name2}"
	tagline = "Nagin Nagin ...."

	def place_text(row_index: int, text: str) -> None:
		row = canvas[row_index][:]
		if len(text) >= len(row):
			text = text[: len(row)]
		start = (len(row) - len(text)) // 2
		for i, char in enumerate(text):
			if row[start + i] == " ":
				row[start + i] = char
		canvas[row_index] = row

	place_text(center_y, name_line)
	place_text(center_y + 2, tagline)
	return "\n".join("".join(row) for row in canvas)


def main() -> None:
	print(make_heart())


if __name__ == "__main__":
	main()
