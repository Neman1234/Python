import math
from PIL import Image, ImageDraw, ImageFilter

picture = Image.new("RGB", (120, 120), "white")
draw = ImageDraw.Draw(picture)

# Build a 5-pointed star by alternating between outer and inner radii
cx, cy = 60, 60          # center
outer_r, inner_r = 40, 16
points = []
for i in range(10):
    angle = math.radians(-90 + i * 36)   # start pointing straight up
    r = outer_r if i % 2 == 0 else inner_r
    points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))

draw.polygon(points, fill="orange")

edges = picture.filter(ImageFilter.FIND_EDGES)
edges.save("shape_edges.png")

print("Saved shape_edges.png")