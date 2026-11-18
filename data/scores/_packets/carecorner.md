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
- C003 ((meeting-notes startup), by Kushal / Aditya (partner notes, Meeting 4)): Scored 7 before anyone noticed it overlaps portfolio company MeetRecord. Check every application against the full portfolio list; default is no to competitors unless both founders know. Prefer a false-alarm flag to a miss.  (matched on: portfolio_overlap)
</partner_corrections>

<dossier>
{
 "company": "CareCorner",
 "slug": "carecorner",
 "one_liner": "Chain of 1,200 sq ft neighbourhood primary-care clinics with in-house diagnostics and a pharmacy; three clinics open in Hyderabad suburbs.",
 "sector": "other",
 "sub_sector": "Healthcare services / primary-care clinic chain with diagnostics and pharmacy",
 "stage": "Pre-seed",
 "ask": "INR 3 Cr at INR 18 Cr post-money",
 "business_model": "Owned clinics earning consultation, diagnostics and pharmacy revenue (at maturity 62% consultations+diagnostics, 38% pharmacy, per deck). Capex INR 28 L per clinic; first clinic broke even in month 8.",
 "founders": [
  {
   "name": "Dr. Lakshmi Reddy",
   "role": "CEO",
   "background_claimed": "MBBS, 8 years in family medicine. Designs the clinical protocols.",
   "background_verified": "Not verified. LinkedIn link is a placeholder. A 'Dr K Lakshmi Reddy' (MBBS, MD General Medicine, '5 Yrs Experience') is listed as a consultant at Continental Hospitals, Hyderabad, but nothing links her to CareCorner and the profile does not match the claimed 8 years in family medicine; treated as an unrelated same-name person. No medical council registration number provided to check.",
   "public_footprint": "not_found",
   "source_ids": [
    "D8",
    "F10",
    "W5"
   ]
  },
  {
   "name": "Vikram Rao",
   "role": "COO",
   "background_claimed": "6 years in operations at a hospital chain. Runs site selection and rollout.",
   "background_verified": "Not verified. LinkedIn link is a placeholder; hospital chain not named; search for name + CareCorner + Hyderabad found nothing.",
   "public_footprint": "not_found",
   "source_ids": [
    "D9",
    "F11"
   ]
  }
 ],
 "claims": [
  {
   "text": "Dr. Lakshmi Reddy (CEO) is an MBBS with 8 years in family medicine.",
   "source_ids": [
    "D8",
    "F10"
   ],
   "status": "founder_stated",
   "note": "Deck and form agree. No council registration or LinkedIn to verify."
  },
  {
   "text": "Vikram Rao (COO) has 6 years in operations at a hospital chain.",
   "source_ids": [
    "D9",
    "F11"
   ],
   "status": "founder_stated",
   "note": "Chain not named."
  },
  {
   "text": "A same-name doctor, Dr K Lakshmi Reddy, is a consultant in internal medicine at Continental Hospitals, Hyderabad; it could not be established that she is the CareCorner founder.",
   "source_ids": [
    "W5",
    "F10"
   ],
   "status": "unverifiable",
   "note": "Profile lists MD General Medicine and 5 years' experience, and a current hospital affiliation, which does not fit 'full-time since August 2025' and '8 years in family medicine'. Do not treat as verification either way."
  },
  {
   "text": "Both founders' LinkedIn links are placeholders and no public footprint was found for either.",
   "source_ids": [
    "F10",
    "F11"
   ],
   "status": "unverifiable",
   "note": null
  },
  {
   "text": "Deck positions CareCorner as clinics 'for Tier-2 India', but the three clinics are in Hyderabad suburbs.",
   "source_ids": [
    "D1",
    "F1"
   ],
   "status": "contradicted",
   "note": "Hyderabad is a metro; the SAM is built on Tier-2 cities of Telangana, AP and Karnataka where no clinic is yet open. The deck's '20 to 40 km' travel problem is unlikely to describe Hyderabad suburbs."
  },
  {
   "text": "Three clinics generated INR 9.8 L revenue in October 2026; the first clinic reached monthly breakeven in month 8.",
   "source_ids": [
    "D3",
    "F2"
   ],
   "status": "founder_stated",
   "note": "Deck and form agree. Implies ~INR 3.3 L per clinic per month."
  },
  {
   "text": "The month-by-month revenue trend (Jun 3.9 L to Oct 9.8 L) is an assumed ordering; the PDF extraction listed values as 9.8, 8.6, 7.0, 3.9, 5.2.",
   "source_ids": [
    "D4"
   ],
   "status": "unverifiable",
   "note": "Only October (9.8 L) is confirmed by the form. Growth shape, and whether there was a dip, must be confirmed from clinic P&Ls."
  },
  {
   "text": "Mature clinic revenue is projected at INR 1.4 Cr a year, 62% consultations and diagnostics, 38% pharmacy.",
   "source_ids": [
    "D6"
   ],
   "status": "founder_stated",
   "note": "Our arithmetic: current ~INR 3.3 L/clinic/month annualises to ~INR 39 L, so maturity assumes ~3.6x today's average clinic. SOM of INR 35 Cr (25 clinics x INR 1.4 Cr) rests on this."
  },
  {
   "text": "Twelve-month target is 8 clinics, INR 45 L monthly revenue and 3 clinics at breakeven.",
   "source_ids": [
    "D11"
   ],
   "status": "founder_stated",
   "note": "Implies ~INR 5.6 L per clinic per month on average with 5 new clinics still ramping; 70% above today's per-clinic average."
  },
  {
   "text": "Patient acquisition cost is about INR 210 per new patient; 45% local doctor referrals, 35% WhatsApp and Google listings, 20% health camps.",
   "source_ids": [
    "F3"
   ],
   "status": "founder_stated",
   "note": "Deck slide 7 gives the same figures. Patient retention/visit frequency (the deciding metric for primary care) is not given."
  },
  {
   "text": "Capex is INR 28 L per clinic, funded by angels and an INR 40 L bank loan; existing funding is angels INR 60 L plus bank loan INR 40 L.",
   "source_ids": [
    "F4",
    "F7"
   ],
   "status": "founder_stated",
   "note": "Consistent: 3 clinics x 28 L = 84 L against INR 1 Cr raised/borrowed. 47% of the INR 3 Cr ask (INR 1.41 Cr) for five clinics matches INR 28 L each."
  },
  {
   "text": "Angels hold 25% for INR 60 L (implied ~INR 2.4 Cr post-money); the founders now seek INR 18 Cr post-money.",
   "source_ids": [
    "F8",
    "F7",
    "F6"
   ],
   "status": "founder_stated",
   "note": "Our arithmetic: ~7.5x step-up in valuation within about a year."
  },
  {
   "text": "Team of 14 including 3 doctors.",
   "source_ids": [
    "D10",
    "F13"
   ],
   "status": "founder_stated",
   "note": "Deck and form agree. With three clinics, each relies on one doctor; doctor retention is a founder-named key risk."
  },
  {
   "text": "Both founders full-time since August 2025, when the company was incorporated; no prior startup experience.",
   "source_ids": [
    "F12"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Each clinic includes in-house diagnostics with same-day results and a pharmacy.",
   "source_ids": [
    "D13",
    "F1"
   ],
   "status": "founder_stated",
   "note": "Diagnostics and pharmacy each carry their own licensing (lab registration, drug licence); none is mentioned."
  },
  {
   "text": "Market sizing: TAM INR 1.14 lakh Cr, SAM INR 5,400 Cr, with household spend estimated from clinic billing and a 90-household survey.",
   "source_ids": [
    "D5"
   ],
   "status": "founder_stated",
   "note": "Arithmetic checks (190M x INR 6,000; 9M x INR 6,000). The INR 6,000/household input rests on a 90-household survey."
  },
  {
   "text": "Telangana has adopted the Clinical Establishments (Registration and Regulation) Act; all healthcare facilities must register with the District Registering Authority, including diagnostic laboratories.",
   "source_ids": [
    "W1"
   ],
   "status": "verified",
   "note": "Article dated June 2022. CareCorner does not mention registration status for its clinics or labs."
  },
  {
   "text": "Hyderabad health authorities found ~224 private hospitals operating without mandatory registration in January 2026, issuing show-cause notices and ordering temporary shutdowns.",
   "source_ids": [
    "W2"
   ],
   "status": "verified",
   "note": "Shows registration is actively enforced in CareCorner's city."
  },
  {
   "text": "Preventify, a Kerala clinic chain for Tier-2/3 India with three clinics, raised INR 2 Cr pre-seed (Feb 2026) led by PedalStart.",
   "source_ids": [
    "W3"
   ],
   "status": "verified",
   "note": "Closest comparable: same clinic count and stage, raised at a smaller ask."
  },
  {
   "text": "Hoola Health (paediatric primary care with diagnostics) raised USD 5 M led by Peak XV's Surge and plans 30 more clinics including in Hyderabad.",
   "source_ids": [
    "W4"
   ],
   "status": "verified",
   "note": "A funded clinic chain entering CareCorner's city."
  },
  {
   "text": "Founder-listed key risks: capital intensity, doctor retention and slower ramp in new locations.",
   "source_ids": [
    "F5"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Founders offer clinic-level P&Ls and are in conversation with two healthcare-focused funds.",
   "source_ids": [
    "F15",
    "F9"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Sector selected as 'Other (Healthcare)', consistent with an owned clinic chain (classified here as other).",
   "source_ids": [
    "F14"
   ],
   "status": "founder_stated",
   "note": null
  }
 ],
 "gaps": [
  {
   "what": "Founder identity and credentials",
   "why_it_matters": "Clinical leadership is core to the model; the CEO's medical registration and the COO's hospital-chain operations record are unverified.",
   "searched": [
    "web: \"CareCorner\" clinics Hyderabad \"Lakshmi Reddy\"",
    "web: \"CareCorner Health\" Hyderabad \"Vikram Rao\" clinics",
    "LinkedIn links in form (placeholders)"
   ],
   "ask_founder": "Please share Dr Reddy's Telangana/NMC medical registration number and real LinkedIn profiles; which hospital chain did Vikram work at, in what role?",
   "blocks_criteria": [
    "team",
    "founder_market_fit"
   ]
  },
  {
   "what": "Regulatory registrations for clinics, labs and pharmacies",
   "why_it_matters": "Telangana enforces Clinical Establishments Act registration (including diagnostic labs) with shutdowns and fines; pharmacy is 38% of mature revenue and needs a drug licence.",
   "searched": [
    "web: Telangana clinical establishments registration act private clinics diagnostics",
    "deck",
    "form"
   ],
   "ask_founder": "Are all three clinics and their labs registered under the Clinical Establishments Act, and do the pharmacies hold retail drug licences? Is any lab NABL-accredited?",
   "blocks_criteria": [
    "regulatory"
   ]
  },
  {
   "what": "Clinic-level P&Ls and actual monthly revenue series",
   "why_it_matters": "The chart's month order is an extraction assumption; ramp per clinic is the deciding metric for a clinic chain.",
   "searched": [
    "deck slide 5 (chart and extraction note)",
    "form Revenue"
   ],
   "ask_founder": "Send the clinic-level P&Ls you offered: revenue, gross margin and EBITDA by clinic by month since opening, with opening dates.",
   "blocks_criteria": [
    "traction",
    "unit_economics"
   ]
  },
  {
   "what": "Patient retention and visit frequency",
   "why_it_matters": "The family-doctor thesis depends on repeat visits; CAC of INR 210 means little without visits per patient per year.",
   "searched": [
    "deck",
    "form"
   ],
   "ask_founder": "What share of patients return within 90 days, and how many visits per registered family per year?",
   "blocks_criteria": [
    "unit_economics"
   ]
  },
  {
   "what": "Basis for INR 1.4 Cr mature clinic revenue",
   "why_it_matters": "Current clinics average ~INR 39 L annualised; the SOM, breakeven and 12-month plan all depend on a 3.6x ramp.",
   "searched": [
    "deck slides 6-7"
   ],
   "ask_founder": "What does your best clinic make today, and what patient volume per day does INR 1.4 Cr require?",
   "blocks_criteria": [
    "market",
    "unit_economics"
   ]
  },
  {
   "what": "Tier-2 expansion evidence",
   "why_it_matters": "The pitch is Tier-2 India but every clinic is in Hyderabad suburbs; ramp in a genuine Tier-2 town is untested.",
   "searched": [
    "deck",
    "form"
   ],
   "ask_founder": "Where will the five new clinics open, and why will a Tier-2 town ramp like a Hyderabad suburb?",
   "blocks_criteria": [
    "market"
   ]
  },
  {
   "what": "Bank loan terms and personal guarantees",
   "why_it_matters": "An INR 40 L loan on a pre-seed balance sheet may carry founder guarantees or covenants that shape use of the new round.",
   "searched": [
    "form Capex, Existing investors"
   ],
   "ask_founder": "What are the INR 40 L loan's rate, tenor, collateral and guarantees?",
   "blocks_criteria": [
    "capital_efficiency"
   ]
  },
  {
   "what": "Company registration and web presence",
   "why_it_matters": "No website (placeholder), Google listing or MCA record for CareCorner Health Pvt. Ltd. was found, though the deck claims 35% of patients come from WhatsApp and Google listings.",
   "searched": [
    "web: \"CareCorner\" clinics Hyderabad",
    "web: \"CareCorner Health\" Hyderabad"
   ],
   "ask_founder": "Share the CIN and the Google Business listings for the three clinics.",
   "blocks_criteria": [
    "traction"
   ]
  }
 ],
 "competitors_named": [],
 "competitors_found": [
  "Preventify",
  "Hoola Health",
  "MedySeva",
  "Apollo Clinic (Hyderabad locations)",
  "CARE Hospitals clinics (Hyderabad)"
 ],
 "keywords": [
  "primary care",
  "neighbourhood clinic",
  "family doctor",
  "diagnostics",
  "pathology lab",
  "pharmacy",
  "clinic chain",
  "health record",
  "Tier-2 healthcare",
  "Hyderabad"
 ],
 "founder_contact": null,
 "sources": [
  {
   "id": "D1",
   "kind": "deck",
   "title": "CareCorner deck - cover",
   "url": null,
   "locator": "Cover",
   "retrieved_on": null,
   "quote": "Neighbourhood clinics with diagnostics for Tier-2 India"
  },
  {
   "id": "D3",
   "kind": "deck",
   "title": "CareCorner deck - Traction",
   "url": null,
   "locator": "Slide 5 (Traction)",
   "retrieved_on": null,
   "quote": "Traction: 3 clinics, INR 9.8 L in October"
  },
  {
   "id": "D4",
   "kind": "deck",
   "title": "CareCorner deck - Traction chart extraction note",
   "url": null,
   "locator": "Slide 5 (chart comment)",
   "retrieved_on": null,
   "quote": "chart values as extracted from the PDF, in extraction order: 9.8, 8.6, 7.0, 3.9, 5.2, against months Jun, Jul, Aug, Sep, Oct."
  },
  {
   "id": "D5",
   "kind": "deck",
   "title": "CareCorner deck - Market size",
   "url": null,
   "locator": "Slide 6 (Market size)",
   "retrieved_on": null,
   "quote": "Spend per household is our estimate from clinic billing and a 90-household survey."
  },
  {
   "id": "D6",
   "kind": "deck",
   "title": "CareCorner deck - Clinic economics",
   "url": null,
   "locator": "Slide 7 (Patient acquisition and clinic economics)",
   "retrieved_on": null,
   "quote": "Revenue per clinic at maturity: INR 1.4 Cr a year, 62% from consultations and diagnostics, 38% from pharmacy."
  },
  {
   "id": "D8",
   "kind": "deck",
   "title": "CareCorner deck - The team (CEO)",
   "url": null,
   "locator": "Slide 8 (The team)",
   "retrieved_on": null,
   "quote": "MBBS, 8 years in family medicine. Designs the clinical protocols."
  },
  {
   "id": "D9",
   "kind": "deck",
   "title": "CareCorner deck - The team (COO)",
   "url": null,
   "locator": "Slide 8 (The team)",
   "retrieved_on": null,
   "quote": "6 years in operations at a hospital chain. Runs site selection and rollout."
  },
  {
   "id": "D10",
   "kind": "deck",
   "title": "CareCorner deck - The team (size)",
   "url": null,
   "locator": "Slide 8 (The team)",
   "retrieved_on": null,
   "quote": "Team of 14, including 3 doctors."
  },
  {
   "id": "D11",
   "kind": "deck",
   "title": "CareCorner deck - The ask",
   "url": null,
   "locator": "Slide 9 (The ask)",
   "retrieved_on": null,
   "quote": "In 12 months: 8 clinics, INR 45 L monthly revenue, 3 clinics at breakeven."
  },
  {
   "id": "D13",
   "kind": "deck",
   "title": "CareCorner deck - Test",
   "url": null,
   "locator": "Slide 4 (Consult, test, follow up)",
   "retrieved_on": null,
   "quote": "In-house diagnostics with results the same day."
  },
  {
   "id": "F1",
   "kind": "form",
   "title": "Application form - What have you built?",
   "url": null,
   "locator": "Product and traction > What have you built?",
   "retrieved_on": null,
   "quote": "Three 1,200 sq ft neighbourhood clinics in Hyderabad suburbs, each with a family doctor, in-house diagnostics and a pharmacy."
  },
  {
   "id": "F2",
   "kind": "form",
   "title": "Application form - Revenue",
   "url": null,
   "locator": "Product and traction > Revenue",
   "retrieved_on": null,
   "quote": "INR 9.8 L across the three clinics in October 2026. The first clinic reached monthly breakeven in month 8."
  },
  {
   "id": "F3",
   "kind": "form",
   "title": "Application form - Patient acquisition",
   "url": null,
   "locator": "Product and traction > Patient acquisition",
   "retrieved_on": null,
   "quote": "About INR 210 per new patient. Local doctor referrals 45%, WhatsApp and Google listings 35%, health camps 20%."
  },
  {
   "id": "F4",
   "kind": "form",
   "title": "Application form - Capex",
   "url": null,
   "locator": "Product and traction > Capex",
   "retrieved_on": null,
   "quote": "INR 28 L per clinic, funded by angels and a INR 40 L bank loan."
  },
  {
   "id": "F5",
   "kind": "form",
   "title": "Application form - Key risks",
   "url": null,
   "locator": "Product and traction > Key risks",
   "retrieved_on": null,
   "quote": "Capital intensity, doctor retention, and slower ramp in new locations."
  },
  {
   "id": "F6",
   "kind": "form",
   "title": "Application form - Valuation expectation",
   "url": null,
   "locator": "Fundraising > Valuation expectation",
   "retrieved_on": null,
   "quote": "INR 18 Cr post-money"
  },
  {
   "id": "F7",
   "kind": "form",
   "title": "Application form - Existing investors",
   "url": null,
   "locator": "Fundraising > Existing investors",
   "retrieved_on": null,
   "quote": "Angels INR 60 L, bank loan INR 40 L."
  },
  {
   "id": "F8",
   "kind": "form",
   "title": "Application form - Equity split",
   "url": null,
   "locator": "Founders > Equity split",
   "retrieved_on": null,
   "quote": "Founders 75%, angels 25%."
  },
  {
   "id": "F9",
   "kind": "form",
   "title": "Application form - Other investors in conversation",
   "url": null,
   "locator": "Fundraising > Other investors in conversation",
   "retrieved_on": null,
   "quote": "Two healthcare-focused funds."
  },
  {
   "id": "F10",
   "kind": "form",
   "title": "Application form - Founder 1",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "Dr. Lakshmi Reddy, CEO. MBBS, 8 years in family medicine. linkedin.com/in/lakshmi-reddy-example"
  },
  {
   "id": "F11",
   "kind": "form",
   "title": "Application form - Founder 2",
   "url": null,
   "locator": "Founders > Founder 2",
   "retrieved_on": null,
   "quote": "Vikram Rao, COO. 6 years in operations at a hospital chain. linkedin.com/in/vikram-rao-example"
  },
  {
   "id": "F12",
   "kind": "form",
   "title": "Application form - Time commitment",
   "url": null,
   "locator": "Founders > Time commitment",
   "retrieved_on": null,
   "quote": "Both full-time since August 2025."
  },
  {
   "id": "F13",
   "kind": "form",
   "title": "Application form - Team size",
   "url": null,
   "locator": "Company > Team size",
   "retrieved_on": null,
   "quote": "14, including 3 doctors"
  },
  {
   "id": "F14",
   "kind": "form",
   "title": "Application form - Sector (as selected)",
   "url": null,
   "locator": "Company > Sector (as selected)",
   "retrieved_on": null,
   "quote": "Other (Healthcare)"
  },
  {
   "id": "F15",
   "kind": "form",
   "title": "Application form - Anything else",
   "url": null,
   "locator": "Anything else we should know?",
   "retrieved_on": null,
   "quote": "We can share clinic-level P\\&Ls."
  },
  {
   "id": "W1",
   "kind": "web",
   "title": "Telangana Today - Telangana govt adopts Clinical Establishment Act to regulate private hospitals (16 Jun 2022)",
   "url": "https://telanganatoday.com/telangana-govt-adopts-clinical-establishment-act-to-regulate-private-hospitals",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "from now on all the healthcare facilities have to register themselves with the District Registering Authority"
  },
  {
   "id": "W2",
   "kind": "web",
   "title": "Medical Dialogues - 224 private hospitals in Hyderabad operating without mandatory registration (19 Jan 2026)",
   "url": "https://medicaldialogues.in/news/health/hospital-diagnostics/hyderabad-224-private-hospitals-operating-without-mandatory-registration-162923",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Nearly 224 private hospitals in Hyderabad were found operating without mandatory registration"
  },
  {
   "id": "W3",
   "kind": "web",
   "title": "BioVoice News - Preventify raises INR 2 crore pre-seed led by PedalStart (10 Feb 2026)",
   "url": "https://biovoicenews.com/preventify-raises-₹2-crore-pre-seed-funding-led-by-pedalstart-to-expand-branded-healthcare-clinics-in-tier-2-and-tier-3-india/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "The startup currently operates three clinics in Kerala and has already served over 40,000 patients"
  },
  {
   "id": "W4",
   "kind": "web",
   "title": "BioSpectrum India - Hoola Health raises $5 M to expand paediatric healthcare (10 Jun 2026)",
   "url": "https://www.biospectrumindia.com/news/16/27940/hoola-health-raises-5-m-to-expand-child-first-paediatric-healthcare-across-india.html",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "open 30 additional clinics across Bengaluru, Hyderabad and Delhi NCR"
  },
  {
   "id": "W5",
   "kind": "web",
   "title": "Continental Hospitals - Dr K Lakshmi Reddy profile (same-name doctor; not linked to CareCorner)",
   "url": "https://continentalhospitals.com/doctors/dr-k-lakshmi-reddy",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "MD General Medicine, MNR Medical College"
  }
 ],
 "produced_by": "claude-code-session (in-session run of prompts/research.md; no API key)",
 "research_notes": "Founder/company searches returned no CareCorner footprint (placeholder links). One same-name doctor found at Continental Hospitals; not linkable and recorded as unverifiable. Deck and form agree on every number; the main inconsistency is Tier-2 positioning vs Hyderabad-suburb clinics, plus the assumed chart ordering. Web quotes were extracted via a fetch tool and should be re-verified with verify_web."
}
</dossier>

Score every criterion in both lenses (R1-R6, S1-S4) and evaluate gates G1-G4.