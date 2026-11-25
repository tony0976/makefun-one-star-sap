"""Writes a houseplant's one-star review of its human owner to /output/entry.txt."""
import os

TEXT = "One star. You bought me to 'bring life to the room' and I have spent three months watching you bring takeout to your desk instead. The light is excellent. The company is not."

# Rule: the review must be a single line of 1 to 279 characters.
# The joke lands on the plant grading its owner back: the light is fine,
# the company is not — a genuine one-star review, not a wilting cliché.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 279, f"entry must be one line, 1-279 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
