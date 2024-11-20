import os

# Define the folder and disaster information
folder_name = "todo"
disasters = {
    "Earthquake": "1. Drop to your hands and knees to prevent being knocked over.\n2. Cover your head and neck to protect yourself from falling debris.\n3. Hold on to your shelter until the shaking stops.\n4. Stay indoors and away from windows and heavy objects.\n5. If outside, move to an open area away from buildings, trees, and power lines.",
    "Tsunami": "1. Move to higher ground immediately and stay there until the danger has passed.\n2. Avoid going to the beach or trying to watch the tsunami.\n3. Follow official warnings and evacuation orders.\n4. If you are in a boat, head out to deep water if possible.\n5. Be prepared for possible aftershocks and additional waves.",
    "Flood": "1. Move to higher ground or a safe location immediately.\n2. Avoid walking or driving through floodwaters.\n3. Turn off utilities if instructed to do so.\n4. Follow local evacuation orders and avoid flooded areas.\n5. Be aware of potential landslides in flood-affected areas.",
    "Volcanic Eruption": "1. Follow evacuation orders and move to a safe location away from the volcano.\n2. Wear a mask to protect your lungs from ash inhalation.\n3. Protect your eyes and skin from volcanic ash.\n4. Avoid driving as ash can reduce visibility and damage engines.\n5. Stay indoors and keep windows and doors closed to prevent ash from entering.",
    "Landslide": "1. Move to higher ground and away from areas prone to landslides.\n2. Avoid crossing areas with visible landslide damage.\n3. Follow evacuation orders and avoid using roads that may be unstable.\n4. Be cautious of possible debris flows and aftershocks.\n5. Stay informed through local authorities about potential risks.",
    "Wildfire": "1. Follow evacuation orders and leave the area immediately if instructed.\n2. Stay indoors with windows and doors closed if you cannot evacuate.\n3. Use N95 masks to protect your lungs from smoke inhalation.\n4. Avoid driving through smoky areas and use headlights.\n5. Stay informed through local news and emergency services."
}

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# Write the disaster responses to corresponding text files
for disaster, response in disasters.items():
    file_path = os.path.join(folder_name, f"{disaster}.txt")
    with open(file_path, 'w') as file:
        file.write(response)

print("Files created successfully in the 'todo' folder.")
