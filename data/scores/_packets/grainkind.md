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
- C001 [R3] (Petalry, by Kushal (partner notes, Meeting 1)): Riya scored 6.5/10; too high. A consumer brand that cannot give a repeat rate must be scored down on traction - a missing number drags the score, it is not skipped. If repeat is good CAC is survivable; if we can't see it we're guessing.  (matched on: consumer_brand, d2c, missing_repeat_rate, paid_growth)
</partner_corrections>

<dossier>
{
 "company": "GrainKind",
 "slug": "grainkind",
 "one_liner": "Taste-first millet-based breakfast cereals and snacks for urban families, sold on its own site, Amazon and quick commerce.",
 "sector": "consumer_brand",
 "sub_sector": "Better-for-you packaged food (millet breakfast and snacks), D2C plus marketplaces",
 "stage": "Pre-seed",
 "ask": "INR 2.5 Cr at INR 14 Cr post-money",
 "business_model": "Sells seven millet SKUs (made by one co-packer) direct and via Amazon and quick commerce; 48% gross margin, 11% contribution after CAC and logistics.",
 "founders": [
  {
   "name": "Ritu Hegde",
   "role": "CEO",
   "background_claimed": "6 years in category and brand roles at a large packaged-food company; food science training/degree.",
   "background_verified": null,
   "public_footprint": "not_found",
   "source_ids": [
    "D10",
    "F14",
    "F2"
   ]
  },
  {
   "name": "Sanjay Kulkarni",
   "role": "COO",
   "background_claimed": "5 years in supply chain at a quick-commerce company; runs sourcing and the co-packer.",
   "background_verified": null,
   "public_footprint": "not_found",
   "source_ids": [
    "D11",
    "F3"
   ]
  }
 ],
 "claims": [
  {
   "text": "90-day repeat rate by cohort: 31% (June), 34% (July), 38% (August), from cohort data covering 3,100 customers.",
   "source_ids": [
    "F5",
    "D4",
    "D5"
   ],
   "status": "founder_stated",
   "note": "The deck shows only the best cohort (August, 38%); the form gives the full trend. The August cohort's 90-day window cannot be complete for customers acquired late in August if the data is as of October 2026, so 38% may be partial."
  },
  {
   "text": "Repeat trend is improving and above a founder-reported peer benchmark: Wild Date reports ~37% 90-day repeat, and the same page calls >30% within 90 days strong for a D2C food brand.",
   "source_ids": [
    "F5",
    "W1",
    "W2"
   ],
   "status": "founder_stated",
   "note": "Benchmark is anecdotal (one founder interview plus an unattributed FAQ line), not audited category data. GrainKind's 12-month target is 45% (D13)."
  },
  {
   "text": "October 2026 revenue INR 16.5 L; INR 72 L cumulative since launch in November 2025; monthly revenue grew 4.8 -> 7.1 -> 10.2 -> 13.0 -> 16.5 (INR L) June to October.",
   "source_ids": [
    "D3",
    "F4"
   ],
   "status": "founder_stated",
   "note": "Consistent: June-October sums to INR 51.6 L, leaving INR 20.4 L for November-May."
  },
  {
   "text": "Gross margin 48% after COGS and packaging; blended CAC INR 340; contribution after CAC and logistics 11%; 12-month LTV:CAC about 1.8x.",
   "source_ids": [
    "F6",
    "F7",
    "D9"
   ],
   "status": "founder_stated",
   "note": "LTV:CAC 1.8x is thin for a brand and partly extrapolated (oldest cohorts are under 12 months old)."
  },
  {
   "text": "First order does not pay back acquisition: average first order INR 540 at 48% gross margin is ~INR 259 gross profit against INR 340 blended CAC (INR 410 on paid social). June cohort averages 2.4 orders in 5 months.",
   "source_ids": [
    "D6",
    "D7",
    "F6",
    "D8"
   ],
   "status": "founder_stated",
   "note": "Derived from the founders' numbers. Payback depends on repeat holding."
  },
  {
   "text": "About 70% of new customers come through bought channels: paid social 45% (CAC INR 410) and quick commerce 25% (INR 290 after promos); nutritionist referrals 20% (INR 210), gyms and sampling 10% (INR 380).",
   "source_ids": [
    "F8",
    "F17",
    "D8"
   ],
   "status": "founder_stated",
   "note": "Echoes the Petalry precedent (C001: paid social ~2/3 of orders). Here, unlike Petalry, cohort repeat data is provided. Nutritionist referral is the cheapest channel but only 20%."
  },
  {
   "text": "Revenue mix: own site 55%, Amazon 25%, quick commerce 20%.",
   "source_ids": [
    "D17"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Seven products; three hero SKUs (Ragi choco crunch, Millet muesli, Jowar puffs) account for 87% of orders.",
   "source_ids": [
    "F10"
   ],
   "status": "founder_stated",
   "note": "Founders flag slower repeat on Jowar puffs, the quick-commerce favourite (F9)."
  },
  {
   "text": "All products made by a single co-packer in Hosur; founders list single co-packer, rising paid-social costs and slower Jowar puffs repeat as key risks.",
   "source_ids": [
    "D12",
    "F9"
   ],
   "status": "founder_stated",
   "note": "Founders name their risks unprompted (R1-positive) and offer the co-packer agreement (F13)."
  },
  {
   "text": "Priced at INR 62 per 100 g versus INR 45 for large cereal brands and INR 70 for other millet brands (founders' comparison).",
   "source_ids": [
    "D15"
   ],
   "status": "founder_stated",
   "note": "Prices of comparators not verified."
  },
  {
   "text": "Founder background differs slightly between documents: deck says Ritu Hegde is 'trained in food science'; form says 'Food science degree'.",
   "source_ids": [
    "D10",
    "F14"
   ],
   "status": "founder_stated",
   "note": "Minor wording difference rather than a contradiction; confirm the qualification."
  },
  {
   "text": "Founders: Ritu Hegde (CEO) claims 6 years in category/brand roles at a large packaged-food company; Sanjay Kulkarni (COO) claims 5 years in supply chain at a quick-commerce company. First-time founders, full-time since July 2025, team of 9.",
   "source_ids": [
    "D10",
    "D11",
    "D12",
    "F15"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Founder LinkedIn links are placeholders (*-example) and the website is a .example domain; no independent footprint for founders or brand found.",
   "source_ids": [
    "F2",
    "F3",
    "F1"
   ],
   "status": "unverifiable",
   "note": null
  },
  {
   "text": "Founders surveyed 420 urban parents (July 2025) before launch.",
   "source_ids": [
    "D2"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Tata Consumer acquired 100% of Kottaram Agro Foods (Soulfull), a millet-based breakfast brand for kids and adults, in 2021.",
   "source_ids": [
    "W3",
    "W4"
   ],
   "status": "verified",
   "note": "Direct category competitor (Soulfull Ragi Bites overlaps with Ragi choco crunch) backed by Tata distribution."
  },
  {
   "text": "Wholsum Foods (Slurrp Farm), a millet-led brand, reported FY25 revenue of Rs 97.5 crore (+33% YoY) and a net loss of Rs 32.67 crore.",
   "source_ids": [
    "W5",
    "W6"
   ],
   "status": "verified",
   "note": "Benchmark: the scaled millet D2C peer is still loss-making at ~Rs 100 Cr revenue."
  },
  {
   "text": "ITC completed its acquisition of 100% of Yoga Bar (Sproutlife Foods) in September 2026.",
   "source_ids": [
    "W8"
   ],
   "status": "verified",
   "note": "Large FMCG companies are consolidating the better-for-you snack/breakfast shelf - both competition and a possible exit route."
  },
  {
   "text": "The Indian healthy-snack shelf is described as increasingly crowded (Slurrp Farm, Early Foods, The Whole Truth, Farmley, Happilo named).",
   "source_ids": [
    "W7"
   ],
   "status": "verified",
   "note": null
  },
  {
   "text": "12-month targets: INR 40 L monthly revenue, 90-day repeat at 45%, contribution margin 15%; 40% of the raise goes to inventory and working capital.",
   "source_ids": [
    "D13",
    "D14"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Market sizing: INR 2,400 annual household spend is the founders' estimate from order data and a parent survey.",
   "source_ids": [
    "D16"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Sector as selected (Consumer brands) matches the business: a packaged millet food brand.",
   "source_ids": [
    "F16",
    "D1"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Raising INR 2.5 Cr at INR 14 Cr post-money; three food/retail angels have invested INR 45 L.",
   "source_ids": [
    "F11",
    "F12"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Founders offer to share the cohort sheet and the co-packer agreement.",
   "source_ids": [
    "F13"
   ],
   "status": "founder_stated",
   "note": null
  }
 ],
 "gaps": [
  {
   "what": "Ritu Hegde (CEO): no public footprint confirming the packaged-food category/brand roles or food-science qualification.",
   "why_it_matters": "Category-management experience is the main founder-market-fit claim.",
   "searched": [
    "WebSearch: \"Ritu Hegde\" GrainKind millet Bengaluru (2026-11-18) - no match; results were other millet brands",
    "Application LinkedIn link linkedin.com/in/ritu- hegde-example is a placeholder"
   ],
   "ask_founder": "Which company and categories did you manage, and what is your food-science qualification?",
   "blocks_criteria": [
    "S3"
   ]
  },
  {
   "what": "Sanjay Kulkarni (COO): no public footprint confirming supply-chain work at a quick-commerce company.",
   "why_it_matters": "He runs sourcing and the single co-packer, the main operational risk.",
   "searched": [
    "WebSearch: \"Sanjay Kulkarni\" GrainKind COO Bengaluru (2026-11-18) - no match",
    "Application LinkedIn link linkedin.com/in/sanjay-kulkarni-example is a placeholder"
   ],
   "ask_founder": "Which quick-commerce company and what scope did you own?",
   "blocks_criteria": [
    "S3"
   ]
  },
  {
   "what": "Brand existence: no website, marketplace listing, FSSAI licence or MCA record found for GrainKind.",
   "why_it_matters": "Basic verification that the products are on Amazon/quick commerce as claimed.",
   "searched": [
    "WebSearch: GrainKind millet ragi choco crunch brand (2026-11-18) - only Soulfull, Slurrp Farm and other brands returned",
    "Website www.grainkind.example is a placeholder",
    "FSSAI and MCA portals not queried"
   ],
   "ask_founder": "Share Amazon ASINs / quick-commerce listings, FSSAI licence number and CIN.",
   "blocks_criteria": [
    "R4"
   ]
  },
  {
   "what": "Repeat by channel and by SKU, and repeat net of discounts.",
   "why_it_matters": "Repeat rate is the deciding metric for a brand; a blended 38% can hide weak repeat in paid-social or quick-commerce cohorts.",
   "searched": [
    "Deck slides 5-8",
    "Form Repeat behaviour"
   ],
   "ask_founder": "What is 90-day repeat for paid-social-acquired vs nutritionist-referred customers, and for Jowar puffs vs Ragi choco crunch?",
   "blocks_criteria": [
    "R3",
    "R1"
   ]
  },
  {
   "what": "Return/complaint rate and Amazon/quick-commerce ratings.",
   "why_it_matters": "Return rate is a listed key metric for brands; nothing in the application.",
   "searched": [
    "Deck and form - not mentioned"
   ],
   "ask_founder": "What are your return/refund rate and average marketplace rating?",
   "blocks_criteria": [
    "R3"
   ]
  },
  {
   "what": "Contribution margin by channel (own site vs Amazon vs quick commerce after commissions and promos).",
   "why_it_matters": "45% of revenue is on marketplaces/quick commerce where take rates are high; blended 11% contribution may hide negative channels.",
   "searched": [
    "Deck slide 6 and 8",
    "Form Unit economics"
   ],
   "ask_founder": "What is contribution after CAC and logistics separately for own site, Amazon and quick commerce?",
   "blocks_criteria": [
    "R3",
    "R5"
   ]
  },
  {
   "what": "Co-packer dependency: contract terms, capacity, exclusivity and a second-source plan.",
   "why_it_matters": "All seven products come from one co-packer in Hosur; supply interruption would stop revenue.",
   "searched": [
    "Deck slide 10",
    "Form Key risks"
   ],
   "ask_founder": "What capacity headroom does the co-packer have, and when will a second co-packer be qualified?",
   "blocks_criteria": [
    "R1",
    "R4"
   ]
  }
 ],
 "competitors_named": [
  "Large cereal brands (unnamed)",
  "Other millet brands (unnamed)"
 ],
 "competitors_found": [
  "Tata Soulfull",
  "Slurrp Farm / Wholsum Foods",
  "Yoga Bar (ITC)",
  "Early Foods",
  "The Whole Truth",
  "Farmley",
  "Happilo"
 ],
 "keywords": [
  "millet",
  "breakfast cereal",
  "healthy snacks",
  "kids snacks",
  "muesli",
  "ragi",
  "packaged food",
  "D2C food brand",
  "quick commerce",
  "better-for-you"
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
   "quote": "Millet-based breakfast and snacks for urban families"
  },
  {
   "id": "D2",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 3 (problem)",
   "retrieved_on": null,
   "quote": "Survey of 420 urban parents, July 2025."
  },
  {
   "id": "D3",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "INR 16.5 L October revenue"
  },
  {
   "id": "D4",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "38% 90-day repeat, August cohort"
  },
  {
   "id": "D5",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "3,100 customers in cohort data"
  },
  {
   "id": "D6",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 6 (unit economics table; row value INR 540)",
   "retrieved_on": null,
   "quote": "Average first order value"
  },
  {
   "id": "D7",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 6 (unit economics table; row value 2.4)",
   "retrieved_on": null,
   "quote": "Orders per customer, June cohort (5 months)"
  },
  {
   "id": "D8",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 8 (GTM)",
   "retrieved_on": null,
   "quote": "CAC by channel: paid social INR 410, nutritionists INR 210, quick commerce INR 290 after promos, sampling INR 380."
  },
  {
   "id": "D9",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 8 (GTM)",
   "retrieved_on": null,
   "quote": "1.8x 12-month LTV to CAC"
  },
  {
   "id": "D10",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 10 (team)",
   "retrieved_on": null,
   "quote": "6 years in category and brand roles at a large packaged-food company. Trained in food science."
  },
  {
   "id": "D11",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 10 (team)",
   "retrieved_on": null,
   "quote": "5 years in supply chain at a quick-commerce company. Runs sourcing and the co-packer."
  },
  {
   "id": "D12",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 10 (team)",
   "retrieved_on": null,
   "quote": "First-time founders. Team of 9. All products made by one co-packer in Hosur."
  },
  {
   "id": "D13",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 11 (ask)",
   "retrieved_on": null,
   "quote": "In 12 months: INR 40 L monthly revenue, 90-day repeat at 45%, contribution margin at 15%."
  },
  {
   "id": "D14",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 11 (ask)",
   "retrieved_on": null,
   "quote": "40% Inventory and working capital"
  },
  {
   "id": "D15",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 9 (differentiation table; GrainKind INR 62, large cereal brands INR 45, other millet brands INR 70)",
   "retrieved_on": null,
   "quote": "Price per 100 g"
  },
  {
   "id": "D16",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 7 (market size)",
   "retrieved_on": null,
   "quote": "INR 2,400 is our estimate from order data and a parent survey."
  },
  {
   "id": "D17",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 8 (GTM)",
   "retrieved_on": null,
   "quote": "Revenue mix: own site 55%, Amazon 25%, quick commerce 20%."
  },
  {
   "id": "F1",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Company > Website",
   "retrieved_on": null,
   "quote": "www.grainkind.example"
  },
  {
   "id": "F2",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "linkedin.com/in/ritu- hegde-example"
  },
  {
   "id": "F3",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 2",
   "retrieved_on": null,
   "quote": "linkedin.com/in/sanjay-kulkarni-example"
  },
  {
   "id": "F4",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Revenue",
   "retrieved_on": null,
   "quote": "INR 16.5 L in October 2026. INR 72 L since launch in November 2025."
  },
  {
   "id": "F5",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Repeat behaviour",
   "retrieved_on": null,
   "quote": "90-day repeat rate was 31% (June cohort), 34% (July) and 38% (August). Cohort data covers 3,100 customers."
  },
  {
   "id": "F6",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Unit economics",
   "retrieved_on": null,
   "quote": "Gross margin 48% after COGS and packaging. Blended CAC INR 340. Contribution after CAC and logistics is 11%."
  },
  {
   "id": "F7",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Unit economics",
   "retrieved_on": null,
   "quote": "12-month LTV to CAC is about 1.8x on current data."
  },
  {
   "id": "F8",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Customer acquisition",
   "retrieved_on": null,
   "quote": "Paid social 45% of new customers (CAC INR 410)"
  },
  {
   "id": "F9",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Key risks",
   "retrieved_on": null,
   "quote": "Single co-packer, rising paid social costs, and slower repeat on Jowar puffs."
  },
  {
   "id": "F10",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > What have you built?",
   "retrieved_on": null,
   "quote": "Seven millet-based products. Three hero SKUs account for 87% of orders."
  },
  {
   "id": "F11",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > Valuation expectation",
   "retrieved_on": null,
   "quote": "INR 14 Cr post-money"
  },
  {
   "id": "F12",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > Existing investors",
   "retrieved_on": null,
   "quote": "Three angels from the food and retail industry, INR 45 L in total."
  },
  {
   "id": "F13",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Anything else",
   "retrieved_on": null,
   "quote": "We can share our cohort sheet and co-packer agreement on request."
  },
  {
   "id": "F14",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "6 years in category and brand roles at a large packaged-food company. Food science degree."
  },
  {
   "id": "F15",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Time commitment",
   "retrieved_on": null,
   "quote": "Both full-time since July 2025."
  },
  {
   "id": "F16",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Company > Sector (as selected)",
   "retrieved_on": null,
   "quote": "Consumer brands"
  },
  {
   "id": "F17",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Customer acquisition",
   "retrieved_on": null,
   "quote": "quick commerce 25% (INR 290 after promos)"
  },
  {
   "id": "W1",
   "kind": "web",
   "title": "How to build a clean-label D2C snack brand for India - Wild Date (Fynd podcast page)",
   "url": "https://www.fynd.com/podcast/how-to-build-clean-label-d2c-snack-brand-for-india-wild-date",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Our repeat rate over a 90-day window is around 37%, and over 30 days it is 17% to 18%."
  },
  {
   "id": "W2",
   "kind": "web",
   "title": "How to build a clean-label D2C snack brand for India - Wild Date (Fynd) - FAQ benchmark",
   "url": "https://www.fynd.com/podcast/how-to-build-clean-label-d2c-snack-brand-for-india-wild-date",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "A strong repeat rate for a D2C food brand is typically above 30% within a 90-day window."
  },
  {
   "id": "W3",
   "kind": "web",
   "title": "Tata Consumer Products to acquire Kottaram Agro Foods, owner of the brand 'Soulfull' (Tata Consumer, 2 Feb 2021)",
   "url": "https://tataconsumer.com/news/tata-consumer-products-acquire-kottaram-agro-foods-owner-brand-soulfull",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "signed definitive agreements to acquire 100% equity shares of Kottaram Agro Foods (KAF), owner of the brand ‘Soulfull’."
  },
  {
   "id": "W4",
   "kind": "web",
   "title": "Tata Consumer acquires Soulfull - product description",
   "url": "https://tataconsumer.com/news/tata-consumer-products-acquire-kottaram-agro-foods-owner-brand-soulfull",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "with a portfolio of millet-based products for kids and adults."
  },
  {
   "id": "W5",
   "kind": "web",
   "title": "Wholsum Foods (Slurrp Farm) approaches Rs 100 crore revenue in FY25, loss widens 30% (Startuppedia, 20 Feb 2026)",
   "url": "https://startuppedia.in/trending/startup-news/anushka-sharma-backed-wholsum-foods-parent-company-of-slurrp-farm-approaches-rs-100-crore-revenue-mark-in-fy25-loss-widens-30-11133954",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "reported 33% year-on-year revenue growth in FY25, reaching Rs 97.5 crore"
  },
  {
   "id": "W6",
   "kind": "web",
   "title": "Wholsum Foods (Slurrp Farm) FY25 loss (Startuppedia)",
   "url": "https://startuppedia.in/trending/startup-news/anushka-sharma-backed-wholsum-foods-parent-company-of-slurrp-farm-approaches-rs-100-crore-revenue-mark-in-fy25-loss-widens-30-11133954",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "The company reported a net loss of Rs 32.67 crore in FY25"
  },
  {
   "id": "W7",
   "kind": "web",
   "title": "Troovy's Rs 100-crore bet on India's crowded healthy-snack shelf (Open Magazine, 27 Oct 2026)",
   "url": "https://openthemagazine.com/business/troovys-100-crore-bet-on-indias-crowded-healthy-snack-shelf",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "It is pursuing that ambition on an increasingly crowded shelf."
  },
  {
   "id": "W8",
   "kind": "web",
   "title": "ITC completes Yoga Bar acquisition for Rs 645 Cr (Inc42, 29 Sep 2026)",
   "url": "https://inc42.com/?p=574080",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "has completed the acquisition of 100% of Sproutlife Foods, the parent of healthy snacking brand Yoga Bar"
  }
 ],
 "produced_by": "claude-code-session (in-session run of prompts/research.md; no API key)",
 "research_notes": "Founder and brand searches returned nothing (placeholder links). Repeat-rate benchmarks for Indian D2C food are mostly anecdotal; the cited Wild Date figure is one founder's number. Search snippets also listed Little Joys, Millet Mantra and Monsoon Harvest millet products but those pages were not opened. Comparator prices per 100 g were not verified."
}
</dossier>

Score every criterion in both lenses (R1-R6, S1-S4) and evaluate gates G1-G4.