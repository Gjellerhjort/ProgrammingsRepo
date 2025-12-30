from sage.all import *

# Define the number
w = -2 * I
n = 8
in_interval = [0, 2*pi]
rounding = 3

radius = abs(w)**(1/n)          # 2^(1/8)

# Get argument and move to [0, 2π)
theta = arg(w)
theta = theta + 2*pi if theta < 0 else theta   # corrected line

print("Argument used:", theta, "=", theta/pi, "π")   # should print 3/2 π

# Generate the 8 roots as complex numbers
roots = []
arguments = []
for k in range(n):
    phi = (theta + 2*k*pi) / n
    z_k = radius * (cos(phi) + I * sin(phi))
    roots.append(z_k)
    arguments.append(phi)


# --- printing arguments ---
print("\nArgumnets:")
for i, phi in enumerate(arguments):
    print(f"phi_{i} = {phi}")
# --- printing roots ----
print("\nRoots:")
for i, z in enumerate(roots):
    print(f"z_{i} = {z}")
# --- Plotting ---
p = Graphics()

# Background circle
p += circle((0,0), float(radius), color='lightgray', linestyle='--', thickness=1.2)

# Axes
p += line([(-1.4,0), (1.4,0)], color='gray', thickness=0.8)
p += line([(0,-1.4), (0,1.4)], color='gray', thickness=0.8)

# Plot points + labels

rainbow_colors = rainbow(n)
print("\nk   Re(z)     Im(z)       (afrundet til 3 decimaler)")
for i, z in enumerate(roots):
    re = real(z)
    im = imag(z)
    p += line([(0,0), (re, im)], color='gray', thickness=0.8, linestyle='--')
    p += point((re, im), size=70, color=rainbow_colors[i], zorder=10)
    print(f"z_{i} = {N(re, digits=3)}{N(im, digits=3):+}i")
    p += text(f"z_{i}", (re, im), 
              color='black', fontsize=11,
              horizontal_alignment='right',
              vertical_alignment='bottom')

# Diagram styling
p.axes_labels(['Re(z)', 'Im(z)'])
p.set_aspect_ratio(1)
p.axes_range(xmin=-1.35, xmax=1.35, ymin=-1.35, ymax=1.35)

p.show()
p.save('roots.png', figsize=[7,7], dpi=120, gridlines=True)
