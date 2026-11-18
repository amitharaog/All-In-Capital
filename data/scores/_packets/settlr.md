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
- C004 [R1] (CampusCredit vs Jai Kisan, by Kushal (partner notes, Meeting 2)): Same sector, opposite answer: for any lender the deciding question is whether the founders own credit/default risk themselves. 'The NBFC partner handles it' is a low R1 regardless of distribution strength.  (matched on: fintech, lending, lending_risk)
- C003 ((meeting-notes startup), by Kushal / Aditya (partner notes, Meeting 4)): Scored 7 before anyone noticed it overlaps portfolio company MeetRecord. Check every application against the full portfolio list; default is no to competitors unless both founders know. Prefer a false-alarm flag to a miss.  (matched on: portfolio_overlap)
</partner_corrections>

<dossier>
{
 "company": "Settlr",
 "slug": "settlr",
 "one_liner": "Invoicing, payment collection (payment links via UPI/card/bank transfer) and NBFC-funded invoice financing for Indian SMEs.",
 "sector": "fintech",
 "sub_sector": "SME payments and invoice financing (lending service provider to NBFC partners)",
 "stage": "Series A",
 "ask": "INR 30 Cr at INR 180 Cr post-money; seeking a lead",
 "business_model": "0.4% fee on payments collected plus about 1.2% a month on invoices financed, with financing funded through NBFC partners. Founder-stated October 2026: INR 86 Cr payment volume, INR 78 L net revenue, 1,150 SMEs, 58% gross margin.",
 "founders": [
  {
   "name": "Rahul Mehta",
   "role": "CEO",
   "background_claimed": "10 years in transaction banking; led SME product at a private bank.",
   "background_verified": "Not verified. LinkedIn link is a placeholder; the bank is not named. Searches for name + Settlr + Mumbai returned only unrelated invoice-financing companies.",
   "public_footprint": "not_found",
   "source_ids": [
    "D10",
    "F8"
   ]
  },
  {
   "name": "Sonal Iyer",
   "role": "CTO",
   "background_claimed": "8 years in payments engineering at a large fintech.",
   "background_verified": "Not verified. LinkedIn link is a placeholder; the fintech is not named. Search for name + Settlr + CTO + Mumbai returned nothing matching.",
   "public_footprint": "not_found",
   "source_ids": [
    "D11",
    "F9"
   ]
  }
 ],
 "claims": [
  {
   "text": "Rahul Mehta (CEO) has 10 years in transaction banking and led SME product at a private bank.",
   "source_ids": [
    "D10",
    "F8"
   ],
   "status": "founder_stated",
   "note": "Deck and form agree; employer not named."
  },
  {
   "text": "Sonal Iyer (CTO) has 8 years in payments engineering at a large fintech.",
   "source_ids": [
    "D11",
    "F9"
   ],
   "status": "founder_stated",
   "note": "Deck and form agree; employer not named."
  },
  {
   "text": "No public footprint found for either founder; both LinkedIn links are placeholders.",
   "source_ids": [
    "F8",
    "F9"
   ],
   "status": "unverifiable",
   "note": null
  },
  {
   "text": "October 2026 payment volume INR 86 Cr and net revenue INR 78 L, from 1,150 SME customers.",
   "source_ids": [
    "D3",
    "F2",
    "F12"
   ],
   "status": "founder_stated",
   "note": "Deck and form agree. Cross-check: 1,150 SMEs x INR 6,800 average monthly fees = INR 78.2 L, consistent."
  },
  {
   "text": "The month-by-month volume trend (Jun 52 to Oct 86 Cr) is an assumed ordering; the PDF extraction listed 79, 86, 70, 52, 61.",
   "source_ids": [
    "D4"
   ],
   "status": "unverifiable",
   "note": "Only October (INR 86 Cr) is confirmed by the form."
  },
  {
   "text": "Revenue comes from a 0.4% fee on payments collected and about 1.2% a month on invoices financed, funded through NBFC partners.",
   "source_ids": [
    "D8",
    "D9",
    "F1"
   ],
   "status": "founder_stated",
   "note": "Our arithmetic: 0.4% x INR 86 Cr = ~INR 34 L, so ~INR 44 L/month would come from financing. If Settlr keeps the full 1.2%/month that implies ~INR 36 Cr financed in the month while the NBFC funds it, which only works if Settlr shares credit risk or reports gross charges. Split not disclosed."
  },
  {
   "text": "45% of the INR 30 Cr Series A is earmarked for a 'financing book'.",
   "source_ids": [
    "D15"
   ],
   "status": "founder_stated",
   "note": "Settlr says financing is funded by NBFC partners and does not claim its own NBFC licence. Equity going into a book implies either balance-sheet lending (needs RBI registration) or a default loss guarantee/co-lending arrangement; which one is not stated."
  },
  {
   "text": "Under RBI's digital lending framework, default loss guarantee (DLG/FLDG) cover from a lending service provider is capped at 5% of the loan portfolio.",
   "source_ids": [
    "W1",
    "W2"
   ],
   "status": "verified",
   "note": "June 2023 DLG guidelines, consolidated into the RBI (Digital Lending) Directions, 2025 (8 May 2025). If Settlr guarantees its NBFC partners' losses, any first-loss cover above 5% would be non-compliant; credit risk above that sits with the NBFC."
  },
  {
   "text": "RBI rules require loan servicing and repayment to go directly to the regulated lender's bank account without any pass-through or pool account of a third party.",
   "source_ids": [
    "W3",
    "W2"
   ],
   "status": "verified",
   "note": "Relevant because Settlr also collects buyer payments on its payment links; repayments of financed invoices cannot route through a Settlr-controlled pool account."
  },
  {
   "text": "Unit economics: CAC INR 14,500 per SME, 7-month payback, 58% gross margin, 112% net revenue retention.",
   "source_ids": [
    "F3",
    "D7"
   ],
   "status": "founder_stated",
   "note": "Our arithmetic: INR 6,800 x 58% = ~INR 3,940 gross profit per SME per month, implying ~3.7-month payback, not 7. The stated 7 months may include other costs; method not given."
  },
  {
   "text": "Deck market sizing understates its own inputs by 10x: SOM is shown as INR 6,750 Cr from 15,000 SMEs x INR 4.5 Cr, which equals INR 67,500 Cr; SAM (400K x 4.5 Cr) and TAM (2.1M x 4.5 Cr) are likewise 10x below their stated products.",
   "source_ids": [
    "D5",
    "D6"
   ],
   "status": "founder_stated",
   "note": "Also: current average volume per SME is ~INR 0.9 Cr a year (INR 86 Cr x 12 / 1,150), far below the INR 4.5 Cr per SME assumed. Sizing should be rebuilt from revenue, not volume."
  },
  {
   "text": "Settlr prices financing at about 1.2% a month, positioned against informal invoice discounting at 24 to 36% a year.",
   "source_ids": [
    "D2",
    "D14"
   ],
   "status": "founder_stated",
   "note": "1.2%/month is ~14.4% a year simple. Deck promises early payment 'against any invoice', which implies taking on unrated buyer risk."
  },
  {
   "text": "Credlix advertises invoice-discounting financing for MSMEs from 1% per month.",
   "source_ids": [
    "W5"
   ],
   "status": "verified",
   "note": "Pricing benchmark: Settlr's 1.2% is not cheaper than funded competitors."
  },
  {
   "text": "TReDS is an RBI-authorised electronic platform for discounting MSME bills on large corporates; RXIL, M1xchange and Invoicemart operate platforms.",
   "source_ids": [
    "W4"
   ],
   "status": "verified",
   "note": "Regulated, auction-priced alternative for SME invoices on large buyers; Settlr does not mention TReDS."
  },
  {
   "text": "Mumbai-headquartered Cashinvoice raised USD 3.4 M (INR 28.2 Cr) Series A in Feb 2024 for invoice-discounting / supply-chain finance for MSMEs.",
   "source_ids": [
    "W6"
   ],
   "status": "verified",
   "note": null
  },
  {
   "text": "Seed round of INR 9 Cr raised in 2024, led by two institutional funds; cap table founders 58%, seed investors 30%, ESOP 12%.",
   "source_ids": [
    "D12",
    "F6",
    "F7"
   ],
   "status": "founder_stated",
   "note": "No press or database record of a Settlr seed round found. Implied seed post-money ~INR 30 Cr; ask is INR 180 Cr post (~6x)."
  },
  {
   "text": "Name collision: 'Settlrs' is an unrelated Bengaluru office-equipment rental company (founded 2017), not Settlr Fintech.",
   "source_ids": [
    "W7",
    "F13"
   ],
   "status": "verified",
   "note": "Search results also surfaced an unrelated co-living startup 'Settl' (not opened, not cited). Any database lookup on the name must be checked against the CIN."
  },
  {
   "text": "Team of 31; both founders full-time since 2023; incorporated April 2023.",
   "source_ids": [
    "D12"
   ],
   "status": "founder_stated",
   "note": "Deck and form agree on team size."
  },
  {
   "text": "Acquisition mix: CA and accountant partners 40%, direct sales 35%, inbound and referrals 25%.",
   "source_ids": [
    "F14"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "18-month plan: INR 300 Cr monthly volume, 4,500 SMEs and break-even operations.",
   "source_ids": [
    "D13"
   ],
   "status": "founder_stated",
   "note": "3.5x volume and 3.9x customers in 18 months."
  },
  {
   "text": "Founder-listed key risks: credit losses on financed invoices, dependence on NBFC partners, regulation of digital lending.",
   "source_ids": [
    "F4"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Raising INR 30 Cr Series A at INR 180 Cr post-money, looking for a lead; four Series A funds in conversation.",
   "source_ids": [
    "D1",
    "F5",
    "F10",
    "F11"
   ],
   "status": "founder_stated",
   "note": null
  }
 ],
 "gaps": [
  {
   "what": "Who holds credit risk on financed invoices",
   "why_it_matters": "This decides whether Settlr is a capital-light LSP or a thinly capitalised lender; 45% of the raise is for a 'financing book' and revenue implies Settlr keeps most of the 1.2%/month spread.",
   "searched": [
    "deck slides 8 and 10",
    "form What have you built / Key risks",
    "web: RBI default loss guarantee digital lending 5 per cent cap"
   ],
   "ask_founder": "Name the NBFC partners. For each: is there a DLG/FLDG, what % of portfolio, co-lending share, and who books the loss on a buyer default? What will the INR 13.5 Cr 'financing book' legally be?",
   "blocks_criteria": [
    "regulatory",
    "unit_economics"
   ]
  },
  {
   "what": "Credit performance of the financed book",
   "why_it_matters": "For invoice financing the deciding metric is loss rate and DPD on financed volume; none is disclosed.",
   "searched": [
    "deck",
    "form"
   ],
   "ask_founder": "Monthly financed volume, outstanding book, 30/90+ DPD and write-offs since launch, by vintage.",
   "blocks_criteria": [
    "unit_economics",
    "traction"
   ]
  },
  {
   "what": "Payment-aggregator status for collections",
   "why_it_matters": "Collecting buyer payments via UPI/card on Settlr links requires an RBI payment-aggregator authorisation or a licensed PA partner, and repayments must not pool through Settlr.",
   "searched": [
    "deck slide 4",
    "form"
   ],
   "ask_founder": "Which licensed PA processes your payment links, whose nodal/escrow account receives funds, and how are financed-invoice repayments routed to the NBFC?",
   "blocks_criteria": [
    "regulatory"
   ]
  },
  {
   "what": "Founder employment history",
   "why_it_matters": "Transaction-banking and payments credentials are the core founder-market-fit claim; neither employer is named.",
   "searched": [
    "web: \"Settlr\" fintech Mumbai invoice financing SME \"Rahul Mehta\"",
    "web: \"Sonal Iyer\" CTO Settlr payments Mumbai",
    "web: Rahul Mehta transaction banking SME product private bank founder Mumbai"
   ],
   "ask_founder": "Which bank did Rahul lead SME product at, and which fintech did Sonal work at? Share real LinkedIn profiles.",
   "blocks_criteria": [
    "team"
   ]
  },
  {
   "what": "Seed investors and company registration",
   "why_it_matters": "An INR 9 Cr institutional seed should leave a public trace; none found, and the name collides with unrelated companies.",
   "searched": [
    "web: \"Settlr Fintech\" OR \"Settlr\" seed round 2024 INR 9 crore"
   ],
   "ask_founder": "Name the two seed funds and share the CIN; can we speak to the seed lead?",
   "blocks_criteria": [
    "traction"
   ]
  },
  {
   "what": "Revenue split and monthly series",
   "why_it_matters": "The volume chart's month order is an extraction assumption, and fee vs financing revenue split determines quality of revenue.",
   "searched": [
    "deck slide 5 (chart and extraction note)",
    "form Volume and revenue"
   ],
   "ask_founder": "Monthly payment volume, financed volume, fee revenue and financing revenue (gross and net of NBFC share) for the last 12 months.",
   "blocks_criteria": [
    "traction",
    "unit_economics"
   ]
  },
  {
   "what": "Market sizing basis",
   "why_it_matters": "TAM/SAM/SOM are each 10x below their own multiplication, and the INR 4.5 Cr per-SME volume assumption is ~5x current actuals.",
   "searched": [
    "deck slide 6"
   ],
   "ask_founder": "Which is right, the per-SME volume or the totals, and what revenue per SME does the SOM assume?",
   "blocks_criteria": [
    "market"
   ]
  },
  {
   "what": "Payback calculation method",
   "why_it_matters": "Stated 7-month payback does not match INR 6,800 x 58% against INR 14,500 CAC (~3.7 months).",
   "searched": [
    "deck slide 7",
    "form Unit economics"
   ],
   "ask_founder": "Show the payback calculation: which costs are included beyond gross margin, and does 'net revenue' exclude NBFC share and credit losses?",
   "blocks_criteria": [
    "unit_economics"
   ]
  }
 ],
 "competitors_named": [],
 "competitors_found": [
  "TReDS platforms (RXIL, M1xchange, Invoicemart)",
  "Credlix",
  "Cashinvoice",
  "CredAble",
  "KredX",
  "Cashflo",
  "CapitalXB",
  "Reevoy"
 ],
 "keywords": [
  "invoice financing",
  "invoice discounting",
  "SME payments",
  "payment links",
  "collections",
  "receivables",
  "reconciliation",
  "working capital",
  "NBFC partner",
  "B2B payments",
  "UPI collections"
 ],
 "founder_contact": null,
 "sources": [
  {
   "id": "D1",
   "kind": "deck",
   "title": "Settlr deck - cover",
   "url": null,
   "locator": "Cover",
   "retrieved_on": null,
   "quote": "Series A | Raising INR 30 Cr | Mumbai"
  },
  {
   "id": "D2",
   "kind": "deck",
   "title": "Settlr deck - Invoice, collect, finance",
   "url": null,
   "locator": "Slide 4",
   "retrieved_on": null,
   "quote": "Get paid early against any invoice, at 1.2% a month."
  },
  {
   "id": "D3",
   "kind": "deck",
   "title": "Settlr deck - Traction",
   "url": null,
   "locator": "Slide 5 (Traction)",
   "retrieved_on": null,
   "quote": "Traction: INR 86 Cr monthly volume"
  },
  {
   "id": "D4",
   "kind": "deck",
   "title": "Settlr deck - Traction chart extraction note",
   "url": null,
   "locator": "Slide 5 (chart comment)",
   "retrieved_on": null,
   "quote": "chart values as extracted from the PDF, in extraction order: 79, 86, 70, 52, 61, against months Jun, Jul, Aug, Sep, Oct."
  },
  {
   "id": "D5",
   "kind": "deck",
   "title": "Settlr deck - Market size (SOM row; SOM shown as INR 6,750 Cr)",
   "url": null,
   "locator": "Slide 6 (Market size), SOM row",
   "retrieved_on": null,
   "quote": "In 3 years: 15,000 SMEs x INR 4.5 Cr"
  },
  {
   "id": "D6",
   "kind": "deck",
   "title": "Settlr deck - Market size (SAM row; SAM shown as INR 1.8 lakh Cr)",
   "url": null,
   "locator": "Slide 6 (Market size), SAM row",
   "retrieved_on": null,
   "quote": "400K SMEs in 6 metros x INR 4.5 Cr"
  },
  {
   "id": "D7",
   "kind": "deck",
   "title": "Settlr deck - Go-to-market and CAC",
   "url": null,
   "locator": "Slide 7",
   "retrieved_on": null,
   "quote": "Average SME pays INR 6,800 a month in fees and financing charges. Gross margin 58%."
  },
  {
   "id": "D8",
   "kind": "deck",
   "title": "Settlr deck - How we make money (payment fee)",
   "url": null,
   "locator": "Slide 8",
   "retrieved_on": null,
   "quote": "0.4% on each payment collected."
  },
  {
   "id": "D9",
   "kind": "deck",
   "title": "Settlr deck - How we make money (financing spread)",
   "url": null,
   "locator": "Slide 8",
   "retrieved_on": null,
   "quote": "About 1.2% a month on invoices financed, funded through NBFC partners."
  },
  {
   "id": "D10",
   "kind": "deck",
   "title": "Settlr deck - The team (CEO)",
   "url": null,
   "locator": "Slide 9",
   "retrieved_on": null,
   "quote": "10 years in transaction banking. Led SME product at a private bank."
  },
  {
   "id": "D11",
   "kind": "deck",
   "title": "Settlr deck - The team (CTO)",
   "url": null,
   "locator": "Slide 9",
   "retrieved_on": null,
   "quote": "8 years in payments engineering at a large fintech."
  },
  {
   "id": "D12",
   "kind": "deck",
   "title": "Settlr deck - The team (size, seed)",
   "url": null,
   "locator": "Slide 9",
   "retrieved_on": null,
   "quote": "Team of 31. Seed round of INR 9 Cr raised in 2024."
  },
  {
   "id": "D13",
   "kind": "deck",
   "title": "Settlr deck - The ask (18-month plan)",
   "url": null,
   "locator": "Slide 10",
   "retrieved_on": null,
   "quote": "In 18 months: INR 300 Cr monthly volume, 4,500 SMEs, break-even operations."
  },
  {
   "id": "D14",
   "kind": "deck",
   "title": "Settlr deck - Problem (costly credit)",
   "url": null,
   "locator": "Slide 3",
   "retrieved_on": null,
   "quote": "Informal invoice discounting costs 24 to 36% a year."
  },
  {
   "id": "D15",
   "kind": "deck",
   "title": "Settlr deck - The ask (use of funds)",
   "url": null,
   "locator": "Slide 10",
   "retrieved_on": null,
   "quote": "45% Financing book"
  },
  {
   "id": "F1",
   "kind": "form",
   "title": "Application form - What have you built?",
   "url": null,
   "locator": "Product and traction > What have you built?",
   "retrieved_on": null,
   "quote": "A payments platform for SMEs with payment links, collections reconciliation and invoice financing funded by NBFC partners."
  },
  {
   "id": "F2",
   "kind": "form",
   "title": "Application form - Volume and revenue",
   "url": null,
   "locator": "Product and traction > Volume and revenue",
   "retrieved_on": null,
   "quote": "INR 86 Cr payment volume in October 2026. Net revenue INR 78 L."
  },
  {
   "id": "F3",
   "kind": "form",
   "title": "Application form - Unit economics",
   "url": null,
   "locator": "Product and traction > Unit economics",
   "retrieved_on": null,
   "quote": "CAC INR 14,500 per SME, payback 7 months, gross margin 58%, net revenue retention 112%."
  },
  {
   "id": "F4",
   "kind": "form",
   "title": "Application form - Key risks",
   "url": null,
   "locator": "Product and traction > Key risks",
   "retrieved_on": null,
   "quote": "Credit losses on financed invoices, dependence on NBFC partners, regulation of digital lending."
  },
  {
   "id": "F5",
   "kind": "form",
   "title": "Application form - Valuation expectation",
   "url": null,
   "locator": "Fundraising > Valuation expectation",
   "retrieved_on": null,
   "quote": "INR 180 Cr post-money"
  },
  {
   "id": "F6",
   "kind": "form",
   "title": "Application form - Existing investors",
   "url": null,
   "locator": "Fundraising > Existing investors",
   "retrieved_on": null,
   "quote": "INR 9 Cr seed round in 2024, led by two institutional funds."
  },
  {
   "id": "F7",
   "kind": "form",
   "title": "Application form - Equity split",
   "url": null,
   "locator": "Founders > Equity split",
   "retrieved_on": null,
   "quote": "Founders 58%, seed investors 30%, ESOP 12%."
  },
  {
   "id": "F8",
   "kind": "form",
   "title": "Application form - Founder 1",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "Rahul Mehta, CEO. 10 years in transaction banking; led SME product at a private bank. linkedin.com/in/rahul-mehta-example"
  },
  {
   "id": "F9",
   "kind": "form",
   "title": "Application form - Founder 2",
   "url": null,
   "locator": "Founders > Founder 2",
   "retrieved_on": null,
   "quote": "Sonal Iyer, CTO. 8 years in payments engineering at a large fintech. linkedin.com/in/sonal-iyer-example"
  },
  {
   "id": "F10",
   "kind": "form",
   "title": "Application form - Other investors in conversation",
   "url": null,
   "locator": "Fundraising > Other investors in conversation",
   "retrieved_on": null,
   "quote": "Four Series A funds."
  },
  {
   "id": "F11",
   "kind": "form",
   "title": "Application form - Anything else",
   "url": null,
   "locator": "Anything else we should know?",
   "retrieved_on": null,
   "quote": "We are looking for a lead investor for our Series A."
  },
  {
   "id": "F12",
   "kind": "form",
   "title": "Application form - Customers",
   "url": null,
   "locator": "Product and traction > Customers",
   "retrieved_on": null,
   "quote": "1,150 SMEs."
  },
  {
   "id": "F13",
   "kind": "form",
   "title": "Application form - Company name",
   "url": null,
   "locator": "Company > Company name",
   "retrieved_on": null,
   "quote": "Settlr (Settlr Fintech Pvt. Ltd.)"
  },
  {
   "id": "F14",
   "kind": "form",
   "title": "Application form - Customer acquisition",
   "url": null,
   "locator": "Product and traction > Customer acquisition",
   "retrieved_on": null,
   "quote": "CA and accountant partners 40%, direct sales 35%, inbound and referrals 25%."
  },
  {
   "id": "W1",
   "kind": "web",
   "title": "RBI - Guidelines on Default Loss Guarantee (DLG) in Digital Lending, 8 June 2023 (since repealed into the 2025 Directions)",
   "url": "https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12514",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "shall not exceed five per cent of the amount of that loan portfolio"
  },
  {
   "id": "W2",
   "kind": "web",
   "title": "Argus Partners - RBI Digital Lending Directions, 2025: an overview",
   "url": "https://www.argus-p.com/updates/updates/rbi-digital-lending-directions-2025-an-overview/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "DLG cover on any outstanding portfolio must not exceed 5 (five) % of the total disbursed amount,"
  },
  {
   "id": "W3",
   "kind": "web",
   "title": "RBI - Guidelines on Digital Lending, 2 September 2022 (since repealed into the 2025 Directions)",
   "url": "https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12382",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "without any pass-through account/ pool account of any third party"
  },
  {
   "id": "W4",
   "kind": "web",
   "title": "SIDBI - TReDS",
   "url": "https://www.sidbi.in/en/treds",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "TReDS is an electronic platform for online discounting of bills of MSMEs for supplies to large Corporates."
  },
  {
   "id": "W5",
   "kind": "web",
   "title": "Credlix - Invoice discounting",
   "url": "https://www.credlix.com/invoice-discounting/invoice-discounting-for-fintech",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Smart Financing Begins at just 1% per month"
  },
  {
   "id": "W6",
   "kind": "web",
   "title": "Inc42 - Cashinvoice bags $3.4 Mn (7 Feb 2024)",
   "url": "https://inc42.com/buzz/cashinvoice-bags-3-4-mn-to-aid-new-business-in-supply-chain-finance",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "has raised $3.4 Mn (INR 28.2 Cr)"
  },
  {
   "id": "W7",
   "kind": "web",
   "title": "Inc42 company profile - Settlrs (unrelated Bengaluru rental company)",
   "url": "https://inc42.com/company/settlrs/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Settlrs is headquartered in Bengaluru, India."
  }
 ],
 "produced_by": "claude-code-session (in-session run of prompts/research.md; no API key)",
 "research_notes": "Deck and form agree on every number; the one deck-internal issue is market sizing that is 10x below its own inputs, plus an assumed chart ordering. The decisive open question is credit-risk allocation with NBFC partners (DLG 5% cap; 45% of raise to a 'financing book'). No founder or company footprint found; name collides with unrelated Settlrs (Bengaluru; cited) and, per search results only, a co-living startup 'Settl'. Web quotes were extracted via a fetch tool and should be re-verified with verify_web."
}
</dossier>

Score every criterion in both lenses (R1-R6, S1-S4) and evaluate gates G1-G4.