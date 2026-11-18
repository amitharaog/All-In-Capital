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
- C004 [R1] (CampusCredit vs Jai Kisan, by Kushal (partner notes, Meeting 2)): Same sector, opposite answer: for any lender the deciding question is whether the founders own credit/default risk themselves. 'The NBFC partner handles it' is a low R1 regardless of distribution strength.  (matched on: credit, fintech)
</partner_corrections>

<dossier>
{
 "company": "RentRoute",
 "slug": "rentroute",
 "one_liner": "Mobile app that lets tenants pay rent by credit card, with the landlord paid by bank transfer through a payment aggregator partner.",
 "sector": "fintech",
 "sub_sector": "Consumer payments - rent via credit card",
 "stage": "Pre-seed",
 "ask": "INR 1.8 Cr at INR 12 Cr post-money",
 "business_model": "Users pay a 1.8% fee on rent; ~0.9% goes to the payment aggregator, leaving ~0.9% net take rate.",
 "founders": [
  {
   "name": "Sameer Qureshi",
   "role": "CEO",
   "background_claimed": "Product manager at a fintech for 4 years; launched two payments features.",
   "background_verified": null,
   "public_footprint": "not_found",
   "source_ids": [
    "D9",
    "F2"
   ]
  },
  {
   "name": "Divya Menon",
   "role": "Growth",
   "background_claimed": "5 years in consumer marketing.",
   "background_verified": null,
   "public_footprint": "not_found",
   "source_ids": [
    "D10",
    "F3"
   ]
  }
 ],
 "claims": [
  {
   "text": "Revenue is presented differently: deck shows 'INR 11 L revenue (1.8% fee)'; form says INR 11 L is gross and net revenue after the 0.9% paid to the payment partner is INR 5.5 L.",
   "source_ids": [
    "D4",
    "F6"
   ],
   "status": "contradicted",
   "note": "Deck reports gross fees as revenue; true net take rate is ~0.9% of rent volume."
  },
  {
   "text": "Deck reports '1,900 users'; form clarifies 1,900 registered of whom 1,100 have paid at least once.",
   "source_ids": [
    "D3",
    "F4"
   ],
   "status": "founder_stated",
   "note": "Not a numeric contradiction, but the deck omits that ~42% of registered users have never paid."
  },
  {
   "text": "Competition differs across sources: deck says 'We have no direct competitors'; the form itself acknowledges banks and card networks have changed rent-payment rules before; the web shows several platforms offering card rent payments (RedGiraffe, PayZapp, NoBroker per W7; HDFC PayZapp's own rent page lists credit card as a method, W10).",
   "source_ids": [
    "D6",
    "D7",
    "F8",
    "W7",
    "W10"
   ],
   "status": "contradicted",
   "note": "Deck claim is contradicted by independent sources; CRED, PhonePe and Paytm also offered the product until September 2025 (W2)."
  },
  {
   "text": "Rent paid: INR 6.1 Cr across 2,400 payments since July 2026 (avg ~INR 25,400 per payment); monthly volume grew 0.4 -> 1.0 -> 1.9 -> 2.8 Cr (Jul-Oct).",
   "source_ids": [
    "D5",
    "F5"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Acquisition: mostly organic/word of mouth; small paid tests cost ~INR 120 per registered user; cost per paying user not measured.",
   "source_ids": [
    "F7"
   ],
   "status": "founder_stated",
   "note": "At a 58% registered-to-paid rate, ~INR 207 per paying user vs ~INR 229 net revenue per average payment (25,400 x 0.9%) - payback depends on repeat monthly use, which is not reported."
  },
  {
   "text": "RentRoute pays landlords through a single payment aggregator partner and states that a change in bank or card-network rules would hit it directly.",
   "source_ids": [
    "F9",
    "F8"
   ],
   "status": "founder_stated",
   "note": "Founders acknowledge the defining risk but give no mitigation plan."
  },
  {
   "text": "In February 2024 the RBI instructed Visa to suspend all transactions involving business payment solution providers (BPSPs), which routed card payments such as rent through fintechs.",
   "source_ids": [
    "W1"
   ],
   "status": "verified",
   "note": null
  },
  {
   "text": "RBI's Payment Aggregator Directions (September 2025) require a PA to aggregate funds only for merchants with whom it has a contractual relationship and prohibit PAs from running marketplaces.",
   "source_ids": [
    "W5",
    "W6"
   ],
   "status": "verified",
   "note": "A landlord receiving card-funded rent must effectively be an onboarded merchant of the PA."
  },
  {
   "text": "CRED, PhonePe and Paytm halted credit-card rent payments in September 2025 following the RBI PA directions, because landlords were not onboarded with full merchant KYC.",
   "source_ids": [
    "W2",
    "W3",
    "W4"
   ],
   "status": "verified",
   "note": null
  },
  {
   "text": "By January 2026 some platforms (RedGiraffe, PayZapp, NoBroker) had restarted or continued card rent payments with stricter verification - PAN of both payer and payee plus rent agreement documents; PhonePe stayed out.",
   "source_ids": [
    "W7",
    "W8",
    "W9"
   ],
   "status": "verified",
   "note": "Shows a compliant route may exist, but with KYC friction RentRoute does not describe (deck: 'Enter your landlord's bank details once')."
  },
  {
   "text": "Whether RentRoute's flow complies with the 2025 PA directions (landlord onboarded as the PA's merchant with KYC) is not established by the application.",
   "source_ids": [
    "F9",
    "D2",
    "W5"
   ],
   "status": "unverifiable",
   "note": "Relevant to gate G2 (exists only if the rules are favourable): the business launched in July 2026, after the rules that shut the incumbents' version."
  },
  {
   "text": "Planned issuer referral income ('Referral income from card issuers is coming') is unsupported in the application.",
   "source_ids": [
    "D8"
   ],
   "status": "founder_stated",
   "note": "No issuer partnership named."
  },
  {
   "text": "Founders: Sameer Qureshi (CEO) claims 4 years as a fintech product manager who launched two payments features; Divya Menon (Growth) claims 5 years in consumer marketing. Engineering is outsourced to contract developers. Sameer full-time since June 2026, Divya since August 2026.",
   "source_ids": [
    "D9",
    "D10",
    "D11",
    "F10",
    "F14"
   ],
   "status": "founder_stated",
   "note": "No in-house engineering or compliance/payments-regulation lead on the team."
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
   "text": "Market sizing is top-down: INR 1.5 lakh Cr annual urban rent, 'capturing just 1%' = INR 1,500 Cr volume.",
   "source_ids": [
    "D14"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "12-month target INR 20 Cr monthly rent volume (~7x October); 55% of the raise goes to marketing.",
   "source_ids": [
    "D12",
    "D13"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Raising INR 1.8 Cr at INR 12 Cr post-money; no outside investors; founders have put in INR 18 L and own 100%.",
   "source_ids": [
    "F12",
    "F11"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Sector as selected (Fintech) matches the business: a consumer payments app (rent via credit card).",
   "source_ids": [
    "D1"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Founders frame rent as a large, underserved payment category and the problem as landlords not accepting cards.",
   "source_ids": [
    "F13",
    "D15"
   ],
   "status": "founder_stated",
   "note": null
  }
 ],
 "gaps": [
  {
   "what": "Sameer Qureshi (CEO): no public footprint confirming 4 years as a fintech product manager.",
   "why_it_matters": "Payments-product experience is the main founder claim in a regulator-exposed category.",
   "searched": [
    "WebSearch: \"Sameer Qureshi\" RentRoute Bengaluru rent credit card (2026-11-18) - no match; generic rent-by-card pages",
    "Application LinkedIn link linkedin.com/in/sameer-qureshi- example is a placeholder"
   ],
   "ask_founder": "Which fintech, which two payments features, and did you work with PA/compliance teams?",
   "blocks_criteria": [
    "S3"
   ]
  },
  {
   "what": "Divya Menon (Growth): no public footprint confirming 5 years in consumer marketing.",
   "why_it_matters": "Growth lead for a plan that puts 55% of funds into marketing.",
   "searched": [
    "WebSearch: \"Divya Menon\" RentRoute growth Bengaluru (2026-11-18) - no match",
    "Application LinkedIn link linkedin.com/in/divya-menon-example is a placeholder"
   ],
   "ask_founder": "Which brands/companies and what channels did you run?",
   "blocks_criteria": [
    "S3"
   ]
  },
  {
   "what": "Company existence: no website, app-store listing or MCA record found for RentRoute Technologies Pvt. Ltd.",
   "why_it_matters": "Basic verification; 1,900 users should leave an app-store footprint.",
   "searched": [
    "WebSearch: RentRoute app pay rent with credit card India (2026-11-18) - no result",
    "Website www.rentroute.example is a placeholder",
    "MCA portal not queried"
   ],
   "ask_founder": "Share app-store links and CIN.",
   "blocks_criteria": [
    "R4"
   ]
  },
  {
   "what": "Regulatory compliance of the payment flow under RBI's 2025 PA Directions: is each landlord onboarded as the PA's merchant with KYC, and who is the PA?",
   "why_it_matters": "Incumbents (CRED, PhonePe, Paytm) exited this exact product over this rule; if RentRoute's flow is not compliant the business can be switched off overnight.",
   "searched": [
    "Web: Entrackr, Inc42, IndiaCorpLaw, Whalesbook (W2-W9)",
    "Form Dependencies and What have you built?"
   ],
   "ask_founder": "Which payment aggregator do you use, does it KYC each landlord as a merchant, do you collect payer/payee PAN and rent agreements, and has the PA confirmed the flow in writing against the September 2025 directions?",
   "blocks_criteria": [
    "R1",
    "R4"
   ]
  },
  {
   "what": "Card-network / issuer stance: treatment of rent transactions as commercial/BPSP payments and issuer fees or reward exclusions on rent.",
   "why_it_matters": "Network or issuer changes (as in February 2024) directly remove the product's value proposition.",
   "searched": [
    "Web: RBI-Visa BPSP suspension (W1)",
    "Deck slide 8"
   ],
   "ask_founder": "Which card networks and issuers currently work on your flow, and what happens to users if issuers stop rewards on rent?",
   "blocks_criteria": [
    "R1"
   ]
  },
  {
   "what": "Repeat monthly usage: share of paying users who pay rent again the following month; fraud/chargeback rate.",
   "why_it_matters": "Trust/repeat usage is a key fintech metric; rent is monthly so repeat should be measurable. Rent-by-card is also a known channel for cash-out abuse.",
   "searched": [
    "Deck slide 5",
    "Form Users / Rent volume"
   ],
   "ask_founder": "Of users who paid in August, what share paid again in September and October? Any chargebacks or fake-landlord cases?",
   "blocks_criteria": [
    "R3"
   ]
  },
  {
   "what": "Mitigation plan for single-PA dependency.",
   "why_it_matters": "Founders name the risk but give no plan; precedent rewards founders who own the defining risk.",
   "searched": [
    "Form Dependencies"
   ],
   "ask_founder": "What is your plan if the PA partner drops rent payments - second PA, landlord-side onboarding, or a pivot?",
   "blocks_criteria": [
    "R1"
   ]
  }
 ],
 "competitors_named": [],
 "competitors_found": [
  "CRED (RentPay, halted Sep 2025)",
  "PhonePe (exited)",
  "Paytm (halted Sep 2025)",
  "RedGiraffe",
  "HDFC PayZapp",
  "NoBroker"
 ],
 "keywords": [
  "rent payment",
  "credit card",
  "tenant",
  "landlord",
  "bill payment",
  "card rewards",
  "payment aggregator",
  "consumer payments",
  "rent"
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
   "quote": "Pay your rent with your credit card"
  },
  {
   "id": "D2",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 4 (product)",
   "retrieved_on": null,
   "quote": "Rent reaches the landlord's bank account within a day."
  },
  {
   "id": "D3",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "1,900 users"
  },
  {
   "id": "D4",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "INR 11 L revenue (1.8% fee)"
  },
  {
   "id": "D5",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "Traction: INR 6.1 Cr of rent paid in 4 months"
  },
  {
   "id": "D6",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 7 (competition)",
   "retrieved_on": null,
   "quote": "We have no direct competitors."
  },
  {
   "id": "D7",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 7 (competition)",
   "retrieved_on": null,
   "quote": "Existing payment apps focus on other bills like electricity, mobile and credit card repayments."
  },
  {
   "id": "D8",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 8 (revenue model)",
   "retrieved_on": null,
   "quote": "Referral income from card issuers is coming."
  },
  {
   "id": "D9",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 9 (team)",
   "retrieved_on": null,
   "quote": "Product manager at a fintech for 4 years. Launched two payments features."
  },
  {
   "id": "D10",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 9 (team)",
   "retrieved_on": null,
   "quote": "5 years in consumer marketing."
  },
  {
   "id": "D11",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 9 (team)",
   "retrieved_on": null,
   "quote": "Engineering handled by contract developers."
  },
  {
   "id": "D12",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 10 (ask)",
   "retrieved_on": null,
   "quote": "In 12 months: INR 20 Cr monthly rent volume."
  },
  {
   "id": "D13",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 10 (ask)",
   "retrieved_on": null,
   "quote": "55% Marketing"
  },
  {
   "id": "D14",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 6 (market)",
   "retrieved_on": null,
   "quote": "Capturing just 1% would mean INR 1,500 Cr of annual rent volume."
  },
  {
   "id": "D15",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 3 (problem)",
   "retrieved_on": null,
   "quote": "Landlords will not accept cards, so reward points go unused."
  },
  {
   "id": "F1",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Company > Website",
   "retrieved_on": null,
   "quote": "www.rentroute.example"
  },
  {
   "id": "F2",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "linkedin.com/in/sameer-qureshi- example"
  },
  {
   "id": "F3",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 2",
   "retrieved_on": null,
   "quote": "linkedin.com/in/divya-menon-example"
  },
  {
   "id": "F4",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Users",
   "retrieved_on": null,
   "quote": "1,900 registered. 1,100 have paid at least once."
  },
  {
   "id": "F5",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Rent volume",
   "retrieved_on": null,
   "quote": "INR 6.1 Cr paid since July 2026 across 2,400 payments."
  },
  {
   "id": "F6",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Revenue",
   "retrieved_on": null,
   "quote": "Users pay a 1.8% fee: INR 11 L gross. After the 0.9% we pay the payment partner, net revenue is INR 5.5 L."
  },
  {
   "id": "F7",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Customer acquisition",
   "retrieved_on": null,
   "quote": "In small paid tests we saw about INR 120 per registered user. We have not measured cost per paying user."
  },
  {
   "id": "F8",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Dependencies",
   "retrieved_on": null,
   "quote": "We rely on a single payment aggregator partner. Banks and card networks have changed rules on rent payments before, and a change would hit us directly."
  },
  {
   "id": "F9",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > What have you built?",
   "retrieved_on": null,
   "quote": "We pay the landlord's bank account through a payment aggregator partner."
  },
  {
   "id": "F10",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Time commitment",
   "retrieved_on": null,
   "quote": "Sameer full-time since June 2026. Divya full-time since August 2026."
  },
  {
   "id": "F11",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > Existing investors",
   "retrieved_on": null,
   "quote": "None. Founders have put in INR 18 L of savings."
  },
  {
   "id": "F12",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > Valuation expectation",
   "retrieved_on": null,
   "quote": "INR 12 Cr post-money"
  },
  {
   "id": "F13",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Anything else",
   "retrieved_on": null,
   "quote": "We believe rent is a large, underserved payment category."
  },
  {
   "id": "F14",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Company > Team size",
   "retrieved_on": null,
   "quote": "4 (2 founders, 2 contract developers)"
  },
  {
   "id": "W1",
   "kind": "web",
   "title": "Visa, Mastercard to stop commercial card payments via fintech intermediaries in India (Fintech News Singapore, 15 Feb 2024)",
   "url": "https://fintechnews.sg/86371/fintech-india/visa-mastercard-to-stop-commercial-card-payments-via-fintech-intermediaries-in-india/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "The communication from the RBI instructed Visa to temporarily suspend all transactions involving BPSPs."
  },
  {
   "id": "W2",
   "kind": "web",
   "title": "CRED, PhonePe, Paytm stop rent payments via credit cards (Entrackr, 17 Sep 2025)",
   "url": "https://entrackr.com/news/cred-phonepe-paytm-stop-rent-payments-via-credit-cards-10474094",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "CRED, PhonePe, and Paytm have halted rent payments via credit cards on their platforms."
  },
  {
   "id": "W3",
   "kind": "web",
   "title": "CRED, PhonePe, Paytm stop rent payments via credit cards (Entrackr) - cause",
   "url": "https://entrackr.com/news/cred-phonepe-paytm-stop-rent-payments-via-credit-cards-10474094",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "The move follows the Reserve Bank of India’s (RBI) latest master directions on payment aggregator regulations."
  },
  {
   "id": "W4",
   "kind": "web",
   "title": "PhonePe, Paytm & CRED halt rent payments via credit cards (Inc42, 18 Sep 2025)",
   "url": "https://inc42.com/?p=532025",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Rent payments routed via fintechs were impacted as landlords are not often onboarded on fintech platforms with full KYC"
  },
  {
   "id": "W5",
   "kind": "web",
   "title": "Decoding RBI's overhaul of the Payment Aggregator Directions (IndiaCorpLaw, 9 Oct 2025)",
   "url": "https://indiacorplaw.in/2025/10/09/decoding-rbis-overhaul-of-the-payment-aggregator-directions/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "mandate that a PA shall aggregate funds only for the merchant with whom it has a contractual relationship."
  },
  {
   "id": "W6",
   "kind": "web",
   "title": "Decoding RBI's overhaul of the Payment Aggregator Directions (IndiaCorpLaw) - marketplaces",
   "url": "https://indiacorplaw.in/2025/10/09/decoding-rbis-overhaul-of-the-payment-aggregator-directions/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "The 2025 directions further prohibit PAs from running marketplaces"
  },
  {
   "id": "W7",
   "kind": "web",
   "title": "Fintech rent payments resume amidst RBI scrutiny; PhonePe stays out (Whalesbook, 27 Jan 2026)",
   "url": "https://www.whalesbook.com/news/English/tech/Fintech-Rent-Payments-Resume-Amidst-RBI-Scrutiny-PhonePe-Stays-Out/6978a52d657adf9c86c60534",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "have either quietly restarted or continued to offer rent payment facilities."
  },
  {
   "id": "W8",
   "kind": "web",
   "title": "Fintech rent payments resume (Whalesbook) - new verification requirements",
   "url": "https://www.whalesbook.com/news/English/tech/Fintech-Rent-Payments-Resume-Amidst-RBI-Scrutiny-PhonePe-Stays-Out/6978a52d657adf9c86c60534",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "including the mandatory submission of PAN cards for both payer and payee, alongside rent agreement documents"
  },
  {
   "id": "W9",
   "kind": "web",
   "title": "Fintech rent payments resume (Whalesbook) - PhonePe",
   "url": "https://www.whalesbook.com/news/English/tech/Fintech-Rent-Payments-Resume-Amidst-RBI-Scrutiny-PhonePe-Stays-Out/6978a52d657adf9c86c60534",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Walmart-owned PhonePe has elected to maintain its discontinuation of rent payment services."
  },
  {
   "id": "W10",
   "kind": "web",
   "title": "Pay rent in Bengaluru - PayZapp (HDFC Bank)",
   "url": "https://www.hdfc.bank.in/ps/payzapp/rent/bengaluru",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Transfer rent digitally via UPI, Credit Card, Debit Card or Zapp Account on PayZapp."
  }
 ],
 "produced_by": "claude-code-session (in-session run of prompts/research.md; no API key)",
 "research_notes": "Founder and company searches returned nothing (placeholder links). Business Standard article on the September 2025 shutdown returned 403; Inc42, Entrackr and IndiaCorpLaw used instead. Search snippets also reported HDFC Bank's June 2024 1% fee on card rent payments and ICICI/SBI Card removing rewards on rent, but no page with a verbatim quote was retrieved for these, so they are not cited as sources. Whalesbook (Jan 2026) is a lesser-known outlet; its report that some platforms resumed rent payments should be confirmed."
}
</dossier>

Score every criterion in both lenses (R1-R6, S1-S4) and evaluate gates G1-G4.