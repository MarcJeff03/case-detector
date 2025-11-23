 # RA Law Keywords/Synonyms
 # Add or update as needed

STOP_WORDS = {
    "complaint", "case", "report", "issue", "problem", "concern",
    "incident", "matter", "subject", "topic", "event", "situation"
}

RA_KEYWORDS = {
        "9165": [
            "drug", "drugs", "dangerous drugs", "illegal drugs", "narcotic", "narcotics", "shabu", "marijuana",
            "cocaine", "heroin", "methamphetamine", "opium", "ecstasy", "substance abuse", "drug abuse",
            "drug trafficking", "drug pushing", "drug dealing", "drug possession", "drug use", "drug user", "drug addict",
            "sell drugs", "selling drugs", "buy drugs", "buying drugs", "pusher", "dealer", "push drugs", "deal drugs",
            "controlled substance", "drug paraphernalia", "drug test", "rehabilitation", "rehab", "pdea", "dangerous drugs board",
            "illegal substance", "illegal narcotics", "drug bust", "drug raid", "drug operation", "drug syndicate", "drug ring"
        ],
        "7610": [
            "child", "children", "minor", "minors", "juvenile", "youth", "kid", "kids",
            "child abuse", "abused child", "child exploitation", "child labor", "child trafficking",
            "child pornography", "sexual abuse", "physical abuse", "child neglect", "neglected child",
            "child protection", "child welfare", "best interest of the child", "parental authority",
            "custody", "adoption", "foster care", "dswd", "children in conflict with law", "cicl",
            "child victim", "child endangerment", "child maltreatment", "child rights violation", "child safety",
            "abandonment of child", "abandoned child", "child exploitation online", "child prostitution"
        ],
        "11199": [
            "social security", "sss", "social security system", "social security commission",
            "pension", "retirement", "retirement benefits", "pension benefits", "contributions",
            "sss contribution", "monthly contribution", "employee benefits", "member", "membership",
            "coverage", "unemployment", "disability", "disability benefits", "sickness benefits",
            "maternity benefits", "death benefits", "funeral benefits", "salary loan",
            "calamity loan", "retirement fund", "social insurance", "workers benefits",
            "employment benefits", "dependents", "beneficiary", "self-employed", "ofw",
            "overseas worker", "contribution collection", "benefit claims", "pension fund",
            "sss id", "sss number", "sss loan", "sss pension", "sss claim", "sss office", "sss branch",
            "sss application", "sss inquiry", "sss online", "sss deduction", "sss remittance"
        ],
        "10361": [
            "domestic", "violence", "domestic violence", "vawc", "women", "woman", "abuse",
            "battered", "battered woman", "battered wife", "physical violence", "sexual violence", "psychological violence",
            "economic abuse", "marital abuse", "spousal abuse", "intimate partner violence",
            "protection order", "barangay protection order", "temporary protection order",
            "permanent protection order", "violence against women", "violence against children",
            "battery", "assault", "harassment", "threat", "intimidation", "stalking",
            "domestic abuse", "domestic dispute", "domestic fight", "abused wife", "abused partner", "abused spouse",
            "abusive husband", "abusive partner", "abusive spouse", "family violence", "spousal violence"
        ],
        "10175": [
            "cyber", "cybercrime", "hacking", "hacker", "computer", "internet", "online",
            "cyber attack", "cyber fraud", "phishing", "identity theft", "data breach",
            "unauthorized access", "illegal access", "computer fraud", "online fraud",
            "cyber libel", "libel", "defamation", "online defamation", "cyber bullying",
            "online harassment", "cyber harassment", "malware", "virus", "ransomware",
            "computer misuse", "data theft", "information theft", "credit card fraud",
            "online scam", "scam", "spam", "child pornography online", "cybersex",
            "online pornography", "digital crime", "electronic crime", "website hacking",
            "network intrusion", "password theft", "account hacking", "social media fraud",
            "cyberstalking", "cyber threat", "cyber extortion", "phishing email", "phishing scam", "phishing attack",
            "online identity theft", "online impersonation", "fake account", "fake profile", "doxxing", "doxing"
        ],
        "8293": [
        # Core IP Terms
        "intellectual property", "intellectual property rights", "IPR", "IP rights", "IP law",
        
        # Copyright
        "copyright", "copyright law", "copyright protection", "copyrighted work", "copyrighted material",
        "copyright holder", "copyright owner", "copyright violation", "copyright breach",
        "literary work", "artistic work", "musical composition", "dramatic work", "audiovisual work",
        
        # Patent
        "patent", "patent law", "patent rights", "patent protection", "patented invention",
        "patent holder", "patent owner", "patent violation", "patent application", "patent registration",
        "utility model", "industrial design", "invention", "inventor",
        
        # Trademark
        "trademark", "trademark law", "trademark rights", "trademark protection", "registered trademark",
        "trademark holder", "trademark owner", "trademark violation", "service mark", "brand name",
        "logo", "brand identity", "trade name", "commercial mark",
        
        # Infringement
        "infringement", "copyright infringement", "patent infringement", "trademark infringement",
        "IP infringement", "rights infringement", "violation of rights", "unauthorized use",
        "unlawful use", "illegal reproduction", "unauthorized reproduction", "unlicensed use",
        
        # Piracy & Counterfeiting
        "piracy", "pirated copy", "pirated material", "pirated work", "pirated product",
        "counterfeit", "counterfeit goods", "counterfeit product", "fake product", "fake goods",
        "fake brand", "imitation", "knockoff", "knock-off", "bootleg", "bootlegged",
        "forgery", "forged work", "fraudulent copy",
        
        # Theft & Plagiarism
        "intellectual theft", "IP theft", "idea theft", "plagiarism", "plagiarized work",
        "plagiarize", "copied work", "stolen work", "misappropriation", "unauthorized copying",
        
        # Rights & Licensing
        "exclusive rights", "licensing", "license agreement", "royalty", "royalty payment",
        "intellectual creation", "original work", "creative work", "protected work",
        
        # Violations
        "brand infringement", "IP violation", "IP complaint", "IP dispute", "IP case",
        "unlicensed copy", "unauthorized distribution", "illegal distribution", "illegal sale",
        "selling fake goods", "selling counterfeit", "producing fake", "manufacturing counterfeit"
    ],
    
    "9262": [
        # Core VAWC Terms
        "violence against women", "violence against women and children", "VAWC", "anti-violence",
        "anti-violence against women", "women and children protection",
        
        # Types of Abuse
        "abuse", "physical abuse", "physical violence", "bodily harm", "physical assault",
        "sexual abuse", "sexual violence", "sexual assault", "marital rape", "spousal rape",
        "psychological abuse", "psychological violence", "emotional abuse", "mental abuse",
        "economic abuse", "financial abuse", "economic violence", "deprivation",    
        
        # Domestic Violence
        "domestic violence", "domestic abuse", "family violence", "household violence",
        "marital abuse", "spousal abuse", "intimate partner violence", "partner abuse",
        "wife beating", "wife battering", "spouse beating", "partner violence",
        
        # Relationships
        "battered woman", "battered wife", "battered spouse", "battered partner",
        "abused wife", "abused partner", "abused spouse", "abused woman",
        "abusive husband", "abusive partner", "abusive spouse", "abusive boyfriend",
        "abusive girlfriend", "abusive relationship", "abusive marriage", "toxic relationship",
        "abusive ex", "abusive ex-partner", "abusive ex-spouse", "abusive ex-husband", "abusive ex-wife",
        
        # Actions & Behaviors
        "harassment", "threat", "threatening", "intimidation", "intimidating behavior",
        "stalking", "following", "monitoring", "controlling behavior", "coercion",
        "verbal abuse", "insult", "humiliation", "degradation", "belittling",
        "hitting", "beating", "slapping", "punching", "kicking", "pushing", "shoving",
        
        # Protection & Legal
        "protection order", "barangay protection order", "BPO", "temporary protection order",
        "TPO", "permanent protection order", "PPO", "restraining order",
        "protective measure", "safety order",
        
        # Victims & Survivors
        "victim", "survivor", "abuse victim", "abuse survivor", "battered victim",
        "violence victim", "violence survivor",
        
        # Legal Actions
        "VAWC case", "VAWC complaint", "VAWC violation", "abuse complaint", "abuse case",
        "violence complaint", "domestic violence case", "marital abuse case"
    ],
    
    "10173": [
        # Core Privacy Terms
        "data privacy", "privacy", "privacy rights", "right to privacy", "privacy law",
        "data privacy act", "data protection", "information privacy", "personal privacy",
        
        # Personal Data
        "personal information", "personal data", "private data", "private information",
        "sensitive personal information", "sensitive data", "privileged information",
        "confidential information", "confidential data", "personally identifiable information", "PII",
        
        # Data Subject Rights
        "data subject", "data owner", "information owner", "right to access", "right to rectify",
        "right to erasure", "right to object", "right to portability", "right to be forgotten",
        
        # Data Processing
        "processing", "data processing", "information processing", "data collection",
        "data gathering", "data storage", "data retention", "data use", "data utilization",
        "data sharing", "data transfer", "data transmission", "data disclosure",
        
        # Controllers & Processors
        "data controller", "data processor", "personal information controller", "PIC",
        "personal information processor", "PIP", "data custodian", "data handler",
        
        # Consent
        "consent", "informed consent", "explicit consent", "voluntary consent",
        "consent withdrawal", "permission", "authorization", "approval",
        
        # Security
        "information security", "data security", "security measures", "safeguards",
        "confidentiality", "encryption", "access control", "security breach",
        
        # Breaches & Violations
        "data breach", "privacy breach", "security breach", "information breach",
        "data leak", "data leakage", "leaked information", "leaked data", "information leak",
        "data exposure", "data compromise", "unauthorized disclosure",
        
        # Unauthorized Actions
        "data theft", "information theft", "identity theft", "data misuse", "data abuse",
        "unauthorized access", "illegal access", "unlawful access", "improper access",
        "unauthorized use", "unauthorized collection", "unauthorized processing",
        
        # Privacy Commission
        "privacy commission", "National Privacy Commission", "NPC", "privacy complaint",
        "privacy violation", "privacy offense", "data privacy violation",
        
        # Risks & Concerns
        "privacy risk", "privacy concern", "privacy issue", "data loss", "information loss",
        "breach notification", "privacy breach notification", "data incident"
    ],
    
    "10627": [
        # Core Bullying Terms
        "bullying", "anti-bullying", "anti-bullying act", "bullying prevention",
        "bully", "bullied", "being bullied",
        
        # Types of Bullying
        "cyberbullying", "cyber-bullying", "online bullying", "internet bullying",
        "social media bullying", "digital bullying", "electronic bullying",
        "physical bullying", "verbal bullying", "social bullying", "relational bullying",
        "psychological bullying", "emotional bullying",
        
        # School Context
        "school violence", "school bullying", "classroom bullying", "campus bullying",
        "playground bullying", "bullying at school", "bullying in school", "bullying in class",
        "peer abuse", "peer violence", "peer harassment", "peer intimidation",
        "student harassment", "student violence", "student intimidation",
        
        # Actions & Behaviors
        "harassment", "intimidation", "threatening", "taunting", "teasing",
        "name-calling", "mocking", "ridiculing", "humiliation", "embarrassment",
        "exclusion", "isolation", "ostracism", "rejection", "shunning",
        "physical attack", "hitting", "pushing", "shoving", "kicking",
        "spreading rumors", "gossip", "defamation", "false accusations",
        
        # Online Bullying Actions
        "posting", "sharing", "messaging", "commenting", "tagging",
        "trolling", "flaming", "impersonation", "fake account", "fake profile",
        "doxing", "doxxing", "outing", "exclusion", "cyberstalking",
        
        # Victims & Perpetrators
        "victim", "bullying victim", "target", "perpetrator", "bully", "aggressor",
        "offender", "harasser", "tormentor",
        
        # Locations & Platforms
        "in school", "in class", "in classroom", "in campus", "in playground",
        "in internet", "in social media", "online", "on Facebook", "on Twitter",
        "on Instagram", "on TikTok", "on messaging apps",
        
        # Perpetrators by Role
        "bullying by teacher", "bullying by classmate", "bullying by peer",
        "bullying by student", "bullying by group", "bullying by gang",
        "bullying by staff", "bullying by principal", "bullying by administrator",
        
        # Protection & Response
        "child protection", "student protection", "safe school", "safe learning environment",
        "disciplinary measures", "disciplinary action", "intervention", "reporting",
        
        # Legal & Administrative
        "bullying incident", "bullying case", "bullying report", "bullying complaint",
        "bullying violation", "bullying offense", "anti-bullying law", "anti-bullying policy"
    ],
    
    "11313": [
        # Core Act Terms
        "safe spaces", "safe spaces act", "bawal bastos", "bawal bastos law",
        "gender-based", "gender equality", "women's rights",
        
        # Types of Harassment
        "harassment", "sexual harassment", "gender-based harassment", "gender harassment",
        "public harassment", "street harassment", "workplace harassment", "online harassment",
        "community harassment", "verbal harassment", "physical harassment",
        
        # Specific Behaviors
        "catcalling", "cat-calling", "wolf-whistling", "whistling", "hooting",
        "lewd remarks", "lewd comments", "offensive remarks", "offensive comments",
        "sexual remarks", "sexual comments", "sexual innuendo", "vulgar remarks",
        "inappropriate remarks", "inappropriate comments", "inappropriate behavior",
        "unwanted remarks", "unwanted comments", "unwanted attention",
        
        # Sexual Advances
        "sexual advances", "unwanted advances", "unwelcome advances", "unsolicited advances",
        "persistent advances", "aggressive advances", "inappropriate advances",
        
        # Violence & Discrimination
        "gender-based violence", "gender violence", "sexist violence",
        "gender-based discrimination", "sex discrimination", "sexism", "misogyny",
        
        # Public Spaces
        "public misconduct", "public disturbance", "public offense", "street offense",
        "public indecency", "indecent behavior", "improper conduct",
        
        # Online Context
        "online harassment", "cyber harassment", "digital harassment",
        "social media harassment", "internet harassment", "electronic harassment",
        "online abuse", "cyber abuse", "digital abuse",
        
        # Actions & Conduct
        "sexist remarks", "sexist behavior", "discriminatory remarks", "discriminatory behavior",
        "objectification", "sexualization", "unwanted touching", "groping",
        "stalking", "following", "persistent following", "unwanted following",
        
        # Insults & Threats
        "gender-based insult", "sexist insult", "gender-based slur", "sexist slur",
        "gender-based threat", "sexual threat", "threat of violence",
        "intimidation", "intimidating behavior", "threatening behavior",
        
        # Contexts
        "in public", "in workplace", "in community", "in school", "in street",
        "in online", "in internet", "in social media", "in public space",
        "in public transport", "in establishment",
        
        # Legal Terms
        "gender-based offense", "gender-based violation", "harassment complaint",
        "harassment case", "safe spaces violation", "bawal bastos violation"
    ],
    
    "9003": [
        # Core Waste Terms
        "solid waste", "ecological solid waste", "solid waste management", "waste management",
        "waste", "garbage", "trash", "rubbish", "refuse", "litter", "junk",
        
        # Waste Types
        "biodegradable waste", "non-biodegradable waste", "recyclable waste",
        "organic waste", "inorganic waste", "hazardous waste", "toxic waste",
        "electronic waste", "e-waste", "plastic waste", "food waste",
        "garden waste", "yard waste", "construction waste", "demolition waste",
        
        # Waste Management Practices
        "waste segregation", "segregation", "separation", "sorting",
        "waste separation", "waste sorting", "waste classification",
        "recycling", "recycle", "recyclables", "reuse", "reduce",
        "composting", "compost", "organic composting", "vermicomposting",
        
        # Collection & Disposal
        "waste disposal", "garbage disposal", "trash disposal", "disposal",
        "waste collection", "garbage collection", "trash collection", "collection",
        "waste removal", "garbage removal", "hauling", "transport",
        
        # Facilities & Equipment
        "landfill", "sanitary landfill", "dumpsite", "disposal site",
        "waste facility", "transfer station", "material recovery facility", "MRF",
        "waste bin", "garbage bin", "trash bin", "trash can", "waste container",
        "segregation bin", "color-coded bin", "biodegradable bin", "non-biodegradable bin",
        
        # Environmental Terms
        "environmental protection", "environmental law", "ecological balance",
        "pollution prevention", "waste reduction", "zero waste",
        "cleanliness", "sanitation", "hygiene", "clean environment",
        
        # Violations & Issues
        "littering", "illegal dumping", "improper disposal", "open burning",
        "burning waste", "burning garbage", "waste burning",
        "mixed waste", "unsegregated waste", "non-segregated waste",
        
        # Programs & Initiatives
        "waste management program", "recycling program", "composting program",
        "clean-up drive", "cleanup", "waste collection drive",
        "environmental campaign", "awareness campaign", "information drive",
        
        # Legal & Compliance
        "waste law", "waste regulation", "waste ordinance", "waste policy",
        "waste violation", "waste offense", "environmental violation",
        "non-compliance", "violation of waste law"
    ],
    
    "8485": [
        # Core Animal Welfare Terms
        "animal welfare", "animal welfare act", "animal rights", "animal protection",
        "protection of animals", "humane treatment", "animal care",
        
        # Animal Cruelty
        "animal cruelty", "cruelty to animals", "animal abuse", "animal mistreatment",
        "animal maltreatment", "animal torture", "animal suffering", "animal harm",
        
        # Types of Abuse
        "physical abuse", "neglect", "animal neglect", "pet neglect",
        "abandonment", "animal abandonment", "pet abandonment",
        "starvation", "animal starvation", "malnutrition", "animal malnutrition",
        "beating", "animal beating", "hitting animals", "kicking animals",
        "torture", "animal torture", "tormenting animals",
        
        # Harm & Injury
        "harming animals", "injuring animals", "hurting animals", "wounding animals",
        "animal injury", "animal wound", "animal pain", "animal distress",
        "animal violence", "violence against animals", "brutal treatment",
        
        # Neglect Terms
        "neglecting animals", "failure to care", "improper care", "inadequate care",
        "lack of care", "insufficient care", "deprivation", "withholding care",
        "unattended animal", "unfed animal", "unwatered animal",
        "unhealthy animal", "sick animal", "diseased animal", "injured animal",
        
        # Pet Care
        "pet care", "pet welfare", "pet health", "pet safety",
        "veterinary care", "vet care", "medical care", "proper care",
        "feeding", "watering", "shelter", "housing",
        
        # Animals
        "pet", "pets", "domestic animal", "companion animal",
        "dog", "cat", "bird", "livestock", "farm animal",
        "stray animal", "stray dog", "stray cat", "wild animal",
        
        # Conditions & States
        "mistreated animal", "neglected animal", "abused animal", "abandoned animal",
        "malnourished animal", "starving animal", "suffering animal",
        "endangered animal", "unprotected animal", "vulnerable animal",
        
        # Facilities & Organizations
        "animal shelter", "animal rescue", "animal sanctuary",
        "veterinary clinic", "vet clinic", "animal hospital",
        "rescue center", "adoption center",
        
        # Legal Terms
        "animal welfare law", "animal protection law", "anti-cruelty law",
        "animal welfare violation", "animal cruelty violation", "cruelty offense",
        "animal abuse case", "animal cruelty case", "cruelty complaint",
        
        # Actions & Responsibilities
        "animal rescue", "rescue operation", "animal seizure", "confiscation",
        "reporting", "complaint filing", "investigation", "prosecution"
    ],
    
    "3019": [
        # Core Anti-Graft Terms
        "anti-graft", "anti-graft law", "anti-graft act", "graft", "graft and corruption",
        "corrupt practices", "corrupt practices act", "corruption",
        
        # Public Officials
        "public officer", "public official", "government official", "government employee",
        "public servant", "civil servant", "elected official", "appointed official",
        "barangay official", "local official", "national official",
        
        # Types of Corruption
        "bribery", "bribe", "bribed", "bribing", "soliciting bribe",
        "giving bribe", "receiving bribe", "accepting bribe", "payoff", "grease money",
        "kickback", "kickback scheme", "commission", "under-the-table payment",
        "protection money", "extortion", "shakedown",
        
        # Malversation
        "malversation", "misappropriation", "embezzlement", "misuse of funds",
        "misuse of public funds", "theft of public funds", "plunder",
        "illegal use of funds", "unauthorized use of funds",
        
        # Illegal Transactions
        "illegal transaction", "illegal contract", "illegal deal", "illegal agreement",
        "unlawful transaction", "unlawful contract", "unlawful deal",
        "anomalous transaction", "anomalous contract", "suspicious transaction",
        
        # Conflict of Interest
        "conflict of interest", "personal interest", "vested interest",
        "self-dealing", "nepotism", "favoritism", "cronyism",
        "unfair advantage", "preferential treatment",
        
        # Prohibited Acts
        "prohibited transaction", "prohibited act", "unlawful act", "illegal act",
        "fraudulent act", "fraudulent transaction", "ghost project",
        "overpricing", "overprice", "price manipulation", "bid rigging",
        
        # Financial Crimes
        "ghost employee", "fake employee", "dummy", "dummy corporation",
        "fake receipt", "falsified document", "forged document",
        "money laundering", "ill-gotten wealth", "unexplained wealth",
        
        # Administrative Terms
        "abuse of authority", "abuse of power", "misuse of authority",
        "gross misconduct", "grave misconduct", "dishonesty",
        "betrayal of public trust", "violation of oath",
        
        # Legal Terms
        "graft case", "graft complaint", "corruption case", "corruption complaint",
        "anti-graft violation", "corrupt practices violation",
        "graft charge", "corruption charge", "indictment",
        
        # Investigation & Evidence
        "investigation", "inquiry", "probe", "audit", "examination",
        "evidence", "proof", "documentation", "record", "testimony",
        "whistleblower", "informant", "witness"
    ],
    
    "8749": [
        # Core Clean Air Terms
        "clean air", "clean air act", "air quality", "air pollution", "air pollution law",
        "air quality law", "atmospheric quality",
        
        # Pollutants
        "pollutant", "air pollutant", "emissions", "emission", "exhaust",
        "toxic fumes", "harmful emissions", "dangerous emissions",
        "particulate matter", "PM", "PM2.5", "PM10", "fine particles",
        "carbon monoxide", "CO", "carbon dioxide", "CO2",
        "nitrogen oxide", "NOx", "sulfur dioxide", "SO2",
        
        # Vehicle Emissions
        "smoke belching", "smoke belcher", "vehicle emission", "automobile emission",
        "vehicular emission", "car emission", "exhaust emission",
        "black smoke", "dark smoke", "excessive smoke", "heavy smoke",
        "diesel smoke", "gasoline fumes",
        
        # Industrial Pollution
        "industrial emission", "factory emission", "plant emission",
        "industrial pollution", "factory pollution", "smokestack emission",
        "chimney emission", "industrial smoke", "industrial waste",
        
        # Burning
        "open burning", "burning waste", "burning garbage", "burning trash",
        "burning leaves", "burning tires", "incineration", "illegal burning",
        
        # Air Quality Issues
        "polluted air", "contaminated air", "dirty air", "toxic air",
        "poor air quality", "bad air quality", "unhealthy air",
        "smog", "haze", "air contamination", "atmospheric pollution",
        
        # Sources
        "pollution source", "emission source", "point source", "non-point source",
        "stationary source", "mobile source", "area source",
        
        # Environmental Protection
        "environmental protection", "environmental law", "anti-pollution",
        "pollution prevention", "pollution control", "emission control",
        "air quality management", "air quality monitoring",
        
        # Standards & Testing
        "emission standards", "air quality standards", "emission testing",
        "smoke test", "emission test", "compliance test",
        "air quality index", "AQI", "pollution level",
        
        # Violations
        "air violation", "emission violation", "air quality violation",
        "air law violation", "clean air violation", "pollution violation",
        "non-compliance", "exceeding limits", "emission excess",
        
        # Legal Terms
        "air complaint", "air case", "emission complaint", "pollution complaint",
        "air offense", "emission offense", "pollution offense"
    ],
    
    "9275": [
        # Core Clean Water Terms
        "clean water", "clean water act", "water quality", "water pollution",
        "water pollution law", "water quality law", "aquatic quality",
        
        # Water Bodies
        "river", "stream", "creek", "lake", "pond", "sea", "ocean",
        "bay", "waterway", "water body", "aquifer", "groundwater",
        "surface water", "freshwater", "saltwater", "marine water",
        
        # Pollutants
        "wastewater", "waste water", "sewage", "effluent", "discharge",
        "runoff", "contaminated water", "polluted water", "dirty water",
        "toxic waste", "hazardous waste", "chemical waste", "industrial waste",
        
        # Pollution Sources
        "water pollution source", "pollution discharge", "illegal discharge",
        "unauthorized discharge", "industrial discharge", "domestic sewage",
        "agricultural runoff", "oil spill", "chemical spill", "waste dumping",
        
        # Treatment & Management
        "water treatment", "wastewater treatment", "sewage treatment",
        "treatment plant", "treatment facility", "septic system",
        "water purification", "water filtration", "water management",
        
        # Standards & Permits
        "discharge permit", "effluent permit", "water quality standards",
        "effluent standards", "pollution control", "emission standards",
        "compliance monitoring", "water testing", "quality testing",
        
        # Contamination
        "contamination", "water contamination", "pollution", "fouling",
        "bacterial contamination", "chemical contamination", "oil contamination",
        "heavy metal", "pathogen", "bacteria", "virus",
        
        # Environmental Impact
        "environmental protection", "environmental law", "anti-pollution",
        "ecosystem protection", "marine protection", "aquatic life protection",
        "water resource protection", "watershed protection",
        
        # Water Quality Issues
        "poor water quality", "unsafe water", "unclean water", "impure water",
        "turbid water", "murky water", "foul-smelling water", "discolored water",
        "algal bloom", "eutrophication", "oxygen depletion",
        
        # Violations
        "water violation", "water quality violation", "discharge violation",
        "pollution violation", "clean water violation", "effluent violation",
        "illegal dumping", "unauthorized dumping", "non-compliance",
        
        # Legal Terms
        "water complaint", "water case", "pollution complaint", "discharge complaint",
        "water offense", "pollution offense", "environmental offense"
    ],
    
    "9514": [
        # Core Fire Code Terms
        "fire code", "fire code of the philippines", "fire code law", "fire code act",
        "fire safety", "fire protection", "fire prevention",
        
        # Fire Safety Equipment
        "fire extinguisher", "fire alarm", "fire alarm system", "smoke detector",
        "smoke alarm", "fire sprinkler", "sprinkler system", "fire hose",
        "fire hydrant", "fire exit", "emergency exit", "exit sign",
        "fire door", "fire escape", "fire ladder", "emergency lighting",
        
        # Fire Hazards
        "fire hazard", "fire risk", "fire danger", "combustible material",
        "flammable material", "flammable liquid", "flammable gas",
        "explosive material", "hazardous material", "ignition source",
        
        # Fire Prevention
        "fire prevention measures", "fire safety measures", "preventive measures",
        "fire inspection", "safety inspection", "fire drill", "fire exercise",
        "evacuation drill", "emergency drill", "fire safety training",
        
        # Building Safety
        "fire safety compliance", "building safety", "structural safety",
        "occupancy load", "maximum capacity", "fire resistance",
        "fire-resistant material", "fireproof", "fire-rated",
        
        # Firefighting
        "firefighting", "fire suppression", "fire brigade", "fire department",
        "fire station", "firefighter", "fire response", "emergency response",
        "fire control", "fire containment", "fire extinguishment",
        
        # Fire Incidents
        "fire", "fire incident", "fire outbreak", "blaze", "conflagration",
        "fire emergency", "fire disaster", "arson", "deliberate fire",
        "accidental fire", "electrical fire", "kitchen fire",
        
        # Violations
        "fire code violation", "fire safety violation", "fire law violation",
        "non-compliance", "violation", "breach", "infraction",
        "blocked exit", "blocked fire exit", "obstructed exit",
        "missing extinguisher", "expired extinguisher", "non-functional alarm",
        
        # Inspections & Permits
        "fire safety inspection", "fire clearance", "fire safety certificate",
        "occupancy permit", "fire permit", "compliance certificate",
        "BFP", "Bureau of Fire Protection", "fire marshal",
        
        # Legal Terms
        "fire complaint", "fire case", "fire violation case", "fire offense",
        "fire safety complaint", "fire code complaint"
    ],
    
    "4136": [
        # Core Land Transportation Terms
        "land transportation", "land transportation code", "land transportation act",
        "land transportation law", "traffic", "traffic law", "traffic rules",
        "traffic regulations", "road safety", "highway safety",
        
        # Vehicles
        "motor vehicle", "vehicle", "automobile", "car", "truck", "bus",
        "motorcycle", "motorbike", "tricycle", "jeepney", "van",
        "private vehicle", "public vehicle", "commercial vehicle",
        
        # Registration & Licensing
        "vehicle registration", "car registration", "registration", "plate number",
        "license plate", "unregistered vehicle", "expired registration",
        "driver's license", "driver license", "license", "professional driver's license",
        "student permit", "expired license", "suspended license", "revoked license",
        "no license", "without license", "unlicensed driver", "driving without license",
        
        # LTO
        "LTO", "Land Transportation Office", "LTO registration", "LTO requirements",
        "LTO clearance", "LTO violation", "LTO ticket",
        
        # Traffic Violations
        "traffic violation", "traffic ticket", "traffic citation", "violation ticket",
        "driving violation", "moving violation", "traffic offense", "traffic infraction",
        
        # Reckless Driving
        "reckless driving", "careless driving", "dangerous driving", "aggressive driving",
        "speeding", "overspeeding", "over-speeding", "speed limit violation",
        "tailgating", "weaving", "swerving", "illegal overtaking",
        
        # DUI/DWI
        "drunk driving", "driving under the influence", "DUI", "driving while intoxicated",
        "DWI", "intoxicated driver", "drunk driver", "alcohol-related",
        
        # Road Safety
        "road accident", "traffic accident", "vehicular accident", "collision",
        "crash", "hit and run", "hit-and-run", "leaving scene of accident",
        "road hazard", "traffic hazard", "unsafe driving",
        
        # Traffic Rules
        "traffic light", "traffic signal", "stop sign", "yield sign", "road sign",
        "beating red light", "running red light", "red light violation",
        "illegal parking", "no parking", "wrong parking", "obstruction",
        "counterflow", "wrong-way driving", "driving on wrong side",
        
        # Equipment Violations
        "no helmet", "without helmet", "missing side mirror", "defective lights",
        "broken lights", "tinted windows", "illegal modification", "loud muffler",
        
        # Public Transport
        "PUV", "public utility vehicle", "jeepney", "bus", "taxi", "tricycle",
        "transport violation", "franchise", "expired franchise", "colorum",
        "out of line", "overloading", "overloaded", "passenger overload",
        
        # Legal Terms
        "traffic complaint", "traffic case", "traffic report", "traffic offense",
        "LTO apprehension", "traffic apprehension", "traffic violation record",
        "demerit points", "penalty points", "traffic fine", "violation fine"
    ],
    
    "8353": [
        # Core Anti-Rape Terms
        "rape", "anti-rape", "anti-rape law", "anti-rape act", "rape law",
        "rape act", "sexual assault", "sexual violence", "sexual attack",
        
        # Types of Rape
        "statutory rape", "marital rape", "spousal rape", "date rape",
        "acquaintance rape", "gang rape", "rape by instrumentation",
        "attempted rape", "frustrated rape", "consummated rape",
        
        # Sexual Crimes
        "sexual abuse", "sexual offense", "sexual violation", "sexual crime",
        "sexual intercourse", "forced intercourse", "non-consensual intercourse",
        "carnal knowledge", "sexual penetration", "forced penetration",
        
        # Consent
        "consent", "lack of consent", "without consent", "against will",
        "non-consensual", "forced", "coerced", "involuntary",
        "inability to consent", "unconscious", "intoxicated", "drugged",
        
        # Violence & Force
        "force", "physical force", "violence", "threat", "intimidation",
        "coercion", "duress", "restraint", "resistance", "struggle",
        
        # Victims & Offenders
        "rape victim", "victim", "survivor", "rape survivor",
        "offender", "rapist", "perpetrator", "accused", "assailant",
        "sex offender", "sexual predator",
        
        # Circumstances
        "under the influence", "drugged victim", "intoxicated victim",
        "unconscious victim", "asleep", "helpless", "vulnerable",
        "minor victim", "child victim", "elderly victim", "disabled victim",
        
        # Support Services
        "rape crisis center", "crisis center", "victim support", "counseling",
        "medical examination", "medico-legal", "rape kit", "forensic examination",
        "psychological support", "trauma counseling",
        
        # Legal Terms
        "rape case", "rape complaint", "rape charge", "rape accusation",
        "rape allegation", "rape report", "rape incident", "sexual assault case",
        "rape prosecution", "rape conviction", "rape sentence"
    ],
    
    "7877": [
        # Core Sexual Harassment Terms
        "sexual harassment", "sexual harassment law", "sexual harassment act",
        "anti-sexual harassment", "anti-sexual harassment law",
        
        # Contexts
        "workplace harassment", "work harassment", "office harassment",
        "employment harassment", "job-related harassment",
        "school harassment", "academic harassment", "education harassment",
        "campus harassment", "teacher-student harassment",
        
        # Types of Harassment
        "quid pro quo", "hostile environment", "hostile work environment",
        "hostile educational environment", "sexual coercion", "sexual exploitation",
        
        # Unwelcome Conduct
        "unwelcome advances", "unwanted advances", "sexual advances",
        "inappropriate advances", "persistent advances", "repeated advances",
        "unwelcome behavior", "unwanted behavior", "inappropriate behavior",
        
        # Verbal Harassment
        "verbal harassment", "sexual remarks", "sexual comments", "sexual jokes",
        "lewd remarks", "lewd comments", "obscene remarks", "vulgar comments",
        "sexual innuendo", "suggestive comments", "offensive remarks",
        "catcalling", "whistling", "sexist remarks", "derogatory remarks",
        
        # Physical Harassment
        "physical harassment", "unwanted touching", "inappropriate touching",
        "groping", "fondling", "sexual touching", "physical contact",
        "blocking path", "cornering", "invasion of personal space",
        
        # Visual Harassment
        "leering", "staring", "ogling", "sexual gestures", "indecent exposure",
        "showing pornography", "sexual images", "sexual materials",
        
        # Digital Harassment
        "electronic harassment", "online harassment", "cyber harassment",
        "sexual messages", "sexual texts", "sexual emails", "sexual calls",
        "sending sexual content", "sharing sexual images",
        
        # Power Dynamics
        "abuse of authority", "abuse of power", "superior-subordinate",
        "boss-employee", "teacher-student", "professor-student",
        "position of authority", "position of power", "leverage",
        
        # Retaliation
        "retaliation", "reprisal", "revenge", "punishment", "adverse action",
        "demotion", "termination", "failing grade", "discrimination",
        
        # Victims & Perpetrators
        "victim", "complainant", "harassed person", "target",
        "perpetrator", "harasser", "offender", "accused harasser",
        
        # Environment
        "hostile environment", "intimidating environment", "offensive environment",
        "uncomfortable environment", "toxic workplace", "toxic environment",
        
        # Sexual Misconduct
        "sexual misconduct", "sexual impropriety", "inappropriate conduct",
        "unprofessional conduct", "unethical behavior",
        
        # Legal Terms
        "harassment case", "harassment complaint", "harassment charge",
        "sexual harassment report", "harassment allegation", "harassment claim",
        "harassment investigation", "harassment violation"
    ],
    
    "6713": [
        # Core Code of Conduct Terms
        "code of conduct", "code of conduct and ethical standards",
        "ethical standards", "ethics", "professional ethics", "public service ethics",
        
        # Values & Principles
        "integrity", "honesty", "probity", "uprightness", "rectitude",
        "accountability", "responsibility", "answerability",
        "transparency", "openness", "disclosure", "public disclosure",
        "public interest", "national interest", "common good",
        
        # Public Service
        "public service", "public office", "government service",
        "civil service", "public duty", "official duty", "public trust",
        "public accountability", "public responsibility",
        
        # Public Officials
        "public official", "public officer", "government official",
        "civil servant", "public servant", "elected official", "appointed official",
        "barangay official", "local official", "national official",
        
        # Prohibited Acts
        "conflict of interest", "personal interest", "private interest",
        "financial interest", "business interest", "incompatible interest",
        "gift", "receiving gift", "accepting gift", "soliciting gift",
        "donation", "favor", "gratuity", "benefit", "entertainment",
        
        # Violations
        "ethics violation", "ethical violation", "code violation",
        "conduct violation", "breach of ethics", "ethical breach",
        "unethical conduct", "unethical behavior", "improper conduct",
        "misconduct", "misbehavior", "impropriety",
        
        # Disclosure Requirements
        "SALN", "Statement of Assets, Liabilities and Net Worth",
        "asset disclosure", "wealth disclosure", "financial disclosure",
        "business interest disclosure", "relationship disclosure",
        
        # Prohibited Relationships
        "nepotism", "favoritism", "patronage", "preferential treatment",
        "special treatment", "biased treatment", "unfair advantage",
        
        # Standards
        "norms", "standards of conduct", "ethical norms", "moral standards",
        "professional standards", "conduct standards", "behavioral standards",
        
        # Duties & Obligations
        "duty", "obligation", "responsibility", "commitment",
        "oath of office", "official oath", "sworn duty",
        "fiduciary duty", "public duty", "official responsibility",
        
        # Accountability Mechanisms
        "ombudsman", "ethics committee", "accountability office",
        "investigation", "inquiry", "fact-finding", "hearing",
        
        # Penalties & Sanctions
        "administrative case", "administrative charge", "disciplinary action",
        "penalty", "sanction", "suspension", "dismissal", "termination",
        "fine", "forfeiture", "disqualification",
        
        # Legal Terms
        "ethics complaint", "ethics case", "conduct complaint", "misconduct case",
        "violation of code", "breach of conduct", "ethics charge"
    ],
    
    "3815": [
        # Core Revised Penal Code Terms
        "revised penal code", "RPC", "penal code", "criminal law",
        "Philippine criminal law", "criminal code",
        
        # Crimes & Offenses
        "crime", "felony", "offense", "criminal offense", "criminal act",
        "misdemeanor", "violation", "wrongdoing", "illegal act", "unlawful act",
        
        # Criminal Liability
        "criminal liability", "liability", "responsibility", "culpability",
        "guilt", "criminal responsibility", "legal responsibility",
        "accountable", "answerable", "liable",
        
        # Intent & Circumstances
        "intent", "criminal intent", "malicious intent", "deliberate",
        "premeditated", "willful", "intentional", "negligence", "recklessness",
        "aggravating circumstance", "mitigating circumstance", "justifying circumstance",
        
        # Penalties & Punishment
        "penalty", "punishment", "sanction", "sentence", "sentencing",
        "imprisonment", "jail", "prison", "detention", "incarceration",
        "fine", "monetary penalty", "pecuniary penalty",
        "death penalty", "reclusion perpetua", "reclusion temporal",
        "prision mayor", "prision correccional", "arresto mayor", "arresto menor",
        
        # Types of Crimes
        "murder", "homicide", "parricide", "infanticide", "physical injuries",
        "theft", "robbery", "qualified theft", "estafa", "fraud",
        "falsification", "forgery", "perjury", "libel", "slander",
        "arson", "kidnapping", "illegal detention", "coercion", "threats",
        "trespass", "malicious mischief", "grave threats", "light threats",
        
        # Criminal Process
        "arrest", "apprehension", "detention", "custody", "imprisonment",
        "arraignment", "trial", "prosecution", "conviction", "acquittal",
        "guilty", "not guilty", "verdict", "judgment", "sentence",
        
        # Parties to Crime
        "principal", "accomplice", "accessory", "co-conspirator", "conspirator",
        "offender", "perpetrator", "accused", "defendant", "suspect",
        "victim", "injured party", "complainant",
        
        # Stages of Crime
        "attempted", "frustrated", "consummated", "conspiracy", "proposal",
        
        # Legal Terms
        "criminal case", "criminal complaint", "criminal charge", "indictment",
        "information", "criminal prosecution", "criminal action",
        "penal code violation", "RPC violation", "criminal offense case"
    ],
    
    "8972": [
        # Core Solo Parent Terms
        "solo parent", "solo parents", "solo parent law", "solo parent act",
        "solo parent welfare", "solo parent benefits", "solo parent rights",
        
        # Single Parent Terms
        "single parent", "single mother", "single father", "single mom", "single dad",
        "lone parent", "unmarried parent", "unwed parent",
        
        # Circumstances
        "separated", "legally separated", "divorced", "widowed", "widow", "widower",
        "abandoned", "abandoned parent", "deserted", "deserted parent",
        "unmarried", "never married", "unwed mother", "unwed father",
        "partner death", "spouse death", "death of spouse", "death of partner",
        
        # Care Responsibilities
        "sole custody", "single custody", "exclusive parental authority",
        "sole parental responsibility", "primary caregiver", "custodial parent",
        "raising child alone", "caring for child alone", "single-handedly raising",
        
        # Benefits & Support
        "parental leave", "solo parent leave", "parental benefit", "leave benefit",
        "flexible work schedule", "flexible working hours", "work arrangement",
        "educational assistance", "scholarship", "educational discount",
        "housing assistance", "housing benefit", "housing priority",
        
        # Financial Support
        "benefits", "assistance", "financial assistance", "financial support",
        "government assistance", "government benefit", "subsidy",
        "child support", "parental support", "financial aid",
        "livelihood assistance", "employment assistance",
        
        # Social Services
        "social welfare", "social services", "DSWD", "Department of Social Welfare",
        "counseling", "psychological support", "family services",
        "day care", "child care", "child care assistance",
        
        # Identification & Documentation
        "solo parent ID", "solo parent identification card", "solo parent certificate",
        "solo parent certification", "barangay certification", "DSWD certification",
        
        # Legal Rights
        "rights", "entitlement", "privilege", "protection", "legal protection",
        "work protection", "employment protection", "discrimination protection",
        
        # Work-Related
        "parental duty", "parental obligation", "work-life balance",
        "employment discrimination", "workplace discrimination",
        
        # Legal Terms
        "solo parent complaint", "solo parent case", "solo parent violation",
        "benefit denial", "discrimination case", "rights violation"
    ],
    
    "9700": [
        # Core Agrarian Reform Terms
        "agrarian reform", "agrarian reform law", "land reform", "land reform law",
        "CARP", "CARPER", "Comprehensive Agrarian Reform Program",
        "agrarian justice", "social justice", "land justice",
        
        # Land Terms
        "agricultural land", "farm land", "farmland", "arable land",
        "landholding", "land ownership", "land title", "land distribution",
        "land transfer", "land redistribution", "land allocation",
        "estate", "hacienda", "plantation",
        
        # Parties Involved
        "farmer", "farmers", "peasant", "tiller", "cultivator",
        "agricultural worker", "farm worker", "tenant", "tenant farmer",
        "landowner", "landlord", "landholding owner", "estate owner",
        "agrarian reform beneficiary", "ARB", "farmer-beneficiary",
        
        # Tenancy & Arrangements
        "tenancy", "leasehold", "share tenancy", "share cropping",
        "agricultural leasehold", "tenant relationship", "landlord-tenant",
        "tenancy agreement", "leasehold contract", "tenurial arrangement",
        
        # DAR Terms
        "DAR", "Department of Agrarian Reform", "agrarian reform office",
        "DARAB", "DAR Adjudication Board", "agrarian court",
        "land bank", "Land Bank of the Philippines", "LBP",
        
        # Land Acquisition
        "land acquisition", "acquisition", "compulsory acquisition",
        "voluntary offer to sell", "VOS", "voluntary land transfer", "VLT",
        "notice of coverage", "claim folder", "land valuation",
        "just compensation", "payment", "land payment",
        
        # Emancipation & Titles
        "emancipation patent", "EP", "Certificate of Land Ownership Award", "CLOA",
        "land title", "land certificate", "ownership document",
        "land registration", "title transfer", "land award",
        
        # Violations & Issues
        "land grabbing", "land dispute", "agrarian dispute", "land conflict",
        "illegal conversion", "land use conversion", "unauthorized conversion",
        "eviction", "illegal eviction", "forced eviction", "ejectment",
        "land harassment", "farmer harassment", "intimidation",
        
        # Rights & Support
        "farmer rights", "tenurial security", "security of tenure",
        "agrarian rights", "land rights", "cultivation rights",
        "support services", "agricultural support", "farming assistance",
        "credit", "loan", "financing", "subsidy",
        
        # Legal Terms
        "agrarian case", "agrarian complaint", "land reform case",
        "agrarian dispute case", "DARAB case", "agrarian violation",
        "land dispute case", "ejection case", "dispossession"
    ],
    
    "10591": [
        # Core Firearms Terms
        "firearms", "firearm", "gun", "guns", "weapon", "deadly weapon",
        "firearms law", "firearms act", "gun law", "gun control law",
        
        # Types of Firearms
        "handgun", "pistol", "revolver", "shotgun", "rifle",
        "automatic weapon", "semi-automatic", "assault rifle",
        "high-powered firearm", "long firearm", "short firearm",
        
        # Ammunition
        "ammunition", "ammo", "bullets", "cartridge", "rounds",
        "live ammunition", "blank ammunition", "explosive",
        
        # Licensing & Registration
        "license to own", "LTO", "firearm license", "gun license",
        "permit to carry", "PTC", "carry permit", "gun permit",
        "license renewal", "license application", "permit application",
        "gun registration", "firearm registration", "registration certificate",
        
        # Illegal Possession
        "illegal possession", "unlawful possession", "unauthorized possession",
        "illegal gun", "illegal firearm", "unlicensed firearm", "unregistered firearm",
        "loose firearm", "unlicensed gun", "hot gun",
        "possession without license", "carrying without permit",
        
        # Violations
        "gun ban", "gun ban period", "election gun ban", "ban violation",
        "carrying during ban", "firearm violation", "gun violation",
        "illegal carry", "illegal transport", "unauthorized carry",
        
        # Gun-Related Crimes
        "gun crime", "firearm offense", "armed", "armed person",
        "brandishing", "display of firearm", "threatening with gun",
        "illegal discharge", "firing gun", "gunfire", "shooting",
        "stray bullet", "indiscriminate firing", "celebratory firing",
        
        # Regulation & Control
        "firearm regulation", "gun control", "gun regulation",
        "firearms control", "weapon control", "arms control",
        "PNP", "Philippine National Police", "Firearms and Explosives Office",
        "FEO", "gun registry", "firearms database",
        
        # Safety & Storage
        "gun safety", "firearm safety", "safe storage", "gun locker",
        "trigger lock", "safety mechanism", "safe handling",
        
        # Transfer & Sale
        "gun sale", "firearm sale", "illegal sale", "gun transfer",
        "firearm transfer", "gun dealer", "licensed dealer",
        "gun shop", "firearms store",
        
        # Legal Terms
        "gun case", "gun complaint", "firearm case", "firearm complaint",
        "illegal possession case", "gun charge", "firearm charge",
        "confiscation", "seizure", "surrender"
    ],
    
    "6969": [
        # Core Toxic Substances Terms
        "toxic substances", "toxic substances law", "toxic substances act",
        "hazardous waste", "hazardous material", "hazmat",
        "toxic waste", "dangerous substances", "harmful substances",
        
        # Nuclear & Radioactive
        "nuclear waste", "radioactive waste", "radioactive material",
        "radiation", "radioactive contamination", "nuclear contamination",
        "nuclear material", "radioactive substance",
        
        # Chemical Safety
        "chemical safety", "chemical hazard", "chemical risk",
        "toxic chemicals", "hazardous chemicals", "dangerous chemicals",
        "industrial chemicals", "commercial chemicals",
        "chemical substance", "chemical compound", "chemical agent",
        
        # Types of Hazardous Materials
        "corrosive", "flammable", "explosive", "oxidizing", "toxic",
        "carcinogenic", "mutagenic", "teratogenic", "poisonous",
        "irritant", "harmful", "dangerous", "lethal",
        
        # Waste Management
        "waste management", "hazardous waste management", "waste disposal",
        "toxic waste disposal", "chemical disposal", "safe disposal",
        "waste treatment", "chemical treatment", "neutralization",
        "waste storage", "chemical storage", "containment",
        
        # Environmental Protection
        "environmental protection", "environmental safety", "pollution prevention",
        "contamination prevention", "chemical regulation", "substance control",
        
        # Incidents & Accidents
        "chemical spill", "toxic spill", "chemical leak", "toxic leak",
        "chemical release", "accidental release", "chemical accident",
        "hazmat incident", "chemical exposure", "toxic exposure",
        "contamination", "chemical contamination", "toxic contamination",
        "environmental contamination", "soil contamination", "water contamination",
        
        # Handling & Transport
        "chemical handling", "hazmat handling", "safe handling",
        "chemical transport", "hazmat transport", "dangerous goods transport",
        "shipping", "labeling", "packaging", "containment",
        
        # Regulation & Compliance
        "chemical regulation", "substance regulation", "import control",
        "export control", "permit", "clearance", "authorization",
        "registration", "notification", "reporting requirement",
        
        # EMB Terms
        "EMB", "Environmental Management Bureau", "DENR",
        "Department of Environment and Natural Resources",
        
        # Health & Safety
        "occupational safety", "worker safety", "health hazard",
        "safety data sheet", "SDS", "MSDS", "material safety data sheet",
        "protective equipment", "PPE", "personal protective equipment",
        
        # Legal Terms
        "toxic substances violation", "chemical violation", "hazmat violation",
        "illegal disposal", "improper disposal", "unlicensed handling",
        "chemical complaint", "hazmat complaint", "toxic waste case"
    ],
    
    "7581": [
        # Core Price Act Terms
        "price act", "price control", "price control act", "price control law",
        "price regulation", "price ceiling", "price limit", "price freeze",
        
        # Price Manipulation
        "price manipulation", "profiteering", "overpricing", "overprice", "overpriced",
        "price gouging", "excessive pricing", "unreasonable pricing",
        "price fixing", "price collusion", "price cartel",
        "artificial price increase", "unjustified price increase",
        
        # Hoarding
        "hoarding", "hoarded goods", "stockpiling", "withholding supply",
        "artificial scarcity", "supply manipulation", "supply hoarding",
        
        # Commodities
        "basic commodities", "basic necessities", "essential goods",
        "prime commodities", "basic goods", "staple goods",
        "rice", "sugar", "oil", "cooking oil", "salt", "fish", "meat",
        "vegetables", "food items", "medicine", "fuel", "LPG",
        
        # Supply & Distribution
        "supply", "shortage", "supply shortage", "scarcity",
        "distribution", "supply chain", "supply disruption",
        "artificial shortage", "induced shortage",
        
        # Emergency Measures
        "emergency", "state of emergency", "calamity", "disaster",
        "emergency price control", "emergency measures",
        "price stabilization", "price intervention",
        
        # Market Terms
        "market", "marketplace", "retail", "wholesale",
        "suggested retail price", "SRP", "maximum retail price", "MRP",
        "market price", "prevailing price", "fair price",
        
        # Violations
        "price violation", "overpricing violation", "hoarding violation",
        "profiteering violation", "price control violation",
        "selling above ceiling", "selling above SRP",
        "refusing to sell", "refusal to sell", "withholding goods",
        
        # Consumer Protection
        "consumer protection", "consumer rights", "consumer welfare",
        "DTI", "Department of Trade and Industry", "price monitoring",
        "price surveillance", "market monitoring",
        
        # Legal Terms
        "price complaint", "price case", "overpricing complaint",
        "profiteering case", "hoarding case", "price manipulation case",
        "price gouging complaint", "price violation case"
    ],
    
    "9995": [
        # Core Voyeurism Terms
        "voyeurism", "voyeurism law", "voyeurism act",
        "anti-photo voyeurism", "anti-video voyeurism",
        "photo voyeurism", "video voyeurism", "image voyeurism",
        
        # Recording & Capturing
        "recording", "video recording", "photo recording", "image recording",
        "capturing", "filming", "photographing", "taking picture",
        "taking video", "taking photo", "secret recording", "hidden recording",
        "covert recording", "unauthorized recording", "illegal recording",
        
        # Devices & Methods
        "hidden camera", "spy camera", "secret camera", "concealed camera",
        "pinhole camera", "surveillance camera", "recording device",
        "camera phone", "mobile phone camera", "smartphone camera",
        
        # Content Types
        "voyeur video", "voyeur photo", "voyeur image", "voyeur footage",
        "intimate image", "private image", "sexual image", "nude image",
        "compromising photo", "compromising video", "sensitive content",
        
        # Distribution & Sharing
        "distribution", "sharing", "circulation", "dissemination",
        "publication", "posting", "uploading", "sending",
        "selling", "trading", "exchanging", "transmitting",
        "viral", "going viral", "spread", "leaked",
        
        # Leaked Content
        "leaked video", "leaked photo", "leaked image", "leaked recording",
        "leaked content", "leaked material", "exposed photo", "exposed video",
        "revenge porn", "ex-girlfriend video", "ex-boyfriend photo",
        
        # Privacy Violation
        "privacy violation", "invasion of privacy", "breach of privacy",
        "violation of privacy", "privacy breach", "privacy invasion",
        "private moment", "intimate moment", "personal moment",
        
        # Locations
        "bathroom", "restroom", "comfort room", "CR", "toilet",
        "changing room", "fitting room", "locker room", "shower",
        "bedroom", "private room", "hotel room", "motel room",
        
        # Consent
        "without consent", "no consent", "lack of consent",
        "unauthorized", "non-consensual", "against will",
        "secret", "hidden", "covert", "surreptitious",
        
        # Victims
        "victim", "subject", "unsuspecting victim", "unknowing subject",
        "recorded person", "photographed person",
        
        # Online Context
        "online posting", "social media posting", "internet posting",
        "viral video", "viral photo", "online sharing", "cloud storage",
        "file sharing", "group chat", "messaging app",
        
        # Private Acts
        "private act", "intimate act", "sexual act", "personal act",
        "bathing", "changing clothes", "undressing", "dressing",
        
        # Legal Terms
        "voyeurism case", "voyeurism complaint", "voyeurism violation",
        "illegal recording case", "privacy violation case",
        "unauthorized recording complaint", "leaked video case"
    ],
    
    "8049": [
        # Core Anti-Hazing Terms
        "hazing", "anti-hazing", "anti-hazing law", "anti-hazing act",
        "hazing law", "fraternity hazing", "sorority hazing",
        
        # Organizations
        "fraternity", "sorority", "brotherhood", "sisterhood",
        "organization", "student organization", "Greek organization",
        "society", "club", "group", "gang",
        
        # Initiation
        "initiation", "initiation rites", "initiation ritual", "rites",
        "ritual", "ceremony", "pledging", "pledge period",
        "recruitment", "membership initiation", "admission rites",
        
        # Violence & Abuse
        "initiation violence", "physical violence", "violent hazing",
        "initiation abuse", "physical abuse", "physical harm",
        "bodily harm", "paddling", "beating", "whipping", "flogging",
        "punching", "kicking", "hitting", "striking",
        
        # Forms of Hazing
        "psychological hazing", "mental hazing", "emotional abuse",
        "psychological harm", "mental torture", "humiliation",
        "degradation", "embarrassment", "intimidation",
        "forced drinking", "alcohol poisoning", "binge drinking",
        "forced eating", "sleep deprivation", "physical exhaustion",
        
        # Consequences
        "injury", "physical injury", "serious injury", "bodily injury",
        "harm", "hurt", "trauma", "scarring", "disfigurement",
        "death", "hazing death", "fatality", "killing",
        
        # Parties Involved
        "victim", "neophyte", "recruit", "pledge", "initiate",
        "applicant", "prospective member", "candidate",
        "perpetrator", "hazer", "fraternity member", "sorority member",
        "officer", "leader", "organizer", "facilitator",
        
        # Organizational Roles
        "master", "grand master", "president", "vice president",
        "member", "senior member", "alumni", "alumnus", "alumna",
        
        # Consent Issues
        "forced", "coerced", "involuntary", "against will",
        "no consent", "unwilling", "compelled", "pressured",
        
        # Location
        "fraternity house", "frat house", "sorority house",
        "initiation site", "camp", "compound", "venue",
        
        # Legal Terms
        "hazing case", "hazing complaint", "hazing incident",
        "hazing violation", "anti-hazing violation", "hazing death case",
        "hazing injury case", "criminal liability", "organizational liability"
    ],
    
    "11596": [
        # Core Child Marriage Terms
        "child marriage", "anti-child marriage", "anti-child marriage law",
        "child marriage law", "child marriage act", "early marriage",
        "underage marriage", "minor marriage", "marriage of minors",
        
        # Forced Marriage
        "forced marriage", "forced marriage law", "forced marriage act",
        "coerced marriage", "involuntary marriage", "compelled marriage",
        "marriage against will", "unwilling marriage",
        
        # Arranged Marriage
        "arranged marriage", "arranged marriage law", "arranged marriage act",
        "family arrangement", "parental arrangement", "traditional arrangement",
        
        # Age & Consent
        "below 18", "under 18", "underage", "minor", "child",
        "below legal age", "age of consent", "marriageable age",
        "legal age for marriage", "minimum age", "age requirement",
        "immature", "not of age", "juvenile",
        
        # Marriage Terms
        "marriage", "wedding", "matrimony", "union", "betrothal",
        "married", "wed", "wedded", "spouse", "husband", "wife",
        "marriage ceremony", "marriage rites", "wedding ceremony",
        
        # Consent Issues
        "lack of consent", "no consent", "without consent",
        "inability to consent", "coercion", "pressure", "forcing",
        "forced into marriage", "pressured into marriage",
        
        # Parental Involvement
        "parental consent", "parental authority", "parental decision",
        "family pressure", "family tradition", "family custom",
        "parents forcing", "parents arranging", "guardian consent",
        
        # Child Protection
        "child protection", "child welfare", "child rights", "children's rights",
        "best interest of child", "protection of minors", "minor protection",
        
        # Exploitation
        "child exploitation", "exploitation of child", "abuse of child",
        "child abuse", "taking advantage", "manipulation",
        
        # Cultural Context
        "cultural practice", "traditional practice", "customary practice",
        "tradition", "custom", "cultural marriage", "tribal marriage",
        
        # Legal Aspects
        "marriage license", "marriage certificate", "marriage registration",
        "void marriage", "voidable marriage", "invalid marriage",
        "annulment", "nullity", "declaration of nullity",
        
        # Violations
        "facilitating", "arranging", "solemnizing", "officiating",
        "conducting marriage", "performing marriage", "enabling marriage",
        "allowing marriage", "permitting marriage", "consenting to marriage",
        
        # Legal Terms
        "child marriage case", "child marriage complaint", "child marriage violation",
        "forced marriage case", "forced marriage complaint", "arranged marriage case",
        "underage marriage case", "illegal marriage", "unlawful marriage"
    ],
    
    "386": [
        # Core Civil Code Terms
        "civil code", "civil code of the philippines", "civil code law",
        "civil law", "private law", "civil legislation",
        
        # Property & Ownership
        "property", "real property", "personal property", "immovable property",
        "movable property", "estate", "asset", "possession",
        "ownership", "owner", "proprietor", "title", "land title",
        "property rights", "ownership rights", "right to property",
        "acquisition", "alienation", "transfer", "conveyance",
        "deed", "deed of sale", "property deed", "title transfer",
        
        # Succession & Inheritance
        "succession", "inheritance", "heir", "heiress", "beneficiary",
        "estate settlement", "estate distribution", "hereditary succession",
        "will", "testament", "last will", "last will and testament",
        "testator", "testatrix", "intestate", "testate",
        "probate", "estate proceedings", "settlement of estate",
        "legitime", "compulsory heir", "legal heir", "forced heir",
        
        # Obligations & Contracts
        "obligation", "duty", "debt", "liability", "responsibility",
        "debtor", "creditor", "obligor", "obligee",
        "contract", "agreement", "covenant", "pact", "deal",
        "contractual obligation", "breach of contract", "contract violation",
        "performance", "non-performance", "fulfillment", "compliance",
        "default", "breach", "violation of agreement",
        
        # Family Law
        "family", "family code", "family law", "family relations",
        "marriage", "matrimony", "husband", "wife", "spouse",
        "marital", "conjugal", "conjugal property", "conjugal partnership",
        "separation of property", "absolute community", "property regime",
        
        # Marriage Issues
        "annulment", "declaration of nullity", "legal separation",
        "void marriage", "voidable marriage", "marriage dissolution",
        "grounds for annulment", "psychological incapacity",
        
        # Parental Authority
        "parental authority", "parental responsibility", "custody",
        "child custody", "sole custody", "joint custody",
        "support", "child support", "spousal support", "financial support",
        "visitation rights", "parental rights", "guardianship",
        
        # Adoption & Guardianship
        "adoption", "adopted child", "adoptee", "adopter", "adoptive parent",
        "legal adoption", "adoption decree", "adoption proceedings",
        "guardianship", "guardian", "ward", "legal guardian",
        "guardian ad litem", "court-appointed guardian",
        
        # Torts & Damages
        "tort", "quasi-delict", "civil wrong", "injury", "harm",
        "negligence", "fault", "culpa", "culpable act",
        "damages", "actual damages", "moral damages", "exemplary damages",
        "nominal damages", "temperate damages", "compensation",
        "indemnity", "restitution", "reparation",
        
        # Civil Liability
        "civil liability", "civil obligation", "civil responsibility",
        "liable", "answerable", "accountable", "legally responsible",
        "joint and several liability", "solidary liability",
        
        # Legal Actions
        "civil action", "civil suit", "lawsuit", "litigation",
        "complaint", "petition", "pleading", "legal claim",
        "plaintiff", "defendant", "party", "litigant",
        
        # Contracts Types
        "sale", "lease", "loan", "donation", "partnership",
        "agency", "trust", "mortgage", "pledge", "guaranty",
        "contract of sale", "lease agreement", "loan agreement",
        
        # Property Relations
        "co-ownership", "usufruct", "easement", "servitude",
        "right of way", "encumbrance", "lien", "mortgage",
        "real estate mortgage", "chattel mortgage",
        
        # Civil Rights
        "civil rights", "personal rights", "property rights",
        "right to privacy", "right to honor", "right to reputation",
        "right to name", "right to image",
        
        # Legal Terms
        "civil case", "civil complaint", "civil action", "civil suit",
        "civil liability case", "breach of contract case",
        "property dispute", "inheritance dispute", "family dispute",
        "obligation case", "damages case", "tort case"
    ]
}