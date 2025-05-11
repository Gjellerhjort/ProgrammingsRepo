import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def IntersectionOverArea(bbox1, bbox2):
    # find the area for the box1 (x1,y1) (x2,y2) and box2 (x3,y3) (x4,y4)
    area1 = (bbox1[2] - bbox1[0]) * (bbox1[3] - bbox1[1])
    area2 = (bbox2[2] - bbox2[0]) * (bbox2[3] - bbox2[1])

    # now we need to fidn the intersection area
    xx = max(bbox1[0], bbox2[0])
    yy = max(bbox1[1], bbox2[1])
    xx2 = min(bbox1[2], bbox2[2])
    yy2 = min(bbox1[3], bbox2[3])

    w = max(0, xx2 - xx)
    h = max(0, yy2 - yy)

    intersection = w * h

    union_area = area1 + area2 - intersection

    return intersection / union_area

def non_max_suppression(boxes, scores, iou_threshold):
    if not boxes:
        return []
    
    # Create list of (index, score) tuples and sort by score in descending order
    score_with_index = list(enumerate(scores))
    score_with_index.sort(key=lambda x: x[1], reverse=True)
    
    keep = []
    while score_with_index:
        # Pick the box with highest score
        idx = score_with_index[0][0]
        keep.append(idx)
        
        # Compute IoU of the picked box with the rest
        ious = [IntersectionOverArea(boxes[idx], boxes[item[0]]) for item in score_with_index[1:]]
        
        # Keep boxes with IoU less than threshold
        score_with_index = [
            item for i, item in enumerate(score_with_index[1:])
            if ious[i] <= iou_threshold
        ]
    
    return keep

# Create sample bounding boxes and scores
boxes = [
    [50, 50, 150, 150],   # Box 1: Overlaps with Boxes 2, 6, 7
    [60, 60, 160, 160],   # Box 2: Overlaps with Boxes 1, 6, 7
    [200, 200, 300, 300], # Box 3: Overlaps with Boxes 4, 8
    [210, 210, 310, 310], # Box 4: Overlaps with Boxes 3, 8
    [350, 350, 450, 450], # Box 5: No overlap
    [55, 55, 155, 155],   # Box 6: Overlaps with Boxes 1, 2, 7
    [70, 70, 170, 170],   # Box 7: Overlaps with Boxes 1, 2, 6
    [205, 205, 305, 305], # Box 8: Overlaps with Boxes 3, 4
    [100, 350, 200, 450], # Box 9: Overlaps with Boxes 10, 11
    [110, 360, 210, 460], # Box 10: Overlaps with Boxes 9, 11
    [120, 370, 220, 470], # Box 11: Overlaps with Boxes 9, 10
    [400, 50, 500, 150],  # Box 12: No overlap
]
scores = [0.9, 0.8, 0.95, 0.85, 0.7, 0.88, 0.82, 0.87, 0.91, 0.83, 0.86, 0.75]  # Confidence scores
iou_threshold = 0.2

# Apply NMS
keep_indices = non_max_suppression(boxes, scores, iou_threshold)

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 500)
ax.set_ylim(0, 500)
# Generate distinct colors for original boxes
colors = ['red', 'green', 'purple', 'orange', 'cyan']
if len(colors) < len(boxes):
    # If we need more colors, generate random ones
    colors += [(random.random(), random.random(), random.random()) for _ in range(len(boxes) - len(colors))]

# Plot all original boxes with distinct colors
for i, box in enumerate(boxes):
    x, y, x2, y2 = box
    width = x2 - x
    height = y2 - y
    rect = patches.Rectangle(
        (x, y), width, height, 
        linewidth=1, edgecolor=colors[i], facecolor='none', 
        alpha=0.6, label=f'Original Box {i+1} (Score: {scores[i]})'
    )
    ax.add_patch(rect)

# Plot kept boxes (in blue, solid, thicker line)
for i in keep_indices:
    x, y, x2, y2 = boxes[i]
    width = x2 - x
    height = y2 - y
    rect = patches.Rectangle(
        (x, y), width, height, 
        linewidth=3, edgecolor='blue', facecolor='none', 
        label=f'Kept Box {i+1} (Score: {scores[i]})' if i == keep_indices[0] else None
    )
    ax.add_patch(rect)

# Add legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Save and show the plot
plt.show()