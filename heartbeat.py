age = int(input("Please enter your age "))
heart_beat_65 = round((220 - age) * 0.65)
heart_beat_85 = round((220 - age) * 0.85)
print(f"Keep your heart rate between {heart_beat_65} and {heart_beat_85} beats per minute")