# ============================================================
# DISEASE DATABASE
# PART 1 — CLASSES 1 TO 11
# ============================================================
PART_1_DATABASE = {


    # ========================================================
    # 1. anthracnose
    # ========================================================

    "anthracnose": {

        "plant": "Multiple / unspecified",
        "disease": "Anthracnose",
        "affected_part": "Leaf / Fruit / Stem",
        "disease_type": "Fungal",

        "cause": (
            "Anthracnose is a group of fungal diseases caused by "
            "different fungi depending on the host plant."
        ),

        "pathogen": (
            "Host-dependent anthracnose fungi; the exact pathogen "
            "cannot be determined from this generic model class alone."
        ),

        "symptoms": [
            "Dark or brown leaf spots",
            "Sunken lesions on fruit",
            "Dark lesions on stems or twigs",
            "Premature leaf drop may occur",
            "Fruit lesions may enlarge and become sunken"
        ],

        "why_it_happens": [
            "Infection is favored by prolonged leaf wetness",
            "High humidity can increase disease development",
            "Infected plant debris can provide a source of fungal inoculum",
            "Rain splash can spread spores"
        ],

        "favorable_conditions": [
            "Warm and humid weather",
            "Frequent rainfall",
            "Long periods of leaf wetness",
            "Poor air circulation",
            "Dense plant canopy"
        ],

        "prevention": [
            "Use disease-free planting material",
            "Improve air circulation",
            "Avoid unnecessary overhead irrigation",
            "Remove infected plant debris",
            "Monitor plants regularly"
        ],

        "immediate_action": [
            "Remove severely infected plant parts",
            "Separate severely diseased plants when practical",
            "Avoid handling plants when foliage is wet",
            "Remove fallen infected debris"
        ],

        "cultural_control": [
            "Prune to improve airflow",
            "Maintain appropriate plant spacing",
            "Remove infected debris",
            "Use clean tools",
            "Avoid excessive irrigation"
        ],

        "biological_control": [
            "Biological control options depend on the crop and pathogen.",
            "Use only products registered for the specific crop and disease."
        ],

        "chemical_control": (
            "Chemical control is host-specific. Use only a locally "
            "registered fungicide whose label lists the crop and "
            "anthracnose. Follow the product label exactly."
        ),

        "safety_warning": (
            "Do not apply a fungicide solely because a plant is "
            "classified as anthracnose. Confirm the crop, disease, "
            "local registration, label directions, PPE and harvest "
            "interval before treatment."
        )
    },


    # ========================================================
    # 2. anthracnose_disease
    # ========================================================

    "anthracnose_disease": {

        "plant": "Multiple / unspecified",
        "disease": "Anthracnose",
        "affected_part": "Leaf / Fruit / Stem",
        "disease_type": "Fungal",

        "cause": (
            "A generic anthracnose disease classification. "
            "The exact causal fungus depends on the host plant."
        ),

        "pathogen": (
            "Host-specific anthracnose fungi; exact species "
            "cannot be determined from this generic class label."
        ),

        "symptoms": [
            "Brown to dark leaf lesions",
            "Sunken fruit spots",
            "Dark stem lesions",
            "Lesions may enlarge during wet weather",
            "Severe infections can cause tissue death"
        ],

        "why_it_happens": [
            "Fungal spores can spread by rain splash",
            "High humidity favors infection",
            "Wet plant surfaces increase infection risk",
            "Infected crop residue can maintain inoculum"
        ],

        "favorable_conditions": [
            "Warm temperatures",
            "High relative humidity",
            "Frequent rain",
            "Long periods of leaf wetness",
            "Dense foliage"
        ],

        "prevention": [
            "Use clean planting material",
            "Remove diseased plant material",
            "Improve canopy ventilation",
            "Avoid prolonged leaf wetness",
            "Monitor plants frequently"
        ],

        "immediate_action": [
            "Remove severely affected tissue where practical",
            "Collect fallen infected material",
            "Avoid spreading water from infected to healthy plants",
            "Sanitize tools after working on infected plants"
        ],

        "cultural_control": [
            "Improve plant spacing",
            "Prune dense growth where appropriate",
            "Use drip or base irrigation where suitable",
            "Remove crop debris",
            "Maintain field sanitation"
        ],

        "biological_control": [
            "Use only crop-specific biological products "
            "that are registered for the disease."
        ],

        "chemical_control": (
            "Because this is a generic class, no single fungicide "
            "should be recommended without knowing the host crop. "
            "Use a locally registered product labeled for the "
            "specific crop and anthracnose."
        ),

        "safety_warning": (
            "This model class does not identify the host crop. "
            "Do not automatically recommend a pesticide until "
            "the crop and disease have been confirmed."
        )
    },


    # ========================================================
    # 3. apple__black_rot
    # ========================================================

    "apple__black_rot": {

        "plant": "Apple",
        "disease": "Black Rot",
        "affected_part": "Leaf / Fruit / Branch",
        "disease_type": "Fungal",

        "cause": (
            "Apple black rot is a fungal disease that can affect "
            "leaves, fruit and branches."
        ),

        "pathogen": (
            "Diplodia seriata "
            "(synonym historically associated with Botryosphaeria obtusa)."
        ),

        "symptoms": [
            "Frogeye-type circular leaf spots",
            "Purple or reddish margins around leaf spots",
            "Tan centers in leaf lesions",
            "Brown to black fruit rot",
            "Concentric rings may develop on fruit",
            "Mummified fruit may remain attached to the tree",
            "Sunken reddish-brown branch cankers",
            "Cracked or rough bark around cankers"
        ],

        "why_it_happens": [
            "The fungus survives in dead or diseased plant tissue",
            "Mummified fruit and branch cankers can produce spores",
            "Spores spread through wind and splashing water",
            "Tree stress can increase susceptibility",
            "Dead or damaged wood provides infection sites"
        ],

        "favorable_conditions": [
            "Wet weather",
            "High moisture",
            "Damaged wood",
            "Drought-stressed trees",
            "Poorly drained conditions",
            "Existing dead branches or mummified fruit"
        ],

        "prevention": [
            "Prune dead and diseased branches",
            "Remove mummified fruit",
            "Remove infected plant material",
            "Maintain good tree health",
            "Avoid unnecessary tree injury",
            "Monitor trees for cankers"
        ],

        "immediate_action": [
            "Remove infected fruit",
            "Prune infected branches where appropriate",
            "Remove dead wood",
            "Remove fallen or mummified fruit",
            "Dispose of infected material appropriately"
        ],

        "cultural_control": [
            "Maintain orchard sanitation",
            "Prune correctly",
            "Reduce tree stress",
            "Remove dead wood",
            "Improve tree structure and airflow"
        ],

        "biological_control": [
            "No universal biological treatment should be assumed "
            "for this class. Crop-specific registered biological "
            "products should be considered only where supported."
        ],

        "chemical_control": (
            "Extension guidance indicates that fungicides are rarely "
            "needed for apple black rot when sanitation and tree-care "
            "practices are properly used. If chemical control is "
            "needed, use only a fungicide registered for apples and "
            "black rot in your region."
        ),

        "safety_warning": (
            "Follow the fungicide label for crop, disease, rate, "
            "PPE, application timing and pre-harvest interval."
        )
    },


    # ========================================================
    # 4. apple__healthy
    # ========================================================

    "apple__healthy": {

        "plant": "Apple",
        "disease": "No Disease",
        "affected_part": "Leaf / Plant",
        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Leaf appears consistent with a healthy apple class"
        ],

        "why_it_happens": [
            "The image was classified as the healthy apple class."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain balanced irrigation",
            "Maintain appropriate nutrition",
            "Monitor leaves and fruit regularly",
            "Maintain good orchard sanitation",
            "Monitor for early signs of pests and disease"
        ],

        "immediate_action": [
            "No disease treatment is indicated from this classification.",
            "Continue routine plant monitoring."
        ],

        "cultural_control": [
            "Maintain good airflow",
            "Remove dead plant material",
            "Maintain appropriate irrigation",
            "Use clean pruning equipment"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for a "
            "healthy plant based solely on this model classification."
        ),

        "safety_warning": (
            "A healthy classification does not guarantee that the "
            "entire plant is disease-free. Continue normal monitoring."
        )
    },


    # ========================================================
    # 5. apple_leaf
    # ========================================================

    "apple_leaf": {

        "plant": "Apple",
        "disease": "Apple Leaf",
        "affected_part": "Leaf",
        "disease_type": "Unspecified / Dataset Class",

        "cause": (
            "This class name identifies an apple leaf but does not "
            "specify a particular disease."
        ),

        "pathogen": "",

        "symptoms": [
            "No specific disease can be inferred from this class label alone."
        ],

        "why_it_happens": [
            "The dataset class represents an apple leaf image rather "
            "than a clearly named disease."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain good plant hygiene",
            "Monitor leaves regularly",
            "Maintain adequate airflow",
            "Avoid prolonged leaf wetness"
        ],

        "immediate_action": [
            "Do not apply disease-specific treatment solely from this class.",
            "Inspect the plant for visible disease symptoms."
        ],

        "cultural_control": [
            "Maintain sanitation",
            "Remove obviously diseased material",
            "Maintain appropriate irrigation",
            "Monitor the tree regularly"
        ],

        "biological_control": [],

        "chemical_control": (
            "No chemical treatment should be recommended from this "
            "generic class alone because the class does not identify "
            "a specific disease."
        ),

        "safety_warning": (
            "Do not treat an unspecified apple-leaf classification "
            "as a confirmed disease."
        )
    },


    # ========================================================
    # 6. apple_rust_leaf
    # ========================================================

    "apple_rust_leaf": {

        "plant": "Apple",
        "disease": "Apple Rust",
        "affected_part": "Leaf / Fruit",
        "disease_type": "Fungal",

        "cause": (
            "Apple rust is caused by rust fungi and, for cedar-apple "
            "rust, requires a compatible alternate host such as juniper "
            "or red cedar."
        ),

        "pathogen": (
            "Gymnosporangium species; the exact species depends on "
            "the rust disease."
        ),

        "symptoms": [
            "Yellow spots on leaves",
            "Bright orange leaf spots",
            "Red or reddish margins around spots",
            "Small raised structures may develop on leaf surfaces",
            "Fruit can develop rough green-brown lesions"
        ],

        "why_it_happens": [
            "Rust fungi can require alternate hosts to complete their life cycle",
            "Spores can be carried between host plants",
            "Wet conditions favor infection"
        ],

        "favorable_conditions": [
            "Wet spring weather",
            "Leaf wetness",
            "Presence of compatible alternate hosts",
            "Suitable temperatures during infection periods"
        ],

        "prevention": [
            "Monitor trees early in the season",
            "Use resistant cultivars where available",
            "Manage alternate hosts where locally appropriate",
            "Maintain good tree health"
        ],

        "immediate_action": [
            "Inspect surrounding plants for alternate hosts",
            "Remove severely affected plant material where appropriate",
            "Monitor new growth for additional symptoms"
        ],

        "cultural_control": [
            "Maintain tree vigor",
            "Improve airflow",
            "Use resistant varieties where available",
            "Manage alternate hosts according to local extension guidance"
        ],

        "biological_control": [],

        "chemical_control": (
            "If fungicide treatment is required, use a product "
            "registered for apples and the specific rust disease. "
            "Timing is generally important because fungicides are "
            "most useful preventively."
        ),

        "safety_warning": (
            "Confirm the exact rust disease and check that the product "
            "label permits use on apple before applying any fungicide."
        )
    },


    # ========================================================
    # 7. apple_scab_leaf
    # ========================================================

    "apple_scab_leaf": {

        "plant": "Apple",
        "disease": "Apple Scab",
        "affected_part": "Leaf / Fruit",
        "disease_type": "Fungal",

        "cause": (
            "Apple scab is caused by the fungus Venturia inaequalis."
        ),

        "pathogen": "Venturia inaequalis",

        "symptoms": [
            "Olive-green to brown leaf spots",
            "Irregular or feathered lesion margins",
            "Spots can become dark brown to black",
            "Leaves may yellow and drop prematurely",
            "Brown raised corky spots can occur on fruit",
            "Severely affected fruit may become deformed or cracked"
        ],

        "why_it_happens": [
            "The fungus survives winter in infected fallen leaves",
            "Spring rain releases spores from infected leaf litter",
            "Spores spread by rain and wind",
            "Repeated wetting events can produce repeated infection cycles"
        ],

        "favorable_conditions": [
            "Wet spring weather",
            "Leaf wetness",
            "Rainfall",
            "Dense canopies that dry slowly"
        ],

        "prevention": [
            "Remove or accelerate decomposition of fallen leaves",
            "Maintain an open canopy",
            "Prune appropriately",
            "Use resistant varieties where available",
            "Monitor during wet spring conditions"
        ],

        "immediate_action": [
            "Remove fallen infected leaves",
            "Improve canopy airflow",
            "Monitor new leaves",
            "Follow a locally appropriate apple-scab management program"
        ],

        "cultural_control": [
            "Rake and remove fallen leaves",
            "Chop leaves to accelerate decomposition",
            "Prune to improve air movement",
            "Avoid excessive canopy density"
        ],

        "biological_control": [
            "Biological products may be available in some production "
            "systems, but their suitability depends on local registration "
            "and the specific management program."
        ],

        "chemical_control": (
            "Fungicides may be used in commercial disease-management "
            "programs when appropriate. Product choice and timing "
            "must follow local apple-scab recommendations and the "
            "current pesticide label."
        ),

        "safety_warning": (
            "Do not give a fixed pesticide dose in this database. "
            "Rates, permitted products and pre-harvest intervals "
            "depend on the product label and jurisdiction."
        )
    },


    # ========================================================
    # 8. banana_cordana
    # ========================================================

    "banana_cordana": {

        "plant": "Banana",
        "disease": "Cordana Leaf Spot",
        "affected_part": "Leaf",
        "disease_type": "Fungal",

        "cause": (
            "Cordana leaf spot is a fungal leaf disease of banana."
        ),

        "pathogen": (
            "Cordana species; exact species identification may vary "
            "by diagnostic source and region."
        ),

        "symptoms": [
            "Brown leaf spots",
            "Spots may enlarge into larger necrotic areas",
            "Older leaves may show more severe damage",
            "Severe leaf damage can reduce functional leaf area"
        ],

        "why_it_happens": [
            "Fungal spores can spread under humid conditions",
            "Wet foliage favors foliar disease development",
            "Dense banana canopies can retain moisture"
        ],

        "favorable_conditions": [
            "High humidity",
            "Frequent rainfall",
            "Long periods of leaf wetness",
            "Poor air circulation"
        ],

        "prevention": [
            "Remove severely infected leaves",
            "Improve plantation airflow",
            "Avoid unnecessary leaf wetness",
            "Maintain field sanitation",
            "Monitor leaves regularly"
        ],

        "immediate_action": [
            "Remove severely damaged leaves when practical",
            "Dispose of diseased material appropriately",
            "Avoid spreading contaminated material",
            "Improve airflow around plants"
        ],

        "cultural_control": [
            "Maintain appropriate plant spacing",
            "Remove heavily diseased leaves",
            "Keep the plantation clean",
            "Avoid excessive overhead irrigation"
        ],

        "biological_control": [
            "Use only biological products registered for banana "
            "and the relevant fungal disease."
        ],

        "chemical_control": (
            "Use only a fungicide registered for banana and labeled "
            "for the relevant leaf-spot disease in your region. "
            "Follow the label and local banana disease-management guidance."
        ),

        "safety_warning": (
            "Do not assume a fungicide used for one banana leaf disease "
            "is appropriate for Cordana leaf spot."
        )
    },


    # ========================================================
    # 9. bell_pepper_leaf
    # ========================================================

    "bell_pepper_leaf": {

        "plant": "Bell Pepper",
        "disease": "Bell Pepper Leaf",
        "affected_part": "Leaf",
        "disease_type": "Unspecified / Dataset Class",

        "cause": (
            "The class identifies a bell pepper leaf but does not "
            "identify a specific disease."
        ),

        "pathogen": "",

        "symptoms": [
            "No specific disease can be confirmed from the class name alone."
        ],

        "why_it_happens": [
            "This dataset class represents a bell pepper leaf rather "
            "than a clearly specified disease."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Monitor leaves regularly",
            "Use clean planting material",
            "Maintain good airflow",
            "Avoid unnecessary leaf wetness",
            "Maintain field sanitation"
        ],

        "immediate_action": [
            "Inspect the leaf for visible disease symptoms",
            "Do not apply disease-specific pesticide based only on this class"
        ],

        "cultural_control": [
            "Maintain good plant spacing",
            "Use clean tools",
            "Remove confirmed diseased plant material",
            "Avoid working with plants when foliage is wet"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific chemical treatment should be "
            "recommended from this class alone."
        ),

        "safety_warning": (
            "This is an unspecified bell-pepper leaf class. "
            "A separate diagnosis is needed before recommending treatment."
        )
    },


    # ========================================================
    # 10. bell_pepper_leaf_spot
    # ========================================================

    "bell_pepper_leaf_spot": {

        "plant": "Bell Pepper",
        "disease": "Bacterial Leaf Spot",
        "affected_part": "Leaf / Fruit",
        "disease_type": "Bacterial",

        "cause": (
            "Bacterial leaf spot of pepper is caused by several "
            "Xanthomonas species."
        ),

        "pathogen": (
            "Xanthomonas vesicatoria, X. euvesicatoria, "
            "X. gardneri and X. perforans can cause bacterial spot "
            "on tomato and pepper."
        ),

        "symptoms": [
            "Small brown circular spots on leaves",
            "Pepper leaf spots may not have a strong yellow halo",
            "Spots may occur on stems and fruit calyx",
            "Fruit can develop raised brown spots",
            "Severe infections can cause extensive leaf damage"
        ],

        "why_it_happens": [
            "Bacteria can enter through infected seed or transplants",
            "Rain splash and irrigation water can spread bacteria",
            "Tools and hands can spread the pathogen",
            "Infected crop debris can support survival"
        ],

        "favorable_conditions": [
            "Warm temperatures",
            "High humidity",
            "Frequent rainfall",
            "Overhead irrigation",
            "Wet foliage"
        ],

        "prevention": [
            "Use disease-free seed and transplants",
            "Avoid overhead irrigation",
            "Water at the base of plants",
            "Provide adequate spacing",
            "Remove infected plant debris",
            "Sanitize tools"
        ],

        "immediate_action": [
            "Remove leaves with significant symptoms when practical",
            "Avoid handling plants when wet",
            "Remove heavily infected plants when necessary",
            "Disinfect tools after working with infected plants"
        ],

        "cultural_control": [
            "Use certified disease-free seed",
            "Inspect transplants before planting",
            "Use drip or soaker irrigation",
            "Maintain plant spacing",
            "Remove crop debris after harvest",
            "Rotate away from susceptible crops where appropriate"
        ],

        "biological_control": [
            "Some biological products may be registered for bacterial "
            "disease management depending on location and production system."
        ],

        "chemical_control": (
            "Chemical options for bacterial spot are limited and "
            "resistance to copper can occur. If a bactericide is used, "
            "choose a product currently registered for pepper and "
            "bacterial spot in your region and follow the label."
        ),

        "safety_warning": (
            "Do not use a generic pesticide dose. Confirm that the "
            "product is labeled for bell pepper and bacterial spot, "
            "and follow PPE, application and harvest restrictions."
        )
    },


    # ========================================================
    # 11. black_rot
    # ========================================================

    "black_rot": {

        "plant": "Multiple / unspecified",
        "disease": "Black Rot",
        "affected_part": "Leaf / Fruit / Stem",
        "disease_type": "Unspecified",

        "cause": (
            "Black rot is a name used for different diseases on "
            "different crops. The exact cause depends on the host."
        ),

        "pathogen": (
            "Host-specific. This generic class does not identify "
            "the crop or causal organism."
        ),

        "symptoms": [
            "Dark or black lesions",
            "Leaf necrosis",
            "Fruit rot may develop",
            "Stem or branch lesions may occur depending on host"
        ],

        "why_it_happens": [
            "The name black rot describes multiple crop diseases",
            "Moisture can favor several black-rot pathogens",
            "Infected plant debris may act as a source of inoculum",
            "Wounds can provide entry points for some pathogens"
        ],

        "favorable_conditions": [
            "High humidity",
            "Wet foliage",
            "Rainfall",
            "Poor airflow",
            "Plant injury"
        ],

        "prevention": [
            "Identify the host crop before treatment",
            "Use disease-free planting material",
            "Remove infected debris",
            "Improve airflow",
            "Avoid unnecessary plant injury"
        ],

        "immediate_action": [
            "Determine the plant species first",
            "Inspect affected plant parts",
            "Remove severely infected material where appropriate",
            "Avoid spreading contaminated water or tools"
        ],

        "cultural_control": [
            "Maintain sanitation",
            "Improve drainage where relevant",
            "Improve air circulation",
            "Remove infected debris",
            "Use clean tools"
        ],

        "biological_control": [
            "Biological control depends on the host and pathogen."
        ],

        "chemical_control": (
            "No single chemical treatment should be attached to this "
            "generic class. The correct treatment depends on the host "
            "plant and the actual pathogen."
        ),

        "safety_warning": (
            "Do not recommend a pesticide from the term 'black rot' "
            "alone. Different crops can have completely different "
            "black-rot pathogens and treatment programs."
        )
    }

}
# ============================================================
# DISEASE DATABASE
# PART 2 — CLASSES 12 TO 22
# ============================================================


# NOTE:
# These entries are keyed by the EXACT model class names.
# Do not rename the dictionary keys unless labels.txt is also changed.


PART_2_DATABASE = {


    # ========================================================
    # 12. brown_stem_spot
    # ========================================================

    "brown_stem_spot": {

        "plant": "Multiple / unspecified",

        "disease": "Brown Stem Spot",

        "affected_part": "Stem / Branch",

        "disease_type": "Unspecified",

        "cause": (
            "The model class identifies a brown spot condition on "
            "stem tissue, but the class name alone does not identify "
            "the host plant or causal organism."
        ),

        "pathogen": (
            "Not specified by the model class. The causal organism "
            "must be determined from the host crop and diagnostic evidence."
        ),

        "symptoms": [
            "Brown or dark lesions on stems",
            "Localized discoloration of stem tissue",
            "Lesions may enlarge over time",
            "Severe lesions may weaken affected tissue",
            "Additional symptoms depend on the host plant"
        ],

        "why_it_happens": [
            "The exact cause depends on the host plant",
            "Some stem-spot diseases are associated with fungi or bacteria",
            "Plant wounds can provide infection sites",
            "High moisture can favor some plant pathogens"
        ],

        "favorable_conditions": [
            "High humidity",
            "Prolonged moisture",
            "Poor air circulation",
            "Plant injury",
            "Weak or stressed plants"
        ],

        "prevention": [
            "Maintain plant vigor",
            "Avoid unnecessary stem injury",
            "Maintain good airflow",
            "Remove confirmed diseased plant material",
            "Use clean planting material",
            "Monitor stems regularly"
        ],

        "immediate_action": [
            "Inspect the entire plant",
            "Determine the plant species",
            "Remove severely affected tissue where appropriate",
            "Keep tools clean",
            "Avoid spreading contaminated material"
        ],

        "cultural_control": [
            "Improve air circulation",
            "Avoid excessive moisture around plant tissue",
            "Remove diseased debris",
            "Use clean pruning equipment",
            "Maintain appropriate plant spacing"
        ],

        "biological_control": [
            "Biological control depends on the crop and causal organism.",
            "Use only products registered for the specific crop and disease."
        ],

        "chemical_control": (
            "No universal pesticide should be assigned to this generic "
            "class. Chemical treatment depends on the crop and confirmed "
            "pathogen. Use only a locally registered product labeled for "
            "the specific crop and disease."
        ),

        "safety_warning": (
            "Do not apply a fungicide or bactericide based only on the "
            "name 'brown stem spot'. Confirm the host and disease first."
        )
    },


    # ========================================================
    # 13. canker_disease
    # ========================================================

    "canker_disease": {

        "plant": "Multiple / unspecified",

        "disease": "Canker Disease",

        "affected_part": "Stem / Branch / Trunk",

        "disease_type": "Fungal or Bacterial / Unspecified",

        "cause": (
            "Plant cankers are localized areas of dead tissue on "
            "branches, stems, trunks, or sometimes roots. Different "
            "plants can develop cankers from different pathogens."
        ),

        "pathogen": (
            "Host-dependent. Common canker pathogens include various "
            "fungi such as Botryosphaeria, Cytospora and Nectria species, "
            "while some cankers are bacterial."
        ),

        "symptoms": [
            "Sunken or discolored lesions",
            "Dead areas on stems or branches",
            "Cracked bark",
            "Oozing may occur in some diseases",
            "Cankers may enlarge and girdle stems",
            "Leaves above a girdling canker may wilt or die"
        ],

        "why_it_happens": [
            "Pathogens can enter through wounds",
            "Environmental stress can increase susceptibility",
            "Dead or weakened branches can provide infection sites",
            "Poor plant adaptation to the site can increase disease risk"
        ],

        "favorable_conditions": [
            "Plant stress",
            "Drought or inadequate moisture",
            "Excessive moisture for some pathogens",
            "Stem or branch injuries",
            "Poor sanitation"
        ],

        "prevention": [
            "Maintain plant vigor",
            "Avoid mechanical injury",
            "Prune correctly",
            "Remove dead and dying branches",
            "Use clean tools",
            "Choose suitable or resistant plant varieties where available"
        ],

        "immediate_action": [
            "Inspect the stem or branch carefully",
            "Prune affected branches when appropriate",
            "Cut below visible canker tissue into healthy wood",
            "Remove infected cuttings",
            "Clean pruning equipment"
        ],

        "cultural_control": [
            "Maintain proper irrigation",
            "Protect roots and stems from injury",
            "Remove dead wood",
            "Improve plant growing conditions",
            "Maintain sanitation"
        ],

        "biological_control": [
            "Biological control is pathogen- and crop-specific.",
            "Do not assume one biological product works for all cankers."
        ],

        "chemical_control": (
            "There is no universal chemical treatment for the generic "
            "canker class. Management is primarily based on identifying "
            "the host and pathogen, improving plant health, and removing "
            "infected tissue where appropriate."
        ),

        "safety_warning": (
            "The word 'canker' describes a symptom/disease group rather "
            "than one single disease. Confirm the crop and causal agent "
            "before recommending a pesticide."
        )
    },


    # ========================================================
    # 14. citrus_canckerleaf
    # Exact model spelling retained.
    # ========================================================

    "citrus_canckerleaf": {

        "plant": "Citrus",

        "disease": "Citrus Canker",

        "affected_part": "Leaf / Fruit / Stem",

        "disease_type": "Bacterial",

        "cause": (
            "Citrus canker is a bacterial disease affecting citrus "
            "leaves, fruit and stems."
        ),

        "pathogen": (
            "Xanthomonas citri subsp. citri is the principal pathogen "
            "associated with Asiatic citrus canker."
        ),

        "symptoms": [
            "Raised brown lesions",
            "Water-soaked margins around lesions",
            "Yellow halos may surround lesions",
            "Corky lesions can develop as they age",
            "Leaf lesions may become raised and rough",
            "Fruit lesions can become conspicuous and corky",
            "Premature leaf or fruit drop may occur"
        ],

        "why_it_happens": [
            "Bacteria can spread through wind-driven rain",
            "Rain splash can move bacteria between plant tissues",
            "Infected plant material can spread the pathogen",
            "Leaf injury can increase infection opportunities",
            "Some insect damage can create entry points"
        ],

        "favorable_conditions": [
            "Warm conditions",
            "High moisture",
            "Rainfall",
            "Wind-driven rain",
            "Young susceptible foliage",
            "Plant injury"
        ],

        "prevention": [
            "Use certified disease-free citrus planting material",
            "Follow local citrus quarantine requirements",
            "Avoid moving infected plant material",
            "Manage irrigation to reduce unnecessary leaf wetness",
            "Protect young foliage from injury where practical",
            "Inspect citrus plants regularly"
        ],

        "immediate_action": [
            "Isolate suspected infected plants where appropriate",
            "Avoid moving infected plant material",
            "Contact local plant-health authorities where required",
            "Do not transport suspected infected citrus material",
            "Follow local citrus-canker regulations"
        ],

        "cultural_control": [
            "Use certified nursery stock",
            "Maintain sanitation",
            "Control movement of infected material",
            "Reduce unnecessary plant injury",
            "Follow local quarantine and eradication requirements"
        ],

        "biological_control": [
            "No universal biological cure should be assumed.",
            "Management depends heavily on local regulatory programs."
        ],

        "chemical_control": (
            "Citrus canker is a regulated bacterial disease in many "
            "regions. Copper-based protectants may be used in some "
            "management programs to reduce disease development, but "
            "they do not cure infected tissue. Use only products "
            "registered for citrus and citrus canker in your region."
        ),

        "safety_warning": (
            "Citrus canker is subject to plant-health regulations in "
            "some regions. Do not move or dispose of infected citrus "
            "material contrary to local regulations. Chemical treatment "
            "does not cure an infected tree."
        )
    },


    # ========================================================
    # 15. citrus_fruit_disease
    # ========================================================

    "citrus_fruit_disease": {

        "plant": "Citrus",

        "disease": "Citrus Fruit Disease",

        "affected_part": "Fruit",

        "disease_type": "Unspecified",

        "cause": (
            "The model class identifies a diseased citrus fruit but "
            "does not identify the specific disease."
        ),

        "pathogen": (
            "Not specified by the class. Citrus fruit diseases can "
            "have fungal, bacterial, viral, physiological or pest-related causes."
        ),

        "symptoms": [
            "Fruit discoloration",
            "Fruit spots or lesions",
            "Fruit decay may occur",
            "Surface abnormalities",
            "Premature fruit drop may occur"
        ],

        "why_it_happens": [
            "Different citrus diseases have different causes",
            "Wounds can allow some fruit-rotting organisms to enter",
            "High humidity can favor some fungal diseases",
            "Insect damage can create infection sites"
        ],

        "favorable_conditions": [
            "High humidity",
            "Wet conditions",
            "Fruit injury",
            "Poor sanitation",
            "Improper postharvest handling"
        ],

        "prevention": [
            "Handle fruit carefully",
            "Remove diseased fruit",
            "Maintain orchard sanitation",
            "Monitor fruit regularly",
            "Avoid unnecessary fruit injury"
        ],

        "immediate_action": [
            "Inspect the fruit for characteristic symptoms",
            "Separate severely diseased fruit",
            "Remove rotting fruit from the orchard or storage area",
            "Determine the specific disease before treatment"
        ],

        "cultural_control": [
            "Maintain orchard sanitation",
            "Minimize fruit wounds",
            "Remove fallen diseased fruit",
            "Maintain good canopy management"
        ],

        "biological_control": [
            "Biological control depends on the confirmed disease."
        ],

        "chemical_control": (
            "No chemical treatment should be assigned from this generic "
            "class alone. Identify the specific citrus fruit disease first."
        ),

        "safety_warning": (
            "Do not recommend a pesticide based solely on 'citrus fruit "
            "disease'. Different citrus diseases require different management."
        )
    },


    # ========================================================
    # 16. citrus_healthy_fruit
    # ========================================================

    "citrus_healthy_fruit": {

        "plant": "Citrus",

        "disease": "No Disease",

        "affected_part": "Fruit",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Fruit appears consistent with the healthy citrus class"
        ],

        "why_it_happens": [
            "The image was classified as healthy citrus fruit."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain balanced irrigation",
            "Maintain appropriate nutrition",
            "Monitor fruit regularly",
            "Maintain orchard sanitation",
            "Prevent unnecessary fruit injury"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated from this classification.",
            "Continue routine inspection."
        ],

        "cultural_control": [
            "Maintain orchard hygiene",
            "Remove damaged or rotting fruit",
            "Maintain appropriate irrigation",
            "Monitor plants regularly"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for healthy "
            "citrus fruit based solely on this classification."
        ),

        "safety_warning": (
            "A healthy fruit classification does not prove the entire "
            "citrus tree is free from disease or pests."
        )
    },


    # ========================================================
    # 17. citrus_healthy_leaf
    # ========================================================

    "citrus_healthy_leaf": {

        "plant": "Citrus",

        "disease": "No Disease",

        "affected_part": "Leaf",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Leaf appears consistent with the healthy citrus class"
        ],

        "why_it_happens": [
            "The image was classified as a healthy citrus leaf."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain adequate nutrition",
            "Maintain appropriate irrigation",
            "Monitor leaves for pests and disease",
            "Maintain good orchard sanitation",
            "Avoid unnecessary plant injury"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue regular citrus monitoring."
        ],

        "cultural_control": [
            "Maintain orchard hygiene",
            "Monitor new flush growth",
            "Maintain appropriate irrigation",
            "Control weeds where appropriate"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific chemical treatment is recommended "
            "for a healthy citrus leaf."
        ),

        "safety_warning": (
            "A healthy-leaf classification only describes the uploaded "
            "image; it does not guarantee that the whole tree is healthy."
        )
    },


    # ========================================================
    # 18. corn_leaf_blight
    # ========================================================

    "corn_leaf_blight": {

        "plant": "Corn",

        "disease": "Corn Leaf Blight",

        "affected_part": "Leaf",

        "disease_type": "Fungal",

        "cause": (
            "Corn leaf blight is a group of fungal diseases. "
            "The exact pathogen depends on whether the disease is "
            "northern or southern leaf blight."
        ),

        "pathogen": (
            "Northern leaf blight is associated with Exserohilum turcicum. "
            "Southern leaf blight is associated with Bipolaris maydis."
        ),

        "symptoms": [
            "Elongated leaf lesions",
            "Tan to brown lesions",
            "Lesions may enlarge and merge",
            "Severe disease can destroy large areas of foliage",
            "Premature loss of green leaf tissue may occur"
        ],

        "why_it_happens": [
            "Fungal spores can survive in infected crop residue",
            "Spores can spread by wind and rain",
            "Wet foliage favors infection",
            "Dense crop canopies can retain humidity"
        ],

        "favorable_conditions": [
            "Warm and humid conditions",
            "Frequent rainfall",
            "Extended leaf wetness",
            "Dense crop canopy",
            "Infected crop residue"
        ],

        "prevention": [
            "Use resistant or tolerant hybrids where available",
            "Practice crop rotation where appropriate",
            "Manage crop residue",
            "Monitor fields during favorable weather",
            "Maintain balanced crop nutrition"
        ],

        "immediate_action": [
            "Scout the field for disease progression",
            "Estimate disease severity",
            "Remove volunteer or heavily infected material where practical",
            "Consult local corn disease-management recommendations"
        ],

        "cultural_control": [
            "Use resistant hybrids",
            "Rotate crops where appropriate",
            "Manage infected residue",
            "Maintain balanced fertility",
            "Avoid unnecessary crop stress"
        ],

        "biological_control": [
            "Biological control options are not universal and depend "
            "on the production system and local registration."
        ],

        "chemical_control": (
            "Fungicides can be used in some corn production systems "
            "when disease risk and economic thresholds justify them. "
            "Use only a fungicide labeled for corn and the specific "
            "leaf-blight disease in your region."
        ),

        "safety_warning": (
            "The generic class does not distinguish northern from "
            "southern leaf blight. Confirm the disease before selecting "
            "a treatment."
        )
    },


    # ========================================================
    # 19. disease_apple_fruit
    # ========================================================

    "disease_apple_fruit": {

        "plant": "Apple",

        "disease": "Apple Fruit Disease",

        "affected_part": "Fruit",

        "disease_type": "Unspecified",

        "cause": (
            "The model class indicates diseased apple fruit but does "
            "not identify the specific disease."
        ),

        "pathogen": (
            "Not specified by the class. Apple fruit diseases can "
            "be caused by different fungi, bacteria, pests or physiological problems."
        ),

        "symptoms": [
            "Fruit spots",
            "Fruit discoloration",
            "Rotting tissue",
            "Sunken lesions may occur",
            "Premature fruit drop may occur",
            "Symptoms vary by the actual disease"
        ],

        "why_it_happens": [
            "Different apple fruit diseases have different causes",
            "Fruit wounds can allow pathogens to enter",
            "Wet conditions can favor some fungal pathogens",
            "Poor sanitation can increase inoculum"
        ],

        "favorable_conditions": [
            "High humidity",
            "Wet weather",
            "Fruit injury",
            "Poor orchard sanitation",
            "Infected fruit remaining on the tree or ground"
        ],

        "prevention": [
            "Remove diseased and mummified fruit",
            "Handle fruit carefully",
            "Maintain orchard sanitation",
            "Prune to improve airflow",
            "Monitor fruit regularly"
        ],

        "immediate_action": [
            "Separate severely diseased fruit",
            "Remove infected fruit from the tree where appropriate",
            "Remove fallen diseased fruit",
            "Identify the specific disease before chemical treatment"
        ],

        "cultural_control": [
            "Maintain orchard sanitation",
            "Remove mummified fruit",
            "Minimize fruit injury",
            "Improve canopy airflow",
            "Maintain healthy trees"
        ],

        "biological_control": [
            "Biological options depend on the confirmed apple fruit disease."
        ],

        "chemical_control": (
            "No single fungicide should be associated with this generic "
            "class. Confirm the specific disease and use only a product "
            "registered for that disease on apple."
        ),

        "safety_warning": (
            "Do not interpret this class as a specific apple disease. "
            "The model class only indicates diseased apple fruit."
        )
    },


    # ========================================================
    # 20. disease_banana_fruit
    # ========================================================

    "disease_banana_fruit": {

        "plant": "Banana",

        "disease": "Banana Fruit Disease",

        "affected_part": "Fruit",

        "disease_type": "Unspecified",

        "cause": (
            "The class indicates diseased banana fruit but does not "
            "identify the specific disease."
        ),

        "pathogen": (
            "Not specified. Banana fruit diseases can be caused by "
            "different fungi, bacteria and other factors."
        ),

        "symptoms": [
            "Dark fruit spots",
            "Brown or black lesions",
            "Fruit softening",
            "Fruit rot",
            "Premature ripening",
            "Shriveling may occur"
        ],

        "why_it_happens": [
            "Fruit wounds can provide entry points for pathogens",
            "High humidity can favor fruit-rotting fungi",
            "Poor sanitation can increase inoculum",
            "Improper harvesting and handling can increase bruising"
        ],

        "favorable_conditions": [
            "High humidity",
            "Warm conditions",
            "Fruit bruising",
            "Poor sanitation",
            "Poor postharvest handling"
        ],

        "prevention": [
            "Avoid bruising fruit",
            "Maintain field sanitation",
            "Harvest carefully",
            "Remove infected fruit",
            "Handle fruit carefully during transport and storage"
        ],

        "immediate_action": [
            "Separate diseased fruit",
            "Remove badly rotted fruit",
            "Avoid storing damaged fruit with healthy fruit",
            "Inspect adjacent fruit for symptoms"
        ],

        "cultural_control": [
            "Maintain field sanitation",
            "Minimize fruit injury",
            "Use clean harvesting equipment",
            "Maintain appropriate storage conditions",
            "Remove infected fruit"
        ],

        "biological_control": [
            "Biological control depends on the specific banana fruit disease."
        ],

        "chemical_control": (
            "No universal chemical treatment should be assigned to "
            "this generic class. Confirm the disease and use only "
            "products registered for banana and that specific disease."
        ),

        "safety_warning": (
            "Do not apply a pesticide to harvested banana fruit unless "
            "the product is specifically labeled for that use and "
            "postharvest application."
        )
    },


    # ========================================================
    # 21. disease_mango_fruit
    # ========================================================

    "disease_mango_fruit": {

        "plant": "Mango",

        "disease": "Mango Fruit Disease",

        "affected_part": "Fruit",

        "disease_type": "Unspecified",

        "cause": (
            "The model class identifies diseased mango fruit but does "
            "not identify the exact disease."
        ),

        "pathogen": (
            "Not specified. Mango fruit diseases include several "
            "fungal and bacterial diseases and postharvest rots."
        ),

        "symptoms": [
            "Dark fruit spots",
            "Brown or black lesions",
            "Sunken areas",
            "Fruit softening or decay",
            "Premature fruit drop",
            "Postharvest rot may occur"
        ],

        "why_it_happens": [
            "Different mango fruit diseases have different causes",
            "Fruit wounds can provide entry points",
            "Warm and humid conditions can favor fungal diseases",
            "Poor postharvest handling can increase fruit decay"
        ],

        "favorable_conditions": [
            "Warm humid weather",
            "High moisture",
            "Fruit injury",
            "Poor sanitation",
            "Poor postharvest handling"
        ],

        "prevention": [
            "Minimize fruit injury",
            "Remove diseased fruit",
            "Maintain orchard sanitation",
            "Harvest carefully",
            "Maintain suitable postharvest handling"
        ],

        "immediate_action": [
            "Separate visibly diseased fruit",
            "Remove severely rotted fruit",
            "Inspect nearby fruit",
            "Determine the specific disease before treatment"
        ],

        "cultural_control": [
            "Maintain orchard sanitation",
            "Avoid unnecessary fruit injury",
            "Remove fallen diseased fruit",
            "Handle harvested fruit carefully",
            "Maintain good tree health"
        ],

        "biological_control": [
            "Biological control depends on the specific mango fruit disease."
        ],

        "chemical_control": (
            "No single chemical treatment should be assigned from this "
            "generic class. Identify the specific mango disease first."
        ),

        "safety_warning": (
            "Mango fruit can be affected by several different diseases. "
            "Do not use a generic pesticide recommendation without "
            "confirming the disease and whether the product is permitted "
            "for mango fruit."
        )
    },


    # ========================================================
    # 22. fruit_rot
    # ========================================================

    "fruit_rot": {

        "plant": "Multiple / unspecified",

        "disease": "Fruit Rot",

        "affected_part": "Fruit",

        "disease_type": "Fungal / Bacterial / Unspecified",

        "cause": (
            "Fruit rot is a broad disease category. Different crops "
            "can develop fruit rot from different fungi, bacteria, "
            "or combinations of pathogens."
        ),

        "pathogen": (
            "Host-dependent. The exact pathogen cannot be determined "
            "from the generic class name alone."
        ),

        "symptoms": [
            "Softening of fruit tissue",
            "Brown or black discoloration",
            "Water-soaked lesions may occur",
            "Sunken lesions may develop",
            "Fruit may collapse as decay progresses",
            "Fungal growth may appear on some rots"
        ],

        "why_it_happens": [
            "Pathogens can enter through wounds",
            "Overripe fruit can be more susceptible",
            "High humidity can favor many fruit-rotting organisms",
            "Poor sanitation can increase pathogen sources",
            "Improper storage can accelerate decay"
        ],

        "favorable_conditions": [
            "High humidity",
            "Warm temperatures for many pathogens",
            "Fruit wounds",
            "Overripe fruit",
            "Poor ventilation",
            "Poor sanitation"
        ],

        "prevention": [
            "Handle fruit carefully",
            "Avoid bruising",
            "Remove diseased fruit",
            "Maintain sanitation",
            "Provide suitable ventilation",
            "Harvest at appropriate maturity"
        ],

        "immediate_action": [
            "Separate rotten fruit from healthy fruit",
            "Remove severely affected fruit",
            "Clean contaminated storage areas",
            "Inspect nearby fruit",
            "Identify the crop and specific disease before treatment"
        ],

        "cultural_control": [
            "Maintain field sanitation",
            "Remove infected fruit",
            "Minimize fruit injury",
            "Maintain appropriate storage conditions",
            "Avoid unnecessary moisture"
        ],

        "biological_control": [
            "Biological control depends on the crop and specific "
            "fruit-rot pathogen."
        ],

        "chemical_control": (
            "No universal pesticide should be assigned to the generic "
            "fruit-rot class. Chemical control must be selected for "
            "the crop, pathogen, production stage and local registration."
        ),

        "safety_warning": (
            "Do not treat every fruit rot with the same pesticide. "
            "Some fruit rots are fungal, some bacterial, and some "
            "symptoms may have non-infectious causes."
        )
    }

}
# ============================================================
# DISEASE DATABASE
# PART 3 — CLASSES 23 TO 33
# ============================================================


PART_3_DATABASE = {


    # ========================================================
    # 23. fungi
    # ========================================================

    "fungi": {

        "plant": "Multiple / unspecified",

        "disease": "Fungal Disease / Fungi",

        "affected_part": "Unspecified",

        "disease_type": "Fungal / Unspecified",

        "cause": (
            "The class indicates a fungal or fungus-associated "
            "condition but does not identify a particular plant, "
            "disease, or fungal species."
        ),

        "pathogen": (
            "Not specified. Different fungal diseases are caused "
            "by different fungal pathogens."
        ),

        "symptoms": [
            "Leaf spots may occur",
            "Blight may occur",
            "Fruit rot may occur",
            "Stem lesions may occur",
            "Wilting may occur",
            "Visible fungal growth may occur in some diseases"
        ],

        "why_it_happens": [
            "Different fungi survive and spread in different ways",
            "Many fungal diseases are favored by moisture",
            "Infected plant debris can act as an inoculum source",
            "Plant wounds can provide infection sites"
        ],

        "favorable_conditions": [
            "High humidity",
            "Prolonged leaf wetness",
            "Rainfall",
            "Poor air circulation",
            "Plant stress"
        ],

        "prevention": [
            "Maintain good plant sanitation",
            "Improve air circulation",
            "Avoid unnecessary leaf wetness",
            "Remove confirmed diseased material",
            "Use healthy planting material",
            "Monitor plants regularly"
        ],

        "immediate_action": [
            "Identify the plant species",
            "Inspect the affected plant part",
            "Look for characteristic disease symptoms",
            "Remove severely affected material where appropriate",
            "Obtain a specific diagnosis before chemical treatment"
        ],

        "cultural_control": [
            "Remove infected plant debris",
            "Improve canopy airflow",
            "Avoid excessive irrigation",
            "Use clean tools",
            "Maintain appropriate plant spacing"
        ],

        "biological_control": [
            "Biological control is disease- and crop-specific.",
            "Use only products registered for the identified crop and disease."
        ],

        "chemical_control": (
            "No universal fungicide should be recommended for this "
            "generic class. The crop and specific fungal disease must "
            "be identified first."
        ),

        "safety_warning": (
            "Do not treat the word 'fungi' as a confirmed diagnosis. "
            "Different fungal diseases require different management "
            "and pesticide programs."
        )
    },


    # ========================================================
    # 24. grape_leaf
    # ========================================================

    "grape_leaf": {

        "plant": "Grape",

        "disease": "Grape Leaf",

        "affected_part": "Leaf",

        "disease_type": "Unspecified / Dataset Class",

        "cause": (
            "The class identifies a grape leaf but does not specify "
            "a particular disease."
        ),

        "pathogen": "",

        "symptoms": [
            "No specific disease can be determined from this class alone",
            "Visible leaf condition should be evaluated separately"
        ],

        "why_it_happens": [
            "This is a general grape-leaf class rather than a named disease"
        ],

        "favorable_conditions": [],

        "prevention": [
            "Monitor grape leaves regularly",
            "Maintain good canopy airflow",
            "Remove confirmed diseased material",
            "Use clean planting material",
            "Avoid prolonged leaf wetness"
        ],

        "immediate_action": [
            "Inspect the entire vine",
            "Look for characteristic disease lesions",
            "Check leaves, shoots and fruit",
            "Do not apply disease-specific pesticide based only on this class"
        ],

        "cultural_control": [
            "Maintain canopy management",
            "Remove infected debris",
            "Maintain adequate airflow",
            "Avoid unnecessary irrigation onto foliage"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific chemical treatment should be "
            "recommended from this generic grape-leaf class."
        ),

        "safety_warning": (
            "A grape leaf classification is not a diagnosis of a "
            "specific grape disease."
        )
    },


    # ========================================================
    # 25. grape_leaf_black_rot
    # ========================================================

    "grape_leaf_black_rot": {

        "plant": "Grape",

        "disease": "Black Rot",

        "affected_part": "Leaf / Shoot / Fruit",

        "disease_type": "Fungal",

        "cause": (
            "Grape black rot is a fungal disease caused by "
            "Guignardia bidwellii."
        ),

        "pathogen": "Guignardia bidwellii",

        "symptoms": [
            "Round tan to reddish-brown leaf spots",
            "Dark borders around leaf lesions",
            "Small black fruiting bodies may appear inside lesions",
            "Young shoots can develop dark lesions",
            "Fruit can develop dark brown lesions",
            "Infected berries can shrivel into black mummies",
            "Mummified berries may remain attached to clusters"
        ],

        "why_it_happens": [
            "The fungus can survive in mummified fruit",
            "The pathogen can survive in old infected clusters",
            "Cane lesions can also provide overwintering sites",
            "Rain can release spores from infected material",
            "Long periods of leaf wetness favor infection"
        ],

        "favorable_conditions": [
            "Warm and wet weather",
            "Prolonged leaf wetness",
            "Rainfall",
            "Dense canopy",
            "Infected mummified berries"
        ],

        "prevention": [
            "Remove mummified grapes",
            "Remove infected prunings",
            "Improve vineyard canopy airflow",
            "Use resistant varieties where suitable",
            "Monitor vines early in the season"
        ],

        "immediate_action": [
            "Remove mummified fruit",
            "Remove infected plant debris",
            "Inspect nearby leaves and clusters",
            "Improve canopy ventilation",
            "Monitor disease development"
        ],

        "cultural_control": [
            "Remove mummified berries before new growth",
            "Remove infected prunings",
            "Maintain an open canopy",
            "Use appropriate trellising and canopy management",
            "Maintain vineyard sanitation"
        ],

        "biological_control": [
            "No universal biological treatment should be assumed.",
            "Use only products registered for grapes and the target disease."
        ],

        "chemical_control": (
            "Fungicide programs can be useful for grape black rot, "
            "especially when disease pressure is high. Product choice "
            "and application timing should follow local grape disease "
            "recommendations and the current pesticide label."
        ),

        "safety_warning": (
            "Do not use a fixed pesticide dose in this database. "
            "The permitted product, rate, timing and harvest interval "
            "depend on the label and local regulations."
        )
    },


    # ========================================================
    # 26. gray_blight
    # ========================================================

    "gray_blight": {

        "plant": "Multiple / unspecified",

        "disease": "Gray Blight",

        "affected_part": "Leaf / Shoot",

        "disease_type": "Fungal / Unspecified",

        "cause": (
            "The term gray blight is used for different diseases "
            "depending on the crop. The model class does not identify "
            "the host or exact causal organism."
        ),

        "pathogen": (
            "Host-dependent. Exact pathogen should be determined "
            "from the crop and disease diagnosis."
        ),

        "symptoms": [
            "Gray or gray-brown leaf lesions",
            "Leaf tissue may become necrotic",
            "Lesions may enlarge or merge",
            "Premature leaf drop may occur in severe infections",
            "Symptoms vary by host"
        ],

        "why_it_happens": [
            "Some blight pathogens are favored by prolonged moisture",
            "Infected plant debris can provide inoculum",
            "Dense canopies can retain humidity",
            "Plant stress may increase disease severity"
        ],

        "favorable_conditions": [
            "High humidity",
            "Frequent rainfall",
            "Extended leaf wetness",
            "Poor air circulation",
            "Dense foliage"
        ],

        "prevention": [
            "Improve air circulation",
            "Remove infected debris",
            "Avoid prolonged leaf wetness",
            "Use healthy planting material",
            "Monitor plants regularly"
        ],

        "immediate_action": [
            "Identify the host plant",
            "Inspect affected leaves",
            "Remove severely affected tissue where practical",
            "Improve ventilation",
            "Obtain a specific diagnosis before pesticide use"
        ],

        "cultural_control": [
            "Maintain sanitation",
            "Improve canopy ventilation",
            "Remove fallen infected leaves",
            "Avoid excessive overhead irrigation"
        ],

        "biological_control": [
            "Biological control depends on the confirmed crop and pathogen."
        ],

        "chemical_control": (
            "No universal fungicide should be assigned to this generic "
            "class. Confirm the host and causal disease before treatment."
        ),

        "safety_warning": (
            "The term 'gray blight' is not sufficiently specific to "
            "determine a single pesticide recommendation."
        )
    },


    # ========================================================
    # 27. guava_disease_fruit
    # ========================================================

    "guava_disease_fruit": {

        "plant": "Guava",

        "disease": "Guava Fruit Disease",

        "affected_part": "Fruit",

        "disease_type": "Unspecified",

        "cause": (
            "The class identifies diseased guava fruit but does not "
            "identify the exact disease."
        ),

        "pathogen": (
            "Not specified. Guava fruit can be affected by multiple "
            "fungal and other diseases."
        ),

        "symptoms": [
            "Fruit spots",
            "Dark or brown lesions",
            "Fruit softening",
            "Fruit rot",
            "Sunken lesions may occur",
            "Premature fruit drop may occur"
        ],

        "why_it_happens": [
            "Fruit wounds can provide entry points for pathogens",
            "High humidity can favor some fruit diseases",
            "Poor orchard sanitation can increase inoculum",
            "Overripe or damaged fruit can decay more easily"
        ],

        "favorable_conditions": [
            "Warm humid weather",
            "High moisture",
            "Fruit injury",
            "Poor sanitation",
            "Overripe fruit"
        ],

        "prevention": [
            "Maintain orchard sanitation",
            "Remove diseased fruit",
            "Minimize fruit injury",
            "Monitor fruit regularly",
            "Maintain healthy trees"
        ],

        "immediate_action": [
            "Remove severely diseased fruit",
            "Separate diseased fruit from healthy fruit",
            "Inspect nearby fruit",
            "Identify the exact disease before treatment"
        ],

        "cultural_control": [
            "Remove fallen and diseased fruit",
            "Maintain canopy airflow",
            "Avoid unnecessary fruit injury",
            "Use clean harvesting equipment"
        ],

        "biological_control": [
            "Biological control depends on the confirmed guava disease."
        ],

        "chemical_control": (
            "No universal chemical treatment should be attached to "
            "this generic class. Confirm the disease before treatment."
        ),

        "safety_warning": (
            "Do not assume all diseased guava fruit is caused by the "
            "same pathogen."
        )
    },


    # ========================================================
    # 28. guava_healthly_fruit
    # Exact model spelling retained.
    # ========================================================

    "guava_healthly_fruit": {

        "plant": "Guava",

        "disease": "No Disease",

        "affected_part": "Fruit",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Fruit is consistent with the healthy guava class"
        ],

        "why_it_happens": [
            "The model classified the uploaded image as healthy guava fruit."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain orchard sanitation",
            "Handle fruit carefully",
            "Maintain balanced irrigation",
            "Maintain appropriate nutrition",
            "Monitor fruit regularly"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue routine monitoring."
        ],

        "cultural_control": [
            "Remove damaged or rotting fruit",
            "Maintain orchard hygiene",
            "Avoid unnecessary fruit injury",
            "Maintain good tree health"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for "
            "healthy guava fruit."
        ),

        "safety_warning": (
            "A healthy fruit classification does not guarantee that "
            "the entire guava tree is disease-free."
        )
    },


    # ========================================================
    # 29. guava_healthly_leaf
    # Exact model spelling retained.
    # ========================================================

    "guava_healthly_leaf": {

        "plant": "Guava",

        "disease": "No Disease",

        "affected_part": "Leaf",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Leaf is consistent with the healthy guava class"
        ],

        "why_it_happens": [
            "The model classified the image as healthy guava leaf."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain good orchard sanitation",
            "Maintain balanced nutrition",
            "Provide appropriate irrigation",
            "Monitor leaves regularly",
            "Maintain adequate airflow"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue regular plant monitoring."
        ],

        "cultural_control": [
            "Maintain canopy airflow",
            "Remove confirmed diseased material",
            "Maintain orchard hygiene",
            "Avoid unnecessary leaf wetness"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific chemical treatment is recommended "
            "for a healthy guava leaf."
        ),

        "safety_warning": (
            "Healthy classification applies to the uploaded image "
            "and does not guarantee the entire tree is healthy."
        )
    },


    # ========================================================
    # 30. guava_red_rust
    # ========================================================

    "guava_red_rust": {

        "plant": "Guava",

        "disease": "Red Rust / Algal Leaf Spot",

        "affected_part": "Leaf / Fruit",

        "disease_type": "Algal",

        "cause": (
            "Guava red rust is associated with parasitic algae in "
            "the genus Cephaleuros. Different Cephaleuros species "
            "have been reported on guava."
        ),

        "pathogen": (
            "Cephaleuros species, including Cephaleuros virescens "
            "and C. parasiticus reported on guava."
        ),

        "symptoms": [
            "Orange to rust-colored spots on leaves",
            "Reddish-brown circular lesions may occur",
            "Raised or velvety-looking growth may be visible",
            "Lesions may occur on both leaf surfaces",
            "Fruit spots can occur with some Cephaleuros species",
            "Severe infections can reduce healthy leaf area"
        ],

        "why_it_happens": [
            "Parasitic algae can colonize plant surfaces",
            "Plant stress can increase susceptibility",
            "Poor canopy ventilation can favor disease development",
            "High moisture can support algal growth",
            "Poor plant vigor can predispose plants"
        ],

        "favorable_conditions": [
            "High humidity",
            "Frequent rainfall",
            "Poor air circulation",
            "Plant stress",
            "Poor nutrition or soil conditions"
        ],

        "prevention": [
            "Maintain plant vigor",
            "Use appropriate irrigation",
            "Maintain balanced nutrition",
            "Improve canopy airflow",
            "Maintain orchard sanitation",
            "Reduce unnecessary plant stress"
        ],

        "immediate_action": [
            "Inspect the affected leaves",
            "Improve airflow through the canopy",
            "Correct plant stress where identified",
            "Remove severely affected tissue where practical",
            "Monitor new growth"
        ],

        "cultural_control": [
            "Prune to improve aeration",
            "Maintain appropriate nutrition",
            "Maintain proper irrigation",
            "Control other pests and diseases",
            "Avoid unnecessary mechanical injury"
        ],

        "biological_control": [
            "No universal biological treatment should be assumed "
            "for guava red rust."
        ],

        "chemical_control": (
            "Because guava red rust can involve Cephaleuros algae, "
            "it should not automatically be treated like a fungal rust. "
            "Cultural management and plant-vigor improvement are important. "
            "Use a locally registered product only if specifically labeled "
            "for the confirmed disease and crop."
        ),

        "safety_warning": (
            "Do not assume 'rust' means a fungal rust. Guava red rust "
            "can be caused by Cephaleuros algae, so diagnosis matters "
            "before selecting a pesticide."
        )
    },


    # ========================================================
    # 31. healthy
    # ========================================================

    "healthy": {

        "plant": "Plant not specified",

        "disease": "No Disease",

        "affected_part": "Unspecified",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Image classified as the generic healthy class"
        ],

        "why_it_happens": [
            "The model assigned the highest probability to its "
            "generic healthy class."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain appropriate irrigation",
            "Maintain balanced plant nutrition",
            "Monitor plants regularly",
            "Maintain sanitation",
            "Watch for early pest and disease symptoms"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue routine plant inspection."
        ],

        "cultural_control": [
            "Maintain good sanitation",
            "Remove dead plant material",
            "Maintain plant vigor",
            "Use clean tools"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for the "
            "generic healthy class."
        ),

        "safety_warning": (
            "The generic healthy class does not identify a particular "
            "plant species and does not guarantee that the entire plant "
            "is free of pests or disease."
        )
    },


    # ========================================================
    # 32. healthy_banana_fruit
    # ========================================================

    "healthy_banana_fruit": {

        "plant": "Banana",

        "disease": "No Disease",

        "affected_part": "Fruit",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Fruit is consistent with the healthy banana class"
        ],

        "why_it_happens": [
            "The model classified the image as healthy banana fruit."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Handle fruit carefully",
            "Maintain field sanitation",
            "Monitor bunches regularly",
            "Avoid unnecessary fruit injury",
            "Maintain healthy plants"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue routine inspection."
        ],

        "cultural_control": [
            "Remove damaged or rotting fruit",
            "Maintain plantation sanitation",
            "Use clean harvesting equipment",
            "Minimize fruit bruising"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for "
            "healthy banana fruit."
        ),

        "safety_warning": (
            "Healthy fruit classification does not guarantee that "
            "the banana plant or entire bunch is disease-free."
        )
    },


    # ========================================================
    # 33. healthy_banana_leaf
    # ========================================================

    "healthy_banana_leaf": {

        "plant": "Banana",

        "disease": "No Disease",

        "affected_part": "Leaf",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Leaf is consistent with the healthy banana class"
        ],

        "why_it_happens": [
            "The model classified the image as healthy banana leaf."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain adequate nutrition",
            "Maintain suitable irrigation",
            "Monitor leaves regularly",
            "Maintain plantation sanitation",
            "Maintain good airflow"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue routine banana plantation monitoring."
        ],

        "cultural_control": [
            "Remove severely diseased leaves if they appear",
            "Maintain plantation sanitation",
            "Avoid excessive leaf wetness",
            "Maintain appropriate plant spacing"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for "
            "healthy banana leaves."
        ),

        "safety_warning": (
            "Healthy leaf classification applies to the uploaded "
            "image and does not guarantee the whole banana plant is healthy."
        )
    }

}
# ============================================================
# DISEASE DATABASE
# PART 4 — CLASSES 34 TO 44
# ============================================================

PART_4_DATABASE = {

    # ========================================================
    # 34. healthy_fruit
    # ========================================================

    "healthy_fruit": {

        "plant": "Plant not specified",

        "disease": "No Disease",

        "affected_part": "Fruit",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Fruit appears consistent with the generic healthy-fruit class"
        ],

        "why_it_happens": [
            "The model classified the uploaded image as healthy fruit."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain appropriate irrigation",
            "Maintain balanced plant nutrition",
            "Handle fruit carefully",
            "Maintain sanitation",
            "Monitor fruit regularly"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue routine monitoring."
        ],

        "cultural_control": [
            "Remove damaged or rotten fruit",
            "Maintain field or orchard sanitation",
            "Avoid unnecessary fruit injury",
            "Maintain healthy plants"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for "
            "the generic healthy-fruit class."
        ),

        "safety_warning": (
            "A healthy-fruit classification applies to the uploaded "
            "image and does not prove that the entire plant is healthy."
        )
    },


    # ========================================================
    # 35. healthy_leaf
    # ========================================================

    "healthy_leaf": {

        "plant": "Plant not specified",

        "disease": "No Disease",

        "affected_part": "Leaf",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Leaf appears consistent with the generic healthy-leaf class"
        ],

        "why_it_happens": [
            "The model classified the uploaded image as a healthy leaf."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain appropriate irrigation",
            "Maintain balanced nutrition",
            "Monitor leaves regularly",
            "Maintain plant sanitation",
            "Avoid unnecessary leaf injury"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue regular inspection."
        ],

        "cultural_control": [
            "Maintain good airflow",
            "Remove confirmed diseased leaves",
            "Maintain clean growing conditions",
            "Use clean tools"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for "
            "the generic healthy-leaf class."
        ),

        "safety_warning": (
            "A healthy-leaf classification does not guarantee that "
            "the whole plant is free from pests or disease."
        )
    },


    # ========================================================
    # 36. healthy_mango_fruit
    # ========================================================

    "healthy_mango_fruit": {

        "plant": "Mango",

        "disease": "No Disease",

        "affected_part": "Fruit",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Fruit is consistent with the healthy mango-fruit class"
        ],

        "why_it_happens": [
            "The model classified the image as healthy mango fruit."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain orchard sanitation",
            "Maintain appropriate irrigation",
            "Maintain balanced nutrition",
            "Avoid fruit injury",
            "Monitor fruit regularly"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue routine orchard monitoring."
        ],

        "cultural_control": [
            "Remove damaged or rotten fruit",
            "Maintain orchard hygiene",
            "Avoid unnecessary fruit injury",
            "Maintain healthy trees"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for "
            "healthy mango fruit."
        ),

        "safety_warning": (
            "Healthy fruit classification does not guarantee that "
            "the entire mango tree is healthy."
        )
    },


    # ========================================================
    # 37. mang_healthy_leaf
    # Exact model spelling retained.
    # ========================================================

    "mang_healthy_leaf": {

        "plant": "Mango",

        "disease": "No Disease",

        "affected_part": "Leaf",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Leaf is consistent with the healthy mango-leaf class"
        ],

        "why_it_happens": [
            "The model classified the image as a healthy mango leaf."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain balanced nutrition",
            "Provide appropriate irrigation",
            "Maintain orchard sanitation",
            "Monitor leaves regularly",
            "Maintain good canopy airflow"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue routine monitoring."
        ],

        "cultural_control": [
            "Maintain canopy airflow",
            "Remove diseased plant material when detected",
            "Maintain orchard hygiene",
            "Avoid unnecessary leaf wetness"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for "
            "a healthy mango leaf."
        ),

        "safety_warning": (
            "Healthy-leaf classification applies to the uploaded "
            "image and does not guarantee that the entire mango tree "
            "is disease-free."
        )
    },


    # ========================================================
    # 38. mango_bacterial_canker
    # ========================================================

    "mango_bacterial_canker": {

        "plant": "Mango",

        "disease": "Mango Bacterial Canker",

        "affected_part": "Leaf / Petiole / Stem / Branch / Fruit",

        "disease_type": "Bacterial",

        "cause": (
            "Mango bacterial canker is a bacterial disease that can "
            "affect leaves, petioles, twigs, branches and fruit."
        ),

        "pathogen": (
            "Xanthomonas campestris pv. mangiferae-indicae "
            "(older literature commonly uses this name; taxonomy "
            "may vary by source)."
        ),

        "symptoms": [
            "Angular to irregular dark brown or black leaf lesions",
            "Leaf lesions may have chlorotic halos",
            "Raised dark lesions on petioles",
            "Dark cankers on twigs and branches",
            "Longitudinal cracks can develop on branches",
            "Raised dark lesions can occur on fruit",
            "Gummy bacterial exudate may occur",
            "Severely affected fruit may drop"
        ],

        "why_it_happens": [
            "The bacterium can spread from infected plant material",
            "Rain can spread bacteria between plant tissues",
            "Plant wounds can provide entry points",
            "High moisture can favor disease development",
            "Poor orchard sanitation can increase disease pressure"
        ],

        "favorable_conditions": [
            "Warm humid weather",
            "Rainfall",
            "High moisture",
            "Wind-driven rain",
            "Plant injury",
            "Poor sanitation"
        ],

        "prevention": [
            "Use healthy planting material",
            "Inspect nursery plants before planting",
            "Maintain orchard sanitation",
            "Avoid unnecessary plant injury",
            "Remove infected plant material where appropriate",
            "Monitor leaves, shoots and fruit regularly"
        ],

        "immediate_action": [
            "Inspect the whole tree for cankers",
            "Remove severely affected branches where appropriate",
            "Remove infected plant debris",
            "Disinfect pruning tools",
            "Avoid moving infected plant material",
            "Monitor nearby trees"
        ],

        "cultural_control": [
            "Use disease-free planting material",
            "Maintain orchard sanitation",
            "Prune infected branches where appropriate",
            "Improve canopy airflow",
            "Avoid unnecessary irrigation onto foliage",
            "Disinfect pruning equipment"
        ],

        "biological_control": [
            "Some biological control approaches have been studied "
            "for mango bacterial diseases, but availability and "
            "registration depend on location.",
            "Use only a product registered for mango and the target disease."
        ],

        "chemical_control": (
            "Copper-based bactericidal products may be included in "
            "some management programs, but chemical control is "
            "preventive/suppressive rather than a cure for infected "
            "tissue. Use only a product currently registered for "
            "mango bacterial canker in your region."
        ),

        "safety_warning": (
            "Do not use a fixed pesticide dose from this database. "
            "Product registration, concentration, PPE, application "
            "interval and harvest restrictions must come from the "
            "current local label."
        )
    },


    # ========================================================
    # 39. mealybug_infestation
    # ========================================================

    "mealybug_infestation": {

        "plant": "Multiple / unspecified",

        "disease": "Mealybug Infestation",

        "affected_part": "Leaf / Stem / Fruit / Growing Points",

        "disease_type": "Insect Pest",

        "cause": (
            "Mealybugs are sap-sucking insects covered by a waxy or "
            "cotton-like coating. They feed on plant sap."
        ),

        "pathogen": "",

        "symptoms": [
            "White cottony or waxy insects",
            "Insects may occur on leaf undersides",
            "Insects may cluster around leaf axils and stems",
            "Sticky honeydew may be present",
            "Black sooty mold may develop on honeydew",
            "Leaves may yellow",
            "Plant growth may become stunted",
            "Heavy infestations can cause dieback"
        ],

        "why_it_happens": [
            "Mealybugs can enter on infested planting material",
            "They can spread between nearby plants",
            "Ants may protect and transport honeydew-producing insects",
            "Excessive tender plant growth can favor infestations",
            "Poor inspection of new plants can introduce pests"
        ],

        "favorable_conditions": [
            "Warm conditions",
            "Dense plant growth",
            "Protected areas around stems and leaf axils",
            "Presence of ants",
            "High pest pressure"
        ],

        "prevention": [
            "Inspect new plants before introducing them",
            "Isolate infested plants",
            "Monitor regularly",
            "Control ants where appropriate",
            "Avoid excessive nitrogen fertilization",
            "Remove heavily infested plant material"
        ],

        "immediate_action": [
            "Isolate the affected plant where practical",
            "Remove visible mealybugs",
            "Prune heavily infested portions where appropriate",
            "Wash exposed insects off with water where suitable",
            "Inspect leaf undersides and stem junctions",
            "Continue monitoring after treatment"
        ],

        "cultural_control": [
            "Inspect plants regularly",
            "Quarantine newly purchased plants",
            "Remove heavily infested plants when necessary",
            "Prune infested parts",
            "Manage ants",
            "Avoid excessive nitrogen fertilizer"
        ],

        "biological_control": [
            "Natural enemies such as parasitic wasps and predatory "
            "insects can help suppress mealybug populations outdoors.",
            "Protect beneficial insects whenever possible."
        ],

        "chemical_control": (
            "Insecticidal soaps and horticultural oils can suppress "
            "mealybugs when they contact the insects directly. "
            "Systemic insecticides may be appropriate in some crop "
            "systems, but the product must specifically list the "
            "crop and mealybugs on its label."
        ),

        "safety_warning": (
            "Mealybugs have a waxy coating and hide in protected areas, "
            "so contact sprays may not reach all individuals. Never "
            "recommend a pesticide without checking that the crop and "
            "pest are listed on the current label."
        )
    },


    # ========================================================
    # 40. papaya_fruit_disease
    # ========================================================

    "papaya_fruit_disease": {

        "plant": "Papaya",

        "disease": "Papaya Fruit Disease",

        "affected_part": "Fruit",

        "disease_type": "Unspecified",

        "cause": (
            "The class identifies diseased papaya fruit but does "
            "not identify the exact disease."
        ),

        "pathogen": (
            "Not specified. Papaya fruit can be affected by several "
            "fungal, bacterial, viral and postharvest problems."
        ),

        "symptoms": [
            "Fruit discoloration",
            "Fruit spots",
            "Sunken lesions",
            "Softening or decay",
            "Fruit rot",
            "Premature fruit drop may occur"
        ],

        "why_it_happens": [
            "Different papaya fruit diseases have different causes",
            "Fruit wounds can allow pathogens to enter",
            "High humidity can favor fruit rots",
            "Poor sanitation can increase disease pressure",
            "Poor handling can increase fruit injury"
        ],

        "favorable_conditions": [
            "Warm humid conditions",
            "High moisture",
            "Fruit injury",
            "Poor sanitation",
            "Improper postharvest handling"
        ],

        "prevention": [
            "Handle fruit carefully",
            "Maintain field sanitation",
            "Remove diseased fruit",
            "Avoid unnecessary fruit injury",
            "Monitor fruit regularly"
        ],

        "immediate_action": [
            "Separate diseased fruit",
            "Remove severely rotten fruit",
            "Inspect nearby fruit",
            "Identify the exact disease before chemical treatment"
        ],

        "cultural_control": [
            "Remove fallen diseased fruit",
            "Maintain field sanitation",
            "Minimize fruit wounds",
            "Maintain good plant health",
            "Handle harvested fruit carefully"
        ],

        "biological_control": [
            "Biological control depends on the confirmed papaya disease."
        ],

        "chemical_control": (
            "No universal chemical treatment should be assigned to "
            "this generic class. Identify the specific papaya disease "
            "before recommending treatment."
        ),

        "safety_warning": (
            "Do not assume every diseased papaya fruit has the same "
            "pathogen or requires the same pesticide."
        )
    },


    # ========================================================
    # 41. papaya_fruit_healthy
    # ========================================================

    "papaya_fruit_healthy": {

        "plant": "Papaya",

        "disease": "No Disease",

        "affected_part": "Fruit",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Fruit is consistent with the healthy papaya-fruit class"
        ],

        "why_it_happens": [
            "The model classified the image as healthy papaya fruit."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain good field sanitation",
            "Avoid fruit injury",
            "Maintain appropriate irrigation",
            "Maintain balanced nutrition",
            "Monitor fruit regularly"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue routine monitoring."
        ],

        "cultural_control": [
            "Remove damaged or rotten fruit",
            "Maintain sanitation",
            "Handle fruit carefully",
            "Maintain healthy plants"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for "
            "healthy papaya fruit."
        ),

        "safety_warning": (
            "Healthy fruit classification does not guarantee that "
            "the whole papaya plant is free from disease or pests."
        )
    },


    # ========================================================
    # 42. papaya_healthy_leaf
    # ========================================================

    "papaya_healthy_leaf": {

        "plant": "Papaya",

        "disease": "No Disease",

        "affected_part": "Leaf",

        "disease_type": "Healthy",

        "cause": "",

        "pathogen": "",

        "symptoms": [
            "No disease-specific symptoms detected by the model",
            "Leaf is consistent with the healthy papaya-leaf class"
        ],

        "why_it_happens": [
            "The model classified the image as a healthy papaya leaf."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Maintain balanced nutrition",
            "Provide appropriate irrigation",
            "Monitor leaves regularly",
            "Maintain field sanitation",
            "Avoid unnecessary leaf injury"
        ],

        "immediate_action": [
            "No disease-specific treatment is indicated.",
            "Continue routine monitoring."
        ],

        "cultural_control": [
            "Remove confirmed diseased leaves when necessary",
            "Maintain field hygiene",
            "Avoid unnecessary leaf wetness",
            "Maintain healthy plants"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific pesticide is recommended for "
            "a healthy papaya leaf."
        ),

        "safety_warning": (
            "A healthy-leaf classification applies to the uploaded "
            "image and does not guarantee the entire plant is healthy."
        )
    },


    # ========================================================
    # 43. papaya_ringspot
    # ========================================================

    "papaya_ringspot": {

        "plant": "Papaya",

        "disease": "Papaya Ringspot",

        "affected_part": "Leaf / Petiole / Stem / Fruit",

        "disease_type": "Viral",

        "cause": (
            "Papaya ringspot is caused by Papaya ringspot virus (PRSV)."
        ),

        "pathogen": "Papaya ringspot virus (PRSV)",

        "symptoms": [
            "Vein clearing",
            "Mosaic mottling",
            "Leaf distortion",
            "Leaf curling",
            "Blister-like patterns",
            "Narrow or shoestring-like leaves in severe cases",
            "Plant stunting",
            "Dark green streaks on petioles and stems",
            "Concentric rings on fruit",
            "Fruit quality and production can be reduced"
        ],

        "why_it_happens": [
            "The virus is transmitted primarily by aphids",
            "Infected plants act as sources of virus",
            "Aphids can acquire and transmit the virus while feeding",
            "The disease can spread rapidly through susceptible crops"
        ],

        "favorable_conditions": [
            "Presence of infected plants",
            "Presence of aphid vectors",
            "Nearby susceptible cucurbit hosts",
            "High vector activity",
            "Continuous susceptible plantings"
        ],

        "prevention": [
            "Use disease-free seedlings",
            "Raise seedlings in insect-protected conditions",
            "Remove infected plants promptly",
            "Control or reduce sources of aphid vectors",
            "Avoid planting susceptible cucurbits immediately around papaya",
            "Monitor young plants frequently"
        ],

        "immediate_action": [
            "Remove severely infected plants promptly",
            "Do not keep infected plants as virus sources",
            "Inspect nearby papaya plants",
            "Monitor for aphids",
            "Prevent movement of infected plant material"
        ],

        "cultural_control": [
            "Use healthy seedlings",
            "Rogue infected plants",
            "Use barrier crops where locally recommended",
            "Manage weeds and alternate hosts where appropriate",
            "Maintain field sanitation"
        ],

        "biological_control": [
            "Conservation of natural aphid enemies can support pest "
            "management, but it does not cure virus-infected plants."
        ],

        "chemical_control": (
            "There is no pesticide that cures a plant already infected "
            "with papaya ringspot virus. Insecticides may affect aphid "
            "populations in some production systems, but vector control "
            "alone does not provide a reliable cure for an infected plant."
        ),

        "safety_warning": (
            "Do not tell users that a pesticide can cure PRSV. "
            "The key management approach is prevention and removal "
            "of infected plants, together with vector management."
        )
    },


    # ========================================================
    # 44. pink_disease
    # ========================================================

    "pink_disease": {

        "plant": "Multiple woody plants / commonly mango and other tropical hosts",

        "disease": "Pink Disease",

        "affected_part": "Stem / Branch / Trunk",

        "disease_type": "Fungal",

        "cause": (
            "Pink disease is caused by a basidiomycete fungus that "
            "infects woody stems and branches."
        ),

        "pathogen": (
            "Erythricium salmonicolor "
            "(older literature commonly uses Corticium salmonicolor)."
        ),

        "symptoms": [
            "White cobweb-like fungal growth may appear first",
            "Pink or salmon-colored encrustation develops later",
            "Bark may crack",
            "Bark may peel away from affected tissue",
            "Branches may develop cankers",
            "Leaves on affected branches may yellow",
            "Affected branches may die back from the tip",
            "Severe infection can kill branches"
        ],

        "why_it_happens": [
            "The fungus infects woody branches",
            "High humidity and rainfall favor disease development",
            "Dense canopies can retain moisture",
            "Stressed trees can be more susceptible",
            "Infected branches can act as sources of inoculum"
        ],

        "favorable_conditions": [
            "Rainy weather",
            "High humidity",
            "Dense canopy",
            "Poor airflow",
            "Stressed trees",
            "Wet branch surfaces"
        ],

        "prevention": [
            "Maintain healthy trees",
            "Improve canopy ventilation",
            "Prune diseased branches",
            "Remove infected plant material",
            "Avoid unnecessary tree injury",
            "Monitor branch junctions regularly"
        ],

        "immediate_action": [
            "Inspect branches for white or pink fungal growth",
            "Prune affected branches below the infection where appropriate",
            "Remove and destroy infected cuttings appropriately",
            "Sanitize pruning tools",
            "Inspect nearby branches"
        ],

        "cultural_control": [
            "Maintain good tree vigor",
            "Improve canopy airflow",
            "Remove infected branches",
            "Avoid excessive canopy density",
            "Maintain orchard sanitation"
        ],

        "biological_control": [
            "Some crop-specific biological approaches may be available.",
            "Use only products registered for the crop and disease."
        ],

        "chemical_control": (
            "Management can involve protecting pruning wounds and, "
            "in some crops, copper-based or Bordeaux-type treatments. "
            "The exact product and concentration must be selected "
            "according to the host crop and current local label."
        ),

        "safety_warning": (
            "Pink disease occurs on multiple woody hosts, so treatment "
            "should not be assumed to be identical across crops. "
            "Do not use a generic pesticide dose."
        )
    }

}
# ============================================================
# DISEASE DATABASE
# PART 5 — CLASSES 45 TO 55
# ============================================================

PART_5_DATABASE = {


    # ========================================================
    # 45. potato_leaf_early_blight
    # ========================================================

    "potato_leaf_early_blight": {

        "plant": "Potato",

        "disease": "Early Blight",

        "affected_part": "Leaf / Stem / Tuber",

        "disease_type": "Fungal",

        "cause": (
            "Potato early blight is a fungal disease caused by "
            "Alternaria species, most commonly Alternaria solani."
        ),

        "pathogen": "Alternaria solani",

        "symptoms": [
            "Small brown to dark spots on older leaves",
            "Spots may develop concentric rings",
            "Lesions can have a target-like appearance",
            "Yellowing may surround some lesions",
            "Severe disease can cause premature leaf death",
            "Stem lesions may occur",
            "Tubers can develop dark, sunken lesions"
        ],

        "why_it_happens": [
            "The pathogen can survive in infected plant debris",
            "Spores can spread by wind and rain",
            "Plant stress can increase disease severity",
            "Older leaves are often affected first",
            "Poor sanitation can increase inoculum"
        ],

        "favorable_conditions": [
            "Warm weather",
            "High humidity",
            "Frequent rainfall",
            "Extended periods of leaf wetness",
            "Plant stress",
            "Poor field sanitation"
        ],

        "prevention": [
            "Use healthy seed tubers",
            "Maintain adequate plant nutrition",
            "Avoid unnecessary plant stress",
            "Remove infected plant debris",
            "Practice crop rotation",
            "Use resistant or tolerant varieties where available"
        ],

        "immediate_action": [
            "Inspect older leaves for target-like lesions",
            "Remove heavily infected plant material where practical",
            "Maintain adequate plant nutrition",
            "Monitor disease progression",
            "Protect remaining healthy foliage according to local guidance"
        ],

        "cultural_control": [
            "Use disease-free seed",
            "Rotate crops",
            "Remove crop debris",
            "Maintain balanced fertility",
            "Avoid excessive plant stress",
            "Maintain good field sanitation"
        ],

        "biological_control": [
            "Biological control options depend on the production system.",
            "Use only products registered for potato and the target disease."
        ],

        "chemical_control": (
            "Fungicides may be used in potato disease-management "
            "programs when appropriate. Product selection and timing "
            "must follow local recommendations and the current label "
            "for potato early blight."
        ),

        "safety_warning": (
            "Do not use a universal fungicide dose. Confirm the product "
            "is registered for potato and early blight and follow the "
            "label for PPE, rate, timing and harvest interval."
        )
    },


    # ========================================================
    # 46. potato_leaf_late_blight
    # ========================================================

    "potato_leaf_late_blight": {

        "plant": "Potato",

        "disease": "Late Blight",

        "affected_part": "Leaf / Stem / Tuber",

        "disease_type": "Oomycete",

        "cause": (
            "Potato late blight is caused by the oomycete "
            "Phytophthora infestans."
        ),

        "pathogen": "Phytophthora infestans",

        "symptoms": [
            "Water-soaked leaf lesions",
            "Brown to black rapidly expanding lesions",
            "Dark lesions on stems",
            "White sporulation may occur under humid conditions",
            "Leaves can rapidly collapse",
            "Tubers may develop brown to reddish-brown internal rot"
        ],

        "why_it_happens": [
            "The pathogen spreads through infected plant material",
            "Spores can spread through wind and water",
            "Wet foliage favors infection",
            "Cool to moderate temperatures with high moisture can favor disease",
            "Infected volunteer potatoes can act as disease sources"
        ],

        "favorable_conditions": [
            "High humidity",
            "Frequent rainfall",
            "Long periods of leaf wetness",
            "Cool to moderate temperatures",
            "Dense crop canopy"
        ],

        "prevention": [
            "Use certified disease-free seed tubers",
            "Remove volunteer potatoes",
            "Avoid prolonged leaf wetness",
            "Monitor weather and disease risk",
            "Use resistant or tolerant varieties where available",
            "Maintain field sanitation"
        ],

        "immediate_action": [
            "Inspect the crop immediately",
            "Remove or destroy severely infected plant material where appropriate",
            "Check nearby plants for rapidly expanding lesions",
            "Do not move infected plant material between fields",
            "Follow local late-blight management recommendations"
        ],

        "cultural_control": [
            "Use certified seed",
            "Remove volunteer potato plants",
            "Destroy cull piles",
            "Maintain good field sanitation",
            "Use appropriate crop rotation",
            "Avoid unnecessary overhead irrigation"
        ],

        "biological_control": [
            "Biological options are limited and depend on the production system.",
            "They should not replace an effective late-blight management program."
        ],

        "chemical_control": (
            "Late blight often requires preventive fungicide protection "
            "when disease risk is high. Use only fungicides registered "
            "for potato late blight and follow local disease-warning "
            "systems and product labels."
        ),

        "safety_warning": (
            "Late blight can develop rapidly. Do not delay management "
            "while relying on an image classification alone. Confirm "
            "the diagnosis and follow local agricultural recommendations."
        )
    },


    # ========================================================
    # 47. rust
    # ========================================================

    "rust": {

        "plant": "Multiple / unspecified",

        "disease": "Rust",

        "affected_part": "Leaf / Stem",

        "disease_type": "Fungal",

        "cause": (
            "Rust diseases are caused by obligate fungal pathogens "
            "in several rust-fungus groups. The exact pathogen depends "
            "on the host plant."
        ),

        "pathogen": (
            "Host-dependent rust fungi. The generic class does not "
            "identify the exact rust species."
        ),

        "symptoms": [
            "Orange, yellow, brown or reddish pustules",
            "Powdery spore masses may occur",
            "Small raised spots on leaves",
            "Leaf yellowing may occur",
            "Premature leaf drop can occur",
            "Stem infections may occur in some rust diseases"
        ],

        "why_it_happens": [
            "Rust fungi produce spores that spread between plants",
            "Some rusts require alternate host plants",
            "Moist foliage favors infection",
            "Dense vegetation can increase humidity"
        ],

        "favorable_conditions": [
            "High humidity",
            "Leaf wetness",
            "Moderate temperatures",
            "Poor airflow",
            "Presence of susceptible hosts"
        ],

        "prevention": [
            "Use resistant varieties where available",
            "Improve plant airflow",
            "Remove heavily infected leaves",
            "Monitor plants regularly",
            "Manage alternate hosts when recommended"
        ],

        "immediate_action": [
            "Identify the host plant",
            "Inspect the underside of leaves",
            "Remove severely infected material where practical",
            "Improve airflow",
            "Confirm the specific rust disease before chemical treatment"
        ],

        "cultural_control": [
            "Maintain good canopy ventilation",
            "Remove infected debris",
            "Use resistant varieties",
            "Avoid prolonged leaf wetness",
            "Maintain healthy plant growth"
        ],

        "biological_control": [
            "Biological control depends on the crop and rust species."
        ],

        "chemical_control": (
            "Fungicide options vary considerably between crops and "
            "rust diseases. Use only a fungicide labeled for the "
            "specific crop and rust disease."
        ),

        "safety_warning": (
            "Do not assume all rust diseases can be treated with the "
            "same fungicide. The generic model class is not sufficient "
            "to determine a crop-specific pesticide."
        )
    },


    # ========================================================
    # 48. scab
    # ========================================================

    "scab": {

        "plant": "Multiple / unspecified",

        "disease": "Scab",

        "affected_part": "Leaf / Fruit",

        "disease_type": "Fungal / Unspecified",

        "cause": (
            "Scab is a name used for different diseases on different "
            "crops. The exact pathogen depends on the host plant."
        ),

        "pathogen": (
            "Host-dependent. Examples include Venturia species on "
            "apple and pear, but the generic class does not identify "
            "the host."
        ),

        "symptoms": [
            "Brown, olive or dark leaf spots",
            "Rough or corky lesions on fruit",
            "Scaly or cracked fruit tissue",
            "Leaf distortion may occur",
            "Premature leaf drop may occur"
        ],

        "why_it_happens": [
            "Many scab pathogens spread through spores",
            "Wet plant surfaces favor infection",
            "Infected plant debris can act as an inoculum source",
            "Dense canopies can retain moisture"
        ],

        "favorable_conditions": [
            "Rainfall",
            "High humidity",
            "Prolonged leaf wetness",
            "Dense foliage",
            "Infected crop debris"
        ],

        "prevention": [
            "Use resistant varieties where available",
            "Remove infected plant debris",
            "Improve canopy airflow",
            "Monitor during wet weather",
            "Maintain good plant sanitation"
        ],

        "immediate_action": [
            "Identify the host plant",
            "Inspect leaves and fruit",
            "Remove infected debris where appropriate",
            "Improve airflow",
            "Confirm the specific scab disease before treatment"
        ],

        "cultural_control": [
            "Remove fallen leaves where relevant",
            "Improve canopy ventilation",
            "Use resistant cultivars",
            "Maintain field or orchard sanitation"
        ],

        "biological_control": [
            "Biological options depend on the crop and pathogen."
        ],

        "chemical_control": (
            "Chemical control is crop-specific. Use only a product "
            "registered for the identified crop and specific scab disease."
        ),

        "safety_warning": (
            "Do not treat every disease labeled 'scab' with the same "
            "pesticide. Confirm the host and pathogen first."
        )
    },


    # ========================================================
    # 49. soft_rot
    # ========================================================

    "soft_rot": {

        "plant": "Multiple / unspecified",

        "disease": "Soft Rot",

        "affected_part": "Fruit / Tuber / Stem / Plant Tissue",

        "disease_type": "Bacterial / Fungal / Unspecified",

        "cause": (
            "Soft rot is a broad disease category. Different crops "
            "can develop soft rot from different bacteria or fungi."
        ),

        "pathogen": (
            "Host-dependent. Several soft-rot bacteria and fungi "
            "can cause rapidly decaying plant tissue."
        ),

        "symptoms": [
            "Water-soaked tissue",
            "Softening of plant tissue",
            "Rapid breakdown of affected tissue",
            "Dark discoloration may develop",
            "Unpleasant odor may occur in some bacterial soft rots",
            "Fruit, tubers or stems may collapse"
        ],

        "why_it_happens": [
            "Wounds provide entry points for many soft-rot organisms",
            "High moisture promotes decay",
            "Poor ventilation can increase humidity",
            "Improper storage can accelerate postharvest decay",
            "Damaged tissue is more susceptible"
        ],

        "favorable_conditions": [
            "High moisture",
            "Warm conditions for many pathogens",
            "Poor ventilation",
            "Plant injury",
            "Improper storage conditions"
        ],

        "prevention": [
            "Avoid bruising and mechanical injury",
            "Maintain sanitation",
            "Provide good ventilation",
            "Handle harvested material carefully",
            "Remove infected tissue promptly",
            "Maintain suitable storage conditions"
        ],

        "immediate_action": [
            "Separate affected material",
            "Remove severely rotted tissue",
            "Clean contaminated surfaces",
            "Improve ventilation",
            "Inspect nearby material for symptoms"
        ],

        "cultural_control": [
            "Minimize wounds",
            "Maintain clean storage areas",
            "Remove infected material",
            "Maintain appropriate humidity and temperature",
            "Use clean harvesting equipment"
        ],

        "biological_control": [
            "Biological control depends on the crop and specific pathogen."
        ],

        "chemical_control": (
            "Chemical treatment is highly dependent on the crop, "
            "pathogen and production stage. Many soft rots are best "
            "managed through sanitation, wound prevention and proper "
            "storage rather than a generic pesticide."
        ),

        "safety_warning": (
            "Do not recommend a universal pesticide for soft rot. "
            "Some soft rots are bacterial and others fungal, and "
            "postharvest pesticide use is subject to specific labels."
        )
    },


    # ========================================================
    # 50. sooty_mold
    # ========================================================

    "sooty_mold": {

        "plant": "Multiple / unspecified",

        "disease": "Sooty Mold",

        "affected_part": "Leaf / Stem / Fruit",

        "disease_type": "Fungal Growth Associated With Honeydew",

        "cause": (
            "Sooty mold fungi grow on honeydew produced by sap-sucking "
            "insects such as aphids, scale insects, whiteflies and "
            "mealybugs. The mold itself generally grows on the surface "
            "rather than directly infecting healthy plant tissue."
        ),

        "pathogen": (
            "Several unrelated fungi can produce sooty mold. "
            "The exact fungus is not identified by this class."
        ),

        "symptoms": [
            "Black or dark powdery coating on leaves",
            "Black coating on stems or fruit",
            "Sticky honeydew may be present",
            "Leaves may become coated with dark fungal growth",
            "Heavy coverage can reduce photosynthesis"
        ],

        "why_it_happens": [
            "Sap-sucking insects produce honeydew",
            "Sooty mold grows on the honeydew",
            "Ants may protect honeydew-producing insects",
            "Heavy insect infestations increase honeydew accumulation"
        ],

        "favorable_conditions": [
            "Presence of honeydew-producing insects",
            "Warm conditions",
            "Dense foliage",
            "Poor pest management",
            "Presence of ants protecting insect colonies"
        ],

        "prevention": [
            "Control the underlying insect infestation",
            "Monitor for aphids, scales, mealybugs and whiteflies",
            "Manage ants where appropriate",
            "Maintain plant vigor",
            "Remove heavily affected material when practical"
        ],

        "immediate_action": [
            "Inspect the plant for sap-sucking insects",
            "Identify the insect causing honeydew",
            "Treat the underlying pest problem rather than the mold alone",
            "Wash surface deposits where practical",
            "Continue monitoring"
        ],

        "cultural_control": [
            "Inspect plants regularly",
            "Control ant activity where appropriate",
            "Prune dense growth",
            "Protect beneficial insects",
            "Remove heavily infested plant material when appropriate"
        ],

        "biological_control": [
            "Conserve natural enemies of aphids, scale insects, "
            "whiteflies and mealybugs.",
            "Biological control of the underlying insect is generally "
            "more useful than treating the sooty mold itself."
        ],

        "chemical_control": (
            "Do not automatically apply a fungicide to sooty mold. "
            "Management should focus primarily on controlling the "
            "honeydew-producing insect. The appropriate insecticide, "
            "if needed, depends on the crop and pest."
        ),

        "safety_warning": (
            "Treating the black mold without controlling the underlying "
            "insect infestation will not solve the main problem."
        )
    },


    # ========================================================
    # 51. stem_blight
    # ========================================================

    "stem_blight": {

        "plant": "Multiple / unspecified",

        "disease": "Stem Blight",

        "affected_part": "Stem / Branch",

        "disease_type": "Fungal / Unspecified",

        "cause": (
            "Stem blight is a general disease description used for "
            "different fungal diseases on different crops."
        ),

        "pathogen": (
            "Host-dependent. The exact pathogen cannot be determined "
            "from this generic class name."
        ),

        "symptoms": [
            "Brown or dark stem lesions",
            "Stem discoloration",
            "Cankers may develop",
            "Leaves above affected areas may wilt",
            "Shoot dieback may occur",
            "Severe infection can kill branches"
        ],

        "why_it_happens": [
            "Pathogens can enter through wounds",
            "Some fungi survive in infected plant debris",
            "High moisture can favor infection",
            "Plant stress can increase susceptibility"
        ],

        "favorable_conditions": [
            "High humidity",
            "Wet conditions",
            "Plant injury",
            "Poor sanitation",
            "Stressed plants"
        ],

        "prevention": [
            "Maintain plant vigor",
            "Avoid unnecessary stem injury",
            "Remove diseased material",
            "Improve airflow",
            "Use clean planting material"
        ],

        "immediate_action": [
            "Inspect the entire stem",
            "Prune affected tissue where appropriate",
            "Remove infected cuttings",
            "Disinfect tools",
            "Identify the crop before treatment"
        ],

        "cultural_control": [
            "Improve air circulation",
            "Maintain sanitation",
            "Remove dead or infected branches",
            "Avoid excessive moisture",
            "Maintain appropriate plant spacing"
        ],

        "biological_control": [
            "Biological control depends on the crop and pathogen."
        ],

        "chemical_control": (
            "No universal fungicide should be assigned to this generic "
            "class. Identify the crop and specific stem-blight pathogen "
            "before chemical treatment."
        ),

        "safety_warning": (
            "The model class alone does not identify the pathogen, "
            "so pesticide recommendations must not be generalized."
        )
    },


    # ========================================================
    # 52. stem_canker
    # ========================================================

    "stem_canker": {

        "plant": "Multiple / unspecified",

        "disease": "Stem Canker",

        "affected_part": "Stem / Branch / Trunk",

        "disease_type": "Fungal / Bacterial / Unspecified",

        "cause": (
            "Stem cankers are localized dead areas of stem or bark. "
            "They can be caused by different fungi or bacteria depending "
            "on the host."
        ),

        "pathogen": (
            "Host-dependent. The model class does not identify the "
            "causal organism."
        ),

        "symptoms": [
            "Sunken stem lesions",
            "Dark or discolored bark",
            "Cracks in bark",
            "Oozing may occur in some bacterial diseases",
            "Branch dieback",
            "Wilting above the affected area",
            "Girdling can kill the stem"
        ],

        "why_it_happens": [
            "Pathogens can enter through wounds",
            "Environmental stress can weaken plants",
            "Infected plant material can spread pathogens",
            "Poor sanitation can increase disease pressure"
        ],

        "favorable_conditions": [
            "Plant stress",
            "High moisture",
            "Stem wounds",
            "Poor sanitation",
            "Dense or poorly ventilated growth"
        ],

        "prevention": [
            "Avoid stem injury",
            "Maintain plant vigor",
            "Use clean planting material",
            "Prune correctly",
            "Remove infected plant material",
            "Disinfect tools"
        ],

        "immediate_action": [
            "Inspect the entire plant",
            "Prune infected branches where appropriate",
            "Remove infected cuttings",
            "Disinfect pruning tools",
            "Monitor nearby plants"
        ],

        "cultural_control": [
            "Maintain sanitation",
            "Improve airflow",
            "Avoid mechanical injury",
            "Remove dead branches",
            "Maintain appropriate irrigation"
        ],

        "biological_control": [
            "Biological control is crop- and pathogen-specific."
        ],

        "chemical_control": (
            "No universal chemical treatment should be associated "
            "with the generic stem-canker class. Confirm the host and "
            "causal organism first."
        ),

        "safety_warning": (
            "A stem canker is a symptom category, not necessarily "
            "one specific disease. Do not give a generic pesticide dose."
        )
    },


    # ========================================================
    # 53. stem_cracking_gummosis
    # ========================================================

    "stem_cracking_gummosis": {

        "plant": "Multiple / unspecified",

        "disease": "Stem Cracking and Gummosis",

        "affected_part": "Stem / Branch / Trunk",

        "disease_type": "Unspecified / Often Pathogen-Associated",

        "cause": (
            "Gummosis is a symptom in which gum or sap-like material "
            "exudes from damaged woody tissue. Causes vary by crop and "
            "can include pathogens, insect injury, mechanical injury "
            "and environmental stress."
        ),

        "pathogen": (
            "Not specified by the generic class. The exact cause "
            "must be determined from the host crop and symptoms."
        ),

        "symptoms": [
            "Cracks in stem or bark",
            "Gum or sap exuding from cracks",
            "Darkened bark",
            "Sunken lesions",
            "Branch dieback may occur",
            "Affected tissue may become weak"
        ],

        "why_it_happens": [
            "Mechanical injury can damage bark",
            "Some fungal or bacterial diseases cause gummosis",
            "Environmental stress can contribute",
            "Insect injury can create entry points",
            "Poor tree health can increase susceptibility"
        ],

        "favorable_conditions": [
            "Stem injury",
            "High moisture",
            "Plant stress",
            "Poor drainage in some crops",
            "Pathogen pressure",
            "Insect damage"
        ],

        "prevention": [
            "Avoid unnecessary stem injury",
            "Maintain appropriate irrigation",
            "Maintain plant vigor",
            "Monitor trunks and branches",
            "Control damaging insects",
            "Maintain good sanitation"
        ],

        "immediate_action": [
            "Inspect the crack and surrounding tissue",
            "Look for insects or pathogen symptoms",
            "Remove severely damaged branches where appropriate",
            "Avoid unnecessary cutting into healthy tissue",
            "Identify the crop and underlying cause before treatment"
        ],

        "cultural_control": [
            "Protect stems from mechanical damage",
            "Maintain good irrigation management",
            "Improve drainage where needed",
            "Maintain sanitation",
            "Monitor for insect damage"
        ],

        "biological_control": [
            "Biological control depends entirely on the confirmed cause."
        ],

        "chemical_control": (
            "No universal pesticide should be assigned to this class. "
            "Gummosis is a symptom with many possible causes. Treatment "
            "must target the confirmed underlying problem."
        ),

        "safety_warning": (
            "Do not assume that all gummosis is caused by a fungus. "
            "Incorrectly applying fungicides can fail to address the "
            "actual cause."
        )
    },


    # ========================================================
    # 54. sunburn
    # ========================================================

    "sunburn": {

        "plant": "Multiple / unspecified",

        "disease": "Sunburn / Sunscald",

        "affected_part": "Leaf / Fruit / Stem",

        "disease_type": "Physiological / Environmental",

        "cause": (
            "Sunburn or sunscald occurs when plant tissue is exposed "
            "to excessive solar radiation and heat, particularly when "
            "tissue is suddenly exposed after canopy loss or during "
            "extreme heat."
        ),

        "pathogen": "",

        "symptoms": [
            "Bleached or pale areas on exposed tissue",
            "Brown or necrotic patches",
            "Scorched leaf areas",
            "Discolored fruit skin",
            "Sunken or damaged fruit areas in severe cases",
            "Damage is usually concentrated on exposed surfaces"
        ],

        "why_it_happens": [
            "Excessive sunlight reaches exposed tissue",
            "High temperatures increase heat stress",
            "Loss of protective canopy can suddenly expose tissue",
            "Water stress can increase susceptibility"
        ],

        "favorable_conditions": [
            "Extreme heat",
            "Intense sunlight",
            "Low humidity",
            "Water stress",
            "Sudden canopy exposure",
            "Long periods of direct sunlight"
        ],

        "prevention": [
            "Maintain adequate plant hydration",
            "Avoid unnecessary removal of protective foliage",
            "Use shade protection where appropriate",
            "Maintain healthy canopy development",
            "Reduce plant stress during extreme heat"
        ],

        "immediate_action": [
            "Provide appropriate irrigation",
            "Protect exposed plants from extreme sunlight where practical",
            "Avoid removing additional protective foliage",
            "Monitor damaged tissue for secondary infections"
        ],

        "cultural_control": [
            "Maintain appropriate canopy cover",
            "Use shade cloth where suitable",
            "Maintain adequate soil moisture",
            "Avoid excessive pruning during extreme heat"
        ],

        "biological_control": [],

        "chemical_control": (
            "Sunburn is not caused by a pathogen, so fungicides or "
            "bactericides do not cure the underlying problem."
        ),

        "safety_warning": (
            "Do not recommend pesticides for sunburn. First determine "
            "whether the symptoms are actually environmental damage "
            "rather than an infectious disease."
        )
    },


    # ========================================================
    # 55. thrips_disease
    # ========================================================

    "thrips_disease": {

        "plant": "Multiple / unspecified",

        "disease": "Thrips Infestation / Thrips Damage",

        "affected_part": "Leaf / Flower / Fruit / Young Shoots",

        "disease_type": "Insect Pest",

        "cause": (
            "Thrips are tiny insects that feed on plant tissue and "
            "can damage leaves, flowers and fruit. Some thrips species "
            "can also transmit plant viruses."
        ),

        "pathogen": "",

        "symptoms": [
            "Silvery or bronzed patches",
            "Fine streaks or scars",
            "Distorted young leaves",
            "Flower damage",
            "Fruit scarring",
            "Black fecal spots may be visible",
            "Stunted young growth",
            "Flower drop may occur"
        ],

        "why_it_happens": [
            "Thrips feed on young plant tissue",
            "Thrips populations can build up in flowers and tender growth",
            "Weeds can provide alternative hosts",
            "Some thrips species transmit plant viruses"
        ],

        "favorable_conditions": [
            "Warm weather",
            "Abundant flowering plants",
            "Dense vegetation",
            "Presence of weeds or alternate hosts",
            "High pest populations"
        ],

        "prevention": [
            "Monitor flowers and young leaves",
            "Remove weeds that can harbor thrips",
            "Use clean planting material",
            "Use insect-exclusion nets where appropriate",
            "Encourage natural enemies",
            "Inspect new plants before introduction"
        ],

        "immediate_action": [
            "Inspect flowers and young leaves",
            "Check for adult thrips and larvae",
            "Remove heavily damaged plant material where practical",
            "Monitor plants frequently",
            "Identify the thrips species when possible"
        ],

        "cultural_control": [
            "Remove weeds and alternate hosts",
            "Use reflective or exclusion methods where appropriate",
            "Maintain field sanitation",
            "Monitor with traps",
            "Protect beneficial insects"
        ],

        "biological_control": [
            "Predatory mites, minute pirate bugs and other natural "
            "enemies can help suppress thrips populations.",
            "Conservation biological control should be considered "
            "before unnecessary broad-spectrum insecticide use."
        ],

        "chemical_control": (
            "If insecticides are required, select a product specifically "
            "registered for the crop and thrips species or pest group. "
            "Thrips can be difficult to control because they hide in "
            "flowers and protected plant parts."
        ),

        "safety_warning": (
            "Do not use the same insecticide program for every crop. "
            "Follow the crop-specific label, rotate effective modes "
            "of action where appropriate, and protect pollinators."
        )
    }

}
# ============================================================
# DISEASE DATABASE
# PART 6 — CLASSES 56 TO 62
# ============================================================

PART_6_DATABASE = {

    # ========================================================
    # 56. tomato_early_blight_leaf
    # ========================================================

    "tomato_early_blight_leaf": {

        "plant": "Tomato",

        "disease": "Early Blight",

        "affected_part": "Leaf / Stem / Fruit",

        "disease_type": "Fungal",

        "cause": (
            "Tomato early blight is a fungal disease commonly caused "
            "by Alternaria solani."
        ),

        "pathogen": "Alternaria solani",

        "symptoms": [
            "Small brown to dark spots on older leaves",
            "Concentric rings may develop inside lesions",
            "Lesions can have a target-like appearance",
            "Yellowing may surround some lesions",
            "Severe infection can cause leaf drop",
            "Dark lesions may occur on stems",
            "Fruit can develop dark sunken lesions near the stem end"
        ],

        "why_it_happens": [
            "The fungus can survive in infected plant debris",
            "Spores can spread through wind and splashing water",
            "Plant stress can increase disease severity",
            "Wet foliage favors infection",
            "Infected volunteer plants can act as disease sources"
        ],

        "favorable_conditions": [
            "Warm weather",
            "High humidity",
            "Frequent rainfall",
            "Extended leaf wetness",
            "Plant stress",
            "Poor field sanitation"
        ],

        "prevention": [
            "Use healthy transplants",
            "Remove infected crop debris",
            "Practice crop rotation where appropriate",
            "Maintain adequate plant nutrition",
            "Avoid unnecessary leaf wetness",
            "Use tolerant varieties where available"
        ],

        "immediate_action": [
            "Inspect older leaves for target-like lesions",
            "Remove severely infected leaves where practical",
            "Remove infected debris",
            "Improve airflow",
            "Monitor nearby plants"
        ],

        "cultural_control": [
            "Remove crop residue",
            "Use crop rotation",
            "Maintain plant spacing",
            "Water at the base of plants",
            "Avoid working with wet foliage",
            "Maintain balanced plant nutrition"
        ],

        "biological_control": [
            "Biological products may be available depending on the "
            "production system and region.",
            "Use only products registered for tomato and the target disease."
        ],

        "chemical_control": (
            "Fungicides can be part of tomato early-blight management "
            "when disease pressure warrants treatment. Use only products "
            "registered for tomato early blight and follow the current label."
        ),

        "safety_warning": (
            "Do not use a fixed fungicide dosage from this database. "
            "Follow the product label for rate, PPE, application interval "
            "and pre-harvest interval."
        )
    },


    # ========================================================
    # 57. tomato_leaf
    # ========================================================

    "tomato_leaf": {

        "plant": "Tomato",

        "disease": "Tomato Leaf",

        "affected_part": "Leaf",

        "disease_type": "Unspecified / Dataset Class",

        "cause": (
            "This class identifies a tomato leaf but does not specify "
            "a particular disease."
        ),

        "pathogen": "",

        "symptoms": [
            "No specific disease can be confirmed from this class alone",
            "The leaf should be inspected for characteristic symptoms"
        ],

        "why_it_happens": [
            "The dataset class represents a tomato leaf rather than "
            "a specific named disease."
        ],

        "favorable_conditions": [],

        "prevention": [
            "Monitor tomato leaves regularly",
            "Maintain good plant spacing",
            "Maintain field sanitation",
            "Avoid prolonged leaf wetness",
            "Use healthy planting material"
        ],

        "immediate_action": [
            "Inspect the leaf carefully",
            "Check the rest of the plant",
            "Look for spots, blight, mosaic or other symptoms",
            "Do not apply a disease-specific pesticide based only on this class"
        ],

        "cultural_control": [
            "Maintain good airflow",
            "Remove confirmed diseased plant material",
            "Avoid excessive overhead irrigation",
            "Use clean tools"
        ],

        "biological_control": [],

        "chemical_control": (
            "No disease-specific chemical treatment should be recommended "
            "from this generic tomato-leaf class."
        ),

        "safety_warning": (
            "This class is not a confirmed disease diagnosis."
        )
    },


    # ========================================================
    # 58. tomato_leaf_bacterial_spot
    # ========================================================

    "tomato_leaf_bacterial_spot": {

        "plant": "Tomato",

        "disease": "Bacterial Spot",

        "affected_part": "Leaf / Stem / Fruit",

        "disease_type": "Bacterial",

        "cause": (
            "Tomato bacterial spot is caused by several Xanthomonas "
            "species."
        ),

        "pathogen": (
            "Xanthomonas species including X. euvesicatoria, "
            "X. vesicatoria, X. perforans and X. gardneri."
        ),

        "symptoms": [
            "Small dark brown or black leaf spots",
            "Lesions may become angular",
            "Yellow halos may occur around some lesions",
            "Leaf tissue can become severely damaged",
            "Stem lesions may occur",
            "Small raised spots can occur on fruit",
            "Severe infection can cause leaf drop"
        ],

        "why_it_happens": [
            "Bacteria can be introduced through infected seed or transplants",
            "Rain splash can spread bacteria",
            "Overhead irrigation can spread bacteria",
            "Plant handling can spread bacteria",
            "Infected crop debris can provide inoculum"
        ],

        "favorable_conditions": [
            "Warm weather",
            "High humidity",
            "Frequent rainfall",
            "Wet foliage",
            "Overhead irrigation",
            "Dense foliage"
        ],

        "prevention": [
            "Use certified disease-free seed",
            "Use healthy transplants",
            "Avoid overhead irrigation",
            "Water at the base of plants",
            "Maintain adequate plant spacing",
            "Remove infected plant debris",
            "Sanitize tools"
        ],

        "immediate_action": [
            "Remove severely affected leaves where practical",
            "Avoid handling wet plants",
            "Remove heavily infected plants when necessary",
            "Disinfect tools",
            "Monitor surrounding plants"
        ],

        "cultural_control": [
            "Use disease-free seed",
            "Inspect transplants before planting",
            "Use drip irrigation where appropriate",
            "Maintain crop sanitation",
            "Rotate crops where appropriate",
            "Avoid working in the field when plants are wet"
        ],

        "biological_control": [
            "Some biological products may be available depending "
            "on local registration and production system."
        ],

        "chemical_control": (
            "Copper-based products may be used in some bacterial-spot "
            "management programs, although resistance can reduce their "
            "effectiveness. Use only a product registered for tomato "
            "and bacterial spot in your region."
        ),

        "safety_warning": (
            "Do not give a universal copper or pesticide dose. "
            "Follow the current product label and local extension "
            "recommendations."
        )
    },


    # ========================================================
    # 59. tomato_leaf_late_blight
    # ========================================================

    "tomato_leaf_late_blight": {

        "plant": "Tomato",

        "disease": "Late Blight",

        "affected_part": "Leaf / Stem / Fruit",

        "disease_type": "Oomycete",

        "cause": (
            "Tomato late blight is caused by the oomycete "
            "Phytophthora infestans."
        ),

        "pathogen": "Phytophthora infestans",

        "symptoms": [
            "Irregular water-soaked leaf lesions",
            "Brown to dark rapidly expanding lesions",
            "White growth may appear on lesion undersides during humid weather",
            "Dark stem lesions",
            "Rapid leaf collapse",
            "Fruit can develop firm brown lesions",
            "Fruit lesions may become greasy or rough"
        ],

        "why_it_happens": [
            "The pathogen spreads through infected plant material",
            "Spores can spread by wind and water",
            "Wet foliage favors infection",
            "Cool to moderate temperatures with high moisture favor disease",
            "Infected volunteer plants can act as sources"
        ],

        "favorable_conditions": [
            "High humidity",
            "Frequent rain",
            "Long periods of leaf wetness",
            "Cool to moderate temperatures",
            "Dense foliage"
        ],

        "prevention": [
            "Use healthy transplants",
            "Remove volunteer tomato and potato plants",
            "Avoid prolonged leaf wetness",
            "Maintain good plant spacing",
            "Monitor disease forecasts where available",
            "Remove infected plant material"
        ],

        "immediate_action": [
            "Inspect the entire plant",
            "Remove severely infected plants where appropriate",
            "Avoid moving infected material",
            "Monitor nearby tomato and potato plants",
            "Follow local late-blight management recommendations"
        ],

        "cultural_control": [
            "Use disease-free transplants",
            "Remove volunteer plants",
            "Maintain sanitation",
            "Improve airflow",
            "Avoid unnecessary overhead irrigation"
        ],

        "biological_control": [
            "Biological control is limited for established late blight "
            "and should not replace an effective disease-management program."
        ],

        "chemical_control": (
            "Preventive fungicide programs may be used when late-blight "
            "risk is high. Select only products registered for tomato "
            "late blight and follow local recommendations and the label."
        ),

        "safety_warning": (
            "Late blight can spread rapidly. A model prediction should "
            "not replace field confirmation. Follow local plant-disease "
            "guidance when the disease is suspected."
        )
    },


    # ========================================================
    # 60. tomato_leaf_yellow_virus
    # ========================================================

    "tomato_leaf_yellow_virus": {

        "plant": "Tomato",

        "disease": "Tomato Yellow Leaf Curl Virus",

        "affected_part": "Leaf / Shoot",

        "disease_type": "Viral",

        "cause": (
            "Tomato yellow leaf curl disease is caused by Tomato yellow "
            "leaf curl virus (TYLCV), a begomovirus."
        ),

        "pathogen": "Tomato yellow leaf curl virus (TYLCV)",

        "symptoms": [
            "Yellowing of young leaves",
            "Upward curling of leaves",
            "Leaf reduction or distortion",
            "Shortened internodes",
            "Stunted plant growth",
            "Reduced flowering",
            "Reduced fruit production",
            "Severe infection can cause major yield loss"
        ],

        "why_it_happens": [
            "The virus is primarily transmitted by whiteflies",
            "Infected plants can act as virus sources",
            "Whiteflies can acquire and transmit the virus",
            "Weeds and volunteer plants can sometimes maintain virus sources"
        ],

        "favorable_conditions": [
            "Presence of infected plants",
            "High whitefly populations",
            "Warm conditions",
            "Continuous susceptible crops",
            "Presence of alternate hosts"
        ],

        "prevention": [
            "Use healthy transplants",
            "Use insect-protected nurseries",
            "Control whitefly populations",
            "Remove infected plants where appropriate",
            "Remove weed hosts where recommended",
            "Use resistant varieties where available"
        ],

        "immediate_action": [
            "Inspect the plant for whiteflies",
            "Remove severely infected plants where appropriate",
            "Inspect nearby plants",
            "Control the vector according to local recommendations",
            "Do not treat the virus itself with a fungicide"
        ],

        "cultural_control": [
            "Use virus-free seedlings",
            "Use insect exclusion in nurseries",
            "Remove infected plants",
            "Manage weeds and volunteer hosts",
            "Use resistant varieties where available"
        ],

        "biological_control": [
            "Natural enemies of whiteflies can contribute to vector "
            "management when conserved appropriately.",
            "Biological control does not cure an already infected plant."
        ],

        "chemical_control": (
            "There is no fungicide that cures a viral infection. "
            "Insecticides may be used against whitefly vectors when "
            "appropriate, but the product must be registered for tomato "
            "and the target pest."
        ),

        "safety_warning": (
            "Do not tell users that a fungicide can cure a viral disease. "
            "Vector management and prevention are more important than "
            "trying to cure infected tissue."
        )
    },


    # ========================================================
    # 61. tomato_septoria_leaf_spot
    # ========================================================

    "tomato_septoria_leaf_spot": {

        "plant": "Tomato",

        "disease": "Septoria Leaf Spot",

        "affected_part": "Leaf / Stem",

        "disease_type": "Fungal",

        "cause": (
            "Tomato Septoria leaf spot is caused by the fungus "
            "Septoria lycopersici."
        ),

        "pathogen": "Septoria lycopersici",

        "symptoms": [
            "Small circular spots on leaves",
            "Dark margins around lesions",
            "Gray or tan centers",
            "Small black fruiting structures may appear",
            "Lower leaves are often affected first",
            "Severe disease can cause extensive defoliation"
        ],

        "why_it_happens": [
            "The fungus can survive in infected plant debris",
            "Spores spread through splashing water",
            "Infected transplants can introduce disease",
            "Wet foliage favors infection",
            "Poor sanitation increases disease pressure"
        ],

        "favorable_conditions": [
            "Warm humid conditions",
            "Frequent rain",
            "Extended leaf wetness",
            "Dense foliage",
            "Overhead irrigation"
        ],

        "prevention": [
            "Use healthy transplants",
            "Remove infected plant debris",
            "Avoid overhead irrigation",
            "Maintain adequate spacing",
            "Use crop rotation where appropriate",
            "Monitor lower leaves regularly"
        ],

        "immediate_action": [
            "Remove severely infected lower leaves",
            "Remove diseased debris",
            "Improve airflow",
            "Avoid wetting foliage",
            "Monitor new symptoms"
        ],

        "cultural_control": [
            "Remove crop residue",
            "Use mulch to reduce soil splash",
            "Water at the base of plants",
            "Maintain good spacing",
            "Rotate crops where appropriate"
        ],

        "biological_control": [
            "Biological options depend on local availability and registration."
        ],

        "chemical_control": (
            "Fungicides can be included in management programs when "
            "appropriate. Use only products registered for tomato "
            "Septoria leaf spot and follow the label."
        ),

        "safety_warning": (
            "Do not use a universal fungicide dose. Product selection "
            "and harvest restrictions must follow the current label."
        )
    },


    # ========================================================
    # 62. yellow_leaf
    # ========================================================

    "yellow_leaf": {

        "plant": "Multiple / unspecified",

        "disease": "Yellow Leaf / Leaf Yellowing",

        "affected_part": "Leaf",

        "disease_type": "Unspecified / Physiological or Disease Symptom",

        "cause": (
            "Leaf yellowing is a symptom rather than one specific "
            "disease. It can result from nutrient deficiency, water "
            "stress, root problems, pests, viruses, or other diseases."
        ),

        "pathogen": (
            "Not specified. The model class does not identify the "
            "underlying cause."
        ),

        "symptoms": [
            "Yellowing of leaves",
            "General chlorosis",
            "Yellow areas between veins may occur",
            "Older or younger leaves may be affected depending on cause",
            "Growth reduction may occur",
            "Additional symptoms depend on the underlying problem"
        ],

        "why_it_happens": [
            "Nutrient deficiencies can cause chlorosis",
            "Overwatering can damage roots",
            "Underwatering can cause stress",
            "Root diseases can interfere with nutrient uptake",
            "Sap-sucking pests can cause yellowing",
            "Some viruses cause yellowing",
            "Poor soil conditions can affect plant health"
        ],

        "favorable_conditions": [
            "Water stress",
            "Poor drainage",
            "Nutrient imbalance",
            "Root damage",
            "Pest infestations",
            "Disease pressure",
            "Poor growing conditions"
        ],

        "prevention": [
            "Maintain appropriate irrigation",
            "Ensure good drainage",
            "Maintain balanced plant nutrition",
            "Monitor for pests",
            "Inspect roots when appropriate",
            "Monitor plants regularly"
        ],

        "immediate_action": [
            "Inspect the entire plant",
            "Check soil moisture",
            "Look for pests",
            "Inspect roots if symptoms are severe",
            "Check other leaves for characteristic disease patterns",
            "Do not apply pesticide until the cause is identified"
        ],

        "cultural_control": [
            "Maintain appropriate irrigation",
            "Improve drainage where necessary",
            "Maintain balanced nutrition",
            "Control confirmed pests",
            "Remove confirmed diseased plant material",
            "Maintain healthy growing conditions"
        ],

        "biological_control": [
            "Biological control depends on the actual underlying cause.",
            "No biological treatment should be selected solely from leaf yellowing."
        ],

        "chemical_control": (
            "No universal pesticide should be recommended for yellow "
            "leaves. Treatment must target the underlying cause."
        ),

        "safety_warning": (
            "Yellowing is a symptom, not a diagnosis. Do not automatically "
            "recommend a fungicide, insecticide or fertilizer without "
            "determining the likely cause."
        )
    }

}
# ============================================================
# COMBINE ALL 6 DATABASE PARTS
# ============================================================

DISEASE_DATABASE = {}
DISEASE_DATABASE.update(PART_1_DATABASE)
DISEASE_DATABASE.update(PART_2_DATABASE)
DISEASE_DATABASE.update(PART_3_DATABASE)
DISEASE_DATABASE.update(PART_4_DATABASE)
DISEASE_DATABASE.update(PART_5_DATABASE)
DISEASE_DATABASE.update(PART_6_DATABASE)
