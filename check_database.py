from web_app.disease_database import DISEASE_DATABASE


# ============================================================
# YOUR MODEL CLASSES
# ============================================================

MODEL_CLASSES = [
    "anthracnose",
    "anthracnose_disease",
    "apple__black_rot",
    "apple__healthy",
    "apple_leaf",
    "apple_rust_leaf",
    "apple_scab_leaf",
    "banana_cordana",
    "bell_pepper_leaf",
    "bell_pepper_leaf_spot",
    "black_rot",
    "brown_stem_spot",
    "canker_disease",
    "citrus_canckerleaf",
    "citrus_fruit_disease",
    "citrus_healthy_fruit",
    "citrus_healthy_leaf",
    "corn_leaf_blight",
    "disease_apple_fruit",
    "disease_banana_fruit",
    "disease_mango_fruit",
    "fruit_rot",
    "fungi",
    "grape_leaf",
    "grape_leaf_black_rot",
    "gray_blight",
    "guava_disease_fruit",
    "guava_healthly_fruit",
    "guava_healthly_leaf",
    "guava_red_rust",
    "healthy",
    "healthy_banana_fruit",
    "healthy_banana_leaf",
    "healthy_fruit",
    "healthy_leaf",
    "healthy_mango_fruit",
    "mang_healthy_leaf",
    "mango_bacterial_canker",
    "mealybug_infestation",
    "papaya_fruit_disease",
    "papaya_fruit_healthy",
    "papaya_healthy_leaf",
    "papaya_ringspot",
    "pink_disease",
    "potato_leaf_early_blight",
    "potato_leaf_late_blight",
    "rust",
    "scab",
    "soft_rot",
    "sooty_mold",
    "stem_blight",
    "stem_canker",
    "stem_cracking_gummosis",
    "sunburn",
    "thrips_disease",
    "tomato_early_blight_leaf",
    "tomato_leaf",
    "tomato_leaf_bacterial_spot",
    "tomato_leaf_late_blight",
    "tomato_leaf_yellow_virus",
    "tomato_septoria_leaf_spot",
    "yellow_leaf"
]


# ============================================================
# CHECK COUNTS
# ============================================================

print("=" * 60)
print("DISEASE DATABASE VERIFICATION")
print("=" * 60)

print()
print("Model classes:", len(MODEL_CLASSES))
print("Database entries:", len(DISEASE_DATABASE))


# ============================================================
# CHECK DUPLICATE MODEL CLASSES
# ============================================================

duplicates = [
    cls for cls in set(MODEL_CLASSES)
    if MODEL_CLASSES.count(cls) > 1
]

print()
print("Duplicate model classes:")

if duplicates:
    for item in duplicates:
        print("  ❌", item)
else:
    print("  ✅ None")


# ============================================================
# FIND MISSING DATABASE ENTRIES
# ============================================================

missing = [
    cls for cls in MODEL_CLASSES
    if cls not in DISEASE_DATABASE
]

print()
print("Missing database entries:")

if missing:
    for item in missing:
        print("  ❌", item)
else:
    print("  ✅ None")


# ============================================================
# FIND EXTRA DATABASE ENTRIES
# ============================================================

extra = [
    key for key in DISEASE_DATABASE
    if key not in MODEL_CLASSES
]

print()
print("Extra database entries:")

if extra:
    for item in extra:
        print("  ⚠️", item)
else:
    print("  ✅ None")


# ============================================================
# VERIFY EVERY ENTRY HAS BASIC INFORMATION
# ============================================================

required_fields = [
    "plant",
    "disease",
    "affected_part",
    "disease_type",
    "cause",
    "pathogen",
    "symptoms",
    "why_it_happens",
    "favorable_conditions",
    "prevention",
    "immediate_action",
    "cultural_control",
    "biological_control",
    "chemical_control",
    "safety_warning"
]


print()
print("Checking database fields...")
print()

bad_entries = []

for class_name in MODEL_CLASSES:

    if class_name not in DISEASE_DATABASE:
        continue

    entry = DISEASE_DATABASE[class_name]

    missing_fields = [
        field
        for field in required_fields
        if field not in entry
    ]

    if missing_fields:

        bad_entries.append(
            (class_name, missing_fields)
        )

        print(
            "❌",
            class_name,
            "missing:",
            ", ".join(missing_fields)
        )


if not bad_entries:
    print("✅ All classes contain all required fields.")


# ============================================================
# FINAL RESULT
# ============================================================

print()
print("=" * 60)

if (
    len(MODEL_CLASSES) == 62
    and
    not missing
    and
    not extra
    and
    not duplicates
    and
    not bad_entries
):

    print("✅ DATABASE VERIFICATION PASSED")
    print("✅ 62 model classes are covered.")
    print("✅ Database structure is ready.")

else:

    print("❌ DATABASE VERIFICATION FAILED")
    print("Fix the problems shown above before connecting app.py.")

print("=" * 60)