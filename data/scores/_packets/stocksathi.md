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
- C004 [R1] (CampusCredit vs Jai Kisan, by Kushal (partner notes, Meeting 2)): Same sector, opposite answer: for any lender the deciding question is whether the founders own credit/default risk themselves. 'The NBFC partner handles it' is a low R1 regardless of distribution strength.  (matched on: credit, fintech, lending, lending_risk)
- C003 ((meeting-notes startup), by Kushal / Aditya (partner notes, Meeting 4)): Scored 7 before anyone noticed it overlaps portfolio company MeetRecord. Check every application against the full portfolio list; default is no to competitors unless both founders know. Prefer a false-alarm flag to a miss.  (matched on: portfolio_overlap)
</partner_corrections>

<dossier>
{
 "company": "StockSathi",
 "slug": "stocksathi",
 "one_liner": "Vernacular B2B ordering app for small-town kirana stores with next-morning delivery from partner distributors and 7-14 day credit.",
 "sector": "fintech",
 "sub_sector": "B2B kirana restocking with embedded trade credit (lending-led)",
 "stage": "Pre-seed",
 "ask": "INR 2 Cr at INR 12 Cr post-money",
 "business_model": "About 4% trade margin from distributors on delivered orders plus a 1.5% fee on credit orders; credit book currently ~INR 85,000.",
 "founders": [
  {
   "name": "Aarav Deshmukh",
   "role": "CEO",
   "background_claimed": "8 years in FMCG distribution and field operations; ran a regional sales team at a large distributor.",
   "background_verified": null,
   "public_footprint": "not_found",
   "source_ids": [
    "D11",
    "F3"
   ]
  },
  {
   "name": "Pooja Nair",
   "role": "CTO",
   "background_claimed": "5 years as a software engineer at a payments company; built the ordering app and credit-scoring rules.",
   "background_verified": null,
   "public_footprint": "not_found",
   "source_ids": [
    "D12",
    "F4"
   ]
  }
 ],
 "claims": [
  {
   "text": "Retailer count differs: deck says 38 retailers onboarded; form says 42 retailers onboarded. Both say 22 have ordered more than once.",
   "source_ids": [
    "D4",
    "D17",
    "F5"
   ],
   "status": "contradicted",
   "note": "38 vs 42. Repeat share is therefore 58% (deck) or 52% (form). May be a timing difference, but neither document dates the count."
  },
  {
   "text": "CAC differs: deck gives INR 2,860 blended CAC for October (INR 40,000 field cost / 14 stores); form says CAC is under INR 2,000 per store.",
   "source_ids": [
    "D6",
    "D7",
    "F7"
   ],
   "status": "contradicted",
   "note": "The deck's own 12-month target is 'CAC under INR 2,000' (D13), which implies the form figure is a goal, not today's number."
  },
  {
   "text": "How credit is funded differs: deck says the credit pilot is funded from the company's own capital with an NBFC partnership 'in discussion'; form says credit is provided through 'our NBFC partner' and StockSathi takes the first-loss risk.",
   "source_ids": [
    "D9",
    "D10",
    "F8",
    "F18"
   ],
   "status": "contradicted",
   "note": "Form also asks the fund for introductions to NBFCs (F18), which is consistent with the deck (no partner signed yet) and inconsistent with the form's credit answer. This is the defining-risk question for a lender."
  },
  {
   "text": "StockSathi is not registered with the RBI as an NBFC.",
   "source_ids": [
    "F11"
   ],
   "status": "founder_stated",
   "note": "If credit is lent from StockSathi's own balance sheet (D9), whether this falls under the RBI Act s.45-IA registration requirement (W1) is a legal question this research cannot settle; it must be put to the founders."
  },
  {
   "text": "Under RBI's default loss guarantee (DLG) framework, first-loss cover on a digital-lending portfolio is capped at 5% of that portfolio, and an LSP giving DLG must be a company incorporated under the Companies Act, 2013.",
   "source_ids": [
    "W2",
    "W3"
   ],
   "status": "verified",
   "note": "The form says StockSathi takes 'the first-loss risk' (F8) without saying how much. Any first-loss arrangement above 5% or outside the permitted forms would not fit the framework. StockSathi is a Pvt. Ltd. company so it can be an LSP in principle."
  },
  {
   "text": "RBI's Digital Lending Directions, 2025 require loans to be disbursed directly to the borrower's account and repayments routed through the regulated entity's account, with no pass-through via LSP accounts.",
   "source_ids": [
    "W4"
   ],
   "status": "verified",
   "note": "StockSathi's pay-later flow (order now, pay in 7-14 days, D3) settles the distributor first. Who disburses to whom, and whose account collects repayment, is not described in the application."
  },
  {
   "text": "Credit book is about INR 85,000 outstanding across 12 retailers, with no defaults to date; late payments are chased personally by the team.",
   "source_ids": [
    "F9",
    "F10",
    "D9"
   ],
   "status": "founder_stated",
   "note": "Four months of operation and a tiny book: 'no defaults' is not yet evidence of credit quality. No late-payment / days-past-due data is given."
  },
  {
   "text": "Credit orders are about a third of October GMV (implying roughly INR 1.3 L of October GMV on credit), charged a 1.5% credit fee.",
   "source_ids": [
    "D10",
    "D5"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "GMV was INR 3.8 L in October; about INR 9 lakh over the last three months; GMV has grown every month since the July launch.",
   "source_ids": [
    "D5",
    "F6"
   ],
   "status": "founder_stated",
   "note": "Figures are consistent with each other (Oct 3.8 L inside a ~9 L quarter). No monthly series or GMV per store is given."
  },
  {
   "text": "Repeat customers reorder about once a week; 22 stores have ordered more than once.",
   "source_ids": [
    "F17",
    "F5"
   ],
   "status": "founder_stated",
   "note": "No cohort table (repeat by onboarding month) or churned-store count."
  },
  {
   "text": "Unit economics: about 4% trade margin per order; INR 520 monthly margin per active store; ~5.5-month payback on trade margin; positive contribution once a store has ordered twice.",
   "source_ids": [
    "D8",
    "F13"
   ],
   "status": "founder_stated",
   "note": "Delivery cost is not shown, so 'margin per store' may be before logistics. Payback uses the INR 2,860 CAC, not the form's sub-2,000 figure."
  },
  {
   "text": "The founders did 60 owner interviews in Karimnagar and Warangal (June-July 2026) before launch; the product is live in Karimnagar only, onboarding via two field agents.",
   "source_ids": [
    "D2",
    "F12"
   ],
   "status": "founder_stated",
   "note": "Evidence of going to the customer first (R2), but entirely self-reported."
  },
  {
   "text": "Sector mismatch: founder selected 'Consumer tech', but the business is a B2B kirana ordering marketplace with embedded trade credit; 40% of the raise goes to the credit book. Classified here as fintech (lending-led B2B commerce).",
   "source_ids": [
    "F2",
    "D1",
    "D14"
   ],
   "status": "founder_stated",
   "note": "Relevant to gate G3 (sector label stretch) and to precedent C004: for a lender the deciding question is who owns default risk."
  },
  {
   "text": "Founders: Aarav Deshmukh (CEO) claims 8 years in FMCG distribution and field operations; Pooja Nair (CTO) claims 5 years as a software engineer at a payments company. Neither has prior startup experience; both full-time since April 2026.",
   "source_ids": [
    "D11",
    "D12",
    "F16"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Founder LinkedIn links in the form are placeholders (*-example) and the website is a .example domain; no independent footprint for the founders or company was found.",
   "source_ids": [
    "F3",
    "F4",
    "F1"
   ],
   "status": "unverifiable",
   "note": null
  },
  {
   "text": "Jumbotail raised USD 120M (Series D, June 2025, led by SC Ventures) and offers kiranas access to credit alongside B2B supply.",
   "source_ids": [
    "W5"
   ],
   "status": "verified",
   "note": "Contradicts the deck's framing that B2B marketplaces offer only 'Limited' credit on orders (D16); a well-funded player already bundles supply and credit for kiranas."
  },
  {
   "text": "ONDC's DigiDukaan kirana-restocking pilot started in Hyderabad in March 2026 (via ONDC partner Qwipo) and signed up 10,000+ retailers and 35+ brands.",
   "source_ids": [
    "W6",
    "W7"
   ],
   "status": "verified",
   "note": "Same state as StockSathi; a subsidised open-network alternative for kirana restocking."
  },
  {
   "text": "B2B BNPL providers (e.g. Rupifi) already embed credit into B2B marketplaces in India.",
   "source_ids": [
    "W8"
   ],
   "status": "verified",
   "note": "Indicates the credit layer can be sourced from specialist lenders; StockSathi's edge must be underwriting/collections in small towns."
  },
  {
   "text": "Application names no specific competitor, only 'Large B2B marketplaces and local wholesale markets'.",
   "source_ids": [
    "F20"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Market sizing is top-down: TAM INR 17 lakh Cr from 12M stores x INR 1.2 L monthly purchases; store counts are the founders' own estimates.",
   "source_ids": [
    "D15"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Raising INR 2 Cr at INR 12 Cr post-money; three FMCG/logistics angels have invested INR 25 lakh.",
   "source_ids": [
    "F15",
    "F19"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Application came via a Fund I portfolio founder. Portfolio company SuperK runs a tech-enabled grocery network for small towns in Andhra Pradesh, which serves the same small-town kirana owners.",
   "source_ids": [
    "F14",
    "S1"
   ],
   "status": "founder_stated",
   "note": "Possible portfolio overlap (same customer: small-town kirana owners; overlapping job: supply and working capital). Flag for the G1 conflict check; also ask which portfolio founder made the intro."
  }
 ],
 "gaps": [
  {
   "what": "Aarav Deshmukh (CEO): no public footprint confirming 8 years in FMCG distribution or the 'large distributor' employer.",
   "why_it_matters": "Founder-market fit is the core of the case (field execution in small-town distribution); it rests entirely on self-reported history.",
   "searched": [
    "WebSearch: \"Aarav Deshmukh\" StockSathi Hyderabad (2026-11-18) - no result mentions the person with StockSathi",
    "Application LinkedIn link linkedin.com/in/aarav-deshmukh-example is a placeholder (.example pattern), not a real profile"
   ],
   "ask_founder": "Which distributor did you work for, which region and team size did you run, and can we speak to a former manager?",
   "blocks_criteria": [
    "R2",
    "S3"
   ]
  },
  {
   "what": "Pooja Nair (CTO): no public footprint confirming 5 years at a payments company or the credit-rules work.",
   "why_it_matters": "She built the credit-scoring rules the founders call their edge; her credit/risk background is unverified.",
   "searched": [
    "WebSearch: \"Pooja Nair\" StockSathi CTO Hyderabad (2026-11-18) - no matching profile",
    "Application LinkedIn link linkedin.com/in/pooja-nair-example is a placeholder, not a real profile"
   ],
   "ask_founder": "Which payments company, which product, and did you work on underwriting or risk there?",
   "blocks_criteria": [
    "R1",
    "S3"
   ]
  },
  {
   "what": "Company existence and registration: no website, app-store listing, press or MCA record found for StockSathi Technologies Pvt. Ltd.",
   "why_it_matters": "Basic verification that the entity and app exist.",
   "searched": [
    "WebSearch: StockSathi kirana restocking app Karimnagar (2026-11-18) - no result",
    "Website www.stocksathi.example is a placeholder",
    "MCA portal not queried in this run"
   ],
   "ask_founder": "Please share the CIN, Play Store link and a live demo.",
   "blocks_criteria": [
    "R4"
   ]
  },
  {
   "what": "Who actually funds the credit and who bears the losses (deck: own capital, NBFC in discussion; form: NBFC partner, StockSathi takes first loss).",
   "why_it_matters": "This is the defining risk for a lender and the fund's precedent (C004) scores it heavily; the two documents give opposite answers.",
   "searched": [
    "Deck slide 8 vs form Credit section",
    "Web: RBI DLG framework (W2, W3)"
   ],
   "ask_founder": "Is there a signed NBFC agreement today? If yes, which NBFC, what DLG percentage and in what form (cash/FD/bank guarantee)? If not, on whose balance sheet is the INR 85,000 book?",
   "blocks_criteria": [
    "R1",
    "R4"
   ]
  },
  {
   "what": "Regulatory structure of the pay-later product: whether lending from own capital without NBFC registration is permissible here, and how disbursal/repayment flows comply with the Digital Lending Directions.",
   "why_it_matters": "If the structure is non-compliant the credit product (40% of the raise) may have to be rebuilt around a regulated lender.",
   "searched": [
    "Web: RBI Act s.45-IA text (W1)",
    "Web: Digital Lending Directions 2025 summary (W4)"
   ],
   "ask_founder": "Have you taken legal advice on the credit structure? Who disburses, into whose account, and where do repayments land?",
   "blocks_criteria": [
    "R1",
    "R4"
   ]
  },
  {
   "what": "Credit performance data: days-past-due, late-payment counts, collection cost, loss assumptions.",
   "why_it_matters": "Sector key metric for fintech is default/NPA data or plan; 'none so far' on a 4-month, 12-borrower book is not data.",
   "searched": [
    "Deck slides 5 and 8",
    "Form Credit section"
   ],
   "ask_founder": "How many credit orders have paid late, by how many days, and what loss rate does your model assume at 300 stores?",
   "blocks_criteria": [
    "R1",
    "R3"
   ]
  },
  {
   "what": "Reconciled traction numbers: retailer count (38 vs 42) and CAC (INR 2,860 vs under INR 2,000).",
   "why_it_matters": "Two of the headline numbers differ between deck and form.",
   "searched": [
    "Deck slides 5 and 7 vs form traction answers"
   ],
   "ask_founder": "What is today's retailer count and the October CAC with field-agent salaries included?",
   "blocks_criteria": [
    "R3"
   ]
  },
  {
   "what": "Contribution after delivery: delivery is 'next-morning from partner distributors' but logistics cost per order is not shown.",
   "why_it_matters": "Ops-heavy B2B supply often fails on contribution at density; the INR 520 margin per store may be gross of logistics.",
   "searched": [
    "Deck slides 4, 7, 8",
    "Form Unit economics"
   ],
   "ask_founder": "Who pays for delivery, and what is contribution per order after delivery and credit losses?",
   "blocks_criteria": [
    "R3",
    "R5"
   ]
  }
 ],
 "competitors_named": [
  "B2B marketplaces (unnamed)",
  "Local wholesale markets"
 ],
 "competitors_found": [
  "Jumbotail",
  "ONDC DigiDukaan (via Qwipo)",
  "Rupifi (B2B BNPL)"
 ],
 "keywords": [
  "kirana",
  "B2B ordering",
  "restocking",
  "retailer credit",
  "pay later",
  "trade credit",
  "wholesale distribution",
  "small-town grocery",
  "FMCG supply",
  "vernacular app"
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
   "quote": "Restocking and credit for India's small-town kirana stores"
  },
  {
   "id": "D2",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 2 (problem)",
   "retrieved_on": null,
   "quote": "Based on 60 owner interviews in Karimnagar and Warangal, June to July 2026."
  },
  {
   "id": "D3",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 4 (product)",
   "retrieved_on": null,
   "quote": "7 to 14 days credit on repeat orders"
  },
  {
   "id": "D4",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "38 retailers onboarded"
  },
  {
   "id": "D5",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "INR 3.8 L GMV in October"
  },
  {
   "id": "D6",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 7 (GTM)",
   "retrieved_on": null,
   "quote": "INR 2,860 blended CAC, October"
  },
  {
   "id": "D7",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 7 (GTM)",
   "retrieved_on": null,
   "quote": "CAC = INR 40,000 field cost / 14 stores onboarded in October. Small sample, one town."
  },
  {
   "id": "D8",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 7 (GTM)",
   "retrieved_on": null,
   "quote": "INR 520 monthly margin per active store"
  },
  {
   "id": "D9",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 8 (revenue model)",
   "retrieved_on": null,
   "quote": "Pilot with 12 retailers, funded from our own capital for now."
  },
  {
   "id": "D10",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 8 (revenue model)",
   "retrieved_on": null,
   "quote": "Credit is about a third of October GMV. NBFC partnership in discussion."
  },
  {
   "id": "D11",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 10 (team)",
   "retrieved_on": null,
   "quote": "8 years in FMCG distribution and field operations. Ran a regional sales team at a large distributor."
  },
  {
   "id": "D12",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 10 (team)",
   "retrieved_on": null,
   "quote": "5 years as a software engineer at a payments company. Built the ordering app and credit rules."
  },
  {
   "id": "D13",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 11 (ask)",
   "retrieved_on": null,
   "quote": "In 12 months: 300 live stores, INR 40 L monthly GMV, CAC under INR 2,000."
  },
  {
   "id": "D14",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 11 (ask)",
   "retrieved_on": null,
   "quote": "40% Credit book"
  },
  {
   "id": "D15",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 6 (market size)",
   "retrieved_on": null,
   "quote": "Store counts are our estimates."
  },
  {
   "id": "D16",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 9 (differentiation)",
   "retrieved_on": null,
   "quote": "Credit on orders"
  },
  {
   "id": "D17",
   "kind": "deck",
   "title": "Pitch deck",
   "url": null,
   "locator": "Slide 5 (traction)",
   "retrieved_on": null,
   "quote": "22 of 38 have ordered more than once"
  },
  {
   "id": "F1",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Company > Website",
   "retrieved_on": null,
   "quote": "www.stocksathi.example"
  },
  {
   "id": "F2",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Company > Sector (as selected)",
   "retrieved_on": null,
   "quote": "Consumer tech"
  },
  {
   "id": "F3",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "LinkedIn: linkedin.com/in/aarav-deshmukh-example"
  },
  {
   "id": "F4",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Founder 2",
   "retrieved_on": null,
   "quote": "LinkedIn: linkedin.com/in/pooja-nair-example"
  },
  {
   "id": "F5",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Active customers",
   "retrieved_on": null,
   "quote": "42 retailers onboarded, 22 of whom have ordered more than once."
  },
  {
   "id": "F6",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Revenue / GMV",
   "retrieved_on": null,
   "quote": "GMV of about INR 9 lakh in the last three months."
  },
  {
   "id": "F7",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Customer acquisition",
   "retrieved_on": null,
   "quote": "Our CAC is under INR 2,000 per store."
  },
  {
   "id": "F8",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Credit > How is credit funded?",
   "retrieved_on": null,
   "quote": "Credit is provided through our NBFC partner. We take the first-loss risk."
  },
  {
   "id": "F9",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Credit > Credit book size",
   "retrieved_on": null,
   "quote": "About INR 85,000 outstanding across 12 retailers."
  },
  {
   "id": "F10",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Credit > Defaults to date",
   "retrieved_on": null,
   "quote": "None so far. We follow up personally on late payments."
  },
  {
   "id": "F11",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Credit > Regulatory status",
   "retrieved_on": null,
   "quote": "Not registered as an NBFC."
  },
  {
   "id": "F12",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > What have you built?",
   "retrieved_on": null,
   "quote": "Live in Karimnagar only."
  },
  {
   "id": "F13",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Unit economics",
   "retrieved_on": null,
   "quote": "Positive contribution on delivered orders once a store has ordered twice."
  },
  {
   "id": "F14",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > How did you hear about us?",
   "retrieved_on": null,
   "quote": "Introduction through a founder in your Fund I portfolio."
  },
  {
   "id": "F15",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > Valuation expectation",
   "retrieved_on": null,
   "quote": "INR 12 Cr post-money"
  },
  {
   "id": "F16",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Founders > Time commitment / prior experience",
   "retrieved_on": null,
   "quote": "None for either founder."
  },
  {
   "id": "F17",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Product and traction > Repeat behaviour",
   "retrieved_on": null,
   "quote": "Repeat customers reorder about once a week."
  },
  {
   "id": "F18",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Anything else",
   "retrieved_on": null,
   "quote": "We would also welcome your help with introductions to NBFCs."
  },
  {
   "id": "F19",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Fundraising > Existing investors",
   "retrieved_on": null,
   "quote": "Three angels from the FMCG and logistics industry, INR 25 lakh in total."
  },
  {
   "id": "F20",
   "kind": "form",
   "title": "Application form",
   "url": null,
   "locator": "Competition > Who else is doing this?",
   "retrieved_on": null,
   "quote": "Large B2B marketplaces and local wholesale markets."
  },
  {
   "id": "W1",
   "kind": "web",
   "title": "Section 45-IA, Reserve Bank of India Act 1934 (lawx.in)",
   "url": "https://lawx.in/acts/section/48/485/4705",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Notwithstanding anything contained in this Chapter or in any other law for the time being in force, no non-banking financial"
  },
  {
   "id": "W2",
   "kind": "web",
   "title": "RBI's new guidelines on Default Loss Guarantee in digital lending (IndiaLaw, posted 12 June 2023)",
   "url": "https://www.indialaw.in/blog/banking-and-finance/rbis-new-guidelines-on-default-loss-guarantee-in-digital-lending/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "the total amount of DLG cover on any outstanding portfolio shall not exceed 5% of the amount of that loan portfolio."
  },
  {
   "id": "W3",
   "kind": "web",
   "title": "RBI's new guidelines on Default Loss Guarantee in digital lending (IndiaLaw) - DLG provider eligibility",
   "url": "https://www.indialaw.in/blog/banking-and-finance/rbis-new-guidelines-on-default-loss-guarantee-in-digital-lending/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "the LSP providing DLG must be a company incorporated under the Companies Act, 2013."
  },
  {
   "id": "W4",
   "kind": "web",
   "title": "RBI notifies Digital Lending Directions, 2025 (IndiaLaw)",
   "url": "https://www.indialaw.in/blog/civil/rbi-notifies-digital-lending-directions/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Loans must be disbursed directly to the borrower's account, with servicing and repayments routed through the RE's account"
  },
  {
   "id": "W5",
   "kind": "web",
   "title": "Jumbotail raises $120M Series D; completes acquisition of Solv (Jumbotail press release, 30 June 2025)",
   "url": "https://jumbotail.com/jumbotail-raises-120m-series-d-funding",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "The platform enables kiranas and MSMEs to digitize operations, access credit"
  },
  {
   "id": "W6",
   "kind": "web",
   "title": "ONDC's DigiDukaan wants to digitise how kirana stores buy stock (Lapaas Voice, 23 June 2026)",
   "url": "https://lapaasvoice.com/ondc-digidukaan-kirana-b2b/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "The first test began in Hyderabad in March 2026."
  },
  {
   "id": "W7",
   "kind": "web",
   "title": "ONDC's DigiDukaan (Lapaas Voice) - pilot scale",
   "url": "https://lapaasvoice.com/ondc-digidukaan-kirana-b2b/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "More than 10,000 retailers (shops) signed up, and 35+ brands joined in."
  },
  {
   "id": "W8",
   "kind": "web",
   "title": "Rupifi raises $25 Mn Series A from Bessemer, Tiger Global (Entrepreneur India, 7 Jan 2022)",
   "url": "https://india.entrepreneur.com/news-and-trends/rupifi-raises-25-million-series-a-from-bessemer-tiger/411960",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Our B2B BNPL is currently operating at some of the category leading B2B marketplaces in India"
  },
  {
   "id": "S1",
   "kind": "seed",
   "title": "All In Capital deal memos (data/seed/deal_memos.md)",
   "url": null,
   "locator": "Memo 9: SuperK",
   "retrieved_on": null,
   "quote": "A tech-enabled grocery retail network for small towns."
  }
 ],
 "produced_by": "claude-code-session (in-session run of prompts/research.md; no API key)",
 "research_notes": "Founder and company searches returned nothing (placeholder links). Search results also surfaced StoreKing, Badho, ShopKirana, KiranaPro and Udaan as kirana B2B players, but those pages were not opened, so they are not listed as sources. Pages that blocked fetching (403): YourStory on Flipkart Wholesale credit, Business Standard. RBI's own DLG FAQ page returned no content, so DLG rules are cited from a law-firm summary. The legal question of whether own-capital trade credit needs NBFC registration is flagged, not answered."
}
</dossier>

Score every criterion in both lenses (R1-R6, S1-S4) and evaluate gates G1-G4.