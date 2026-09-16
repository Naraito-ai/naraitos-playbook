const PRELOADED_LEADS = [
  {
    "id": "cdn-1",
    "name": "Rocket Doctor AI",
    "website": "https://www.rocketdoctor.ai",
    "linkedin": "https://www.linkedin.com/company/rocketdoctorai",
    "email": "marketing@rocketdoctor.ai",
    "founders": "",
    "description": "Rocket Doctor AI offers AI-powered healthcare software and services that support virtual patient care across the full clinical journey.",
    "location": "Vancouver",
    "categories": [
      "Artificial Intelligence (AI)",
      "Health Care",
      "Machine Learning"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-2",
    "name": "MDA Space",
    "website": "https://www.mda-b944.com",
    "linkedin": "https://www.linkedin.com/company/mdaspace/",
    "email": "",
    "founders": "",
    "description": "MDA Space is a space technology company that develops geointelligence, space operations, and satellite systems.",
    "location": "Brampton",
    "categories": [
      "Aerospace",
      "Satellite Communication",
      "Space Travel"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-3",
    "name": "Quantum Secure Encryption Corp.",
    "website": "https://www.scope-carbon-corp.com",
    "linkedin": "https://www.linkedin.com/company/scope-technologies-corp/",
    "email": "info@qse.group",
    "founders": "",
    "description": "Quantum Secure Encryption Corp. is a cutting-edge technological company that specializes in quantum security.",
    "location": "Vancouver",
    "categories": [
      "Artificial Intelligence (AI)",
      "Software",
      "Web Development"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-4",
    "name": "Universal Digital",
    "website": "https://www.universaldigital.io/",
    "linkedin": "https://www.linkedin.com/company/universaldigital/",
    "email": "contact@universaldigital.io",
    "founders": "",
    "description": "Universal Digital is a digital platform focused on blockchain infrastructure and digital assets.",
    "location": "Vancouver",
    "categories": [
      "Asset Management",
      "Blockchain",
      "Digital Signage"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-5",
    "name": "Workleap",
    "website": "https://workleap.com",
    "linkedin": "https://www.linkedin.com/company/workleaphq",
    "email": "questions@workleap.com",
    "founders": "",
    "description": "Workleap is the people management platform built for growing SMBs.",
    "location": "Montr\u00e9al",
    "categories": [
      "Collaboration",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-6",
    "name": "Stardust Solar Energy",
    "website": "http://www.stardustsolar.com",
    "linkedin": "https://www.linkedin.com/company/stardustsolar/",
    "email": "",
    "founders": "",
    "description": "Stardust Solar Energy is a solar energy franchisor that offers NABCEP/CSA certified training.",
    "location": "Burnaby",
    "categories": [
      "Renewable Energy",
      "Semiconductor",
      "Solar"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-7",
    "name": "Intrepid",
    "website": "https://www.intrepidmetals.com",
    "linkedin": "https://www.linkedin.com/company/intrepidmetals",
    "email": "info@intrepidmetals.com",
    "founders": "",
    "description": "Intrepid is developing potential high grade silver/lead/zinc projects in close proximity to producing mines and world class deposits.",
    "location": "Vancouver",
    "categories": [
      "Mining",
      "Mining Technology",
      "Precious Metals"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-8",
    "name": "Yolando",
    "website": "https://yolando.com/",
    "linkedin": "https://www.linkedin.com/company/yolando",
    "email": "support@yolando.com",
    "founders": "",
    "description": "Yolando provides AI visibility management, brand knowledge modeling, and go to market execution to align how AI and buyers understand brands",
    "location": "Toronto",
    "categories": [
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-9",
    "name": "Medicus Pharma",
    "website": "https://medicuspharma.com/",
    "linkedin": "https://www.linkedin.com/company/medicus-pharma-ltd/",
    "email": "ir@medicuspharma.com",
    "founders": "",
    "description": "Medicus Pharma is an biotechnology research firm that accelerates life sciences and bio-technology companies through FDA clinical trials.",
    "location": "Toronto",
    "categories": [
      "Biopharma",
      "Biotechnology",
      "Pharmaceutical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-10",
    "name": "SuperBuzz",
    "website": "https://www.superbuzz.io/",
    "linkedin": "https://www.linkedin.com/company/superbuzz-io",
    "email": "liran@superbuzz.io",
    "founders": "",
    "description": "SuperBuzz is an artificial intelligence company that offers machine learning technology to improve online marketing.",
    "location": "Toronto",
    "categories": [
      "Artificial Intelligence (AI)",
      "Marketing Automation",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-11",
    "name": "Corus Orthodontists",
    "website": "https://www.corusortho.com",
    "linkedin": "https://www.linkedin.com/company/corus-orthodontists",
    "email": "",
    "founders": "",
    "description": "Corus Orthodontists is an orthodontic partnership network that provides exceptional patient care and preserves patient-doctor relationships.",
    "location": "Calgary",
    "categories": [
      "Health Care",
      "Health Diagnostics",
      "Medical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-12",
    "name": "ZofiQ",
    "website": "https://zofiq.ai/",
    "linkedin": "https://www.linkedin.com/company/zofiq/",
    "email": "",
    "founders": "[object Object]",
    "description": "ZofiQ offers AI agents that automate MSP workflows, ticket triage, NOC monitoring, and data analysis.",
    "location": "Toronto",
    "categories": [
      "Artificial Intelligence (AI)",
      "Developer Tools",
      "Information Technology"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-13",
    "name": "Hillcrest Energy Technologies",
    "website": "https://hillcrestenergy.tech/",
    "linkedin": "https://www.linkedin.com/company/hillcrest-energy-technologies/",
    "email": "",
    "founders": "",
    "description": "Hillcrest Energy Technologies specializes in developing energy solutions intended to power a more sustainable and electrified future.",
    "location": "Vancouver",
    "categories": [
      "Clean Energy",
      "CleanTech",
      "Energy Efficiency"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-14",
    "name": "Metavista3D",
    "website": "https://metavista3d.com/",
    "linkedin": "https://www.linkedin.com/company/metavista3d/",
    "email": "info@metavista3d.com",
    "founders": "",
    "description": "Metavista3D A New Generation of Glasses Free 3D Displays.",
    "location": "Toronto",
    "categories": [
      "Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-15",
    "name": "Navacord",
    "website": "https://navacord.com",
    "linkedin": "https://in.linkedin.com/company/navacordinc",
    "email": "",
    "founders": "[object Object]",
    "description": "Navacord is an insurance brokerage firm that offers risk management and consulting solutions.",
    "location": "Toronto",
    "categories": [
      "Consulting",
      "Insurance",
      "InsurTech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-16",
    "name": "MineHub Technologies",
    "website": "https://minehub.com",
    "linkedin": "https://www.linkedin.com/company/minehubtech",
    "email": "",
    "founders": "",
    "description": "MineHub Technologies develops cost-saving applications for the mining and metals industry leveraging blockchain technologies.",
    "location": "Vancouver",
    "categories": [
      "Blockchain",
      "Information Technology",
      "Mining Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-17",
    "name": "Lodestar Metals",
    "website": "https://lodestarmetals.ca",
    "linkedin": "https://www.linkedin.com/company/lodestar-metals-corp",
    "email": "investors@lodestarbatterymetals.ca",
    "founders": "",
    "description": "Lodestar Battery Metals Corp. explores and develops clean energy metals for sustainable energy solutions.",
    "location": "Vancouver",
    "categories": [
      "Battery",
      "Energy",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-18",
    "name": "Psyence Biomedical",
    "website": "https://psyencebiomed.com",
    "linkedin": "https://www.linkedin.com/company/psyence-biomed-ltd",
    "email": "info@psyencebiomed.com",
    "founders": "",
    "description": "Psyence Biomedical is a life science biotechnology company that focuses on advancement of psychedelic medicines.",
    "location": "Toronto",
    "categories": [
      "Life Science",
      "Medical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-19",
    "name": "Power Dime",
    "website": "https://powerdime.io",
    "linkedin": "https://www.linkedin.com/company/power-dime/",
    "email": "info@powerdime.io",
    "founders": "",
    "description": "A SaaS platform that helps data centers buy resilient, reliable and sustainable power",
    "location": "Toronto",
    "categories": [
      "Artificial Intelligence (AI)",
      "Blockchain",
      "Clean Energy"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-20",
    "name": "TenX",
    "website": "https://www.tenx.inc",
    "linkedin": "https://www.linkedin.com/company/layerxinc",
    "email": "info@TenX.inc",
    "founders": "",
    "description": "TenX is a technological startup dedicated to enabling next-generation, high-throughput blockchain technologies.",
    "location": "Toronto",
    "categories": [
      "Blockchain",
      "Cryptocurrency",
      "FinTech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-21",
    "name": "Arctic Gateway Group",
    "website": "https://www.arcticgateway.com",
    "linkedin": "https://www.linkedin.com/company/arctic-gateway-group",
    "email": "info@arcticgateway.com",
    "founders": "",
    "description": "Arctic Gateway Group is an Indigenous- and community-owned infrastructure company that operates critical transport assets.",
    "location": "The Pas",
    "categories": [
      "Logistics",
      "Railroad",
      "Transportation"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-22",
    "name": "Lake",
    "website": "https://www.lake.com",
    "linkedin": "https://www.linkedin.com/company/lakedotcom",
    "email": "help@lake.com",
    "founders": "",
    "description": "Lake is an online vacation rental platform for properties near the water.",
    "location": "Toronto",
    "categories": [
      "Marketplace",
      "Rental",
      "Rental Property"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-23",
    "name": "Pet Valu",
    "website": "http://petvalu.com/",
    "linkedin": "https://www.linkedin.com/company/pet-valu",
    "email": "",
    "founders": "[object Object]",
    "description": "Pet Valu is specialty retailer of pet food.",
    "location": "Markham",
    "categories": [
      "Food Processing",
      "Pet"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-24",
    "name": "Juno Industries",
    "website": "https://www.junoindustries.ca/",
    "linkedin": "https://www.linkedin.com/company/juno-industries-inc/",
    "email": "info@junoindustries.ca.",
    "founders": "",
    "description": "Juno Industries Build advanced defence technology to protect.",
    "location": "Vancouver",
    "categories": [
      "Information Technology",
      "News",
      "Social Media"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-25",
    "name": "Innovation Mining",
    "website": "https://www.rzolv.com",
    "linkedin": "https://www.linkedin.com/company/innovation-mining-inc",
    "email": "ir@rzolv.com",
    "founders": "",
    "description": "RZOLV Technologies focused on developing advanced, technology-driven solutions to improve mining operations.",
    "location": "Vancouver",
    "categories": [
      "Mining",
      "Natural Resources",
      "Precious Metals"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-26",
    "name": "NetraMark",
    "website": "https://netramark.com",
    "linkedin": "https://www.linkedin.com/company/netramark",
    "email": "",
    "founders": "[object Object]",
    "description": "NetraMark is an AI and pharma-tech company, has developed proprietary solutions for pharmaceutical and biotechnology companies.",
    "location": "Toronto",
    "categories": [
      "Artificial Intelligence (AI)",
      "Pharmaceutical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-27",
    "name": "Hertz Energy",
    "website": "https://hertz-energy.com",
    "linkedin": "https://www.linkedin.com/company/hertz-lithium/",
    "email": "",
    "founders": "",
    "description": "Hertz Energy provides sustainable long-term lithium resource investment and extraction.",
    "location": "Vancouver",
    "categories": [
      "Mineral",
      "Mining",
      "Renewable Energy"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-28",
    "name": "Taurus",
    "website": "https://taurusrng.com",
    "linkedin": "https://www.linkedin.com/company/taurus-rng",
    "email": "info@taurusrng.com",
    "founders": "",
    "description": "Taurus is a renewable energy platform that develops and operates renewable natural gas projects and facilities.",
    "location": "Vancouver",
    "categories": [
      "Clean Energy",
      "Project Management",
      "Renewable Energy"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-29",
    "name": "Akanda",
    "website": "https://akandacorp.com",
    "linkedin": "https://www.linkedin.com/company/akandacorp",
    "email": "",
    "founders": "",
    "description": "Akanda is a medical company that produces medical cannabis for patients.",
    "location": "Toronto",
    "categories": [
      "Health Care",
      "Medical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-30",
    "name": "Universal Proptech",
    "website": "https://www.brandpilot.ai",
    "linkedin": "https://www.linkedin.com/company/brandpilot-ai/?originalSubdomain=ca",
    "email": "info@universalproptech.com",
    "founders": "",
    "description": "BrandPilot AI helps you eliminate wasted spend, maximize ROI with AI-driven solutions tailored for enterprise and B2B brands.",
    "location": "Vaughan",
    "categories": [
      "CleanTech",
      "Energy Management",
      "PropTech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-31",
    "name": "Multapplied Networks",
    "website": "http://www.turnium.com",
    "linkedin": "https://www.linkedin.com/company/turnium",
    "email": "sales@ttgi.io",
    "founders": "",
    "description": "Turnium enables Service Providers to rapidly launch white-label SD-WAN solutions for their customers, using any available connectivity.",
    "location": "Vancouver",
    "categories": [
      "Cloud Infrastructure",
      "Internet",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-32",
    "name": "TELUS Health",
    "website": "https://www.telushealth.com",
    "linkedin": "https://www.linkedin.com/company/telus-health/",
    "email": "info@telushealth.com",
    "founders": "",
    "description": "TELUS Health specializes in telehomecare, electronic medical records, consumer health, benefits, and pharmacy management.",
    "location": "Montr\u00e9al",
    "categories": [
      "Health Care",
      "Medical",
      "Telecommunications"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-33",
    "name": "Boba Mint",
    "website": "https://www.bobamint.com",
    "linkedin": "https://www.linkedin.com/company/boba-mint-holdings-ltd/",
    "email": "",
    "founders": "",
    "description": "Boba Mint is a Mobile Gaming App.",
    "location": "Toronto",
    "categories": [
      "Apps",
      "Gaming"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-34",
    "name": "Helium Evolution",
    "website": "https://www.heliumevolution.ca/",
    "linkedin": "https://www.linkedin.com/company/helium-evolution/",
    "email": "info@heliumevolution.ca",
    "founders": "",
    "description": "Helium Evolution is a Canadian helium exploration company that boasts the largest helium land rights position in North America.",
    "location": "Calgary",
    "categories": [
      "Mining",
      "Mining Technology",
      "Sustainability"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-35",
    "name": "Polyalgorithm Machine Learning",
    "website": "https://polyml.com",
    "linkedin": "https://www.linkedin.com/company/polyalgorithm-machine-learning",
    "email": "info@polyml.com",
    "founders": "",
    "description": "Polyalgorithm Machine Learning is a tech company that offers AI and machine learning solutions for various industries.",
    "location": "Waterloo",
    "categories": [
      "Artificial Intelligence (AI)",
      "Automotive",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-36",
    "name": "Birdseye 5349",
    "website": "http://www.birdseyepost.com",
    "linkedin": "https://ca.linkedin.com/company/birdseye-global",
    "email": "support@birdseyepost.com",
    "founders": "",
    "description": "Birdseye helps you discover and engage high-value prospects offline, at home, with data-driven mailing strategies built around your goals.",
    "location": "Toronto",
    "categories": [
      "Artificial Intelligence (AI)",
      "Data Integration",
      "Direct Marketing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-37",
    "name": "Cpkc",
    "website": "https://www.cpkcr.com/en",
    "linkedin": "https://www.linkedin.com/company/cpkcrail",
    "email": "communityconnect@cpkcr.com",
    "founders": "",
    "description": "CPKC operates a single-line rail network connecting Canada, the U.S., and Mexico, providing logistics solutions.",
    "location": "Calgary",
    "categories": [
      "Logistics",
      "Railroad",
      "Shipping"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-38",
    "name": "European Energy Metals",
    "website": "https://www.grit-metals.com/",
    "linkedin": "https://www.linkedin.com/company/european-energy-metals",
    "email": "info@europeanenergymetals.com",
    "founders": "",
    "description": "European Energy Metals is focusing on lithium and rare-earth element projects to aid in global decarbonization and electrification efforts.",
    "location": "Vancouver",
    "categories": [
      "Mineral",
      "Mining",
      "Precious Metals"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-39",
    "name": "EarthDaily Analytics",
    "website": "http://www.earthdaily.com",
    "linkedin": "https://www.linkedin.com/company/earthdailyanalytics",
    "email": "cx@urthecast.com",
    "founders": "[object Object]",
    "description": "EarthDaily Analytics is an integrated data processing and analytics company that provides end-to-end Earth observation solutions.",
    "location": "Vancouver",
    "categories": [
      "Analytics",
      "Artificial Intelligence (AI)",
      "Geospatial"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-40",
    "name": "CoTec",
    "website": "https://www.cotec.ca",
    "linkedin": "",
    "email": "info@cotec.ca",
    "founders": "",
    "description": "CoTec is an ESG-focused business willing to invest in cutting-edge technology.",
    "location": "Vancouver",
    "categories": [
      "Asset Management",
      "Finance",
      "Financial Services"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-41",
    "name": "Cima 0B2E",
    "website": "https://www.cima.ca",
    "linkedin": "https://www.linkedin.com/company/cima-/life/",
    "email": "Paulgregory0000@gmail.com",
    "founders": "",
    "description": "CIMA+ is a multidisciplinary firm specializing in engineering, project management, urban planning, new technologies, and the environment.",
    "location": "Calgary",
    "categories": [
      "Automotive",
      "Consulting",
      "Energy"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-42",
    "name": "Polargrid",
    "website": "https://www.polargrid.ai/",
    "linkedin": "https://www.linkedin.com/company/polargrid",
    "email": "hello@polargrid.ai",
    "founders": "",
    "description": "Low-latency AI Inference for Real-Time Use Cases",
    "location": "Ottawa",
    "categories": [
      "Artificial Intelligence (AI)"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-43",
    "name": "Ondine Biomedical",
    "website": "http://ondinebio.com",
    "linkedin": "http://www.linkedin.com/company/130723",
    "email": "support@ondinebio.com",
    "founders": "",
    "description": "Ondine Biomedical develops non-antibiotic, anti-infective therapies for a broad spectrum of bacterial, viral, and fungal infections.",
    "location": "Vancouver",
    "categories": [
      "Biotechnology",
      "Health Care",
      "Pharmaceutical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-44",
    "name": "VentriPoint",
    "website": "http://www.ventripoint.com",
    "linkedin": "https://www.linkedin.com/company/ventripoint-diagnostics-ltd/?originalSubdomain=ca",
    "email": "info@ventripoint.com",
    "founders": "",
    "description": "VentriPoint is a public company dedicated to making heart analysis more convenient and less expensive using knowledge-based techniques.",
    "location": "Toronto",
    "categories": [
      "Analytics",
      "Biotechnology",
      "Health Care"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-45",
    "name": "Spark Energy Minerals",
    "website": "https://www.sparkenergyminerals.com",
    "linkedin": "https://www.linkedin.com/company/sparkenergymin",
    "email": "",
    "founders": "",
    "description": "Spark Energy Minerals is a Canadian company focused on the acquisition, exploration, and development of battery metals and mineral assets.",
    "location": "Vancouver",
    "categories": [
      "Tech"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-46",
    "name": "ToysRUs",
    "website": "https://www.toysrus.ca/en/home",
    "linkedin": "",
    "email": "customerservice@toysrus.ca",
    "founders": "",
    "description": "ToysRUs is a retail firm that supplies toys and baby products of national brands, and innovative loyalty programs.",
    "location": "Concord",
    "categories": [
      "Baby",
      "Retail",
      "Toys"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-47",
    "name": "Sage Potash",
    "website": "https://sagepotash.com/",
    "linkedin": "https://www.linkedin.com/company/sage-potash-corp/about/",
    "email": "info@sagepotash.com",
    "founders": "",
    "description": "Sage Potash exploration company with a large portfolio of mineral rights in the prolific Paradox Basin in Southeastern Utah, USA.",
    "location": "Vancouver",
    "categories": [
      "Mineral",
      "Mining",
      "Mining Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-48",
    "name": "Maple Leaf Sports Entertainment",
    "website": "http://mlse.com",
    "linkedin": "https://www.linkedin.com/company/maple-leaf-sports-&-entertainment",
    "email": "leafstv@mlse.com",
    "founders": "[object Object]",
    "description": "Maple Leaf Sports & Entertainment is a professional sports and commercial real estate company based in Toronto, Ontario, Canada.",
    "location": "Toronto",
    "categories": [
      "Media and Entertainment"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-49",
    "name": "Canadian Electrical Services",
    "website": "https://www.cestransformers.com/",
    "linkedin": "",
    "email": "info@cestransformers.com",
    "founders": "",
    "description": "Canadian Electrical Services manufactures and supplies custom and standard transformers and offers repair and refurbishing services.",
    "location": "Markham",
    "categories": [
      "Electronics",
      "Industrial Manufacturing",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-50",
    "name": "Advanced Gold Exploration",
    "website": "https://advancedgoldexploration.com/",
    "linkedin": "https://www.linkedin.com/company/advancedgoldexploration",
    "email": "",
    "founders": "",
    "description": "Advanced Gold Exploration increases undervalued gold properties value through modern technology.",
    "location": "Toronto",
    "categories": [
      "Mineral",
      "Mining"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-51",
    "name": "Silver Mountain Resources",
    "website": "https://agmr.ca/",
    "linkedin": "https://www.linkedin.com/company/agmr",
    "email": "abazo@agmr.ca",
    "founders": "",
    "description": "Silver Mountain Resources is a mining company that focuses on identifying large mineralized systems and high-grade mineral deposits.",
    "location": "Toronto",
    "categories": [
      "Impact Investing",
      "Industrial",
      "Mining"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-52",
    "name": "T Rize Group",
    "website": "https://www.t-rize.io",
    "linkedin": "https://www.linkedin.com/company/89581850",
    "email": "support@t-rize.io",
    "founders": "",
    "description": "AI powered DLT and Blockchain integration Network and SaaS",
    "location": "Montr\u00e9al",
    "categories": [
      "Artificial Intelligence (AI)",
      "Blockchain",
      "Information Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-53",
    "name": "Electric Mind",
    "website": "https://www.electricmind.com",
    "linkedin": "https://www.linkedin.com/company/electricmind",
    "email": "electricmind2024@gmail.com",
    "founders": "",
    "description": "Electric Mind is a strategy and technology consulting firm that specializes in financial services and digital transformation services.",
    "location": "Toronto",
    "categories": [
      "Artificial Intelligence (AI)",
      "Consulting",
      "Data Management"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-54",
    "name": "Teck",
    "website": "http://www.teck.com/",
    "linkedin": "https://www.linkedin.com/company/teck-resources-limited",
    "email": "TCAIIndChem@teck.com",
    "founders": "[object Object]",
    "description": "Teck is a diversified resource company with business units focused on copper, steelmaking coal, zinc and energy.",
    "location": "Vancouver",
    "categories": [
      "Mineral",
      "Mining",
      "Mining Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-55",
    "name": "Power Sustainable",
    "website": "https://www.powersustainable.com/",
    "linkedin": "https://www.linkedin.com/company/power-sustainable-capital",
    "email": "info@powersustainable.com",
    "founders": "",
    "description": "Power Sustainable is a multi-platform alternative asset manager investing in sustainable strategies.",
    "location": "Montr\u00e9al",
    "categories": [
      "Financial Services"
    ],
    "funding": " - "
  },
  {
    "id": "cdn-56",
    "name": "Brazil Potash",
    "website": "http://www.brazilpotash.com/",
    "linkedin": "https://www.linkedin.com/company/brazil-potash-corp-",
    "email": "info@brazilpotash.com",
    "founders": "",
    "description": "Brazil Potash is a private company with its base of technical operations located in Belo Horizonte Brazil.",
    "location": "Toronto",
    "categories": [
      "Agriculture",
      "Mineral",
      "Mining"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-57",
    "name": "Glow LifeTech",
    "website": "https://www.glowlifetech.com/",
    "linkedin": "https://www.linkedin.com/company/glowlifetech/",
    "email": "info@glowlifetech.com",
    "founders": "",
    "description": "Glow LifeTech is a Canadian-based biotechnology company focused on producing nutraceutical and cannabinoid-based products.",
    "location": "Toronto",
    "categories": [
      "Biotechnology",
      "Cannabis",
      "Life Science"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-58",
    "name": "Streamex",
    "website": "https://www.streamex.com/",
    "linkedin": "https://www.linkedin.com/company/streamex-exchange/",
    "email": "support@streamex.com",
    "founders": "[object Object]",
    "description": "Streamex is a real-world asset (RWA) tokenization company bringing commodity markets on chain.",
    "location": "Vancouver",
    "categories": [
      "Digital Signage",
      "Financial Exchanges",
      "Financial Services"
    ],
    "funding": " - "
  },
  {
    "id": "cdn-59",
    "name": "Bragg Gaming Group",
    "website": "https://bragg.group",
    "linkedin": "https://www.linkedin.com/company/bragg-gaming-group",
    "email": "info@breakingdatacorp.com",
    "founders": "",
    "description": "Bragg Gaming Group is a technology provider of semantic search, machine learning and natural language processing.",
    "location": "Concord",
    "categories": [
      "Apps",
      "Machine Learning",
      "Mobile"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-60",
    "name": "ZYUS",
    "website": "https://www.zyus.com/",
    "linkedin": "https://in.linkedin.com/company/zyuslifesciences",
    "email": "invest@zyus.com",
    "founders": "",
    "description": "ZYUS is a biopharmaceutical company that offers patients cannabinoid and other phyto-therapeutic medical solutions.",
    "location": "Saskatoon",
    "categories": [
      "Biopharma",
      "Biotechnology",
      "Cannabis"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-61",
    "name": "Bucketlist Fe2F",
    "website": "https://bucketlistrewards.com/",
    "linkedin": "https://www.linkedin.com/company/bucketlistcc/",
    "email": "",
    "founders": "",
    "description": "Bucketlist transforms your company culture. With a select staff dedicated to your company\u2019s success",
    "location": "Vancouver",
    "categories": [
      "Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-62",
    "name": "PharmAla Biotech",
    "website": "https://pharmala.ca/",
    "linkedin": "https://www.linkedin.com/company/pharmala-biotech/",
    "email": "outreach@pharmala.ca",
    "founders": "",
    "description": "PharmAla Biotech is a biotechnology company that provides manufacturing and sales of MDMA substances to the clinical research community.",
    "location": "Toronto",
    "categories": [
      "Biotechnology",
      "Health Care",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-63",
    "name": "Z\u016bm Rails",
    "website": "https://zumrails.com",
    "linkedin": "https://www.linkedin.com/company/z%C5%ABm-rails/",
    "email": "marc@zumrails.com",
    "founders": "",
    "description": "Z\u016bm Rails is a gateway that allows business to pick and choose optimal methods to fit your ideal workflow to pull or push funds in Canada",
    "location": "Montr\u00e9al",
    "categories": [
      "FinTech",
      "Payments"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-64",
    "name": "Cynaptec",
    "website": "https://www.cynaptec-pharmaceuticals.com",
    "linkedin": "",
    "email": "",
    "founders": "",
    "description": "Cynaptec is a biopharmaceutical company focused on creating novel treatments for neurological and psychiatric conditions.",
    "location": "Vancouver",
    "categories": [
      "Biopharma",
      "Biotechnology",
      "Life Science"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-65",
    "name": "Avitia",
    "website": "https://www.avitia.bio",
    "linkedin": "https://www.linkedin.com/company/avitia-bio",
    "email": "hello@avitia.bio",
    "founders": "",
    "description": "Avitia\u00a0improves cancer treatment via advanced molecular testing solutions,\u00a0offers testing tools for use onsite, bioinformatics driven by AI.",
    "location": "Montr\u00e9al",
    "categories": [
      "Artificial Intelligence (AI)",
      "Biotechnology",
      "Oncology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-66",
    "name": "Canadian Fiber Optics",
    "website": "https://canadianfiberoptics.ca/",
    "linkedin": "https://www.linkedin.com/company/canadianfibreoptics/",
    "email": "info@canadianfiberoptics.ca",
    "founders": "",
    "description": "Canadian Fiber Optics design and construct fiber optic systems along with providing network maintenance and fiber connectivity solutions.",
    "location": "Calgary",
    "categories": [
      "Construction",
      "Internet",
      "Telecommunications"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-67",
    "name": "DeepIDV",
    "website": "https://www.deepidv.com",
    "linkedin": "",
    "email": "hello@deepidv.com",
    "founders": "",
    "description": "DeepIDV is a full-suite identity verification platform, leveraging the use of AI for risk analysis and near-instant verification.",
    "location": "Toronto",
    "categories": [
      "Information Technology",
      "Software"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-68",
    "name": "Autocorp",
    "website": "https://www.autocorp.ai",
    "linkedin": "https://www.linkedin.com/company/autocorptech",
    "email": "andrew@autocorp.ai",
    "founders": "",
    "description": "Autocorp's Fintech AI suite, AVA, is re-inventing how online car shoppers access credit & financing.",
    "location": "Ottawa",
    "categories": [
      "Artificial Intelligence (AI)",
      "Automotive",
      "Financial Services"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-69",
    "name": "Terrion",
    "website": "https://terrion.com/en",
    "linkedin": "https://www.linkedin.com/company/terrion/",
    "email": "info@terrion.com",
    "founders": "",
    "description": "Terrion creates secure and sustainable communication infrastructure to enable nationwide connectivity and digital growth.",
    "location": "Montr\u00e9al",
    "categories": [
      "Telecommunications"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-70",
    "name": "Alphawave",
    "website": "https://awavesemi.com",
    "linkedin": "https://www.linkedin.com/company/alphawave-plc",
    "email": "info@awavesemi.com",
    "founders": "",
    "description": "Alphawave Semi designs semiconductors and connectivity solutions that support advanced computing, communications, and data systems.",
    "location": "Toronto",
    "categories": [
      "Infrastructure",
      "Manufacturing",
      "Semiconductor"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-71",
    "name": "Fairstone Bank",
    "website": "https://www.fairstone.ca",
    "linkedin": "https://www.linkedin.com/company/fairstone",
    "email": "",
    "founders": "[object Object]",
    "description": "Fairstone Bank is a non-bank provider of responsible lending solutions for near-prime and non-prime borrowers.",
    "location": "Montr\u00e9al",
    "categories": [
      "Financial Services"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-72",
    "name": "Bright Minds Biosciences",
    "website": "https://brightmindsbio.com/",
    "linkedin": "https://www.linkedin.com/company/bright-minds-biosciences",
    "email": "info@brightmindsbio.com",
    "founders": "",
    "description": "Bright Minds Biosciences is a biotech company that engages in the development of serotonergic therapeutics to treat mental health disorders.",
    "location": "Vancouver",
    "categories": [
      "Biotechnology",
      "Health Care",
      "Medical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-73",
    "name": "CopperCorp Resources",
    "website": "https://coppercorpinc.com/",
    "linkedin": "https://www.linkedin.com/company/coppercorp/",
    "email": "info@coppercorpinc.com",
    "founders": "",
    "description": "CopperCorp Resources is a mineral exploration company.",
    "location": "Vancouver",
    "categories": [
      "Mineral",
      "Mining",
      "Mining Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-74",
    "name": "Canadian Colleges For A Resilient Recovery",
    "website": "https://resilientcolleges.ca/",
    "linkedin": "https://www.linkedin.com/company/resilient-colleges",
    "email": "info@resilientcolleges.ca",
    "founders": "",
    "description": "Canadian Colleges for a Resilient Recovery is a coalition of colleges, cegeps, institutes and polytechnics.",
    "location": "Hamilton",
    "categories": [
      "Education",
      "Higher Education",
      "Universities"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-75",
    "name": "CAMH",
    "website": "https://www.camh.ca",
    "linkedin": "https://www.linkedin.com/company/camh",
    "email": "info@camh.ca",
    "founders": "",
    "description": "CAMH is a mental health and addiction teaching hospital that helps transform the lives of people affected by mental health and addiction.",
    "location": "Toronto",
    "categories": [
      "Education",
      "Health Care",
      "Mental Health"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-76",
    "name": "BIASafe",
    "website": "https://biasafe.ai/",
    "linkedin": "https://ca.linkedin.com/company/biasafe",
    "email": "info@biasafe.ai",
    "founders": "",
    "description": "BIASafe is the end-to-end operating system for systematic investing.",
    "location": "Montreal",
    "categories": [
      "Artificial Intelligence (AI)",
      "FinTech"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-77",
    "name": "Pramana Pharmaceuticals",
    "website": "https://www.pramanapharma.com",
    "linkedin": "",
    "email": "",
    "founders": "",
    "description": "Pramana Pharmaceuticals is a biopharmaceutical company that offers pharmaceutical research and development services.",
    "location": "Vancouver",
    "categories": [
      "Biotechnology",
      "Manufacturing",
      "Pharmaceutical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-78",
    "name": "Augmentt",
    "website": "https://augmentt.com/",
    "linkedin": "https://www.linkedin.com/company/augmentt",
    "email": "derik.belair@augmentt.com",
    "founders": "",
    "description": "SaaS Management platform that helps organizations understand SaaS usage, optimize spend, enforce security policies and improve productivity.",
    "location": "Kanata",
    "categories": [
      "Cloud Management",
      "Cloud Security",
      "Enterprise Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-79",
    "name": "Proshop",
    "website": "https://www.proshoperp.com/",
    "linkedin": "https://www.linkedin.com/company/proshoperp/",
    "email": "contact@proshoperp.com",
    "founders": "",
    "description": "Proshop is a paperless web-based Shop Management Software System.",
    "location": "Vancouver",
    "categories": [
      "Manufacturing",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-80",
    "name": "Toyow",
    "website": "https://www.toyow.com",
    "linkedin": "https://www.linkedin.com/company/toyow/",
    "email": "invest@toyow.com",
    "founders": "",
    "description": "One stop marketplace for tokenized assets with real world value, leading the charge to transform ownership through the power of blockchain.",
    "location": "Toronto",
    "categories": [
      "Blockchain",
      "Film",
      "Funding Platform"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-81",
    "name": "PharmaCorp Rx",
    "website": "https://www.pharmacorprx.ca/",
    "linkedin": "https://www.linkedin.com/company/pharmacorprx/",
    "email": "",
    "founders": "",
    "description": "PharmaCorp Rx specializes in seamless pharmacy ownership transitions with legacy preservation and financial security.",
    "location": "Saskatoon",
    "categories": [
      "Retail"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-82",
    "name": "Nev Gold",
    "website": "https://nev-gold.com/",
    "linkedin": "https://www.linkedin.com/company/nevgold-corp/",
    "email": "",
    "founders": "",
    "description": "Nev Gold focuses on mineral exploration offering district-scale exploration and resource potential in strong geopolitical jurisdictions.",
    "location": "Vancouver",
    "categories": [
      "Mineral",
      "Mining",
      "Mining Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-83",
    "name": "Telmax 09F5",
    "website": "https://telmax.com",
    "linkedin": "https://www.linkedin.com/company/telmaxinc",
    "email": "sales@telmax.com",
    "founders": "",
    "description": "telMAX designs and builds telecommunications platforms for fiber internet, TV, and phone services.",
    "location": "Whitchurch-stouffville",
    "categories": [
      "Internet",
      "Telecommunications",
      "Wireless"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-84",
    "name": "SEIU Healthcare Training Centre",
    "website": "https://www.seiutrainingcentre.ca/",
    "linkedin": "https://www.linkedin.com/company/seiuhealthcare/",
    "email": "seiutrainingcentre@seiuhealthcare.ca",
    "founders": "",
    "description": "SEIU Healthcare Training Centre is union-led training school, dedicated to providing healthcare professionals with education and support.",
    "location": "Toronto",
    "categories": [
      "Education",
      "Health Care",
      "Training"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-85",
    "name": "Minga",
    "website": "https://minga.io",
    "linkedin": "https://www.linkedin.com/company/mingadotio",
    "email": "support@minga.io",
    "founders": "",
    "description": "Minga offers internet-based services including a digital ID and hall pass system.",
    "location": "Kelowna",
    "categories": [
      "Identity Management",
      "Internet",
      "Office Administration"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-86",
    "name": "Valour",
    "website": "https://valour.com/en",
    "linkedin": "https://www.linkedin.com/company/defitechnologies/",
    "email": "hello@defiholdings.ca",
    "founders": "",
    "description": "Valour builds and invests in new technologies to provide trusted, diversified exposure across the decentralized finance ecosystem.",
    "location": "Toronto",
    "categories": [
      "Blockchain",
      "Decentralized Finance (DeFi)",
      "Finance"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-87",
    "name": "Genome Canada",
    "website": "http://www.genomecanada.ca/en/",
    "linkedin": "https://www.linkedin.com/company/genome-canada",
    "email": "info@genomecanada.ca",
    "founders": "",
    "description": "Genome Canada invests in genomic science and technology and its translation into applications across multiple sectors.",
    "location": "Ottawa",
    "categories": [
      "Financial Services",
      "Non Profit",
      "Social Assistance"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-88",
    "name": "Payworks",
    "website": "https://www.payworks.ca/",
    "linkedin": "https://www.linkedin.com/company/payworks/",
    "email": "sales@payworks.ca",
    "founders": "",
    "description": "Payworks delivers innovative workforce management solutions that specialize in cloud-based payroll, HR, employee time & absence management.",
    "location": "Winnipeg",
    "categories": [
      "Human Resources",
      "Outsourcing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-89",
    "name": "Desert Mountain Energy",
    "website": "http://desertmountainenergy.com/",
    "linkedin": "https://www.linkedin.com/company/desert-mountain-energy-corp",
    "email": "don@desertmountainenergy.com",
    "founders": "",
    "description": "Desert Mountain Energy is an exploratory resource company.",
    "location": "Delta",
    "categories": [
      "Mineral",
      "Mining",
      "Natural Resources"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-90",
    "name": "Diesel Tech Industries",
    "website": "https://www.dtiguardian.com",
    "linkedin": "https://www.linkedin.com/company/diesel-tech-industries",
    "email": "info@dtiguardian.com",
    "founders": "",
    "description": "Diesel Tech Industries is an oil and gas energy company located in Edmonton.",
    "location": "Edmonton",
    "categories": [
      "Energy",
      "Industrial",
      "Oil and Gas"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-91",
    "name": "IMAX Corporation",
    "website": "http://www.imax.com",
    "linkedin": "https://www.linkedin.com/company/imax",
    "email": "",
    "founders": "",
    "description": "IMAX Corporation is one of the world's leading entertainment technology companies, specializing in immersive motion picture technologies.",
    "location": "Mississauga",
    "categories": [
      "Consumer",
      "Content",
      "Digital Entertainment"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-92",
    "name": "Denovia Labs",
    "website": "https://denovialabs.com/",
    "linkedin": "https://www.linkedin.com/company/denovia-labs/",
    "email": "ir@denovialabs.com",
    "founders": "",
    "description": "Denovia Labs is an innovative study company that has created a seismic wave in plastic waste and sustainability.",
    "location": "London",
    "categories": [
      "Information Technology",
      "Manufacturing",
      "Product Design"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-93",
    "name": "Aris Mining",
    "website": "https://www.aris-mining.com",
    "linkedin": "https://www.linkedin.com/company/aris-mining",
    "email": "info@aris-mining.com",
    "founders": "",
    "description": "Aris Mining is a mining company.",
    "location": "Vancouver",
    "categories": [
      "Mineral",
      "Mining",
      "Mining Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-94",
    "name": "Binta Financial",
    "website": "https://www.mybinta.com",
    "linkedin": "https://www.linkedin.com/company/binta-financial",
    "email": "info@mybinta.com",
    "founders": "",
    "description": "Fintech, cross-boarder payment, etc.",
    "location": "Vancouver",
    "categories": [
      "Finance",
      "Financial Exchanges",
      "Financial Services"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-95",
    "name": "Zedcor",
    "website": "https://www.zedcor.com",
    "linkedin": "https://www.linkedin.com/company/zedcor-security",
    "email": "info@zedcor.com",
    "founders": "",
    "description": "Zedcor provides mobile surveillance towers and remote video monitoring with analytics for site security.",
    "location": "Calgary",
    "categories": [
      "Construction",
      "Electronics",
      "Energy"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-96",
    "name": "Access Communications Cooperative",
    "website": "https://www.myaccess.ca",
    "linkedin": "https://www.linkedin.com/company/access-communications-cooperative-limited",
    "email": "",
    "founders": "",
    "description": "Access Communications Co-operative has been privileged to work with the people to make those things happen in the communities we serve.",
    "location": "Regina",
    "categories": [
      "Telecommunications",
      "Wired Telecommunications"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-97",
    "name": "Quantum Resistant Cryptographic Solutions Corporation Qrcs",
    "website": "https://www.qrcscorp.ca/",
    "linkedin": "https://www.linkedin.com/in/john-underhill-aaa0031b1/",
    "email": "contact@qrcscorp.ca",
    "founders": "",
    "description": "Quantum Resistant Cryptographic Solutions offers post-quantum cryptographic software and secure communications protocols.",
    "location": "Ottawa",
    "categories": [
      "Cyber Security",
      "FinTech",
      "Quantum Computing"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-98",
    "name": "Tehama",
    "website": "https://tehama.io",
    "linkedin": "https://www.linkedin.com/company/tehama",
    "email": "info@tehama.io",
    "founders": "",
    "description": "Tehama is a daas platform, enterprises can create cloud-based virtual offices, workrooms.",
    "location": "Ottawa",
    "categories": [
      "Information Technology",
      "SaaS",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-99",
    "name": "Orvana",
    "website": "http://www.orvana.com/English/home/default.aspx",
    "linkedin": "https://www.linkedin.com/company/orovalle-minerals",
    "email": "ask_us@orvana.com",
    "founders": "",
    "description": "Orvana is a multi-mine gold-copper producer. Orvana\u2019s operations consist of the El Valle gold-copper mines in northern Spain,",
    "location": "Toronto",
    "categories": [
      "Mineral",
      "Mining"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-100",
    "name": "Levio",
    "website": "https://www.levioconsulting.com/",
    "linkedin": "https://www.linkedin.com/company/levio-conseils/",
    "email": "contact@levioconsulting.com",
    "founders": "",
    "description": "Levio is a Provider of consulting services intended to facilitate program",
    "location": "Clarke City",
    "categories": [
      "Consulting",
      "Information Services",
      "Information Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-101",
    "name": "Frontlineiq",
    "website": "https://www.frontlineiq.ai",
    "linkedin": "https://www.linkedin.com/company/frontlineiq",
    "email": "info@frontlineIQ.ai",
    "founders": "",
    "description": "FrontlineIQ implements AI structured goal-setting, behavioral intelligence, and real-time insights to improve team sales performance.",
    "location": "Montr\u00e9al",
    "categories": [
      "E-Learning",
      "Enterprise Software",
      "Retail Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-102",
    "name": "Nucleus 5318",
    "website": "https://nucleus.com/",
    "linkedin": "https://www.linkedin.com/company/nucleus-tech-inc",
    "email": "josh@corp.nucleus.com",
    "founders": "",
    "description": "AI, SaaS, Vertical SaaS",
    "location": "Waterloo",
    "categories": [
      "Artificial Intelligence (AI)",
      "Enterprise Software",
      "SaaS"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-103",
    "name": "Hercules Metals",
    "website": "https://www.herculesmetals.com",
    "linkedin": "https://www.linkedin.com/company/hercules-silver-corp/",
    "email": "info@herculessilver.com",
    "founders": "",
    "description": "Hercules Metals is focused on the exploration and development of a large-scale disseminated silver-lead-zinc system at Hercules.",
    "location": "Toronto",
    "categories": [
      "Mineral",
      "Mining",
      "Mining Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-104",
    "name": "PROMINO",
    "website": "https://drinkpromino.com",
    "linkedin": "",
    "email": "contact@drinkpromino.com",
    "founders": "",
    "description": "PROMINO is a nutraceutical company specializing in the development of patented and science-based products.",
    "location": "Burlington",
    "categories": [
      "E-Commerce",
      "Health Care",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-105",
    "name": "Ag-West Bio Inc.",
    "website": "http://www.agwest.sk.ca",
    "linkedin": "https://www.linkedin.com/company/ag-west-bio",
    "email": "agwest@agwest.sk.ca",
    "founders": "",
    "description": "Ag-West Bio Inc. is a catalyst for Saskatchewan\u2019s bioeconomy, helping to move research to market. A not-for-profit, member-based",
    "location": "Saskatoon",
    "categories": [
      "Agriculture",
      "Biotechnology",
      "Communities"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-106",
    "name": "Havelock Metal",
    "website": "https://www.havelockmetal.com",
    "linkedin": "https://www.linkedin.com/company/havelock-metal-co.",
    "email": "info@havelockmetal.com",
    "founders": "",
    "description": "Havelock Metal is a building maintenance company that provides steel roofing, siding, trim, and accessories with consultation services.",
    "location": "Peterborough",
    "categories": [
      "Building Maintenance",
      "Building Material",
      "Construction"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-107",
    "name": "Panda Hub",
    "website": "https://pandahub.com",
    "linkedin": "https://www.linkedin.com/company/panda-hub-co/",
    "email": "info@pandahub.ca",
    "founders": "",
    "description": "The Largest Car Detailing Marketplace",
    "location": "Toronto",
    "categories": [
      "Automotive",
      "Mobile Apps",
      "Service Industry"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-108",
    "name": "Enmax Corporation",
    "website": "https://www.enmax.com/home",
    "linkedin": "https://www.linkedin.com/company/enmax",
    "email": "info@albertaonecall.com",
    "founders": "",
    "description": "ENMAX makes, moves, and sells electricity to residential, small business and large commercial customers.",
    "location": "Calgary",
    "categories": [
      "Energy",
      "Information Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-109",
    "name": "Greenbriar Sustainable Living",
    "website": "https://greenbriarliving.com",
    "linkedin": "https://www.linkedin.com/company/greenbriar-capital-corp",
    "email": "",
    "founders": "",
    "description": "Greenbriar Sustainable Living is a developer of renewable energy and sustainable real estate projects.",
    "location": "Coquitlam",
    "categories": [
      "Energy",
      "Real Estate"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-110",
    "name": "Staccato 3C57",
    "website": "https://staccato.ai/",
    "linkedin": "https://www.linkedin.com/company/staccato-ai/",
    "email": "support@staccato.ai",
    "founders": "",
    "description": "Staccato's AI Instrument\u2122 is the AI MIDI cowriter for music producers and composers.",
    "location": "London",
    "categories": [
      "Artificial Intelligence (AI)",
      "Generative AI",
      "Music"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-111",
    "name": "Henon",
    "website": "https://www.henon.io",
    "linkedin": "https://www.linkedin.com/company/henoncapital/",
    "email": "info@henoncapital.ca",
    "founders": "",
    "description": "Henon is a tech-enabled financial services company that helps businesses with their financial needs.",
    "location": "Toronto",
    "categories": [
      "Business Development",
      "Financial Services",
      "FinTech"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-112",
    "name": "Aramis Biotechnologies",
    "website": "https://aramisbiotechnologies.com/",
    "linkedin": "https://www.linkedin.com/company/aramisbiotechnologies/",
    "email": "",
    "founders": "",
    "description": "Aramis Biotechnologies specializes in the development of novel vaccines in plants.",
    "location": "Quebec",
    "categories": [
      "Biotechnology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-113",
    "name": "Blue Star Gold",
    "website": "https://www.bluestargold.ca/",
    "linkedin": "https://www.linkedin.com/company/blue-star-gold-corp/",
    "email": "info@bluestargold.ca",
    "founders": "",
    "description": "Blue Star Gold is a gold company that explores and develops mineral projects.",
    "location": "Vancouver",
    "categories": [
      "Mining",
      "Mining Technology",
      "Precious Metals"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-114",
    "name": "Aviron",
    "website": "https://www.aviron.ai/",
    "linkedin": "https://www.linkedin.com/company/aviron-ai",
    "email": "info@aviron.ai",
    "founders": "",
    "description": "Aviron is transforming finance operations with human-centric AI co-workers",
    "location": "Montr\u00e9al",
    "categories": [
      "Artificial Intelligence (AI)",
      "B2B",
      "Generative AI"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-115",
    "name": "InnovMetric Software",
    "website": "http://www.innovmetric.com",
    "linkedin": "http://www.linkedin.com/company/innovmetric-software",
    "email": "info@innovmetric.com",
    "founders": "",
    "description": "InnovMetric Software is a developer of 3D metrology software.",
    "location": "Quebec",
    "categories": [
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-116",
    "name": "GovernGPT",
    "website": "https://www.governgpt.ai",
    "linkedin": "https://www.linkedin.com/company/governgpt-ai",
    "email": "",
    "founders": "",
    "description": "GovernGPT is an AI company that reviews marketing compliance, and understanding financial regulations.",
    "location": "Toronto",
    "categories": [
      "Financial Services",
      "FinTech"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-117",
    "name": "IcePanel",
    "website": "https://icepanel.io",
    "linkedin": "https://www.linkedin.com/company/icepanel/",
    "email": "mail@icepanel.io",
    "founders": "",
    "description": "IcePanel is a SaaS tool for tech teams to collaborate on their software architecture design.",
    "location": "Vancouver",
    "categories": [
      "Developer Tools",
      "Information Technology",
      "SaaS"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-118",
    "name": "Biocanrx",
    "website": "https://biocanrx.com/",
    "linkedin": "https://www.linkedin.com/company/biocanrx/",
    "email": "info@biocanrx.com",
    "founders": "",
    "description": "BioCanRx deals with translation, manufacture and adoption of cancer immunotherapies.",
    "location": "Ottawa",
    "categories": [
      "Health Care",
      "Medical",
      "Non Profit"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-119",
    "name": "Paradigm Shift",
    "website": "http://paradigmshift.com",
    "linkedin": "https://www.linkedin.com/company/paradigm-shift-tech-inc",
    "email": "info@paradigmshift.com",
    "founders": "",
    "description": "Paradigm Shift provides clients with superior service accompanied by state-of-the-art hardware capabilities.",
    "location": "Toronto",
    "categories": [
      "Information Technology",
      "Service Industry"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-120",
    "name": "Humanoid Global",
    "website": "https://www.humanoidglobal.ai/",
    "linkedin": "",
    "email": "",
    "founders": "",
    "description": "Humanoid Global is the first publicly listed investment issuer dedicated to the global humanoid robotics and embodied AI sector.",
    "location": "Toronto",
    "categories": [
      "Consumer Research",
      "Market Research",
      "Product Research"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-121",
    "name": "Certarus",
    "website": "https://www.certarus.com",
    "linkedin": "https://www.linkedin.com/company/certarus-ltd.",
    "email": "",
    "founders": "[object Object]",
    "description": "Certarus is a provider of low carbon energy solutions through a fully integrated compressed natural gas (CNG) platform.",
    "location": "Calgary",
    "categories": [
      "Clean Energy",
      "CleanTech",
      "Oil and Gas"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-122",
    "name": "AllMind AI",
    "website": "https://allmind.ai",
    "linkedin": "https://www.linkedin.com/company/allmindai/",
    "email": "anwaarmalik@allmindinvestments.com",
    "founders": "",
    "description": "AllMind AI is a research terminal that helps investment teams go from idea to conviction in minutes.",
    "location": "Waterloo",
    "categories": [
      "Artificial Intelligence (AI)",
      "Business Intelligence",
      "Financial Services"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-123",
    "name": "McCain Foods",
    "website": "http://www.mccain.com",
    "linkedin": "https://www.linkedin.com/company/mccainfoods/",
    "email": "",
    "founders": "",
    "description": "McCain Foods is a family-owned business and manufacturer of frozen potato products and a global leader in prepared appetizers and snacks.",
    "location": "Toronto",
    "categories": [
      "Food and Beverage",
      "Food Processing",
      "Snack Food"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-124",
    "name": "Miraterra",
    "website": "http://www.miraterrasoil.com",
    "linkedin": "https://www.linkedin.com/company/miraterrainc",
    "email": "",
    "founders": "",
    "description": "Miraterra's solution produces lab-quality findings in soil labs, the field, and the ground.",
    "location": "Vancouver",
    "categories": [
      "Agriculture",
      "AgTech",
      "Renewable Energy"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-125",
    "name": "Solaires Entreprises Inc.",
    "website": "https://www.solaires.net",
    "linkedin": "https://www.linkedin.com/company/solaires-entreprises-inc",
    "email": "gogreen@solar-ventures.com",
    "founders": "",
    "description": "Solaires Entreprises Inc. is a group of scientists and engineers dedicated to bringing solar energy to a broader audience.",
    "location": "Victoria",
    "categories": [
      "CleanTech",
      "Renewable Energy",
      "Solar"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-126",
    "name": "High Q Technologies",
    "website": "https://highqtechnologies.com",
    "linkedin": "https://www.linkedin.com/company/highqtechnologies",
    "email": "",
    "founders": "",
    "description": "High Q Technologies develops quantum-enabled scientific instruments for ultra-high-sensitivity biophysical and chemical analysis.",
    "location": "Waterloo",
    "categories": [
      "Information Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-127",
    "name": "Shared Tower",
    "website": "https://www.sharedtower.ca",
    "linkedin": "https://www.linkedin.com/company/shared-tower-inc/",
    "email": "dsimmons@sharedtower.ca",
    "founders": "",
    "description": "Canadian Telecommunications Infrastructure Developer and Operator",
    "location": "Oakville",
    "categories": [
      "Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-128",
    "name": "Ciscom",
    "website": "https://www.ciscomcorp.com",
    "linkedin": "https://www.linkedin.com/company/ciscom-corporation",
    "email": "info@CiscomCorp.com",
    "founders": "",
    "description": "Ciscom is an information and communication technology company that offers marketing, document processing, and content management services.",
    "location": "Toronto",
    "categories": [
      "Advertising",
      "Content",
      "Information Technology"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-129",
    "name": "Canadian North",
    "website": "https://www.canadiannorth.com",
    "linkedin": "https://www.linkedin.com/company/canadian-north",
    "email": "contact@canadiannorth.com",
    "founders": "[object Object]",
    "description": "Canadian North is an airline providing passenger and cargo services with a fleet designed for remote and challenging environments.",
    "location": "Toronto",
    "categories": [
      "Aerospace",
      "Charity",
      "Training"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-130",
    "name": "Profound Impact F23F",
    "website": "https://www.profoundimpact.com/",
    "linkedin": "https://www.linkedin.com/company/profound-impact-corporation/",
    "email": "",
    "founders": "",
    "description": "Profound Impact operates as an AI-Powered platform.",
    "location": "Waterloo",
    "categories": [
      "Artificial Intelligence (AI)",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-131",
    "name": "CarboMat",
    "website": "https://carbomatinc.com/",
    "linkedin": "https://www.linkedin.com/company/carbomatinc/",
    "email": "",
    "founders": "",
    "description": "CarboMat specializes in transforming low-value products like Alberta asphaltenes to develop high-value carbon.",
    "location": "Calgary",
    "categories": [
      "Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-132",
    "name": "Browze",
    "website": "http://browze.com/",
    "linkedin": "https://www.linkedin.com/company/browze",
    "email": "support@browze.com",
    "founders": "",
    "description": "Browze provides electronics, jewelry, kitchenware, and other related products in order to curate unique products.",
    "location": "Toronto",
    "categories": [
      "Consumer Goods",
      "E-Commerce",
      "Retail"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-133",
    "name": "Goldmining",
    "website": "https://www.goldmining.com/",
    "linkedin": "https://www.linkedin.com/company/goldmining-inc./",
    "email": "info@goldmining.com",
    "founders": "",
    "description": "Goldmining is a mining company.",
    "location": "Vancouver",
    "categories": [
      "Mining",
      "Natural Resources",
      "Sustainability"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-134",
    "name": "1Valet",
    "website": "https://www.1valet.com/",
    "linkedin": "https://www.linkedin.com/company/1valet",
    "email": "info@1valet.com",
    "founders": "",
    "description": "1VALET integrates and connects IoT smart technologies to create a unified experience between developers, residents and property managers.",
    "location": "Gatineau",
    "categories": [
      "Information Technology",
      "Property Management",
      "SaaS"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-135",
    "name": "Cengn",
    "website": "https://www.cengn.ca/",
    "linkedin": "https://www.linkedin.com/company/cengn---centre-of-excellence-in-next-generation-networks-",
    "email": "info@cengn.ca",
    "founders": "",
    "description": "CENGN\u2019s mission is to accelerate the commercialization of network technologies and applications.",
    "location": "Ottawa",
    "categories": [
      "Information Technology",
      "Internet",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-136",
    "name": "Fort Technology",
    "website": "https://www.fort-technology.com",
    "linkedin": "",
    "email": "",
    "founders": "",
    "description": "Fort Technology develops and supplies products for both amateur and professional use in the pest control and remedial repair industry.",
    "location": "Burnaby",
    "categories": [
      "Extermination Service",
      "Industrial"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-137",
    "name": "Advanced Biofuels Canada",
    "website": "https://advancedbiofuels.ca",
    "linkedin": "https://www.linkedin.com/company/advancedbiofuelsca",
    "email": "admin@advancedbiofuels.ca",
    "founders": "",
    "description": "Advanced Biofuels Canada is a voice for producers, distributors, and technology developers in the biofuels sector.",
    "location": "Vancouver",
    "categories": [
      "Biofuel",
      "Non Profit",
      "Renewable Energy"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-138",
    "name": "PemPem",
    "website": "https://www.pempem.io",
    "linkedin": "https://www.linkedin.com/company/pempem/",
    "email": "info@pempem.org",
    "founders": "",
    "description": "PemPem is an IT company that provides financial instruments, buyer-supplier market platforms, and supply chain software solutions.",
    "location": "Montr\u00e9al",
    "categories": [
      "Apps",
      "Internet",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-139",
    "name": "Emerita Resources",
    "website": "http://www.emeritaresources.com/",
    "linkedin": "https://www.linkedin.com/company/emerita-resources",
    "email": "info@emeritaresources.com",
    "founders": "",
    "description": "A Premier Zinc Exploration Platform.",
    "location": "Toronto",
    "categories": [
      "Mining",
      "Precious Metals"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-140",
    "name": "Devonian",
    "website": "http://groupedevonian.com/",
    "linkedin": "https://www.linkedin.com/company/groupe-devonian/about/",
    "email": "info@groupedevonian.com",
    "founders": "",
    "description": "Devonian is a late stage botanical pharmaceutical corporation",
    "location": "Pointe-claire",
    "categories": [
      "Biotechnology",
      "Medical",
      "Pharmaceutical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-141",
    "name": "E INC",
    "website": "https://e.inc",
    "linkedin": "https://www.linkedin.com/company/e-inc",
    "email": "",
    "founders": "[object Object]",
    "description": "E INC is an auto-tech firm that focuses on improving the online purchasing experience.",
    "location": "Toronto",
    "categories": [
      "Automotive",
      "Consulting",
      "Sales"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-142",
    "name": "Noram Lithium",
    "website": "https://noramlithiumcorp.com/",
    "linkedin": "https://www.linkedin.com/company/noram-lithium-corp",
    "email": "ir@noramlithiumcorp.com",
    "founders": "",
    "description": "Noram Lithium is a lithium exploration stage company that develops lithium deposits.",
    "location": "Vancouver",
    "categories": [
      "Mining",
      "Mining Technology",
      "Precious Metals"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-143",
    "name": "SPIRIT Blockchain",
    "website": "http://spiritblockchain.com",
    "linkedin": "https://www.linkedin.com/company/spiritblockchain/",
    "email": "info@spiritblockchain.com",
    "founders": "",
    "description": "SPIRIT Blockchain is a bridging blockchain and digital assets to capital markets.",
    "location": "Vancouver",
    "categories": [
      "Blockchain",
      "Finance",
      "FinTech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-144",
    "name": "Tenet",
    "website": "https://tenetfintech.com",
    "linkedin": "https://www.linkedin.com/company/tenetfintech",
    "email": "cboyd@tenetfintech.com",
    "founders": "",
    "description": "Tenet is the parent company of a group of six innovative financial technology subsidiaries operating in China\u2019s.",
    "location": "Toronto",
    "categories": [
      "Analytics",
      "Artificial Intelligence (AI)",
      "Developer Platform"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-145",
    "name": "AgentHub",
    "website": "https://www.agenthub.dev",
    "linkedin": "https://www.linkedin.com/company/agenthubai",
    "email": "founders@agenthub.dev",
    "founders": "",
    "description": "AgentHub is used to build powerful automations without writing the single line of code.",
    "location": "Vancouver",
    "categories": [
      "Artificial Intelligence (AI)",
      "Developer Tools",
      "Information Technology"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-146",
    "name": "Secondshop",
    "website": "https://secondshop.ca/",
    "linkedin": "https://www.linkedin.com/company/secondshop-com/",
    "email": "",
    "founders": "",
    "description": "SecondShop operates as an online marketplace to find and purchase home furnishings.",
    "location": "Toronto",
    "categories": [
      "E-Commerce",
      "Marketplace",
      "Retail"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-147",
    "name": "Woodway Assurance",
    "website": "https://www.woodway-assurance.com",
    "linkedin": "https://www.linkedin.com/company/woodway-assurance",
    "email": "",
    "founders": "",
    "description": "Woodway Assurance provides EviData, an AI-driven software for automated privacy assurance on de-identified and synthetic datasets.",
    "location": "Ottawa",
    "categories": [
      "Artificial Intelligence (AI)",
      "Cyber Security",
      "Information Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-148",
    "name": "Anfield Energy",
    "website": "https://anfieldenergy.com/",
    "linkedin": "https://www.linkedin.com/company/anfield-energy-inc",
    "email": "info@anfieldresources.com",
    "founders": "",
    "description": "Anfield Energy is an energy metals exploration, development, and near-term production company.",
    "location": "Vancouver",
    "categories": [
      "Energy",
      "Project Management",
      "Renewable Energy"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-149",
    "name": "Bloom",
    "website": "https://www.bloomfin.ca/",
    "linkedin": "https://www.linkedin.com/company/bloomfinancecompany/",
    "email": "info@bloomfin.ca",
    "founders": "",
    "description": "Bloom is a Canadian fintech that provides home equity release solutions to 55+ homeowners.",
    "location": "Toronto",
    "categories": [
      "Financial Services"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-150",
    "name": "Ednatec",
    "website": "https://ednatec.com",
    "linkedin": "https://www.linkedin.com/company/ednatec",
    "email": "learnmore@ednatec.com",
    "founders": "",
    "description": "eDNAtec is a company that uses environmental DNA technology to enable ocean-based enterprises and promote ocean health.",
    "location": "St. John's",
    "categories": [
      "Biotechnology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-151",
    "name": "One Development Corporation",
    "website": "http://onedevcorp.com",
    "linkedin": "https://www.linkedin.com/company/69947972",
    "email": "jferreira@onedevcorp.com",
    "founders": "",
    "description": "Real Estate, Construction, Housing, PropTech, Urban Infill, Multiplex Development",
    "location": "Toronto",
    "categories": [
      "Construction",
      "Property Development",
      "Real Estate"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-152",
    "name": "Bioharvest Sciences",
    "website": "https://bioharvest.com",
    "linkedin": "https://www.linkedin.com/company/bioharvestsciences/",
    "email": "dave@bioharvest.com",
    "founders": "",
    "description": "BioHarvest Sciences produces and sells a food-based nutraceutical product called ViniaTM.",
    "location": "Vancouver",
    "categories": [
      "Biotechnology",
      "Food and Beverage",
      "Life Science"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-153",
    "name": "Allheart Web",
    "website": "https://allheartweb.com/",
    "linkedin": "https://www.linkedin.com/company/allheartweb/",
    "email": "hello@allheartweb.com",
    "founders": "",
    "description": "Global AI-driven data solutions for Cybersecurity, Leads, and Digital Fortification.",
    "location": "Mississauga",
    "categories": [
      "Artificial Intelligence (AI)",
      "Cyber Security",
      "Database"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-154",
    "name": "Rayhawk Technologies",
    "website": "https://www.rayhawk.ca",
    "linkedin": "https://www.linkedin.com/company/rayhawk",
    "email": "info@rayhawk.ca",
    "founders": "",
    "description": "RAYHAWK Technologies promote a safer working environment and benefit organizations in both small and large facilities.",
    "location": "Saskatoon",
    "categories": [
      "Business Development",
      "Consulting",
      "Employee Benefits"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-155",
    "name": "Peloton Technologies",
    "website": "https://www.peloton-technologies.com",
    "linkedin": "https://www.linkedin.com/company/peloton-technologies",
    "email": "media@peloton-technologies.com",
    "founders": "",
    "description": "Peloton Technologies is an all-in-one cloud-based platform that simplifies payments for organizations of any size.",
    "location": "Victoria",
    "categories": [
      "Accounting",
      "Cloud Data Services",
      "Developer APIs"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-156",
    "name": "Abaxx Technologies",
    "website": "https://www.abaxx.tech/",
    "linkedin": "https://www.linkedin.com/company/abaxx",
    "email": "",
    "founders": "",
    "description": "Abaxx Technologies is a Financial Technology Company",
    "location": "Toronto",
    "categories": [
      "Financial Exchanges",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-157",
    "name": "Visionary Group",
    "website": "https://visiongroupca.com",
    "linkedin": "https://www.linkedin.com/company/visionary-education-technology-holdings-group-inc",
    "email": "info@farvision.ca",
    "founders": "",
    "description": "Visionary Group offers its customers education and related services.",
    "location": "Toronto",
    "categories": [
      "EdTech",
      "Education",
      "Service Industry"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-158",
    "name": "Independent Electricity System Operator",
    "website": "http://www.ieso.ca/en/Get-Involved/Funding-Programs/Grid-Innovation-Fund/Overview",
    "linkedin": "https://www.linkedin.com/company/ieso/",
    "email": "",
    "founders": "",
    "description": "Crown corporation responsible for operating the electricity market of the bulk electrical system in the province of Ontario, Canada",
    "location": "Toronto",
    "categories": [
      "Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-159",
    "name": "Appficiency",
    "website": "https://www.appficiencyinc.com",
    "linkedin": "https://www.linkedin.com/company/appficiency-inc.",
    "email": "",
    "founders": "[object Object]",
    "description": "Appficiency is an information technology enterprise resource planning (ERP) company located in Mississauga.",
    "location": "Mississauga",
    "categories": [
      "Consulting",
      "Information Technology"
    ],
    "funding": " - "
  },
  {
    "id": "cdn-160",
    "name": "Mednow",
    "website": "https://mednow.ca/",
    "linkedin": "https://www.linkedin.com/company/mednow-ca/",
    "email": "yourcare@mednow.ca",
    "founders": "",
    "description": "Mednow is a healthcare technology company that offers free at-home delivery of medications and access to telemedicine virtual care.",
    "location": "Vaughan",
    "categories": [
      "Health Care",
      "Internet",
      "Pharmaceutical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-161",
    "name": "Cora Therapeutics",
    "website": "https://coratherapeutics.com/",
    "linkedin": "https://www.linkedin.com/company/coratherapeutics/",
    "email": "hello@coratherapeutics.com",
    "founders": "",
    "description": "Cora Therapeutics is a biotechnology company that provides research-based solutions for whole body health.",
    "location": "Toronto",
    "categories": [
      "Biotechnology",
      "Health Care",
      "Therapeutics"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-162",
    "name": "Laminar 9A88",
    "website": "https://laminar.run",
    "linkedin": "https://www.linkedin.com/company/laminar-run/",
    "email": "connect@laminar.run",
    "founders": "",
    "description": "Low-code bespoke integration builder for solutions teams.",
    "location": "Toronto",
    "categories": [
      "Software"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-163",
    "name": "Kamazooie Development Corporation",
    "website": "https://kama.ai",
    "linkedin": "https://www.linkedin.com/company/kamazooie-development-corporation/",
    "email": "inquiries@kama.ai",
    "founders": "",
    "description": "kama.ai is the developer of the patented Designed Experiential Intelligence\u2122 system, kama DEI.",
    "location": "Toronto",
    "categories": [
      "Artificial Intelligence (AI)",
      "CRM",
      "E-Commerce"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-164",
    "name": "Optionality.ai",
    "website": "https://optionality.ai/",
    "linkedin": "https://www.linkedin.com/company/optionalityai",
    "email": "simon@optionality.ai",
    "founders": "",
    "description": "Optionality.ai develops an AI-based advisory platform to help clients make improved and informed decisions.",
    "location": "Montreal",
    "categories": [
      "Artificial Intelligence (AI)",
      "Banking",
      "FinTech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-165",
    "name": "Applied Brain Research",
    "website": "http://www.appliedbrainresearch.com",
    "linkedin": "https://www.linkedin.com/company/applied-brain-research/",
    "email": "peter.suma@appliedbrainresearch.com",
    "founders": "",
    "description": "ABR makes the world's smallest edge AI chip for time-series processing and the world's most advanced neuromoprhic compiler.",
    "location": "Waterloo",
    "categories": [
      "AI Infrastructure",
      "Artificial Intelligence (AI)",
      "Intelligent Systems"
    ],
    "funding": " - "
  },
  {
    "id": "cdn-166",
    "name": "Pluribus Technologies",
    "website": "https://www.pluribustechnologies.com",
    "linkedin": "https://in.linkedin.com/company/pluribus-technologies",
    "email": "info@pluribustechnologies.com",
    "founders": "",
    "description": "Pluribus Technologies specializes in acquiring small, profitable software companies.",
    "location": "Toronto",
    "categories": [
      "B2B",
      "Information Technology",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-167",
    "name": "Green Economy Canada",
    "website": "https://greeneconomy.ca",
    "linkedin": "https://www.linkedin.com/company/greeneconomyca",
    "email": "info@greeneconomy.ca",
    "founders": "",
    "description": "Green Economy Canada is a non-profit organization that helps businesses and communities transition toward a net-zero, sustainable economy.",
    "location": "Waterloo",
    "categories": [
      "Business Development",
      "Communities",
      "Non Profit"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-168",
    "name": "Entourage Health",
    "website": "https://entouragehealthcorp.com",
    "linkedin": "https://www.linkedin.com/company/entouragehealth/",
    "email": "sendmeinformation@weedmd.com",
    "founders": "[object Object]",
    "description": "Entourage Health is a Health Canada Licensed Producer under the Access to Cannabis for Medical Purposes Regulations (ACMPR).",
    "location": "Aylmer",
    "categories": [
      "Cannabis",
      "Health Care",
      "Medical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-169",
    "name": "Nextech AR Solutions",
    "website": "http://www.nextechar.com",
    "linkedin": "https://www.linkedin.com/company/nextech-ar-solutions",
    "email": "investor.relations@nextechar.com",
    "founders": "",
    "description": "Nextech AR Solutions is a publicly traded Metaverse company, specializing in augmented reality solutions, spatial mapping and 3D models.",
    "location": "Toronto",
    "categories": [
      "3D Technology",
      "Advertising",
      "Artificial Intelligence (AI)"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-170",
    "name": "Bioform",
    "website": "https://bioformtech.com",
    "linkedin": "https://www.linkedin.com/company/bioform-technologies/",
    "email": "",
    "founders": "",
    "description": "Bioform develops sustainable alternatives to single-use plastics and climate-friendly materials.",
    "location": "Vancouver",
    "categories": [
      "Advanced Materials",
      "Biotechnology",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-171",
    "name": "Aruna Revolution Health",
    "website": "https://www.arunarevolution.com/",
    "linkedin": "https://www.linkedin.com/company/aruna-revolution",
    "email": "hello@arunarevolution.com",
    "founders": "",
    "description": "Aruna Revolution Health is transforming menstrual health and education by offering radically inclusive compostable products.",
    "location": "Vancouver",
    "categories": [
      "Health Care"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-172",
    "name": "OpenHouse.ai",
    "website": "https://www.openhouse.ai/",
    "linkedin": "https://www.linkedin.com/company/openhouse-ai/",
    "email": "info@openhouse.ai",
    "founders": "",
    "description": "OpenHouse.ai is a technological leader in the home building industry that provides data-driven solutions to empower decision-making.",
    "location": "Calgary",
    "categories": [
      "Advertising",
      "Analytics",
      "Business Intelligence"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-173",
    "name": "Luxxfolio",
    "website": "https://luxxfolio.com/",
    "linkedin": "https://ca.linkedin.com/company/luxxfolio-holdings",
    "email": "info@luxxfolio.com",
    "founders": "",
    "description": "Luxxfolio utilizes a secure permission-based technology, record keeping, and other trust-based authentication.",
    "location": "Vancouver",
    "categories": [
      "Bitcoin",
      "Blockchain",
      "Cryptocurrency"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-174",
    "name": "Utradea",
    "website": "https://utradea.com/",
    "linkedin": "https://www.linkedin.com/company/utradea",
    "email": "admin@utradea.com",
    "founders": "",
    "description": "Social platform for investment ideas and insights",
    "location": "Toronto",
    "categories": [
      "Financial Services",
      "FinTech",
      "Social Media"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-175",
    "name": "Gateway Theatre",
    "website": "https://www.gatewaytheatre.com/",
    "linkedin": "https://www.linkedin.com/company/gatewaythtr/",
    "email": "boxoffice@gatewaytheatre.com",
    "founders": "",
    "description": "Gateway Theatre is a performing arts hub that improves the quality of life by engaging people in performing arts through training classes.",
    "location": "Richmond",
    "categories": [
      "Communities",
      "Education",
      "Performing Arts"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-176",
    "name": "Visual Defence",
    "website": "http://www.cityrover.com",
    "linkedin": "https://www.linkedin.com/company/visual-defence",
    "email": "info@cityrover.com",
    "founders": "",
    "description": "Visual Defence is a software development company that specializes in artificial intelligence and vision based applications",
    "location": "Richmond Hill",
    "categories": [
      "Artificial Intelligence (AI)",
      "GovTech",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-177",
    "name": "Canada House Wellness Group",
    "website": "https://mtlcorp.ca",
    "linkedin": "https://www.linkedin.com/company/mtl-cannabis",
    "email": "",
    "founders": "[object Object]",
    "description": "MTL Cannabis produces and distributes cannabis products for recreational and medical use.",
    "location": "Pickering",
    "categories": [
      "Cannabis",
      "Health Care",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-178",
    "name": "Savaria",
    "website": "http://www.savaria.com",
    "linkedin": "https://www.linkedin.com/company/savaria-inc",
    "email": "info@savaria.com",
    "founders": "",
    "description": "Savaria provides accessibility solutions for the elderly and physically challenged to increase their mobility and independence.",
    "location": "Brampton",
    "categories": [
      "Health Care",
      "Manufacturing",
      "Medical Device"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-179",
    "name": "Doksi",
    "website": "https://www.doksi.ai",
    "linkedin": "https://www.linkedin.com/company/doksi",
    "email": "taimur@doksi.ai",
    "founders": "",
    "description": "Doksi is a generative AI platform that enables businesses to create product support assets like help articles, guides, and videos instantly.",
    "location": "Toronto",
    "categories": [
      "Information Technology",
      "Internet",
      "Software"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-180",
    "name": "Actuality E2Bd",
    "website": "https://actuality.live/",
    "linkedin": "https://www.linkedin.com/company/actuality-live/",
    "email": "hello@actuality.live",
    "founders": "",
    "description": "AI powered platform to automate RFPs for construction industry",
    "location": "Toronto",
    "categories": [
      "Architecture",
      "Artificial Intelligence (AI)",
      "Augmented Reality"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-181",
    "name": "HYLQ",
    "website": "https://hylq.com",
    "linkedin": "https://www.linkedin.com/company/tony-g-holdings/",
    "email": "contact@tony.holdings",
    "founders": "",
    "description": "HYLQ is a Canadian public company",
    "location": "Mississauga",
    "categories": [
      "Cannabis",
      "Data Center",
      "Internet of Things"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-182",
    "name": "Popai E94D",
    "website": "https://www.popai.pro",
    "linkedin": "https://www.linkedin.com/company/popailife",
    "email": "connect@popai.pro",
    "founders": "",
    "description": "AI workspace for chatting with files, generating slides, code, images & more",
    "location": "Middlesex",
    "categories": [
      "Artificial Intelligence (AI)"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-183",
    "name": "Homerun Resources",
    "website": "https://homerunresources.com/",
    "linkedin": "https://www.linkedin.com/company/homerunresources/?originalSubdomain=ca",
    "email": "",
    "founders": "",
    "description": "Homerun Resources is an environmental service company that provides environmental remediation solutions.",
    "location": "Vancouver",
    "categories": [
      "Environmental Engineering",
      "Sustainability"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-184",
    "name": "McEwen Mining",
    "website": "http://www.mcewenmining.com/",
    "linkedin": "https://www.linkedin.com/company/mcewen-mining-inc-",
    "email": "info@mcewenmining.com",
    "founders": "",
    "description": "McEwen Mining is a gold and silver producer focused in the Americas with operating mines in Nevada, Canada, Mexico and Argentina.",
    "location": "Toronto",
    "categories": [
      "Mineral",
      "Mining Technology",
      "Natural Resources"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-185",
    "name": "Nature Conservancy Of Canada",
    "website": "http://www.natureconservancy.ca",
    "linkedin": "https://www.linkedin.com/company/the-nature-conservancy-of-canada/about/",
    "email": "nature@natureconservancy.ca",
    "founders": "",
    "description": "Nature Conservancy of Canada  directly protects and cares our country's most vulnerable natural areas & the plants & animals they sustain.",
    "location": "Toronto",
    "categories": [
      "Association",
      "Communities",
      "Government"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-186",
    "name": "Opusense AI",
    "website": "https://www.opusense.com/",
    "linkedin": "https://www.linkedin.com/company/opusense/",
    "email": "rcody@opusense.com",
    "founders": "",
    "description": "Opusense AI is a software that allows engineers and field inspectors to effortlessly generate professional reports in real time.",
    "location": "Toronto",
    "categories": [
      "B2B",
      "Construction",
      "SaaS"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-187",
    "name": "Aucctus",
    "website": "https://www.aucctus.com",
    "linkedin": "https://www.linkedin.com/company/aucctus/",
    "email": "contact@aucctus.com",
    "founders": "",
    "description": "AI-Powered Innovation SaaS",
    "location": "Toronto",
    "categories": [
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-188",
    "name": "Island Passage Exploration",
    "website": "https://islandpassage.ca/",
    "linkedin": "https://www.linkedin.com/company/island-passage-exploration-ltd/",
    "email": "info@islandpassage.ca",
    "founders": "",
    "description": "Island Passage Exploration was founded to provide the finance, technical, marketing, and business development expertise.",
    "location": "Vancouver",
    "categories": [
      "Commercial",
      "Finance",
      "Mineral"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-189",
    "name": "Arkii",
    "website": "https://www.getarki.com",
    "linkedin": "https://www.linkedin.com/company/getarki",
    "email": "info@getarki.com",
    "founders": "",
    "description": "Visual search engine for architects.",
    "location": "Toronto",
    "categories": [
      "Architecture",
      "Civil Engineering",
      "Construction"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-190",
    "name": "Recital Aa37",
    "website": "https://recitalapp.com/",
    "linkedin": "https://www.linkedin.com/company/recital-software",
    "email": "contact@recitalapp.com",
    "founders": "",
    "description": "Organize, simplify and accelerate your contract negotiations without changing how you work.",
    "location": "Vancouver",
    "categories": [
      "CMS",
      "Document Management",
      "Enterprise Applications"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-191",
    "name": "Stocky AI",
    "website": "https://www.stocky-ai.com/",
    "linkedin": "https://www.linkedin.com/company/stocky-ai/",
    "email": "conor@stocky-ai.com",
    "founders": "",
    "description": "Stocky AI is a B2B trading platform and ERP system that develops AI-Agents to create a more resilient and sustainable food system",
    "location": "Vancouver",
    "categories": [
      "AgTech",
      "Artificial Intelligence (AI)",
      "B2B"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-192",
    "name": "Moreover, Montreal Airports",
    "website": "http://www.admtl.com",
    "linkedin": "https://www.linkedin.com/company/adm-aeroports-de-montreal",
    "email": "",
    "founders": "",
    "description": "Moreover, Montreal Airports is keen to provide airport facilities adapted for people with disabilities or reduced mobility.",
    "location": "Dorval",
    "categories": [
      "Health Care",
      "Tourism",
      "Travel"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-193",
    "name": "Clean Metals Recycling",
    "website": "https://www.cleanmetals.com",
    "linkedin": "",
    "email": "",
    "founders": "",
    "description": "Clean Metals Recycling is a metal recycling company that aims to transform industrial waste into valuable metal byproducts.",
    "location": "Toronto",
    "categories": [
      "Precious Metals",
      "Recycling",
      "Waste Management"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-194",
    "name": "Growclass",
    "website": "https://www.growclass.co/",
    "linkedin": "https://www.linkedin.com/school/growclass",
    "email": "",
    "founders": "",
    "description": "Growclass provides Growth Marketing courses that prepare marketers with the technical skills required for high-growth careers.",
    "location": "Toronto",
    "categories": [
      "Marketing",
      "Professional Services",
      "Training"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-195",
    "name": "Proofofid",
    "website": "https://ProofOfID.io",
    "linkedin": "https://www.linkedin.com/company/proof-of-id/",
    "email": "Info@proofofid.io",
    "founders": "",
    "description": "Digital ID, KYC, IDV and Sharing, AI and ML SaaS, Mobile App",
    "location": "Toronto",
    "categories": [
      "Artificial Intelligence (AI)",
      "Cyber Security",
      "Identity Management"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-196",
    "name": "Notary Pro",
    "website": "https://www.notarypro.ca",
    "linkedin": "https://www.linkedin.com/company/notary-pro-canada",
    "email": "info@notarypro.ca",
    "founders": "",
    "description": "Notary Pro provides convenient notary public services for both in-person and remote online notarization.",
    "location": "Ottawa",
    "categories": [
      "Legal",
      "Legal Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-197",
    "name": "Heartee",
    "website": "https://hearteefoods.com",
    "linkedin": "https://www.linkedin.com/company/heartee",
    "email": "steve@adapt.ag",
    "founders": "",
    "description": "Heartee provides a turn-key opportunity for container farming of edible and gourmet mushrooms.",
    "location": "Ottawa",
    "categories": [
      "AgTech",
      "Food and Beverage"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-198",
    "name": "BC Biocarbon",
    "website": "https://www.bcbiocarbon.com/",
    "linkedin": "https://www.linkedin.com/company/bc-biocarbon",
    "email": "info@bcbiocarbon.com",
    "founders": "",
    "description": "BC Biocarbon is an environmental company that offers bio refinery technology.",
    "location": "Prince George",
    "categories": [
      "Biomass Energy",
      "Natural Resources",
      "Renewable Energy"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-199",
    "name": "ARC Medical Devices",
    "website": "https://arcmedinc.com/",
    "linkedin": "https://www.linkedin.com/company/arc-medical-devices-inc.",
    "email": "info@arcmeddev.com",
    "founders": "",
    "description": "ARC Medical Devices is a developer of medical products for the prevention of complications arising from surgeries.",
    "location": "Richmond",
    "categories": [
      "Biotechnology",
      "Health Care",
      "Medical Device"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-200",
    "name": "Goldragon",
    "website": "https://goldragon.io",
    "linkedin": "",
    "email": "contact@goldragon.io",
    "founders": "",
    "description": "Goldragon is a revolutionary, one-of-a-kind and completely unique Play-to-earn game that is fully transparent and community based.",
    "location": "Vancouver",
    "categories": [
      "Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-201",
    "name": "Irving Pulp Paper",
    "website": "https://irvingforestservices.com/",
    "linkedin": "https://www.linkedin.com/company/irving-paper",
    "email": "IrvingForestProducts@JDIrving.com",
    "founders": "",
    "description": "Irving\u2019s highly integrated forest products value chain. The Pulp & Paper division is made up of six different operating units.",
    "location": "Saint John",
    "categories": [
      "Business Development",
      "Customer Service",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-202",
    "name": "Diagnamed Holdings",
    "website": "https://www.diagnamed.com",
    "linkedin": "https://www.linkedin.com/company/diagnamed",
    "email": "",
    "founders": "",
    "description": "Diagnamed Holdings is a digital health firm that aims to improve brain health.",
    "location": "Toronto",
    "categories": [
      "Health Care",
      "Web Development"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-203",
    "name": "Burcon Nutrascience",
    "website": "https://www.burcon.ca",
    "linkedin": "https://www.linkedin.com/company/burcon-nutrascience-corporation",
    "email": "info@burcon.ca",
    "founders": "",
    "description": "Burcon Nutrascience develops plant proteins and ingredients for use in the food and beverage industries in Canada.",
    "location": "Vancouver",
    "categories": [
      "Biotechnology",
      "Food Processing",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-204",
    "name": "Pollin Fertility",
    "website": "https://www.pollinfertility.com",
    "linkedin": "https://www.linkedin.com/company/pollin",
    "email": "",
    "founders": "",
    "description": "Pollin Fertility is an operator of a fertility technology platform.",
    "location": "Toronto",
    "categories": [
      "Health Care",
      "Hospital"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-205",
    "name": "Bouclair",
    "website": "https://www.bouclair.com/",
    "linkedin": "https://www.linkedin.com/company/bouclair/",
    "email": "customerservice@bouclair.com",
    "founders": "",
    "description": "Bouclair is a retailer of home fashion and decor products.",
    "location": "Pointe-claire",
    "categories": [
      "Home Decor",
      "Home Improvement",
      "Retail"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-206",
    "name": "Snow Lake Resources",
    "website": "https://snowlakelithium.com",
    "linkedin": "https://www.linkedin.com/company/snow-lake-resources",
    "email": "dk@snowlakelithium.com",
    "founders": "",
    "description": "Snow Lake Resources is a privately owned mineral exploration company.",
    "location": "Winnipeg",
    "categories": [
      "Mineral",
      "Mining",
      "Mining Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-207",
    "name": "CONVERGX",
    "website": "https://www.convergx.co/",
    "linkedin": "https://www.linkedin.com/in/convergx%C2%AE-congress-509807125/",
    "email": "info@convergx.co",
    "founders": "",
    "description": "CONVERGX provides conference on investment and growth opportunities between the energy, mining, aerospace, defence, and security sectors.",
    "location": "Calgary",
    "categories": [
      "Energy",
      "Marketing",
      "Social Assistance"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-208",
    "name": "Fabricate",
    "website": "https://www.tryfabricate.com",
    "linkedin": "https://www.linkedin.com/company/tryfabricate",
    "email": "contact@tryfabricate.com",
    "founders": "",
    "description": "Fabricate is a Software Development firm that manufactures hardware for teams.",
    "location": "Toronto",
    "categories": [
      "Artificial Intelligence (AI)",
      "B2B",
      "Hardware"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-209",
    "name": "ME Therapeutics",
    "website": "https://www.metherapeutics.com/",
    "linkedin": "",
    "email": "",
    "founders": "",
    "description": "ME Therapeutics is a biotechnology company that focuses on discovery & development of myeloid cell targeted immuno oncology drugs.",
    "location": "Vancouver",
    "categories": [
      "Biopharma",
      "Biotechnology",
      "Life Science"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-210",
    "name": "Aabde Cannabis Processors Exporters And Importers",
    "website": "https://www.aabdecannabisprocessors.ca/",
    "linkedin": "",
    "email": "info@aabdecannabisprocessors.ca",
    "founders": "",
    "description": "AABDE cannabis processors, Exporters and importers INC stand as pioneers in the medical cannabis industry.",
    "location": "Toronto",
    "categories": [
      "Tech"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-211",
    "name": "A B M Tool Die",
    "website": "https://www.abmtool.com",
    "linkedin": "https://www.linkedin.com/company/a.b.m.-tool-&-die-co.-ltd.",
    "email": "abm@abmtool.com",
    "founders": "",
    "description": "A.B.M. TOOL & DIE is at the forefront of contemporary technology in the design and production.",
    "location": "Brampton",
    "categories": [
      "Automotive",
      "Industrial Design",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-212",
    "name": "Dairy Farmers Of Canada",
    "website": "https://dairyfarmersofcanada.ca/en",
    "linkedin": "https://www.linkedin.com/company/dfcplc/?originalSubdomain=ca",
    "email": "communications@dfc-plc.ca",
    "founders": "",
    "description": "Dairy Farmers of Canada helps to improve the Canadian dairy industry's environmental and economic sustainability and resilience.",
    "location": "Ottawa",
    "categories": [
      "Food and Beverage",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-213",
    "name": "UVAD Technologies",
    "website": "https://uvad.ca",
    "linkedin": "https://www.linkedin.com/company/unmanned-vehicle-applied-dynamics-inc-uvad",
    "email": "contact@uvad.ca",
    "founders": "",
    "description": "UVAD Technologies specializes in UAV development and applications.",
    "location": "Burnaby",
    "categories": [
      "Drones"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-214",
    "name": "Voiceflip",
    "website": "https://voiceflip.com",
    "linkedin": "https://www.linkedin.com/company/voiceflip/",
    "email": "kurtis@voiceflip.com",
    "founders": "",
    "description": "SaaS, E-Commerce, V-Commerce, Voice, Voice First, Retail, Alexa, Google Assistant, Siri, Cortana",
    "location": "Ottawa",
    "categories": [
      "Generative AI",
      "Real Estate",
      "SaaS"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-215",
    "name": "Omnicart",
    "website": "https://omnicart.tech/",
    "linkedin": "https://www.linkedin.com/company/omnicart-tech",
    "email": "",
    "founders": "[object Object]",
    "description": "Omnicart provides all of the tools required to build a multi-vendor marketplace with quick delivery.",
    "location": "Vancouver",
    "categories": [
      "Information Services",
      "Information Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-216",
    "name": "Nuron Ai",
    "website": "https://nuronai.org/",
    "linkedin": "https://www.linkedin.com/company/nuron-ai/",
    "email": "sudeepa@nuronai.org",
    "founders": "",
    "description": "Nuron AI enhances the efficiency of visa workflows through the implementation of Intellivisa's AI-powered automation technology.",
    "location": "Toronto",
    "categories": [
      "B2B",
      "Machine Learning",
      "Travel Accommodations"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-217",
    "name": "Mapsted",
    "website": "http://mapsted.com",
    "linkedin": "https://www.linkedin.com/company/mapstedhq/",
    "email": "info@mapsted.com",
    "founders": "",
    "description": "Mapsted is a world leader in location technology, helping businesses with location-based positioning, marketing, and analytics solutions.",
    "location": "Toronto",
    "categories": [
      "Analytics",
      "Indoor Positioning",
      "Internet"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-218",
    "name": "Vianet",
    "website": "https://www.vianet.ca/",
    "linkedin": "https://www.linkedin.com/company/vianet-internet-solutions/",
    "email": "privacy@vianet.ca",
    "founders": "",
    "description": "Vianet provides Internet and telecom services.",
    "location": "Sudbury",
    "categories": [
      "Internet",
      "Telecommunications",
      "Wired Telecommunications"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-219",
    "name": "Azure Sustainable Fuels",
    "website": "https://www.azuresf.com/",
    "linkedin": "https://www.linkedin.com/company/azuresf/",
    "email": "info@azuresf.com",
    "founders": "",
    "description": "Azure Sustainable Fuels is a fuel company that offers low carbon, sustainable aviation fuel (SAF) production facility.",
    "location": "Calgary",
    "categories": [
      "Air Transportation",
      "Clean Energy",
      "Fuel"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-220",
    "name": "Stem Cell Network",
    "website": "https://stemcellnetwork.ca/",
    "linkedin": "https://www.linkedin.com/company/stem-cell-network/",
    "email": "",
    "founders": "",
    "description": "SCN supports cutting-edge projects that translate Canadian stem cell research discoveries into new and better treatments.",
    "location": "Ottawa",
    "categories": [
      "Biotechnology",
      "Medical",
      "Product Research"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-221",
    "name": "Lab2Market",
    "website": "https://lab2market.ca/",
    "linkedin": "https://www.linkedin.com/company/lab2market/",
    "email": "info@lab2market.ca",
    "founders": "",
    "description": "Lab2Market is an entrepreneurship programme that supports researchers and students in advancing ideas toward commercial opportunities.",
    "location": "Toronto",
    "categories": [
      "Consulting",
      "Corporate Training",
      "Education"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-222",
    "name": "Distriq",
    "website": "https://distriq.com/en",
    "linkedin": "https://www.linkedin.com/company/zone-innovation-sherbrooke",
    "email": "info@distriq.com",
    "founders": "",
    "description": "Distriq advances the creation and implementation of quantum technologies.",
    "location": "Sherbrooke",
    "categories": [
      "Coworking",
      "Innovation Management",
      "Non Profit"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-223",
    "name": "Excellon Resources",
    "website": "http://www.excellonresources.com/",
    "linkedin": "https://www.linkedin.com/company/ecellon-resources-inc.",
    "email": "info@excellonresources.com",
    "founders": "",
    "description": "Excellon's 100%-owned La Platosa Mine in Durango is Mexico's highest grade silver mine, with lead and zinc by-products making it one.",
    "location": "Toronto",
    "categories": [
      "Manufacturing",
      "Mining",
      "Mining Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-224",
    "name": "Medical Advanced Platform",
    "website": "https://mapis4u.com",
    "linkedin": "https://www.linkedin.com/company/map-medical-advance-platform/?viewAsMember=true",
    "email": "clientservices@mapis4u.com",
    "founders": "",
    "description": "A.I Enterprise Software, SAAS, Mobile applications",
    "location": "Winnipeg",
    "categories": [
      "3D Technology",
      "Artificial Intelligence (AI)",
      "Health Care"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-225",
    "name": "Synucure Therapeutics",
    "website": "https://synucure.com",
    "linkedin": "https://www.linkedin.com/company/synucure/",
    "email": "",
    "founders": "",
    "description": "Synucure Therapeutics is a Canadian biotechnology business that operates research on degenerative brain illnesses.",
    "location": "Montr\u00e9al",
    "categories": [
      "Biotechnology",
      "Health Care"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-226",
    "name": "NRGene Canada",
    "website": "https://nrgenecanada.com",
    "linkedin": "https://www.linkedin.com/company/nrgene-canada",
    "email": "info@nrgenecanada.com",
    "founders": "",
    "description": "NRGene Canada is a biotechnology company that uses AI-driven genomics and big-data tools to develop biological solutions.",
    "location": "Saskatoon",
    "categories": [
      "Agriculture",
      "AgTech",
      "Biotechnology"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-227",
    "name": "Technl",
    "website": "https://technl.ca",
    "linkedin": "https://www.linkedin.com/company/nltechnl",
    "email": "info@technl.ca",
    "founders": "",
    "description": "techNL provides visibility, business growth services and a collective influential voice to the tech sector in Newfoundland and Labrador.",
    "location": "St. John's",
    "categories": [
      "Information Technology",
      "Non Profit"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-228",
    "name": "Loop",
    "website": "https://www.bankonloop.com",
    "linkedin": "https://www.linkedin.com/company/loop-financial",
    "email": "",
    "founders": "",
    "description": "Loop is a banking platform designed for growing businesses and entrepreneurs.",
    "location": "Toronto",
    "categories": [
      "Banking",
      "Financial Services",
      "Retail"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-229",
    "name": "RFINE Biomass Solutions",
    "website": "https://rfinebiomass.com",
    "linkedin": "https://www.linkedin.com/company/rfinebiomass",
    "email": "info@rfinebiomass.com",
    "founders": "",
    "description": "RFINE Biomass Solutions is to make coffee waste sustainable and delightful.",
    "location": "Dartmouth",
    "categories": [
      "Commercial",
      "Machinery Manufacturing",
      "Service Industry"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-230",
    "name": "Canadian Glycomics Network",
    "website": "https://canadianglycomics.ca/",
    "linkedin": "https://www.linkedin.com/company/glyconet/",
    "email": "glyconet@ualberta.ca",
    "founders": "",
    "description": "Canadian Glycomics Network addresses key challenges in human and animal health.",
    "location": "Edmonton",
    "categories": [
      "Medical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-231",
    "name": "Tech Alliance Corp",
    "website": "http://www.techalliance.ca",
    "linkedin": "https://www.linkedin.com/company/techalliance-of-southwestern-ontario/",
    "email": "hello@techalliance.ca",
    "founders": "",
    "description": "Supporting Ontario's most promising start-ups and fastest growing tech companies, we fuel growth in Canada\u2019s innovation economy.",
    "location": "London",
    "categories": [
      "Advice",
      "Business Development",
      "Financial Services"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-232",
    "name": "Magna Mining",
    "website": "https://magnamining.com/",
    "linkedin": "https://ca.linkedin.com/company/magnamining",
    "email": "",
    "founders": "",
    "description": "Magna Mining is a nickel exploration and development company that aims to develop and build the Shakespeare mine and mill.",
    "location": "Sudbury",
    "categories": [
      "Mineral",
      "Mining",
      "Precious Metals"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-233",
    "name": "Satellos",
    "website": "https://satellos.com/",
    "linkedin": "https://www.linkedin.com/company/satellos-bio/",
    "email": "info@icotherapeutics.com",
    "founders": "",
    "description": "Satellos specializes in the research and development of drug delivery technologies.",
    "location": "Vancouver",
    "categories": [
      "Biotechnology",
      "Health Care",
      "Pharmaceutical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-234",
    "name": "Ionada",
    "website": "http://ionada.com/",
    "linkedin": "https://www.linkedin.com/company/ionada",
    "email": "info@ionada.com",
    "founders": "",
    "description": "Ionada is a global climate technology company committed to reducing greenhouse gas emissions and creating a sustainable future.",
    "location": "Calgary",
    "categories": [
      "Carbon Capture",
      "Manufacturing",
      "Oil and Gas"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-235",
    "name": "Global Fleet Management",
    "website": "http://www.positrace.com",
    "linkedin": "https://www.linkedin.com/company/global-fleet-management/",
    "email": "investor.relations@positrace.com",
    "founders": "",
    "description": "Global Fleet Management is a provider of real-time GPS Fleet Management platform PosiTrace.",
    "location": "Burnaby",
    "categories": [
      "Big Data",
      "Business Intelligence",
      "Fleet Management"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-236",
    "name": "ChessGold",
    "website": "https://www.chessgold.app/",
    "linkedin": "",
    "email": "info@chessgold.app",
    "founders": "",
    "description": "ChessGold is a Canadian-based company that is excited to share its app with the world.",
    "location": "Toronto",
    "categories": [
      "Apps",
      "Online Games",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-237",
    "name": "Habitat",
    "website": "https://en.habitat-nature.com/notre-histoire",
    "linkedin": "https://www.linkedin.com/company/habitatnaturemtl",
    "email": "info@habitat-nature.com",
    "founders": "",
    "description": "Habitat offers environmental services by delivering nature-based land-use solutions to create balanced and healthy ecosystems.",
    "location": "Montr\u00e9al",
    "categories": [
      "Environmental Consulting",
      "Sustainability"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-238",
    "name": "Lucid Vision Labs",
    "website": "https://thinklucid.com/",
    "linkedin": "https://www.linkedin.com/company/lucid-vision-labs/",
    "email": "support@thinklucid.com",
    "founders": "",
    "description": "LUCID Vision Labs designs and manufactures innovative machine vision cameras and components that utilize the latest technologies.",
    "location": "Richmond",
    "categories": [
      "Electronics",
      "Machinery Manufacturing",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-239",
    "name": "Centre For Ocean Applied Sustainable Technologies",
    "website": "http://www.canadacoast.ca",
    "linkedin": "https://www.linkedin.com/company/canadacoast",
    "email": "",
    "founders": "",
    "description": "Coast brings together individuals, concepts, organizations, and communities to establish an innovation hub where concepts are developed.",
    "location": "Victoria",
    "categories": [
      "Clean Energy",
      "Sustainability"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-240",
    "name": "St Joseph S Healthcare Hamilton",
    "website": "https://www.stjoes.ca/",
    "linkedin": "https://www.linkedin.com/company/st--joseph%27s-healthcare-hamilton/?trk=biz-companies-cym",
    "email": "",
    "founders": "",
    "description": "St. Joseph's Healthcare Hamilton is a research and educational health science center that provides all types of health services.",
    "location": "Hamilton",
    "categories": [
      "Health Care",
      "Health Diagnostics",
      "Hospital"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-241",
    "name": "Safehaven",
    "website": "https://safehaven.to",
    "linkedin": "https://www.linkedin.com/company/safehaven",
    "email": "info@safehaven.to",
    "founders": "",
    "description": "Safehaven is a non-profit organisation that offers residential and transitional care to children with medical issues and disabilities.",
    "location": "Toronto",
    "categories": [
      "Child Care",
      "Non Profit",
      "Personal Health"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-242",
    "name": "WERD Studios",
    "website": "https://www.werd.xyz/",
    "linkedin": "https://www.linkedin.com/company/werd-studios/",
    "email": "",
    "founders": "[object Object]",
    "description": "WERD Studios is a full-service online gaming studio specializing in blockchain and Web3.",
    "location": "Toronto",
    "categories": [
      "Blockchain",
      "Online Games",
      "Web3"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-243",
    "name": "Resaas",
    "website": "http://www.resaas.com",
    "linkedin": "http://www.linkedin.com/company/2249641",
    "email": "info@resaas.com",
    "founders": "",
    "description": "The World's Largest Real Estate Technology Platform",
    "location": "Vancouver",
    "categories": [
      "Enterprise Software",
      "PropTech",
      "Real Estate"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-244",
    "name": "Cronometer Com",
    "website": "https://cronometer.com",
    "linkedin": "https://www.linkedin.com/company/cronometer/",
    "email": "support@cronometer.com",
    "founders": "",
    "description": "Bootstrapped Startup for Detailed Personal Nutrition & Fitness Tracking",
    "location": "Revelstoke",
    "categories": [
      "Fitness",
      "Health Care",
      "Software"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-245",
    "name": "Modulari-T Biosciences",
    "website": "https://modularit.bio/",
    "linkedin": "https://www.linkedin.com/company/modulari-t-bio",
    "email": "info@modularit.bio",
    "founders": "",
    "description": "Modulari-T Biosciences develops novel antigen receptor architecture and cell therapies.",
    "location": "Montr\u00e9al",
    "categories": [
      "Biotechnology",
      "Genetics",
      "Life Science"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-246",
    "name": "Discovery Garden",
    "website": "https://www.discoverygarden.com",
    "linkedin": "https://www.linkedin.com/company/discoverygarden-inc",
    "email": "info@discoverygarden.com",
    "founders": "",
    "description": "Discovery Garden specializes in designing and operating institutional repositories and digital collections for libraries, galleries.",
    "location": "Charlottetown",
    "categories": [
      "Information Technology",
      "Internet",
      "Service Industry"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-247",
    "name": "Bidaya",
    "website": "https://www.bidaya.ai",
    "linkedin": "https://www.linkedin.com/company/bidaya-ai",
    "email": "",
    "founders": "",
    "description": "Bidaya is an AI platform that offers discovery, analysis, and proposal writing features for winning government contracts.",
    "location": "Calgary",
    "categories": [
      "Artificial Intelligence (AI)",
      "Software",
      "Web Development"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-248",
    "name": "Remsoft",
    "website": "http://www.remsoft.com",
    "linkedin": "https://www.linkedin.com/company/remsoft-inc.",
    "email": "",
    "founders": "",
    "description": "Integrated Business Planning Software",
    "location": "Fredericton",
    "categories": [
      "Analytics",
      "Career Planning",
      "Software"
    ],
    "funding": " - "
  },
  {
    "id": "cdn-249",
    "name": "Resili\u014d Climate Solutions",
    "website": "https://resiliocs.com/",
    "linkedin": "https://www.linkedin.com/company/resiliocs/",
    "email": "info@resiliocs.com",
    "founders": "",
    "description": "Resili\u014d Climate Solutions is a Climate Data and Analytics firm offering insights on climate for risk management and loss predictions.",
    "location": "Hamilton",
    "categories": [
      "Banking",
      "Commercial Real Estate",
      "FinTech"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-250",
    "name": "Canadian Association Of Science Centres",
    "website": "https://www.canadiansciencecentres.ca",
    "linkedin": "https://www.linkedin.com/company/canadian-association-of-science-centres",
    "email": "",
    "founders": "",
    "description": "Canadian Association Of Science Centres is a information technology company located in Sudbury.",
    "location": "Sudbury",
    "categories": [
      "Education",
      "Information Services",
      "Information Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-251",
    "name": "Southern Cross Gold",
    "website": "https://www.southerncrossgold.com/",
    "linkedin": "https://www.linkedin.com/company/southern-cross-gold/",
    "email": "",
    "founders": "",
    "description": "Southern Cross Gold is a mining and exploration company that specializes in gold exploration and minerals.",
    "location": "Vancouver",
    "categories": [
      "Mineral",
      "Mining",
      "Mining Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-252",
    "name": "Aimia",
    "website": "http://aimia.com",
    "linkedin": "https://www.linkedin.com/company/2353423",
    "email": "info@aimia.com",
    "founders": "",
    "description": "Aimia is a holding company focusing on long-term investments in both public and private companies.",
    "location": "Montr\u00e9al-est",
    "categories": [
      "Analytics",
      "Enterprise Software",
      "Loyalty Programs"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-253",
    "name": "Bioindustrial Innovation Canada",
    "website": "https://www.bincanada.ca",
    "linkedin": "https://www.linkedin.com/company/bioindustrial-innovation-canada/",
    "email": "",
    "founders": "",
    "description": "Bioindustrial Innovation Canada is a Canadian research network aims to position the Sarnia-Lambton region as a hybrid chemistry cluster.",
    "location": "Sarnia",
    "categories": [
      "Agriculture",
      "Association",
      "Biotechnology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-254",
    "name": "Rakovina Therapeutics",
    "website": "https://www.rakovinatherapeutics.com",
    "linkedin": "https://www.linkedin.com/company/rakovina-therapeutics-inc/",
    "email": "",
    "founders": "",
    "description": "Publicly traded (RKV.V) company focused on the development of new cancer treatments based on novel DNA-damage response technologies.",
    "location": "Vancouver",
    "categories": [
      "Biotechnology",
      "Life Science",
      "Oncology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-255",
    "name": "ArcticNet",
    "website": "https://arcticnet.ulaval.ca/",
    "linkedin": "https://www.linkedin.com/company/arcticnet/",
    "email": "arcticnet@arcticnet.ulaval.ca",
    "founders": "",
    "description": "ArcticNet is a research service firm that includes Arctic researchers studying human health, and natural and social sciences in the Arctic.",
    "location": "Laval",
    "categories": [
      "Consulting",
      "Consumer Research",
      "Management Consulting"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-256",
    "name": "Foresight Canada",
    "website": "https://foresightcac.com/",
    "linkedin": "https://www.linkedin.com/company/foresightcac/",
    "email": "info@foresightcac.com",
    "founders": "",
    "description": "Foresight Canada is a cleantech accelerator that brings innovators, industry, investors, government, and academia together.",
    "location": "Port Coquitlam",
    "categories": [
      "Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-257",
    "name": "Alice Smith 85Cf",
    "website": "https://www.aliceandsmith.com/",
    "linkedin": "https://www.linkedin.com/company/alice-&-smith/?originalSubdomain=ca",
    "email": "hello@aliceandsmith.com",
    "founders": "",
    "description": "Alice & Smith is a middleware technology developer for Microsoft in the fields of Media & Entertainment, Azure Cloud, and AI.",
    "location": "Montr\u00e9al",
    "categories": [
      "Apps",
      "Cloud Infrastructure",
      "Gaming"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-258",
    "name": "Minerva Intelligence Inc",
    "website": "https://minervaintelligence.com",
    "linkedin": "https://ca.linkedin.com/company/minerva-intelligence-inc",
    "email": "info@minervaintelligence.com",
    "founders": "",
    "description": "Knowledge Engineering, Artificial Intelligence, SaaS, Semantics, Ontology, Taxonomy, INSPIRE, Explainable AI, Reasoning under uncertainty",
    "location": "Vancouver",
    "categories": [
      "Artificial Intelligence (AI)",
      "Geospatial",
      "Information Technology"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-259",
    "name": "Tactiql",
    "website": "https://www.tactiql.com/",
    "linkedin": "https://www.linkedin.com/company/tactiql/",
    "email": "",
    "founders": "",
    "description": "Tactiql is a veteran-founded firm that prioritizes talent and is focused on rapid commercialization.",
    "location": "Ottawa",
    "categories": [
      "Software"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-260",
    "name": "Draft Goal",
    "website": "https://dng.ai",
    "linkedin": "https://www.linkedin.com/company/draft-goal",
    "email": "info@dng.ai",
    "founders": "",
    "description": "Draft&Goal automates content creation at scale with its AI-powered no-code platform leveraging Ai agentic workflow automation.",
    "location": "Montr\u00e9al",
    "categories": [
      "Artificial Intelligence (AI)",
      "Information Technology",
      "Software"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-261",
    "name": "ECN Capital",
    "website": "http://www.ecncapitalcorp.com/",
    "linkedin": "https://www.linkedin.com/company/ecn-capital/",
    "email": "jwimsatt@ecncapitalcorp.com",
    "founders": "[object Object]",
    "description": "ECN Capital specializes in social trading and provides the best services in this area using SIRIX platform.",
    "location": "Toronto",
    "categories": [
      "Advice",
      "Credit",
      "Financial Services"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-262",
    "name": "Le Pignon Bleu",
    "website": "http://www.pignonbleu.org/",
    "linkedin": "https://www.linkedin.com/company/le-pignon-bleu",
    "email": "com@pignonbleu.org",
    "founders": "",
    "description": "Le Pignon Bleu is a non-profit organization that promotes food security for children and families",
    "location": "Qu\u00e9bec",
    "categories": [
      "Charity",
      "Food and Beverage",
      "Non Profit"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-263",
    "name": "Human Development Council Fd88",
    "website": "https://sjhdc.ca",
    "linkedin": "https://www.linkedin.com/company/sjhdc",
    "email": "info@sjhdc.ca",
    "founders": "",
    "description": "Human Development Council identifies and tackles societal concerns through research, collaboration, and networking.",
    "location": "Saint John",
    "categories": [
      "Business Development",
      "Business Intelligence",
      "Software"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-264",
    "name": "Animal Health Canada",
    "website": "https://animalhealthcanada.ca/",
    "linkedin": "https://www.linkedin.com/company/animalhealthcanada/",
    "email": "info@animalhealthcanada.ca",
    "founders": "",
    "description": "Animal Health leads in developing a collaborative, multi-partner model that clarifies the respective roles, duties, and liability.",
    "location": "Elora",
    "categories": [
      "Farming",
      "Health Care",
      "Non Profit"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-265",
    "name": "Exonetik",
    "website": "https://www.exonetik.com",
    "linkedin": "https://www.linkedin.com/company/exonetik-inc-",
    "email": "info@exonetik.com",
    "founders": "",
    "description": "Exonetik is a company that designs and manufactures magnetorheological actuators for automotive, robotics and aerospace applications.",
    "location": "Sherbrooke",
    "categories": [
      "Manufacturing",
      "Product Design",
      "Product Research"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-266",
    "name": "STEM Animal Health",
    "website": "https://www.stem-animal-health.com",
    "linkedin": "",
    "email": "",
    "founders": "",
    "description": "STEM Animal Health is a veterinary health company that focuses on treating biofilm-related ailments in animals.",
    "location": "Winnipeg",
    "categories": [
      "Health Care",
      "Pet",
      "Veterinary"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-267",
    "name": "Powertrust",
    "website": "https://www.powertrust.com",
    "linkedin": "https://www.linkedin.com/company/positive-capital-partners",
    "email": "nick@powertrust.com",
    "founders": "",
    "description": "Powertrust is the preferred platform for buying renewable electricity in Asia, Latam, and Africa",
    "location": "Vancouver",
    "categories": [
      "Consulting",
      "Energy",
      "Renewable Energy"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-268",
    "name": "Secret City",
    "website": "https://www.secretcityadventures.com",
    "linkedin": "https://www.linkedin.com/company/secret-city/",
    "email": "team@secretcityadventures.com",
    "founders": "",
    "description": "Secret City is a creative agency that specializes in games and experiences.",
    "location": "Toronto",
    "categories": [
      "Creative Agency",
      "Events",
      "Gaming"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-269",
    "name": "Ayro",
    "website": "https://ayro.vc",
    "linkedin": "https://www.linkedin.com/company/ayro1",
    "email": "info@ayro.vc",
    "founders": "",
    "description": "Ayro is a next-generation startup incubator helping you develop and scale your company.",
    "location": "Calgary",
    "categories": [
      "Artificial Intelligence (AI)",
      "Consulting",
      "Financial Services"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-270",
    "name": "Port of Saint John",
    "website": "https://www.sjport.com",
    "linkedin": "https://www.linkedin.com/company/saint-john-port-authority",
    "email": "",
    "founders": "",
    "description": "Port of Saint John is a major transportation infrastructure with a cornerstone goal to proactively manage, in a sustainable manner.",
    "location": "Saint John",
    "categories": [
      "Transportation"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-271",
    "name": "VentureLabs",
    "website": "https://venturelabs.ca",
    "linkedin": "https://www.linkedin.com/company/venturelabs",
    "email": "",
    "founders": "",
    "description": "VentureLabs is a tech accelerator, dedicated to helping technology-based startups scale through mentoring and tailored resources.",
    "location": "Vancouver",
    "categories": [
      "Business Development",
      "Education",
      "Training"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-272",
    "name": "Namakor Holdings",
    "website": "http://namakorholdings.com/",
    "linkedin": "https://www.linkedin.com/company/nama-holdings",
    "email": "info@namakor.com",
    "founders": "",
    "description": "Namakor Holdings is focused on acquiring mid-market companies in the industrial manufacturing sector.",
    "location": "Montr\u00e9al",
    "categories": [
      "Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-273",
    "name": "ParticipACTION",
    "website": "https://www.participaction.com",
    "linkedin": "https://www.linkedin.com/company/participaction",
    "email": "info@participaction.com",
    "founders": "",
    "description": "ParticipACTION is an application that tracks physical activities.",
    "location": "Toronto",
    "categories": [
      "Apps",
      "E-Commerce",
      "Non Profit"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-274",
    "name": "Nergica",
    "website": "https://nergica.com/en/",
    "linkedin": "https://www.linkedin.com/company/nergica/",
    "email": "info@nergica.com",
    "founders": "",
    "description": "Nergica is a centre of applied research that stimulates innovation in the renewable energy industry through research and tech assistance.",
    "location": "Quebec",
    "categories": [
      "Recycling",
      "Renewable Energy",
      "Sustainability"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-275",
    "name": "Norcat",
    "website": "http://www.norcat.org",
    "linkedin": "http://www.linkedin.com/company/norcat",
    "email": "support@norcattraining.com",
    "founders": "",
    "description": "Norcat is a non-profit organization providing health and safety training and short-term event space for companies to enhance their growth.",
    "location": "Toronto",
    "categories": [
      "Consulting",
      "Non Profit",
      "Training"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-276",
    "name": "StockPick",
    "website": "https://www.stockpick.app",
    "linkedin": "https://www.linkedin.com/company/stocpick-technologies",
    "email": "info@stockpick.app",
    "founders": "",
    "description": "StockPick is a video-sharing app and social network for investors.",
    "location": "Oakville",
    "categories": [
      "Financial Services",
      "FinTech",
      "Information Services"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-277",
    "name": "BCE",
    "website": "http://www.bce.ca",
    "linkedin": "http://www.linkedin.com/company/bell",
    "email": "mobility@bell.ca",
    "founders": "",
    "description": "BCE is a communications company that provides a comprehensive suite of broadband communications and content.",
    "location": "Toronto",
    "categories": [
      "Internet",
      "Mobile",
      "Telecommunications"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-278",
    "name": "Our mission at Pegasus Biotech",
    "website": "http://pegasusbio.com",
    "linkedin": "https://www.linkedin.com/company/pegasus-biotech/",
    "email": "info@pegasusbio.com",
    "founders": "",
    "description": "Our mission at Pegasus Biotech is to work with our clients to bring cutting edge innovation to the global human and animal health markets.",
    "location": "Charlottetown",
    "categories": [
      "Biopharma",
      "Biotechnology",
      "Health Care"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-279",
    "name": "Homes For Heroes Foundation",
    "website": "https://homesforheroesfoundation.ca/",
    "linkedin": "https://www.linkedin.com/company/home-for-heroes-foundation-canada/",
    "email": "",
    "founders": "",
    "description": "Homes For Heroes Foundation Building tiny home villages, with wrap around support services to end the issue of Veteran homelessness.",
    "location": "Calgary",
    "categories": [
      "Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-280",
    "name": "Vertical SaaS that",
    "website": "https://www.electrifyconnect.com/",
    "linkedin": "https://www.linkedin.com/company/electrify-connect/",
    "email": "support@electrifyconnect.com",
    "founders": "",
    "description": "Vertical SaaS that provides lighting manufacturers with the rails to digitize and scale.",
    "location": "Toronto",
    "categories": [
      "SaaS",
      "Software",
      "Software Engineering"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-281",
    "name": "Go Fleet",
    "website": "http://www.gofleet.com",
    "linkedin": "http://www.linkedin.com/company/gofleet",
    "email": "sales@gofleet.com",
    "founders": "",
    "description": "Industry leading fleet management solution.",
    "location": "Mississauga",
    "categories": [
      "Information Technology",
      "Management Consulting",
      "Service Industry"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-282",
    "name": "Fsd Pharma",
    "website": "http://fsdpharma.com/",
    "linkedin": "https://www.linkedin.com/company/fsd-pharma-ltd",
    "email": "info@fsdpharma.com",
    "founders": "",
    "description": "Quantum Biopharma's management\u2019s mission is to transform the facility into the largest hydroponic indoor cannabis facility.",
    "location": "Cobourg",
    "categories": [
      "Biotechnology",
      "Manufacturing",
      "Pharmaceutical"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-283",
    "name": "Argo",
    "website": "https://www.rideargo.com",
    "linkedin": "https://www.linkedin.com/company/rideargo/",
    "email": "support@rideargo.com",
    "founders": "",
    "description": "Argo is a mobility technology company that provides electric transit solutions for cities and schools.",
    "location": "Toronto",
    "categories": [
      "SaaS",
      "Software",
      "Transportation"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-284",
    "name": "AGE-WELL",
    "website": "https://agewell-nce.ca/",
    "linkedin": "https://www.linkedin.com/company/agewellnce",
    "email": "info@agewell-nce.ca",
    "founders": "",
    "description": "AGE-WELL is a Canadian network that brings everyone together to develop technologies and services for healthy aging.",
    "location": "Toronto",
    "categories": [
      "Health Care",
      "Non Profit",
      "Wellness"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-285",
    "name": "Mineworx Technologies",
    "website": "https://www.regenx.tech",
    "linkedin": "https://www.linkedin.com/company/regenxtechnologies",
    "email": "",
    "founders": "[object Object]",
    "description": "Regenx Tech manufactures heavy mineral extraction machinery.",
    "location": "North Vancouver",
    "categories": [
      "Machinery Manufacturing",
      "Manufacturing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-286",
    "name": "Grounded People Apparel",
    "website": "https://groundedpeople.com/",
    "linkedin": "https://www.linkedin.com/company/grounded-people-apparel/",
    "email": "",
    "founders": "",
    "description": "Grounded People Apparel is a producer of vegan footwear products.",
    "location": "Vancouver",
    "categories": [
      "Apparel"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-287",
    "name": "C.A.T.",
    "website": "https://cat.ca/",
    "linkedin": "https://www.linkedin.com/company/c-a-t--inc-",
    "email": "",
    "founders": "",
    "description": "C.A.T. is a transportation company.",
    "location": "Pointe-du-lac",
    "categories": [
      "Supply Chain Management",
      "Sustainability",
      "Transportation"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-288",
    "name": "Abivo AI",
    "website": "https://abivo.ai/",
    "linkedin": "https://www.linkedin.com/company/abivo/",
    "email": "info@abivo.ai",
    "founders": "",
    "description": "Abivo AI offers artificial intelligence-based accounts receivable collections staff that can call, text, and email clients.",
    "location": "Toronto",
    "categories": [
      "Artificial Intelligence (AI)",
      "Financial Services",
      "Virtual Workforce"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-289",
    "name": "System-3",
    "website": "https://www.system-3.com/",
    "linkedin": "https://www.linkedin.com/company/system3solution",
    "email": "info@system-3.com",
    "founders": "",
    "description": "System-3 is a SaaS-based predictive Leadership Simulation that minimizes bias, and measures whether experienced and emerging leaders.",
    "location": "Toronto",
    "categories": [
      "Human Resources",
      "Simulation"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-290",
    "name": "Assembly",
    "website": "https://assemblycorp.ca",
    "linkedin": "https://www.linkedin.com/company/assembly-corp",
    "email": "",
    "founders": "",
    "description": "Assembly is a modular wood revolution.",
    "location": "Toronto",
    "categories": [
      "Tech"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-291",
    "name": "Vitalblock",
    "website": "https://vitalblock.org",
    "linkedin": "https://www.linkedin.com/company/vital-block-security/",
    "email": "Info@vitalblock.org",
    "founders": "",
    "description": "Vitalblock is a Defi & Web3 Decentralized Smart Contract Auditing Firm. | Security Research | KYC | Audit Report | NFT Smart Contract Audit.",
    "location": "Vancouver",
    "categories": [
      "Blockchain",
      "Cryptocurrency",
      "Information Technology"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-292",
    "name": "United Way of Winnipeg",
    "website": "https://unitedwaywinnipeg.ca/",
    "linkedin": "https://www.linkedin.com/company/unitedwaywpg/",
    "email": "info@unitedwaywinnipeg.ca",
    "founders": "",
    "description": "United Way of Winnipeg is a nonprofit organization that provides protection for kids & families that offers to build healthier communities.",
    "location": "Winnipeg",
    "categories": [
      "Charity",
      "Non Profit",
      "Wellness"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-293",
    "name": "XTM, Inc.",
    "website": "http://www.xtminc.com/",
    "linkedin": "https://www.linkedin.com/company/xtm-inc/",
    "email": "",
    "founders": "",
    "description": "XTM, Inc. is a digital advertising and marketing agency.",
    "location": "Toronto",
    "categories": [
      "Advertising",
      "Marketing"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-294",
    "name": "Payfi",
    "website": "https://www.payfi.ca",
    "linkedin": "https://www.linkedin.com/company/getpayfi",
    "email": "support@payfi.ca",
    "founders": "",
    "description": "Payfi is a Property Management Marketplace that eliminates misrepresentation, ensuring landlords approve only verified tenants",
    "location": "Toronto",
    "categories": [
      "Payments",
      "PropTech",
      "Real Estate"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-295",
    "name": "Praxis Spinal Cord Institute",
    "website": "https://praxisinstitute.org",
    "linkedin": "https://www.linkedin.com/company/praxis-sci",
    "email": "info@praxisinstitute.org",
    "founders": "",
    "description": "Praxis Spinal Cord Institute is\u00a0a spinal cord injury research care.",
    "location": "Vancouver",
    "categories": [
      "Health Care",
      "Hospitality",
      "Medical Device"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-296",
    "name": "CMAW Canada",
    "website": "https://cmaw.ca/",
    "linkedin": "https://www.linkedin.com/company/cmaw---construction-maintenance-and-allied-workers/",
    "email": "info@cmaw.ca",
    "founders": "",
    "description": "CMAW Canada is a nonprofit association of construction workers that fights for fair compensation and safe work environments for labours.",
    "location": "Burnaby",
    "categories": [
      "Association",
      "Construction",
      "Non Profit"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-297",
    "name": "Savio",
    "website": "https://www.savio.io/",
    "linkedin": "https://www.linkedin.com/company/savio-io/",
    "email": "",
    "founders": "",
    "description": "Savio is a Product Management Platform where SaaS teams centralize customer feedback and create evidence-based roadmaps.",
    "location": "Halifax",
    "categories": [
      "B2B",
      "Information Technology",
      "Internet"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-298",
    "name": "Investipal",
    "website": "https://www.investipal.co",
    "linkedin": "",
    "email": "info@investipal.co",
    "founders": "",
    "description": "Augmenting the modern wealth manager to onboard faster and build personalized portfolios at scale",
    "location": "Toronto",
    "categories": [
      "Financial Services",
      "FinTech"
    ],
    "funding": "K"
  },
  {
    "id": "cdn-299",
    "name": "CMC Microsystems",
    "website": "https://www.cmc.ca/",
    "linkedin": "https://www.linkedin.com/company/cmc-microsystems/",
    "email": "info@cmc.ca",
    "founders": "",
    "description": "CMC Microsystems is a not-for-profit organization managing Canada\u2019s National Design Network.",
    "location": "Kingston",
    "categories": [
      "Embedded Software",
      "Nanotechnology",
      "Non Profit"
    ],
    "funding": "M"
  },
  {
    "id": "cdn-300",
    "name": "Seneca",
    "website": "http://www.seneca.ca",
    "linkedin": "https://www.linkedin.com/company/seneca-experts-conseils/",
    "email": "",
    "founders": "",
    "description": "Seneca offers professional services for investment projects and the introduction of new technologies in transformation processes.",
    "location": "Anjou",
    "categories": [
      "Construction",
      "Industrial",
      "Industrial Engineering"
    ],
    "funding": "M"
  }
];
