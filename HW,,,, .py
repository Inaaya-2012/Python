import math


angle_deg = float(input("Enter the angle in degrees: "))


angle_rad = math.radians(angle_deg)


sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)


print(f"\nFor angle {angle_deg} degrees:")
print(f"Sine (sin): {sin_value:.4f}")
print(f"Cosine (cos): {cos_value:.4f}")


if cos_value == 0:
    print("Tangent (tan): undefined (division by zero)")
else:
    print(f"Tangent (tan): {tan_value:.4f}")
