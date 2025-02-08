import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

font_path = "../AdditionalFilesDirectory/Aloevera.ttf"
custom_font = FontProperties(fname=font_path)

data = {
    "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "temperature": [5, 7, 12, 18, 24, 29, 31, 30, 25, 18, 11, 6],
    "humidity": [80, 78, 70, 60, 50, 45, 50, 55, 60, 65, 75, 80],
    "rainfall": [120, 100, 80, 60, 30, 20, 25, 40, 60, 90, 110, 130]
}

angles = [0, 0.52359878, 1.04719755, 1.57079633, 2.0943951,  2.61799388, 3.14159265, 3.66519143, 4.1887902, 4.71238898, 5.23598776, 5.75958653]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'}, facecolor="#fee4f2", dpi = 250)

ax.plot(angles, data["temperature"], color='orange', linewidth=2, linestyle='-', marker='o', label='Temperature (C)')

ax.plot(angles, data["humidity"], color='skyblue', linewidth=2, linestyle='--', marker='s', label='Humidity (%)')

ax.plot(angles, data["rainfall"], color='purple', linewidth=2, linestyle=':', marker='^', label='Rainfall (mm)')

ax.set_xticks(angles)
ax.set_xticklabels(data["months"], fontsize=12, color="black", fontproperties=custom_font)
ax.set_title("Monthly Climate Data", fontsize=16, color='black', pad=20, fontproperties=custom_font)
ax.set_yticks([10, 20, 30, 40, 50])
ax.set_yticklabels([], fontsize=10, color="black")

legend = ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.2), frameon=True, facecolor="#fee4f2", fontsize=10)
for text in legend.get_texts():
    text.set_font_properties(custom_font)

plt.tight_layout()
plt.show()