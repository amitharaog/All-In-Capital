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
- C002 [R1] (AeroDrop, by Kushal (partner notes, Meeting 3)): Riya scored 7.5 partly on the founder's excellent credentials. Credentials are not a business: score the evidence, not the pedigree, and score founder quality separately from path to market.  (matched on: credentials_heavy, deeptech, regulatory_dependency)
</partner_corrections>

<dossier>
{
 "company": "Pumpwise",
 "slug": "pumpwise",
 "one_liner": "Clip-on vibration and temperature sensors with a self-learning model that sends WhatsApp alerts before small-factory motors and pumps fail.",
 "sector": "deeptech",
 "sub_sector": "Industrial IoT predictive maintenance for MSME factories",
 "stage": "Pre-seed",
 "ask": "INR 2.2 Cr at INR 11 Cr post-money",
 "business_model": "Hardware sale (INR 9,500 per sensor, INR 3,200 cost) plus INR 750 per sensor per month subscription at ~85% gross margin.",
 "founders": [
  {
   "name": "Karthik Subramanian",
   "role": "CEO",
   "background_claimed": "IIT Madras (mechanical); 5 years as a reliability engineer at an engine maker.",
   "background_verified": null,
   "public_footprint": "not_found",
   "source_ids": [
    "D11",
    "F2"
   ]
  },
  {
   "name": "Neeraj Pillai",
   "role": "CTO",
   "background_claimed": "4 years in embedded systems at an auto-components supplier; designed the sensor board and firmware.",
   "background_verified": null,
   "public_footprint": "not_found",
   "source_ids": [
    "D12",
    "F3"
   ]
  }
 ],
 "claims": [
  {
   "text": "6 of 11 pilots converted to paid (55%); 140 paid sensors live, averaging 23 per paying customer; monthly recurring subscription INR 1.05 L.",
   "source_ids": [
    "D4",
    "D5",
    "F4"
   ],
   "status": "founder_stated",
   "note": "Internally consistent: 140 x INR 750 = INR 1.05 L MRR. Paid sensors grew 20 -> 48 -> 80 -> 112 -> 140 from June to October (D6)."
  },
  {
   "text": "Cumulative subscription revenue looks too low for the deck's sensor ramp: form gives INR 14.2 L cumulative revenue of which INR 13.3 L hardware, leaving ~INR 0.9 L non-hardware; the deck's paid-sensor chart at INR 750/sensor/month implies roughly INR 3 L of subscription billed June-October.",
   "source_ids": [
    "F5",
    "D6",
    "D9"
   ],
   "status": "contradicted",
   "note": "Arithmetic from the founders' own figures (20+48+80+112+140 sensor-months x INR 750 = INR 3.0 L). Possible explanations: free months after pilots, annual billing, or unpaid invoices. Hardware (INR 13.3 L = 140 x 9,500) is ~94% of revenue to date."
  },
  {
   "text": "Business is hardware-heavy today: INR 9,500 per sensor against INR 3,200 cost, plus INR 750 per sensor per month subscription at ~85% gross margin; average customer worth ~INR 3.1 L first-year gross profit.",
   "source_ids": [
    "D8",
    "D9",
    "D10"
   ],
   "status": "founder_stated",
   "note": "Checks out: 23 x 6,300 hardware GP + 23 x 750 x 12 x 0.85 = ~INR 3.2 L. Most of it is one-off hardware margin, so 'payback' (D19) is mostly hardware-funded."
  },
  {
   "text": "Cost per paid customer is ~INR 73,000 (INR 4.4 L cost of 11 pilots / 6 paid customers), excluding founder time; a pilot is 10 free sensors for 30 days.",
   "source_ids": [
    "D7",
    "F6"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Channels: 3 of 6 paid customers via a cluster association, 2 via a pump distributor, 1 direct.",
   "source_ids": [
    "F14"
   ],
   "status": "founder_stated",
   "note": "Channel concentration: one association accounts for half of paid customers."
  },
  {
   "text": "Customers report 9 unplanned stoppages caught early during pilots at an estimated INR 1.8 L downtime cost each; the founders state these are customer-reported and unaudited.",
   "source_ids": [
    "F8",
    "F7"
   ],
   "status": "founder_stated",
   "note": "This is the closest thing to the deeptech 'live-site pilot result'. Founders flag it as unaudited themselves, which is a good sign of candour."
  },
  {
   "text": "Founders visited 38 plants in the Pune and Coimbatore clusters (Nov 2025-Feb 2026) before scaling pilots.",
   "source_ids": [
    "D2"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Founders name their own key risks: sensor accuracy across motor types, hardware supply, and longer sales cycles in larger plants.",
   "source_ids": [
    "F9"
   ],
   "status": "founder_stated",
   "note": "Relevant to R1 (owns the defining risk)."
  },
  {
   "text": "12-month targets are internally inconsistent: 30 paying customers at the current ~23 sensors each would be ~690 sensors, i.e. ~INR 5.2 L MRR at INR 750/sensor, not the INR 12 L MRR targeted (which needs ~1,600 sensors, ~53 per customer).",
   "source_ids": [
    "D14",
    "F4",
    "D9"
   ],
   "status": "founder_stated",
   "note": "Derived from the founders' own numbers; ask which assumption (sensors per customer, price, or customer count) drives the INR 12 L."
  },
  {
   "text": "25% of the raise is earmarked for 'Certification and operations', but the application does not name which certifications are needed or the timeline.",
   "source_ids": [
    "D15"
   ],
   "status": "founder_stated",
   "note": "Sensors use low-power radios (D18). Wireless devices sold in India generally need WPC Equipment Type Approval (W5, framed by the source for imports); the founders should state their certification path."
  },
  {
   "text": "Deck claims imported condition monitors cost INR 40,000+ per motor with annual contracts.",
   "source_ids": [
    "D3"
   ],
   "status": "unverifiable",
   "note": "Pricing of imported systems not verified; no page with a citable price was retrieved."
  },
  {
   "text": "Pune-based Infinite Uptime, a predictive-maintenance provider for industrial machinery, raised USD 35M Series C (March 2025, led by Avataar Ventures).",
   "source_ids": [
    "W1",
    "W2"
   ],
   "status": "verified",
   "note": "Well-funded competitor in the same city; deck positions only against 'imported systems' and manual rounds."
  },
  {
   "text": "Pump maker Kirloskar Brothers sells KirloSmart, an IoT pump-monitoring system that generates alerts for probable causes of pump failure.",
   "source_ids": [
    "W3"
   ],
   "status": "verified",
   "note": "Incumbent pump OEM with its own monitoring product; also a possible channel/partner given Pumpwise sells through pump distributors."
  },
  {
   "text": "A BITS Pilani Hyderabad startup launched machine health monitoring products for MSMEs (Mach-Sevak for smaller units) in 2025.",
   "source_ids": [
    "W4"
   ],
   "status": "verified",
   "note": "Evidence of other MSME-focused monitoring entrants."
  },
  {
   "text": "Founders: Karthik Subramanian (CEO) claims IIT Madras mechanical engineering and 5 years as a reliability engineer at an engine maker; Neeraj Pillai (CTO) claims 4 years in embedded systems at an auto-components supplier and designed the sensor and firmware. No prior startup experience; full-time since October 2025.",
   "source_ids": [
    "D11",
    "D12",
    "F12",
    "F16"
   ],
   "status": "founder_stated",
   "note": "Pedigree (IIT) is capped by the fund's pedigree rule; relevant domain experience is the stronger signal but unverified."
  },
  {
   "text": "Founder LinkedIn links are placeholders (*-example) and the website is a .example domain; no independent footprint for the founders or the company was found.",
   "source_ids": [
    "F2",
    "F3",
    "F1"
   ],
   "status": "unverifiable",
   "note": null
  },
  {
   "text": "Team of 7; sensors made by a contract manufacturer in Pune.",
   "source_ids": [
    "D13"
   ],
   "status": "founder_stated",
   "note": "Single contract manufacturer = supply risk the founders themselves list (F9)."
  },
  {
   "text": "Market sizing (TAM INR 16,200 Cr) assumes 300K MSMEs with 20+ motors, a share derived from the founders' own plant visits; subscription only.",
   "source_ids": [
    "D16"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Sector as selected is Deeptech; the business is industrial IoT hardware plus subscription analytics, which fits deeptech.",
   "source_ids": [
    "F13",
    "D1"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Raising INR 2.2 Cr at INR 11 Cr post-money; existing capital INR 30 L (INR 10 L incubator grant + INR 20 L from two angels).",
   "source_ids": [
    "F10",
    "F11"
   ],
   "status": "founder_stated",
   "note": "Incubator not named."
  },
  {
   "text": "Founders invite scrutiny of manufacturing scale-up and calibration and offer to share pilot data.",
   "source_ids": [
    "F15"
   ],
   "status": "founder_stated",
   "note": null
  }
 ],
 "gaps": [
  {
   "what": "Karthik Subramanian (CEO): no public footprint confirming IIT Madras or the reliability-engineer role at an engine maker.",
   "why_it_matters": "Domain credibility in reliability engineering is the core founder claim.",
   "searched": [
    "WebSearch: \"Karthik Subramanian\" Pumpwise Pune predictive maintenance (2026-11-18) - no match; results were Infinite Uptime, Kirloskar, others",
    "Application LinkedIn link linkedin.com/in/karthik- subramanian-example is a placeholder"
   ],
   "ask_founder": "Which engine maker, which years, and can we see your IIT Madras degree or speak to a former manager?",
   "blocks_criteria": [
    "S3",
    "R2"
   ]
  },
  {
   "what": "Neeraj Pillai (CTO): no public footprint confirming embedded-systems work at an auto-components supplier.",
   "why_it_matters": "He designed the sensor and firmware; hardware execution risk sits with him.",
   "searched": [
    "WebSearch: \"Neeraj Pillai\" Pumpwise embedded Pune (2026-11-18) - only an unrelated Mumbai product manager profile",
    "Application LinkedIn link linkedin.com/in/neeraj-pillai-example is a placeholder"
   ],
   "ask_founder": "Which supplier and products did you work on; any prior hardware shipped at volume?",
   "blocks_criteria": [
    "S3",
    "R4"
   ]
  },
  {
   "what": "Company existence: no website, MCA record, press or customer reference found for Pumpwise Technologies Pvt. Ltd.",
   "why_it_matters": "Basic verification of entity and customers.",
   "searched": [
    "WebSearch: Pumpwise Technologies Pune motor pump sensor (2026-11-18) - no result",
    "Website www.pumpwise.example is a placeholder",
    "MCA portal not queried"
   ],
   "ask_founder": "Share CIN, and introductions to two paying customers and the cluster association.",
   "blocks_criteria": [
    "R4"
   ]
  },
  {
   "what": "Subscription revenue reconciliation: ~INR 0.9 L cumulative non-hardware revenue vs ~INR 3 L implied by the paid-sensor ramp.",
   "why_it_matters": "Recurring revenue is the deciding quality-of-revenue question for a hardware+SaaS model.",
   "searched": [
    "Form Revenue answer vs deck slide 6 chart and slide 9 pricing"
   ],
   "ask_founder": "How much subscription has actually been invoiced and collected to date, by month, and are any customers on free months?",
   "blocks_criteria": [
    "R3"
   ]
  },
  {
   "what": "Measured model accuracy: false-alert and missed-failure rates across motor types.",
   "why_it_matters": "The founders list accuracy as their top risk; the only value evidence is 9 customer-reported catches, unaudited.",
   "searched": [
    "Deck slides 5-6",
    "Form Evidence of value and Key risks"
   ],
   "ask_founder": "Across 140 sensors, how many alerts fired, how many were confirmed faults, and were any failures missed?",
   "blocks_criteria": [
    "R3",
    "R1"
   ]
  },
  {
   "what": "Certification and regulatory path: which approvals (e.g. WPC ETA for the radio, any electrical/hazardous-area certifications) and timeline.",
   "why_it_matters": "A quarter of the raise is for certification; deeptech key metric is the certification path.",
   "searched": [
    "Deck slide 12",
    "Web: WPC ETA requirement (W5)"
   ],
   "ask_founder": "Which certifications do you need before selling to larger plants, what do they cost and when will you have them?",
   "blocks_criteria": [
    "R4"
   ]
  },
  {
   "what": "Liability if a monitored motor fails without an alert; contract terms and insurance.",
   "why_it_matters": "Deeptech key metric 'liability and insurance' is absent from the application.",
   "searched": [
    "Deck and form - not mentioned"
   ],
   "ask_founder": "What do your customer contracts say about missed failures, and do you carry product liability cover?",
   "blocks_criteria": [
    "R4"
   ]
  },
  {
   "what": "Retention of paying customers beyond month one; sensor expansion per customer.",
   "why_it_matters": "Paid customers are at most 5 months old; no churn or expansion data.",
   "searched": [
    "Deck slide 6",
    "Form Customers"
   ],
   "ask_founder": "Have any of the 6 paying customers added sensors or cancelled subscriptions?",
   "blocks_criteria": [
    "R3"
   ]
  }
 ],
 "competitors_named": [
  "Imported condition-monitoring systems (unnamed)",
  "Manual technician rounds"
 ],
 "competitors_found": [
  "Infinite Uptime (Pune)",
  "Kirloskar Brothers KirloSmart",
  "BITS Pilani Hyderabad startup (Mach-Sevak / Mach-Nirikshak)"
 ],
 "keywords": [
  "predictive maintenance",
  "condition monitoring",
  "vibration sensor",
  "motor monitoring",
  "pump monitoring",
  "industrial IoT",
  "factory downtime",
  "MSME manufacturing",
  "WhatsApp alerts",
  "anomaly detection"
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
   "quote": "Predictive maintenance for small-factory motors and pumps"
  },
  {
   "id": "D2",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 3 (problem)",
   "retrieved_on": null,
   "quote": "From visits to 38 plants in the Pune and Coimbatore clusters, Nov 2025 to Feb 2026."
  },
  {
   "id": "D3",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 3 (problem)",
   "retrieved_on": null,
   "quote": "Imported condition monitors cost INR 40,000+ per motor, with annual contracts."
  },
  {
   "id": "D4",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 6 (traction)",
   "retrieved_on": null,
   "quote": "6 of 11 pilots converted to paid"
  },
  {
   "id": "D5",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 6 (traction)",
   "retrieved_on": null,
   "quote": "INR 1.05 L monthly recurring"
  },
  {
   "id": "D6",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 6 (traction)",
   "retrieved_on": null,
   "quote": "Chart: Paid sensors deployed"
  },
  {
   "id": "D7",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 8 (GTM)",
   "retrieved_on": null,
   "quote": "CAC = cost of 11 pilots (INR 4.4 L) / 6 paid customers. A pilot is 10 free sensors for 30 days."
  },
  {
   "id": "D8",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 9 (revenue model)",
   "retrieved_on": null,
   "quote": "INR 9,500 per sensor. Cost to us: INR 3,200."
  },
  {
   "id": "D9",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 9 (revenue model)",
   "retrieved_on": null,
   "quote": "INR 750 per sensor a month at about 85% gross margin."
  },
  {
   "id": "D10",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 9 (revenue model)",
   "retrieved_on": null,
   "quote": "Average customer: 23 sensors and INR 3.1 L first-year gross profit."
  },
  {
   "id": "D11",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 11 (team)",
   "retrieved_on": null,
   "quote": "IIT Madras, mechanical. 5 years as a reliability engineer at an engine maker."
  },
  {
   "id": "D12",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 11 (team)",
   "retrieved_on": null,
   "quote": "4 years in embedded systems at an auto- components supplier. Designed the sensor and firmware."
  },
  {
   "id": "D13",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 11 (team)",
   "retrieved_on": null,
   "quote": "Team of 7. Sensors made by a contract manufacturer in Pune."
  },
  {
   "id": "D14",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 12 (ask)",
   "retrieved_on": null,
   "quote": "In 12 months: 30 paying customers, INR 12 L monthly recurring, pilot-to-paid at 65%."
  },
  {
   "id": "D15",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 12 (ask)",
   "retrieved_on": null,
   "quote": "25% Certification and operations"
  },
  {
   "id": "D16",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 7 (market size)",
   "retrieved_on": null,
   "quote": "based on our plant visits. Subscription revenue only; hardware excluded."
  },
  {
   "id": "D17",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (product)",
   "retrieved_on": null,
   "quote": "WhatsApp alert when behaviour drifts, days before failure."
  },
  {
   "id": "D18",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 4 (why now)",
   "retrieved_on": null,
   "quote": "Low-power radios and Indian mobile data make remote monitoring affordable."
  },
  {
   "id": "D19",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 8 (GTM)",
   "retrieved_on": null,
   "quote": "payback on first-year gross profit"
  },
  {
   "id": "F1",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Company > Website",
   "retrieved_on": null,
   "quote": "www.pumpwise.example"
  },
  {
   "id": "F2",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "linkedin.com/in/karthik- subramanian-example"
  },
  {
   "id": "F3",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 2",
   "retrieved_on": null,
   "quote": "linkedin.com/in/neeraj-pillai-example"
  },
  {
   "id": "F4",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Customers",
   "retrieved_on": null,
   "quote": "11 pilots started since March 2026. 6 converted to paid, across 140 sensors (average 23 per customer)."
  },
  {
   "id": "F5",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Revenue",
   "retrieved_on": null,
   "quote": "INR 14.2 L cumulative, of which hardware INR 13.3 L. Monthly recurring subscription INR 1.05 L."
  },
  {
   "id": "F6",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Customer acquisition",
   "retrieved_on": null,
   "quote": "This excludes founder time."
  },
  {
   "id": "F7",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Evidence of value",
   "retrieved_on": null,
   "quote": "These figures are customer-reported, not audited."
  },
  {
   "id": "F8",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Evidence of value",
   "retrieved_on": null,
   "quote": "Customers report 9 unplanned stoppages caught early during pilots, estimated by them at INR 1.8 L average downtime cost each."
  },
  {
   "id": "F9",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Key risks",
   "retrieved_on": null,
   "quote": "Sensor accuracy across motor types, hardware supply, and longer sales cycles in larger plants."
  },
  {
   "id": "F10",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > Valuation expectation",
   "retrieved_on": null,
   "quote": "INR 11 Cr post-money"
  },
  {
   "id": "F11",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > Existing investors",
   "retrieved_on": null,
   "quote": "INR 30 L: a INR 10 L incubator grant and two angels (INR 20 L)."
  },
  {
   "id": "F12",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Time commitment",
   "retrieved_on": null,
   "quote": "Both full-time since October 2025."
  },
  {
   "id": "F13",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Company > Sector (as selected)",
   "retrieved_on": null,
   "quote": "Deeptech"
  },
  {
   "id": "F14",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Customer acquisition",
   "retrieved_on": null,
   "quote": "3 of 6 paid customers came through a cluster association, 2 through a pump distributor, 1 direct."
  },
  {
   "id": "F15",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Anything else",
   "retrieved_on": null,
   "quote": "We would value a conversation about manufacturing scale-up and calibration. Happy to share pilot data."
  },
  {
   "id": "F16",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Prior startup experience",
   "retrieved_on": null,
   "quote": "None for either founder."
  },
  {
   "id": "W1",
   "kind": "web",
   "title": "Infinite Uptime raises $35 Mn in Series C round (Entrackr, 11 Mar 2025)",
   "url": "https://entrackr.com/news/infinite-uptime-raises-35-mn-in-series-c-round-8841757",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "has secured $35 million in its Series C round, led by Avataar Ventures"
  },
  {
   "id": "W2",
   "kind": "web",
   "title": "Infinite Uptime raises $35 Mn in Series C round (Entrackr) - company description",
   "url": "https://entrackr.com/news/infinite-uptime-raises-35-mn-in-series-c-round-8841757",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "a provider of predictive maintenance solutions for industrial machinery."
  },
  {
   "id": "W3",
   "kind": "web",
   "title": "Kirloskar Brothers IoT pump monitoring KirloSmart (The Machine Maker, 10 Aug 2022)",
   "url": "https://themachinemaker.com/news/kirloskar-1008/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "can generate alerts for the probable causes leading to the failure of the pump."
  },
  {
   "id": "W4",
   "kind": "web",
   "title": "BITS Pilani Hyderabad startup unveils smart machine health monitoring solutions for MSMEs (The Hans India, 1 Aug 2025)",
   "url": "https://assets.thehansindia.com/business/bits-pilani-hyderabad-startup-unveils-smart-machine-health-monitoring-solutions-for-msmes-993095",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Mach-Sevak, tailored for smaller units, offers real-time monitoring of machines of the same type."
  },
  {
   "id": "W5",
   "kind": "web",
   "title": "WPC approval (Aleph India, certification consultancy)",
   "url": "https://alephindia.in/wpc-approval.php",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Equipment Type Approval (ETA) is an approval that has to be obtained from WPC before importing any wireless device in India"
  }
 ],
 "produced_by": "claude-code-session (in-session run of prompts/research.md; no API key)",
 "research_notes": "Founder and company searches returned nothing (placeholder links). Search results also mentioned Nanoprecise, Petasense, Covacsis and ABB Ability Smart Sensor as monitoring products; those pages were not successfully retrieved (403/503) so they are not cited. A marketplace listing of a ~INR 12,500 wireless vibration sensor appeared in search snippets but the page returned 429, so the deck's 'INR 40,000+' imported-monitor price could neither be confirmed nor rebutted. Udyam manufacturing-MSME count (deck's ~2.5M) not verified."
}
</dossier>

Score every criterion in both lenses (R1-R6, S1-S4) and evaluate gates G1-G4.