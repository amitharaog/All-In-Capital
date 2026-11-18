<thesis>
{
 "version": "2026-11-18.v3",
 "note": "Two lenses. 'stated' = what All In Capital says publicly (see data/fund/public_thesis.json for sources). 'revealed' = what the fund's own 12 deal memos and partner notes show it actually rewards. Kushal: 'tell me which one you used and why' -> every verdict shows both, recommendation is driven by 'revealed', and any disagreement between lenses is printed.",
 "scale": "Each criterion 0-5. Weighted to 0-10 per lens. A criterion with no evidence is scored as missing_value (it drags the score, it is never skipped) and lowers coverage.",
 "missing_value": 1.0,
 "pedigree_cap": 2.0,
 "pedigree_rule": "Credentials alone (IIT, PhD, ex-FAANG, ex-founder) cannot lift any criterion above pedigree_cap. Score the evidence, not the pedigree. (Partner notes, Meeting 3: 'credentials are not a business'.)",
 "lenses": {
  "revealed": {
   "description": "Reconstructed from the 12 deal memos (6 invested, 6 passed) and 5 partner meetings. Founder behaviour is scored separately from path to market, as agreed in Meeting 3.",
   "criteria": [
    {
     "id": "R1",
     "name": "Founders own the defining risk",
     "weight": 25,
     "definition": "Every business has one risk that kills it: credit/default for a lender, the regulator for drones/aviation/crypto, repeat rate for a brand, profitability-at-density for ops-heavy models. Score whether the founders treat that risk as theirs to manage, with a plan, rather than someone else's problem.",
     "high": "Names the risk unprompted and shows what they are doing about it (credit-risk hire plan, regulator milestone sequence, cohort data, contribution-margin path).",
     "low": "Delegates the risk ('the NBFC handles defaults', 'solved once the tech works', 'rules will get friendlier', 'needs a big raise to reach density').",
     "precedents": [
      "Jai Kisan (invested) vs CampusCredit (passed)",
      "ePlane (invested) vs AeroDrop (passed)",
      "Coinlane (passed)",
      "HopBox (passed)"
     ],
     "intake_observability": "partial - decks rarely show it; form answers about risks/'what would make you quit' do. Full test is on the call."
    },
    {
     "id": "R2",
     "name": "Went to the customer first",
     "weight": 20,
     "definition": "Evidence the founders did unscalable, on-the-ground work with real customers before building or scaling: manual operations, field visits, hand-run transactions, pilots treated as learning.",
     "high": "Specific customer sites, named pilots, store/farm/user visits, what broke and what they changed.",
     "low": "Product built around an assumption; traction is downloads/followers; no customer conversations described.",
     "precedents": [
      "Wint Wealth (invested)",
      "SuperK (invested)",
      "Jai Kisan (invested)",
      "Unbox Robotics (invested)"
     ],
     "intake_observability": "good - decks and forms usually describe how the first customers were found."
    },
    {
     "id": "R3",
     "name": "Earned traction on the metric that matters",
     "weight": 20,
     "definition": "Traction measured on the sector's deciding metric (see sector_key_metrics), and earned rather than bought. A missing deciding metric is scored as missing_value.",
     "high": "Cohort repeat / retention / default data / live-site pilot results given with numbers; growth not mostly paid.",
     "low": "Vanity metrics only (downloads, followers, GMV with no margin); growth mostly paid; deciding metric absent.",
     "precedents": [
      "Giva (invested)",
      "Petalry (passed)",
      "Prepnest (passed)"
     ],
     "intake_observability": "good - either the number is in the application or it is not."
    },
    {
     "id": "R4",
     "name": "Credible path to market",
     "weight": 15,
     "definition": "Who pays, how the product reaches them, and what stands in the way (regulation, liability, procurement cycles) - with a concrete sequence. Scored separately from founder quality.",
     "high": "Paying or signed customer, regulator-facing plan with milestones, liability addressed, channel proven.",
     "low": "No paying customer identified; regulatory path absent; market size asserted rather than evidenced.",
     "precedents": [
      "Unbox Robotics (invested)",
      "AeroDrop (passed)",
      "ePlane (invested despite long path, because the sequence was clear)"
     ],
     "intake_observability": "good"
    },
    {
     "id": "R5",
     "name": "Works on a pre-seed cheque",
     "weight": 10,
     "definition": "Can the company reach its next proof point with the capital a pre-seed fund deploys, without becoming the small cheque that gets diluted or squeezed when larger funds set terms?",
     "high": "Capital-efficient, milestones reachable with the ask; or long-duration but cheque sized to survive a slow path.",
     "low": "Only works at density/scale that needs far more capital than the fund deploys; negative contribution margin with no niche.",
     "precedents": [
      "HopBox (passed)",
      "ePlane (invested, cheque sized for slow path)"
     ],
     "intake_observability": "good"
    },
    {
     "id": "R6",
     "name": "Travels beyond the founder",
     "weight": 10,
     "definition": "Is there something that keeps working and gets harder to copy as it scales (field execution, network, data, distribution), or is the product the founder's personal talent/audience?",
     "high": "Defensibility the founder can articulate and examine; process or network that does not depend on one person.",
     "low": "Product is the founder (one teacher, one influencer); defensive when asked about copycats.",
     "precedents": [
      "Prepnest (passed)",
      "SuperK (invested: field execution hard to copy)"
     ],
     "intake_observability": "partial"
    }
   ]
  },
  "stated": {
   "description": "What All In Capital says publicly (fund site, apply page, Fund II launch coverage, Kushal Bhagia's interviews and posts). Every criterion cites its sources; full quotes in data/fund/public_thesis.json.",
   "criteria": [
    {
     "id": "S1",
     "name": "In a focus sector",
     "weight": 20,
     "definition": "Fund II is sector-agnostic with special focus on consumer tech, deeptech, fintech and consumer brands; intended mix ~50% consumer, ~30% Indian AI, ~20% deeptech. Vertical AI (one industry) preferred over horizontal; thin API wrappers seen as weakly defensible.",
     "high": "Squarely in a focus sector, or vertical AI with a real industry problem.",
     "low": "Outside the focus sectors with no AI/consumer/deeptech angle, or a thin wrapper.",
     "sources": [
      "https://entrackr.com/snippets/all-in-capital-launches-fund-ii-with-tar",
      "https://www.business-standard.com/amp/companies/start-ups/all-in-capit",
      "https://inc42.com/features/inside-all-in-capitals-inr-300-cr-bet-on-in"
     ]
    },
    {
     "id": "S2",
     "name": "Stage and round the fund can lead",
     "weight": 20,
     "definition": "Paper-plan through MVP to early paying customers; first cheque USD 200-600K (INR 3-5 Cr in Fund II), leading or co-leading rounds up to roughly INR 6 Cr, usually on a convertible note. Not a fit for revenue-generating companies where large VCs compete.",
     "high": "First institutional round the fund can lead at its cheque size.",
     "low": "Series A / large round, or already institutionally funded with big VCs competing.",
     "sources": [
      "https://allincapital.vc/",
      "https://allincapital.vc/apply_now",
      "https://x.com/kushalbhagia/status/1902586495778902475",
      "https://inc42.com/features/inside-all-in-capitals-inr-300-cr-bet-on-in"
     ]
    },
    {
     "id": "S3",
     "name": "Founder-market fit and earned secrets",
     "weight": 35,
     "definition": "The core public lens: what the founders know and can or cannot do for this opportunity; the key skills needed and the key risk; 'earned secrets'; proven ability to build (shipped product, handled scale); loving the problem enough to stay 5-6 years; long shared history between co-founders.",
     "high": "Founders with demonstrated, specific knowledge of this problem and a record of building; complementary team with history.",
     "low": "No evidence of insight or ability to build specific to this problem.",
     "sources": [
      "https://inc42.com/features/kushal-baghia-all-in-capital-founder-market",
      "https://x.com/kushalbhagia/status/1902586495778902475"
     ]
    },
    {
     "id": "S4",
     "name": "Non-obvious, ambitious opportunity",
     "weight": 25,
     "definition": "Backs non-obvious founders and non-consensus ideas, a vision that inspires, ambition beyond the first market (global exposure valued); does not follow what is hot.",
     "high": "A non-consensus insight with a large or global ambition.",
     "low": "A me-too in a crowded, hot category; local ambition only.",
     "sources": [
      "https://inc42.com/features/inside-all-in-capitals-inr-300-cr-bet-on-in",
      "https://x.com/kushalbhagia/status/1902586495778902475"
     ]
    }
   ]
  }
 },
 "sector_key_metrics": {
  "consumer_brand": [
   "cohort repeat rate",
   "gross margin",
   "CAC by channel",
   "share of orders from paid",
   "return rate"
  ],
  "consumer_tech": [
   "30/90-day retention",
   "conversion to paid",
   "contribution margin per order/user",
   "organic vs paid acquisition"
  ],
  "fintech": [
   "who holds credit/default risk",
   "default/NPA data or plan",
   "regulatory licence path",
   "trust/repeat usage"
  ],
  "deeptech": [
   "milestone sequence to commercial use",
   "signed pilot or LOI",
   "regulatory/certification path",
   "liability and insurance"
  ],
  "other": [
   "the metric the founder says proves demand"
  ]
 },
 "gates": [
  {
   "id": "G1",
   "name": "Portfolio conflict",
   "rule": "Overlaps an existing portfolio company (same customer + same job). Checked against the full portfolio list, not memory. Default is no; a false alarm is preferred to a miss (Meeting 4).",
   "effect": "HOLD_CONFLICT - Kushal speaks to the portfolio founder before anything else."
  },
  {
   "id": "G2",
   "name": "Exists only if the rules change",
   "rule": "The business depends on a favourable regulatory change to exist (Coinlane). Category decision, not a people decision.",
   "effect": "PASS suggested; Kushal still sees it."
  },
  {
   "id": "G3",
   "name": "Sector label stretch",
   "rule": "Fits a stated sector only by label (rural credit, 'fintech' that is really lending ops). Not a reject: Jai Kisan precedent - founder behaviour mattered more than the label.",
   "effect": "Flag only."
  },
  {
   "id": "G4",
   "name": "Outside mandate",
   "rule": "Round or stage the fund cannot lead at its cheque size: public statements say it leads/co-leads first rounds up to roughly INR 6 Cr with USD 200-600K cheques and is not a fit for revenue-generating companies where large VCs compete (Series A and later).",
   "effect": "PASS suggested on mandate, not on the company; Kushal still sees it.",
   "sources": [
    "https://allincapital.vc/apply_now",
    "https://inc42.com/features/inside-all-in-capitals-inr-300-cr-bet-on-in"
   ]
  }
 ],
 "routing": {
  "take_call": {
   "revealed_min": 6.0,
   "coverage_min": 0.6
  },
  "screen_first": {
   "revealed_min": 4.5
  },
  "note": "Thresholds fixed before running the batch or the backtest. Below screen_first -> PASS with 'what would change our view'. Every outcome goes to Kushal; nothing is auto-advanced or auto-rejected.",
  "deeptech_attendees": [
   "Kushal",
   "Aditya",
   "Riya"
  ],
  "default_attendees": [
   "Kushal",
   "Riya"
  ],
  "pass_requires_founder_evidence": true,
  "rule_history": [
   {
    "version": "v1 (pre-registered, 2026-11-18, before any results)",
    "rule": "PASS whenever revealed < 4.5 or G2 fires."
   },
   {
    "version": "v2 (after backtest, 2026-11-18)",
    "rule": "A score-based PASS also requires R1 (founders own the defining risk) to be evidenced with medium or high confidence; otherwise the application is routed to SCREEN_FIRST. Gate-based passes (G2, G4) are unchanged. Reason: in the blind backtest the only investment marked 'pass' (ePlane) and every investment in the no-founder variant were cases where founder behaviour was not observable. This is the breach response written into the trust contract ('system may not suggest pass' without founder evidence). Thresholds were not retuned."
   }
  ]
 }
}
</thesis>

<portfolio>
[
 {
  "name": "NewMe",
  "aliases": [
   "NEWME",
   "Newme"
  ],
  "sector": "India Consumer",
  "one_line": "Fast Fashion Brand (Shien for India)",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "PierSight",
  "aliases": [
   "PierSight Space",
   "Pier Sight"
  ],
  "sector": "DeepTech,Space",
  "one_line": "Building Synthetic Aperture Radar (SAR) systems tailored to mission specific requirements",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "MeetRecord",
  "aliases": [
   "Meet Record"
  ],
  "sector": "SAAS",
  "one_line": "Meeting intelligence and sales coaching SAAS platform for US SMES",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Broccoli AI",
  "aliases": [
   "Telematica (prior name/pivot)"
  ],
  "sector": "AI / SaaS (not tagged in CSV)",
  "one_line": "AI-native operating system for home service businesses",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Potpie",
  "aliases": [],
  "sector": "AI / Dev Tools (not tagged in CSV)",
  "one_line": "Custom Agents for your codebase in minutes",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Volt",
  "aliases": [
   "Volt Money"
  ],
  "sector": "FinTech",
  "one_line": "Loan against mutual funds / securities consumer app for India. Get low interest secured credit against your equity holdings in a single click",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Vaaree",
  "aliases": [],
  "sector": "India Consumer",
  "one_line": "B2C home / decor products marketplace",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Hotelzify",
  "aliases": [],
  "sector": "Travel,SAAS",
  "one_line": "Shopify for Small hotels",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "SuperSnd",
  "aliases": [
   "SuprSend"
  ],
  "sector": "SAAS",
  "one_line": "Notification Infrastructure for your product. One integration to take all your notification channels live and to build logic on top of them.",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Magma",
  "aliases": [
   "Magma Factory"
  ],
  "sector": "B2B Marketplace",
  "one_line": "B2B Cross Border Marketplace for Ceramics and construction chemicals",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "SuperNova",
  "aliases": [],
  "sector": "EdTech",
  "one_line": "AI Tutor for English",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Sketchnote",
  "aliases": [],
  "sector": "SAAS",
  "one_line": "Building a Startup operating system",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "GloRoots",
  "aliases": [],
  "sector": "SAAS",
  "one_line": "Global Employer of Record Platform - hire employees across the world and Gloroots handles all the headache of payroll for you",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Suite42",
  "aliases": [],
  "sector": "B2B Marketplace",
  "one_line": "On demand manufacturing platform for packaged food products",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Produze",
  "aliases": [],
  "sector": "B2B Marketplace",
  "one_line": "Platform to help Indian brands sell in foreign marketplaces",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Rocketpay",
  "aliases": [
   "RocketPay",
   "UdharPay"
  ],
  "sector": "FinTech",
  "one_line": "P2P Nach mandates for India. Enables any one to deploy a NACH mandate on anyone else (with their consent) to collect money back .",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "EximFiles",
  "aliases": [],
  "sector": "SAAS",
  "one_line": "Generates all the 7- 25 documents a business needs to create to send or receive a shipment anywhere in the world",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "SalesMonk",
  "aliases": [],
  "sector": "SAAS",
  "one_line": "3X Pipeline Generation using AI",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "GigaFun Studios",
  "aliases": [],
  "sector": "Gaming",
  "one_line": "Building Localized Match-3 puzzle games for India,",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Dashwave",
  "aliases": [],
  "sector": "Dev Tools",
  "one_line": "Cloud platform to increase productivity and efficiency of mobile developers and teams.",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "MoMoney",
  "aliases": [],
  "sector": "FinTech",
  "one_line": "Investment App for GenZ India",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Hectar",
  "aliases": [
   "Hectar Global"
  ],
  "sector": "B2B Marketplace",
  "one_line": "B2B cross border marketplace for agri commodities",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Knot",
  "aliases": [],
  "sector": "Social,Consumer Internet",
  "one_line": "Social Media app for teens to share positive feedback with each other",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Mannjal",
  "aliases": [],
  "sector": "FinTech",
  "one_line": "Lending out of the box service for B2B marketplaces",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Nawgati",
  "aliases": [],
  "sector": "SAAS,Climate",
  "one_line": "Complaince and Operations SAAS for Fuelling Stations",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "FanTail",
  "aliases": [],
  "sector": "B2B Marketplace",
  "one_line": "B2B Marketplace for Man made fabrics",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "DressFolk",
  "aliases": [],
  "sector": "India Consumer,D2C",
  "one_line": "Handwoven Ethnic Wear brand for the modern Indian woman",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "DevDham",
  "aliases": [],
  "sector": "India Consumer",
  "one_line": "Platform bringing temples online connecting them to devotees worldwide",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "REint",
  "aliases": [],
  "sector": "SAAS,Climate",
  "one_line": "AI Powered Supply prediction for renewable energy markets",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Segmind",
  "aliases": [],
  "sector": "SAAS,Dev Tools,Generative AI",
  "one_line": "Fastest APIs for Generative AI models",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Arva",
  "aliases": [],
  "sector": "India Consumer,Healthcare",
  "one_line": "Women's Health/Fertility Brand for India focussed on Egg Freezing",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Salty",
  "aliases": [],
  "sector": "D2C,India Consumer",
  "one_line": "Fashion Accessories Brand for Indian GenZ",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Nirmaan",
  "aliases": [],
  "sector": "B2B Marketplace",
  "one_line": "B2B market place for construction materials connecting small brands to retailers",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Karban",
  "aliases": [],
  "sector": "India Consumer,DeepTech",
  "one_line": "Fan+Light+Air Purifier in one Device, AC coming soon!",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Mave Health",
  "aliases": [],
  "sector": "India Consumer,Healthcare",
  "one_line": "Wearable Device + Coaching for treatment of Depression and other Mental Health issues",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Trisu",
  "aliases": [],
  "sector": "India Consumer,D2C",
  "one_line": "Fine Jewellery D2C Brand for India",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Grid",
  "aliases": [],
  "sector": "Manufacturing,B2B Marketplace",
  "one_line": "Original Design Manufacturer Play for IOT products in India",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "FuturElectra",
  "aliases": [],
  "sector": "EV,FinTech",
  "one_line": "EV 2Ws lifecycle management platform",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "BindBee",
  "aliases": [],
  "sector": "SAAS,Dev Tools",
  "one_line": "Unified API for People Data",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Prosparity",
  "aliases": [],
  "sector": "EV,FinTech",
  "one_line": "EV Financing NBFC",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "MagicStudio",
  "aliases": [],
  "sector": "Generative AI,SAAS",
  "one_line": "AI lead Photo Editing App for small businesses",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Everyday",
  "aliases": [],
  "sector": "India Consumer",
  "one_line": "Lab grown diamonds brand for India",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Creatr",
  "aliases": [],
  "sector": "Generative AI,SAAS",
  "one_line": "AI lead Design Tool",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "TractorFactory",
  "aliases": [
   "Tractor Factory"
  ],
  "sector": "India Consumer,AgriTech",
  "one_line": "Omni-channel marketplace for second hand tractors",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Viralme",
  "aliases": [],
  "sector": "B2B Marketplace",
  "one_line": "Sourcing platform for Online Arbitrage Resellers",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "CommandK",
  "aliases": [],
  "sector": "Dev Tools",
  "one_line": "DPDP / GDPR Management SAAS Platform for Tech Companies",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Spiti",
  "aliases": [
   "Spiti.xyz"
  ],
  "sector": "SAAS",
  "one_line": "Private Youtube for Teams to store, curate and watch video content on.",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Suitable",
  "aliases": [
   "Suitable.ai"
  ],
  "sector": "SAAS",
  "one_line": "Employee Referral management SAAS platform",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Piiko",
  "aliases": [],
  "sector": "Healthcare",
  "one_line": "10X Cheaper Blood Testing Machines for India",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Vivahit",
  "aliases": [],
  "sector": "India Consumer",
  "one_line": "App to manage organising weddings and providing a smooth guest experience at a grand indian wedding",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Fijit",
  "aliases": [],
  "sector": "Gaming",
  "one_line": "Hyper Casual play to earn Web3 Meme Games",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Tross",
  "aliases": [],
  "sector": "Healthcare",
  "one_line": "Healthcare technology startup providing enterprise-grade infrastructure and API integrations for electronic health records (EHR) and payer portals",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "SuperLiving",
  "aliases": [
   "Super Living"
  ],
  "sector": "Consumer Tech",
  "one_line": "SuperLiving is Bharat's own lifestyle app uniquely designed for the lifestyle needs of Indian families.",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Taakat",
  "aliases": [],
  "sector": "Consumer Brand",
  "one_line": "Whole Truth for Masses",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Medmitra AI",
  "aliases": [
   "MedMitra"
  ],
  "sector": "SAAS",
  "one_line": "Perplexity for Doctors. AI Decision support tool for doctors, enabling differential diagnosis and prognosis",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Ionic",
  "aliases": [
   "Ionic Professional"
  ],
  "sector": "Consumer Brand",
  "one_line": "Damage reversal professional haircare brand (similar to Olaplex/K18) with a salon-first GTM",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Spill Games",
  "aliases": [],
  "sector": "Consumer Tech",
  "one_line": "Spill Games is game publishing studio that builds casual and hybrid casual games for mobile gamers.",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Krvvy",
  "aliases": [
   "Krrvy"
  ],
  "sector": "Consumer Brand",
  "one_line": "Next-gen innovative intimates, shapewear and lifestyle brand",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "NPrep",
  "aliases": [],
  "sector": "Consumer Tech",
  "one_line": "NPrep is a nursing education platform focused on nursing exam preparation such as NORCET (AIIMS)",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Mixar",
  "aliases": [
   "Mixar3D"
  ],
  "sector": "SAAS",
  "one_line": "A new-age 3D Models builder with text-to-model generation",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Plazza",
  "aliases": [
   "Plazza Club"
  ],
  "sector": "Consumer Tech",
  "one_line": "Quick commerce for medicines",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Cherry",
  "aliases": [],
  "sector": "Consumer Tech",
  "one_line": "Shopping app exclusively for creators",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Returns",
  "aliases": [
   "OptionBase"
  ],
  "sector": "FinTech",
  "one_line": "Options trading made simple.",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "MomsMade",
  "aliases": [],
  "sector": "Consumer Brand",
  "one_line": "Clean label in regional snacks building for Bihari cuisine",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Iztri",
  "aliases": [],
  "sector": "Consumer services (fabric care)",
  "one_line": "Apartment-hub fabric care (ironing, dry cleaning, shoe care) service in Bengaluru",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "CUNIN",
  "aliases": [
   "Cumin (Tracxn spelling)"
  ],
  "sector": "Consumer brand (fragrance/lifestyle)",
  "one_line": "Culture-led fragrance and lifestyle brand",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Mowito",
  "aliases": [],
  "sector": "Deeptech (AI robotics)",
  "one_line": "AI foundation models for industrial robots that learn tasks by observing humans",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Acai Theory",
  "aliases": [
   "A\u00e7a\u00ed Theory",
   "Business Acai Theory"
  ],
  "sector": "Consumer brand (health QSR)",
  "one_line": "Health-focused quick-service restaurant brand (acai bowls, smoothies) in Bengaluru",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "&Done",
  "aliases": [
   "And Done"
  ],
  "sector": "Consumer brand (professional haircare)",
  "one_line": "Professional haircare brand (salon + D2C) for heat-styled/chemically treated hair",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Parsec",
  "aliases": [],
  "sector": "SaaS",
  "one_line": "not found (only described as a SaaS startup)",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "Diagna",
  "aliases": [],
  "sector": "Healthcare AI (per third-party descriptions)",
  "one_line": "not confirmed from a primary source",
  "all_in_capital_fund_investment": true
 },
 {
  "name": "The ePlane Company",
  "aliases": [
   "ePlane",
   "Eplane"
  ],
  "sector": "Deeptech (electric aviation)",
  "one_line": "Building compact electric flying taxis (e200) for passengers and cargo",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Unbox Robotics",
  "aliases": [],
  "sector": "Deeptech (warehouse robotics)",
  "one_line": "Software-defined robotics systems for logistics/warehouse automation",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Wint Wealth",
  "aliases": [
   "GrowFix"
  ],
  "sector": "Fintech (bonds/fixed income)",
  "one_line": "Alternate debt/bond investment platform",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "GIVA",
  "aliases": [
   "Giva"
  ],
  "sector": "Consumer brand (jewellery)",
  "one_line": "Silver/fine jewellery brand for Indian millennials",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "SuperK",
  "aliases": [
   "Super K"
  ],
  "sector": "Consumer retail (kirana chain)",
  "one_line": "Tech-enabled franchised kirana/mini-supermarket chain in Tier 2-3 towns",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Jai Kisan",
  "aliases": [],
  "sector": "Fintech (rural credit)",
  "one_line": "Rural credit and financial products for agri, poultry and dairy value chains",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Rocketlane",
  "aliases": [],
  "sector": "SaaS",
  "one_line": "Customer onboarding/implementation software",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Mailmodo",
  "aliases": [
   "MailModo"
  ],
  "sector": "SaaS (email marketing)",
  "one_line": "Interactive (AMP) email marketing platform",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Fleetx",
  "aliases": [
   "Fleetx.io"
  ],
  "sector": "SaaS (fleet management)",
  "one_line": "AI fleet management SaaS",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Fashinza",
  "aliases": [],
  "sector": "B2B marketplace (fashion supply chain)",
  "one_line": "Managed marketplace for fashion supply chain",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Rigi",
  "aliases": [
   "Plaza / Rigi"
  ],
  "sector": "Creator economy",
  "one_line": "Creator community monetisation platform",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Questbook",
  "aliases": [],
  "sector": "Web3 / edtech",
  "one_line": "Decentralised learning/grants platform",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Anar",
  "aliases": [
   "Anar.biz"
  ],
  "sector": "B2B / SME networking",
  "one_line": "Business networking platform for Indian SMEs",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "BiteSpeed",
  "aliases": [
   "Bitespeed"
  ],
  "sector": "SaaS (eCommerce marketing)",
  "one_line": "Messenger/WhatsApp marketing for Shopify stores",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "RevenueHero",
  "aliases": [
   "Revenue Hero"
  ],
  "sector": "SaaS (sales)",
  "one_line": "Lead routing/meeting scheduling for sales teams",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Masterchow",
  "aliases": [
   "MasterChow"
  ],
  "sector": "Consumer brand (D2C food)",
  "one_line": "D2C Asian food brand",
  "all_in_capital_fund_investment": false
 },
 {
  "name": "Seekho",
  "aliases": [],
  "sector": "Consumer internet (edtech short video)",
  "one_line": "Short-video learning app",
  "all_in_capital_fund_investment": false
 }
]
</portfolio>

<partner_corrections>
No stored partner corrections match this applicant.
</partner_corrections>

<dossier>
{
 "company": "CAPilot",
 "slug": "capilot",
 "one_liner": "AI web app for CA firms that reconciles books against GST portal data and drafts tax-notice replies for the CA to review.",
 "sector": "other",
 "sub_sector": "B2B vertical SaaS / AI for CA firms (GST compliance)",
 "stage": "Pre-seed",
 "ask": "INR 1.5 Cr at INR 10 Cr post-money",
 "business_model": "Seat-based subscription of INR 2,500-6,000 per firm per month plus INR 400 per drafted notice reply above plan limit.",
 "founders": [
  {
   "name": "Dhruv Shah",
   "role": "CEO",
   "background_claimed": "Qualified Chartered Accountant; 4 years in practice handling GST for about 60 clients.",
   "background_verified": null,
   "public_footprint": "not_found",
   "source_ids": [
    "D12",
    "F13",
    "F2"
   ]
  },
  {
   "name": "Isha Merchant",
   "role": "CTO",
   "background_claimed": "3 years at a SaaS company; built the matching engine.",
   "background_verified": null,
   "public_footprint": "not_found",
   "source_ids": [
    "D13",
    "F3"
   ]
  }
 ],
 "claims": [
  {
   "text": "Paying-customer count differs: deck says 31 paying CA firms; form says 24 paying CA firms plus 7 on free trial.",
   "source_ids": [
    "D4",
    "F4"
   ],
   "status": "contradicted",
   "note": "The deck appears to count free-trial firms as paying (24 + 7 = 31)."
  },
  {
   "text": "MRR is INR 78,000 (October); the deck's 'INR 9.4 L annual recurring revenue' is October MRR x 12, not contracted annual revenue.",
   "source_ids": [
    "F5",
    "D5",
    "D7"
   ],
   "status": "founder_stated",
   "note": "MRR ran INR 18k -> 41k -> 78k (Aug-Oct). Fast growth from a small base over three months; the ARR label overstates maturity."
  },
  {
   "text": "Implied average revenue is ~INR 3,250 per paying firm per month (78,000 / 24), inside the stated INR 2,500-6,000 seat-based plan range; extra notice replies are INR 400 each.",
   "source_ids": [
    "F5",
    "F4",
    "D9",
    "D10"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "2 firms have churned (out of ~26 that ever paid).",
   "source_ids": [
    "D6",
    "F4"
   ],
   "status": "founder_stated",
   "note": "Churn base and timing not given; product is ~8 months old."
  },
  {
   "text": "Customer acquisition is mostly founders' network and CA referrals; acquisition cost has not been measured.",
   "source_ids": [
    "F6"
   ],
   "status": "founder_stated",
   "note": "Earned rather than bought, but untested beyond the founders' network."
  },
  {
   "text": "Liability: every drafted reply is reviewed by the CA before filing; responsibility sits with the CA.",
   "source_ids": [
    "F7"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Founders name model errors on unusual notices and dependence on GST portal data formats as key risks.",
   "source_ids": [
    "F8"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Deck claims competitors (Tally/Zoho, ClearTax) do not offer AI notice replies.",
   "source_ids": [
    "D11"
   ],
   "status": "contradicted",
   "note": "Contradicted by the web: GST Reply AI sells AI-drafted GST notice replies (W1). Not a deck-vs-form contradiction but a deck-vs-web one."
  },
  {
   "text": "GST Reply AI offers AI-drafted replies to GST notices from INR 299 per reply, with an INR 999/month unlimited plan for CA firms (per a comment on its launch page).",
   "source_ids": [
    "W1",
    "W2",
    "W3"
   ],
   "status": "verified",
   "note": "Undercuts CAPilot's INR 400 per extra reply and its INR 2,500-6,000 monthly plans on the notice-reply job."
  },
  {
   "text": "Vyapar TaxOne markets AI-driven GST reconciliation for CAs ('automate reconciliations, and identify errors').",
   "source_ids": [
    "W4",
    "W5"
   ],
   "status": "verified",
   "note": "Search snippets (CB Insights, directories) say TaxOne was formerly Suvit, a Surat CA-automation startup; suvit.io URLs now redirect to taxone.vyapar.com (observed during this run). Funding of a well-distributed accounting player into the same job."
  },
  {
   "text": "Third-party GST tools operate as Application Service Providers, connecting to the GST system through GSTN-approved GST Suvidha Providers (GSPs).",
   "source_ids": [
    "W6"
   ],
   "status": "verified",
   "note": "Relevant to the founders' stated dependence on GST portal data; the application does not say whether CAPilot uses a GSP/API route or manual uploads."
  },
  {
   "text": "ICAI data shows roughly 99,000 CA firms (98,967 as of 28 February 2025).",
   "source_ids": [
    "W7"
   ],
   "status": "verified",
   "note": "Bottom-up market: even at 150 firms CAPilot would have ~0.15% of firms. The deck instead sizes the market as 1% of an INR 1.4 lakh Cr services market (D8), which is services revenue, not software spend."
  },
  {
   "text": "Market is sized top-down: 'Even 1% of this market is a INR 1,400 Cr opportunity'.",
   "source_ids": [
    "D8"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Problem claims (staff spend ~40% of time matching GST invoices; each notice reply takes 3-5 hours) are unsourced founder statements.",
   "source_ids": [
    "D2",
    "D3"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Sector mismatch: selected 'Fintech', but the product is AI workflow software for CA firms (tax-compliance SaaS); no money movement or lending. Classified as other (B2B vertical SaaS).",
   "source_ids": [
    "F9",
    "D1"
   ],
   "status": "founder_stated",
   "note": "Relevant to gate G3 / stated-lens S1."
  },
  {
   "text": "Founders: Dhruv Shah (CEO) claims to be a qualified CA with 4 years in practice handling GST for about 60 clients; Isha Merchant (CTO) claims 3 years at a SaaS company and built the matching engine. Full-time since February 2026; no prior startups.",
   "source_ids": [
    "D12",
    "D13",
    "F13",
    "F12"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Founder LinkedIn links are placeholders (*-example) and the website is a .example domain; no independent footprint for founders or company found.",
   "source_ids": [
    "F2",
    "F3",
    "F1"
   ],
   "status": "unverifiable",
   "note": null
  },
  {
   "text": "12-month target: 150 paying firms and INR 7 L MRR (implies ~INR 4,670 per firm, above today's ~INR 3,250).",
   "source_ids": [
    "D14"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Raising INR 1.5 Cr at INR 10 Cr post-money; one angel has invested INR 15 L; no other investors in conversation; 20% of funds for compliance and security.",
   "source_ids": [
    "F10",
    "F11",
    "D15"
   ],
   "status": "founder_stated",
   "note": null
  }
 ],
 "gaps": [
  {
   "what": "Dhruv Shah (CEO): CA qualification and practice history not verified.",
   "why_it_matters": "The CA-in-practice background is the main founder-market-fit claim and the main sales channel (network referrals).",
   "searched": [
    "WebSearch: \"Dhruv Shah\" CAPilot CA Ahmedabad GST (2026-11-18) - no match; generic Ahmedabad CA-service pages",
    "Application LinkedIn link linkedin.com/in/dhruv-shah-example is a placeholder",
    "ICAI member directory not queried"
   ],
   "ask_founder": "What is your ICAI membership number and the name of the practice you worked in?",
   "blocks_criteria": [
    "S3",
    "R2"
   ]
  },
  {
   "what": "Isha Merchant (CTO): no public footprint confirming 3 years at a SaaS company.",
   "why_it_matters": "She built the matching engine and owns model accuracy.",
   "searched": [
    "WebSearch: \"Isha Merchant\" CAPilot CTO Ahmedabad (2026-11-18) - no match",
    "Application LinkedIn link linkedin.com/in/isha-merchant-example is a placeholder"
   ],
   "ask_founder": "Which SaaS company and what did you build there?",
   "blocks_criteria": [
    "S3"
   ]
  },
  {
   "what": "Company existence: no website, product listing or MCA record found for CAPilot Labs Pvt. Ltd.",
   "why_it_matters": "Basic verification.",
   "searched": [
    "WebSearch: CAPilot Labs AI assistant CA firms GST reconciliation notice reply (2026-11-18) - no result for CAPilot; competitors returned",
    "Website www.capilot.example is a placeholder",
    "MCA portal not queried"
   ],
   "ask_founder": "Share CIN and a product demo login.",
   "blocks_criteria": [
    "R4"
   ]
  },
  {
   "what": "Retention and usage: logo and revenue retention by monthly cohort, active seats, replies drafted per firm.",
   "why_it_matters": "For B2B SaaS the deciding metric is retention/conversion; only '2 churned' is given.",
   "searched": [
    "Deck slide 5",
    "Form Customers"
   ],
   "ask_founder": "Of firms that started paying in August, how many still pay and at what MRR? What share of trials convert?",
   "blocks_criteria": [
    "R3"
   ]
  },
  {
   "what": "Accuracy evidence: how often CAs edit or reject drafted replies; reconciliation match accuracy.",
   "why_it_matters": "Model errors are the founders' own top risk and the product's core promise.",
   "searched": [
    "Deck and form - no accuracy data"
   ],
   "ask_founder": "What share of drafted replies are filed with minimal edits, and what is the false-match rate in reconciliation?",
   "blocks_criteria": [
    "R3",
    "R1"
   ]
  },
  {
   "what": "GST data access route: GSP/ASP arrangement, taxpayer consent, and data protection obligations for client tax data.",
   "why_it_matters": "Dependence on GST portal data is a named risk; 20% of the raise goes to compliance and security.",
   "searched": [
    "Web: GSP ecosystem explainer (W6)",
    "Form Key risks"
   ],
   "ask_founder": "Do you pull data via a GSP API or manual uploads, and what security/data-protection certifications do you hold or plan?",
   "blocks_criteria": [
    "R4"
   ]
  },
  {
   "what": "Differentiation versus cheaper AI notice-reply tools and accounting-suite incumbents.",
   "why_it_matters": "Deck says no competitor offers AI notice replies; at least one does at lower prices.",
   "searched": [
    "Web: GST Reply AI (W1-W3), Vyapar TaxOne (W4-W5)"
   ],
   "ask_founder": "Why do firms pay INR 2,500-6,000/month for CAPilot when GST Reply AI offers unlimited replies at INR 999/month?",
   "blocks_criteria": [
    "R6",
    "R4"
   ]
  }
 ],
 "competitors_named": [
  "Tally",
  "Zoho",
  "ClearTax"
 ],
 "competitors_found": [
  "GST Reply AI",
  "Vyapar TaxOne (formerly Suvit)",
  "Tally",
  "Zoho",
  "ClearTax"
 ],
 "keywords": [
  "GST reconciliation",
  "tax notice reply",
  "CA firms",
  "chartered accountants",
  "invoice matching",
  "tax compliance",
  "accounting automation",
  "AI drafting",
  "practice software",
  "GSTR-2B"
 ],
 "founder_contact": null,
 "sources": [
  {
   "id": "D1",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 1 (title)",
   "retrieved_on": null,
   "quote": "AI assistant for CA firms: GST reconciliation and notice replies"
  },
  {
   "id": "D2",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 3 (problem)",
   "retrieved_on": null,
   "quote": "Staff spend about 40% of their time matching GST invoices."
  },
  {
   "id": "D3",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 3 (problem)",
   "retrieved_on": null,
   "quote": "Each tax notice reply takes 3 to 5 hours to draft."
  },
  {
   "id": "D4",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "31 paying CA firms"
  },
  {
   "id": "D5",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "INR 9.4 L annual recurring revenue"
  },
  {
   "id": "D6",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "2 firms churned"
  },
  {
   "id": "D7",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction chart; Aug 18, Sep 41, Oct 78)",
   "retrieved_on": null,
   "quote": "Chart: Monthly recurring revenue (INR thousand)"
  },
  {
   "id": "D8",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 6 (market)",
   "retrieved_on": null,
   "quote": "Even 1% of this market is a INR 1,400 Cr opportunity for CAPilot."
  },
  {
   "id": "D9",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 7 (revenue model)",
   "retrieved_on": null,
   "quote": "INR 2,500 to 6,000 a month per firm, based on seats."
  },
  {
   "id": "D10",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 7 (revenue model)",
   "retrieved_on": null,
   "quote": "INR 400 per drafted reply above the plan limit."
  },
  {
   "id": "D11",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 8 (competition table; CAPilot Yes, Tally and Zoho No, ClearTax No)",
   "retrieved_on": null,
   "quote": "AI notice replies"
  },
  {
   "id": "D12",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 9 (team)",
   "retrieved_on": null,
   "quote": "Qualified CA. 4 years in practice handling GST for 60 clients."
  },
  {
   "id": "D13",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 9 (team)",
   "retrieved_on": null,
   "quote": "3 years at a SaaS company. Built the matching engine."
  },
  {
   "id": "D14",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 10 (ask)",
   "retrieved_on": null,
   "quote": "In 12 months: 150 paying firms and INR 7 L monthly recurring revenue."
  },
  {
   "id": "D15",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 10 (ask)",
   "retrieved_on": null,
   "quote": "20% Compliance and security"
  },
  {
   "id": "F1",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Company > Website",
   "retrieved_on": null,
   "quote": "www.capilot.example"
  },
  {
   "id": "F2",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "linkedin.com/in/dhruv-shah-example"
  },
  {
   "id": "F3",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 2",
   "retrieved_on": null,
   "quote": "linkedin.com/in/isha-merchant-example"
  },
  {
   "id": "F4",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Customers",
   "retrieved_on": null,
   "quote": "24 paying CA firms, 7 on free trial. 2 firms have churned."
  },
  {
   "id": "F5",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Revenue",
   "retrieved_on": null,
   "quote": "Monthly recurring revenue INR 78,000 (INR 9.4 L annualised)."
  },
  {
   "id": "F6",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Customer acquisition",
   "retrieved_on": null,
   "quote": "Mostly the founders' network and referrals from other CAs. We have not measured acquisition cost yet."
  },
  {
   "id": "F7",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Accuracy and liability",
   "retrieved_on": null,
   "quote": "Every drafted reply is reviewed by the CA before filing. Responsibility sits with the CA."
  },
  {
   "id": "F8",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Key risks",
   "retrieved_on": null,
   "quote": "Model errors on unusual notices and dependence on GST portal data formats."
  },
  {
   "id": "F9",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Company > Sector (as selected)",
   "retrieved_on": null,
   "quote": "Fintech"
  },
  {
   "id": "F10",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > Valuation expectation",
   "retrieved_on": null,
   "quote": "INR 10 Cr post-money"
  },
  {
   "id": "F11",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > Existing investors",
   "retrieved_on": null,
   "quote": "One angel, INR 15 L."
  },
  {
   "id": "F12",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Time commitment",
   "retrieved_on": null,
   "quote": "Both full-time since February 2026."
  },
  {
   "id": "F13",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "Qualified Chartered Accountant, 4 years in practice handling GST for about 60 clients."
  },
  {
   "id": "F14",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Anything else",
   "retrieved_on": null,
   "quote": "We believe CA firms are underserved by existing tools. We would welcome a call."
  },
  {
   "id": "W1",
   "kind": "web",
   "title": "GST Reply AI - AI-drafted replies to GST notices (Product Hunt)",
   "url": "https://www.producthunt.com/p/gst-reply-ai/gst-reply-ai",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "AI-drafted replies to GST notices, in 30 seconds"
  },
  {
   "id": "W2",
   "kind": "web",
   "title": "GST Reply AI (Product Hunt) - per-reply pricing",
   "url": "https://www.producthunt.com/p/gst-reply-ai/gst-reply-ai",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "From ₹299 per reply."
  },
  {
   "id": "W3",
   "kind": "web",
   "title": "GST Reply AI (Product Hunt) - CA firm plan, hunter's comment",
   "url": "https://www.producthunt.com/p/gst-reply-ai/gst-reply-ai",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Rs 999/month unlimited for CA firms handling volume"
  },
  {
   "id": "W4",
   "kind": "web",
   "title": "AI-powered software for Indian CAs (Vyapar TaxOne blog)",
   "url": "https://taxone.vyapar.com/post/ai-powered-software-for-indian-cas",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Map multiple GST data, automate reconciliations, and identify errors."
  },
  {
   "id": "W5",
   "kind": "web",
   "title": "AI-powered software for Indian CAs (Vyapar TaxOne blog) - AI positioning",
   "url": "https://taxone.vyapar.com/post/ai-powered-software-for-indian-cas",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Vyapar TaxOne offers India-specific AI automation features."
  },
  {
   "id": "W6",
   "kind": "web",
   "title": "What is GSP and how the GSP ecosystem works (Quicko help centre)",
   "url": "https://help.quicko.com/portal/en/kb/articles/what-is-gsp-and-how-the-gsp-ecosystem-works",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "A software platform that builds tools for GST filing, reconciliation, invoicing, or reporting."
  },
  {
   "id": "W7",
   "kind": "web",
   "title": "Statistics of ICAI members, students and firms till 28 February 2025 (TaxConcept) - firms table TOTAL row",
   "url": "https://taxconcept.net/icai/statistics-of-icai-members-students-firms-till-28th-february-2025/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "98967"
  }
 ],
 "produced_by": "claude-code-session (in-session run of prompts/research.md; no API key)",
 "research_notes": "Founder and company searches returned nothing (placeholder links). Search results also listed GSTGuard, Notice Reply Studio, TaxCopilot, NoticeAI (an ICAI-listed use case) and other AI tools for CAs; the ICAI and G2 pages returned 403 and were not cited. Suvit-to-Vyapar TaxOne relationship is based on search snippets plus an observed redirect, not a primary source. The ICAI firm count is quoted as a bare table value."
}
</dossier>

Score every criterion in both lenses (R1-R6, S1-S4) and evaluate gates G1-G4.