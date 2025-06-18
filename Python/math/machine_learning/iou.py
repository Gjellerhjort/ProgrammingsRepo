import matplotlib.pyplot as plt


bouding_box_1 = [0, 0, 20, 20]
bouding_box_2 = [10, 10, 30, 30]

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


Iou = IntersectionOverArea(bouding_box_1, bouding_box_2)
print(f"IoU: {Iou:.2f}")

fig, ax = plt.subplots()
ax.add_patch(plt.Rectangle((bouding_box_1[0], bouding_box_1[1]), bouding_box_1[2] - bouding_box_1[0], bouding_box_1[3] - bouding_box_1[1], fill=False, edgecolor='red', linewidth=2))
ax.add_patch(plt.Rectangle((bouding_box_2[0], bouding_box_2[1]), bouding_box_2[2] - bouding_box_2[0], bouding_box_2[3] - bouding_box_2[1], fill=False, edgecolor='blue', linewidth=2))
ax.add_patch(plt.Rectangle((max(bouding_box_1[0], bouding_box_2[0]), max(bouding_box_1[1], bouding_box_2[1])), min(bouding_box_1[2], bouding_box_2[2]) - max(bouding_box_1[0], bouding_box_2[0]), min(bouding_box_1[3], bouding_box_2[3]) - max(bouding_box_1[1], bouding_box_2[1]), fill=True, color='purple', alpha=0.5))
plt.xlim(-10, 40)
plt.ylim(-10, 40)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

