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
- C003 ((meeting-notes startup), by Kushal / Aditya (partner notes, Meeting 4)): Scored 7 before anyone noticed it overlaps portfolio company MeetRecord. Check every application against the full portfolio list; default is no to competitors unless both founders know. Prefer a false-alarm flag to a miss.  (matched on: portfolio_overlap, saas)
</partner_corrections>

<dossier>
{
 "company": "Talkbook",
 "slug": "talkbook",
 "one_liner": "B2B SaaS that records and transcribes sales calls (including Hindi/Tamil/Telugu-English code-mixed speech), summarises them and auto-fills CRM fields for Indian inside-sales teams.",
 "sector": "other",
 "sub_sector": "B2B SaaS / conversation intelligence and sales-call AI (call recording, transcription, summaries, CRM auto-update)",
 "stage": "Pre-seed",
 "ask": "INR 2 Cr at INR 12 Cr post-money",
 "business_model": "Per-seat SaaS subscription at INR 500 per seat per month (INR 6,000 a year), sold to sales teams; founder-stated 16 paying teams, 340 seats, 70% gross margin.",
 "founders": [
  {
   "name": "Arun Kumar",
   "role": "CEO",
   "background_claimed": "6 years as a product lead at a CRM software company.",
   "background_verified": "Not verified. LinkedIn link is a placeholder; the CRM company is not named; 'Arun Kumar' is a very common name and search for name + Talkbook + Chennai found nothing linking.",
   "public_footprint": "not_found",
   "source_ids": [
    "D7",
    "F6"
   ]
  },
  {
   "name": "Meenakshi S",
   "role": "CTO",
   "background_claimed": "4 years in speech ML at a speech-technology company.",
   "background_verified": "Not verified. LinkedIn link is a placeholder; employer not named. Search for name + speech ML + Talkbook + Chennai returned only unrelated name-similar profiles.",
   "public_footprint": "not_found",
   "source_ids": [
    "D8",
    "F7"
   ]
  }
 ],
 "claims": [
  {
   "text": "MRR is INR 2.1 L in the deck but INR 1.9 L in the form.",
   "source_ids": [
    "D3",
    "F1"
   ],
   "status": "contradicted",
   "note": "Neither reconciles with the seat count: 340 seats x INR 500 = INR 1.7 L. The deck's 16 teams x INR 13,000 average = INR 2.08 L. Three different MRR figures from the founder's own numbers."
  },
  {
   "text": "16 paying teams and 340 paid seats.",
   "source_ids": [
    "D2",
    "F2"
   ],
   "status": "founder_stated",
   "note": "Deck and form agree. Average ~21 seats per team."
  },
  {
   "text": "Form states 'We do not know of an India-first player'; the web shows several India-built conversation-intelligence products for sales and contact-centre calls (MeetRecord, Convin, Enthu.ai, NoBroker's ConvoZen).",
   "source_ids": [
    "F4",
    "W1",
    "W4",
    "W5",
    "W6"
   ],
   "status": "contradicted",
   "note": "Founder's competitive view is incomplete; MeetRecord and Convin are funded Indian players."
  },
  {
   "text": "MeetRecord (Bengaluru-founded revenue/conversation-intelligence startup, now operating as Outdoo AI) raised a USD 2.7 M pre-Series A in June 2024 led by SWC Global, with existing investor All In Capital participating.",
   "source_ids": [
    "W1",
    "W2"
   ],
   "status": "verified",
   "note": "All In Capital is an existing MeetRecord investor. Portfolio-conflict check required before any call."
  },
  {
   "text": "MeetRecord/Outdoo's product includes full call transcription, AI coaching summaries of real calls and CRM updates from the call, i.e. the same job Talkbook pitches.",
   "source_ids": [
    "W3",
    "W1"
   ],
   "status": "verified",
   "note": "Outdoo's site now leads with AI roleplay and training; its metadata lists MeetRecord as an alternate name. Overlap is on call transcription, summaries and CRM auto-update; Talkbook's claimed difference is code-mixed Indian-language accuracy and INR 500/seat pricing."
  },
  {
   "text": "Convin (Bengaluru) raised a USD 6.5 M Series A in August 2024 led by India Quotient for AI tools for sales, support and collections teams.",
   "source_ids": [
    "W4"
   ],
   "status": "verified",
   "note": null
  },
  {
   "text": "NoBroker's ConvoZen, an India-focused conversational-AI platform with its own speech models, handles over 2 million conversations a day across 50+ enterprises.",
   "source_ids": [
    "W5"
   ],
   "status": "verified",
   "note": "Indian speech-model competitor with BFSI clients, Talkbook's main target segment."
  },
  {
   "text": "Enthu.ai is a SaaS conversation-intelligence platform turning customer calls into insights, priced from USD 25 per agent per month.",
   "source_ids": [
    "W6"
   ],
   "status": "verified",
   "note": "USD 25 (~INR 2,100) per agent per month is well below the deck's 'INR 9,000+' global-tool comparison."
  },
  {
   "text": "Pricing is INR 500 per seat per month (INR 6,000 a year), which is the basis of the TAM/SAM/SOM.",
   "source_ids": [
    "D5",
    "F1"
   ],
   "status": "founder_stated",
   "note": "TAM INR 4,200 Cr (7M reps), SAM INR 660 Cr, SOM INR 27 Cr (45,000 seats) all multiply correctly; rep counts are 'industry estimates' with no source."
  },
  {
   "text": "CAC about INR 48,000 per team including founder time at a nominal salary; 70% gross margin; payback about 5 months.",
   "source_ids": [
    "F3",
    "D4"
   ],
   "status": "founder_stated",
   "note": "Consistent: INR 13,000 x 70% = INR 9,100/month gross profit, 48,000 / 9,100 = ~5.3 months. 9 of 16 teams came from founder-led outbound."
  },
  {
   "text": "MRR grew from INR 40 K (July) to INR 210 K (October) per the deck chart.",
   "source_ids": [
    "D6"
   ],
   "status": "founder_stated",
   "note": "Chart values were extracted in reverse order (210, 140, 85, 40); the ascending mapping is plausible given 'in 4 months' but the October figure conflicts with the form's INR 1.9 L."
  },
  {
   "text": "Acquisition: founder-led outbound 9 teams, customer referrals 5, CRM consultants 2.",
   "source_ids": [
    "F14"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Arun Kumar (CEO) was a product lead for 6 years at a CRM software company; Meenakshi S (CTO) has 4 years in speech ML at a speech-technology company.",
   "source_ids": [
    "D7",
    "D8",
    "F6",
    "F7"
   ],
   "status": "founder_stated",
   "note": "Deck and form agree; employers not named; both LinkedIn links are placeholders."
  },
  {
   "text": "No public footprint found for either founder or for Talkbook AI Pvt. Ltd.",
   "source_ids": [
    "F6",
    "F7"
   ],
   "status": "unverifiable",
   "note": "Searched founder names + Talkbook + Chennai and the company name; nothing matched."
  },
  {
   "text": "Sector was selected as 'Consumer tech', but the product is B2B SaaS sold to sales teams; classified here as other (B2B SaaS).",
   "source_ids": [
    "F8",
    "F13"
   ],
   "status": "founder_stated",
   "note": "Mismatch between founder-selected sector and actual business."
  },
  {
   "text": "The product transcribes Hindi-English, Tamil-English and Telugu-English calls, summarises them in the rep's language and fills CRM fields automatically.",
   "source_ids": [
    "F13",
    "D13",
    "D10"
   ],
   "status": "founder_stated",
   "note": "No accuracy benchmark (e.g. word error rate vs global tools) is provided."
  },
  {
   "text": "Founder-listed key risks: telecom call-recording restrictions, accuracy on noisy calls, customer concentration in BFSI.",
   "source_ids": [
    "F5"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "DPDP Act notice and consent obligations (consent must be free, specific, informed, unconditional and unambiguous) come into force on 13 May 2027.",
   "source_ids": [
    "W7"
   ],
   "status": "verified",
   "note": "Recording and processing customer calls will need a consent and purpose-limitation design before then, and BFSI clients will push this onto vendors."
  },
  {
   "text": "Team of 8; incorporated February 2026; both founders full-time since March 2026; founders hold 95%, ESOP 5%.",
   "source_ids": [
    "D12",
    "F11",
    "F10"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Raising INR 2 Cr at INR 12 Cr post-money; one pre-seed fund in conversation. 12-month target: 80 paying teams and INR 12 L MRR.",
   "source_ids": [
    "F9",
    "F12",
    "D9"
   ],
   "status": "founder_stated",
   "note": "Target implies ~INR 15,000 per team per month, above today's INR 13,000 average."
  },
  {
   "text": "Deck claims cost per call minute has fallen 8x in two years.",
   "source_ids": [
    "D11"
   ],
   "status": "unverifiable",
   "note": "No source given."
  }
 ],
 "gaps": [
  {
   "what": "Portfolio conflict with MeetRecord (Outdoo AI)",
   "why_it_matters": "All In Capital is an existing MeetRecord investor and MeetRecord transcribes sales calls, summarises them and updates the CRM; the application does not mention MeetRecord.",
   "searched": [
    "web: MeetRecord India conversation intelligence startup sales calls funding",
    "Inc42 and Outdoo press release on June 2024 round",
    "outdoo.ai product page"
   ],
   "ask_founder": "Do you compete with MeetRecord/Outdoo in any deals today? Where do your customers sit vs theirs (Indian SMB inside sales vs US-focused revenue teams)?",
   "blocks_criteria": [
    "portfolio_conflict"
   ]
  },
  {
   "what": "True MRR",
   "why_it_matters": "Deck (INR 2.1 L), form (INR 1.9 L) and seats x price (INR 1.7 L) disagree; MRR is the deciding metric at this stage.",
   "searched": [
    "deck slide 6",
    "deck slide 8",
    "form Revenue/Customers"
   ],
   "ask_founder": "Share the billing export for October: invoiced MRR by team, seats and price per seat. Which MRR figure is correct and why do they differ?",
   "blocks_criteria": [
    "traction"
   ]
  },
  {
   "what": "Retention and usage",
   "why_it_matters": "Four months of history; no logo churn, seat expansion or weekly active usage reported.",
   "searched": [
    "deck",
    "form"
   ],
   "ask_founder": "How many teams have churned or reduced seats, and what share of paid seats used the product weekly in October?",
   "blocks_criteria": [
    "traction",
    "product"
   ]
  },
  {
   "what": "Founder employers and track record",
   "why_it_matters": "Speech-ML depth is the claimed moat; neither the CRM company nor the speech-tech company is named.",
   "searched": [
    "web: \"Talkbook\" AI call summaries Chennai \"Arun Kumar\" sales CRM",
    "web: \"Meenakshi S\" speech ML Talkbook Chennai CTO",
    "web: \"Talkbook AI\" OR \"Talkbook\" startup India conversation intelligence"
   ],
   "ask_founder": "Which companies did Arun and Meenakshi work at and what did they ship? Share real LinkedIn/GitHub profiles.",
   "blocks_criteria": [
    "team"
   ]
  },
  {
   "what": "Accuracy advantage on code-mixed speech",
   "why_it_matters": "The only claimed differentiator vs Convin, ConvoZen and global tools; no benchmark provided.",
   "searched": [
    "deck slides 3, 9",
    "form"
   ],
   "ask_founder": "What is your word error rate on Hindi-English and Tamil-English sales calls vs Convin/ConvoZen/Gong on the same test set? Own model or third-party ASR?",
   "blocks_criteria": [
    "moat",
    "product"
   ]
  },
  {
   "what": "Call-recording consent and data handling",
   "why_it_matters": "Founders name telecom recording restrictions as a key risk; DPDP consent duties take effect May 2027 and BFSI buyers require vendor compliance.",
   "searched": [
    "web: call recording consent India DPDP Act sales calls telecom TRAI"
   ],
   "ask_founder": "How is consent captured on calls you record, where is audio stored, and have any BFSI customers completed a security/vendor review?",
   "blocks_criteria": [
    "regulatory"
   ]
  },
  {
   "what": "Customer concentration",
   "why_it_matters": "Founders cite BFSI concentration but give no split.",
   "searched": [
    "form Key risks"
   ],
   "ask_founder": "What share of MRR comes from your top 3 teams and from BFSI?",
   "blocks_criteria": [
    "traction"
   ]
  }
 ],
 "competitors_named": [
  "Gong",
  "Otter",
  "Fireflies"
 ],
 "competitors_found": [
  "MeetRecord / Outdoo AI (All In Capital portfolio)",
  "Convin",
  "ConvoZen (NoBroker)",
  "Enthu.ai",
  "Mihup"
 ],
 "keywords": [
  "call summary",
  "call recording",
  "transcription",
  "speech to text",
  "CRM update",
  "sales calls",
  "conversation intelligence",
  "sales coaching",
  "meeting notes",
  "code-mixed Hindi",
  "inside sales"
 ],
 "founder_contact": null,
 "sources": [
  {
   "id": "D1",
   "kind": "deck",
   "title": "Talkbook deck - cover",
   "url": null,
   "locator": "Cover",
   "retrieved_on": null,
   "quote": "AI call summaries and CRM updates for Indian sales teams"
  },
  {
   "id": "D2",
   "kind": "deck",
   "title": "Talkbook deck - Traction",
   "url": null,
   "locator": "Slide 6 (Traction)",
   "retrieved_on": null,
   "quote": "Traction: 16 paying teams in 4 months"
  },
  {
   "id": "D3",
   "kind": "deck",
   "title": "Talkbook deck - Traction (MRR stat)",
   "url": null,
   "locator": "Slide 6 (Traction)",
   "retrieved_on": null,
   "quote": "INR 2.1 L monthly recurring revenue"
  },
  {
   "id": "D6",
   "kind": "deck",
   "title": "Talkbook deck - Traction chart extraction note",
   "url": null,
   "locator": "Slide 6 (chart comment)",
   "retrieved_on": null,
   "quote": "chart values as extracted from the PDF: 210, 140, 85, 40 against months Jul, Aug, Sep, Oct"
  },
  {
   "id": "D4",
   "kind": "deck",
   "title": "Talkbook deck - Go-to-market and CAC",
   "url": null,
   "locator": "Slide 8",
   "retrieved_on": null,
   "quote": "Average team pays INR 13,000 a month. CAC counts founder time at a nominal salary."
  },
  {
   "id": "D5",
   "kind": "deck",
   "title": "Talkbook deck - Market size",
   "url": null,
   "locator": "Slide 7",
   "retrieved_on": null,
   "quote": "Rep counts from industry estimates. INR 6,000 a seat a year is our current price."
  },
  {
   "id": "D7",
   "kind": "deck",
   "title": "Talkbook deck - The team (CEO)",
   "url": null,
   "locator": "Slide 10",
   "retrieved_on": null,
   "quote": "6 years as a product lead at a CRM software company."
  },
  {
   "id": "D8",
   "kind": "deck",
   "title": "Talkbook deck - The team (CTO)",
   "url": null,
   "locator": "Slide 10",
   "retrieved_on": null,
   "quote": "4 years in speech ML at a speech-technology company."
  },
  {
   "id": "D9",
   "kind": "deck",
   "title": "Talkbook deck - The ask",
   "url": null,
   "locator": "Slide 11",
   "retrieved_on": null,
   "quote": "In 12 months: 80 paying teams and INR 12 L monthly recurring revenue."
  },
  {
   "id": "D10",
   "kind": "deck",
   "title": "Talkbook deck - Problem",
   "url": null,
   "locator": "Slide 3",
   "retrieved_on": null,
   "quote": "Hindi-English and Tamil- English calls are poorly transcribed by global tools."
  },
  {
   "id": "D11",
   "kind": "deck",
   "title": "Talkbook deck - Why now",
   "url": null,
   "locator": "Slide 4",
   "retrieved_on": null,
   "quote": "Cost per call minute has fallen 8x in two years."
  },
  {
   "id": "D12",
   "kind": "deck",
   "title": "Talkbook deck - The team (size)",
   "url": null,
   "locator": "Slide 10",
   "retrieved_on": null,
   "quote": "Team of 8."
  },
  {
   "id": "D13",
   "kind": "deck",
   "title": "Talkbook deck - Call, summarise, update",
   "url": null,
   "locator": "Slide 5",
   "retrieved_on": null,
   "quote": "Fields in the CRM fill in automatically."
  },
  {
   "id": "F1",
   "kind": "form",
   "title": "Application form - Revenue",
   "url": null,
   "locator": "Product and traction > Revenue",
   "retrieved_on": null,
   "quote": "MRR INR 1.9 L (INR 500 per seat per month)."
  },
  {
   "id": "F2",
   "kind": "form",
   "title": "Application form - Customers",
   "url": null,
   "locator": "Product and traction > Customers",
   "retrieved_on": null,
   "quote": "16 paying teams, 340 paid seats."
  },
  {
   "id": "F3",
   "kind": "form",
   "title": "Application form - Unit economics",
   "url": null,
   "locator": "Product and traction > Unit economics",
   "retrieved_on": null,
   "quote": "CAC about INR 48,000 per team, including founder time at a nominal salary. Gross margin 70%. Payback about 5 months."
  },
  {
   "id": "F4",
   "kind": "form",
   "title": "Application form - Competition",
   "url": null,
   "locator": "Product and traction > Competition",
   "retrieved_on": null,
   "quote": "Gong and similar global tools, and meeting note-takers like Otter and Fireflies. We do not know of an India-first player."
  },
  {
   "id": "F5",
   "kind": "form",
   "title": "Application form - Key risks",
   "url": null,
   "locator": "Product and traction > Key risks",
   "retrieved_on": null,
   "quote": "Telecom call-recording restrictions, accuracy on noisy calls, and customer concentration in BFSI."
  },
  {
   "id": "F6",
   "kind": "form",
   "title": "Application form - Founder 1",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "Arun Kumar, CEO. 6 years as a product lead at a CRM software company. linkedin.com/in/arun-kumar-example"
  },
  {
   "id": "F7",
   "kind": "form",
   "title": "Application form - Founder 2",
   "url": null,
   "locator": "Founders > Founder 2",
   "retrieved_on": null,
   "quote": "Meenakshi S, CTO. 4 years in speech ML at a speech-technology company. linkedin.com/in/meenakshi-s-example"
  },
  {
   "id": "F8",
   "kind": "form",
   "title": "Application form - Sector (as selected)",
   "url": null,
   "locator": "Company > Sector (as selected)",
   "retrieved_on": null,
   "quote": "Consumer tech"
  },
  {
   "id": "F9",
   "kind": "form",
   "title": "Application form - Valuation expectation",
   "url": null,
   "locator": "Fundraising > Valuation expectation",
   "retrieved_on": null,
   "quote": "INR 12 Cr post-money"
  },
  {
   "id": "F10",
   "kind": "form",
   "title": "Application form - Equity split",
   "url": null,
   "locator": "Founders > Equity split",
   "retrieved_on": null,
   "quote": "Founders 95%, ESOP 5%."
  },
  {
   "id": "F11",
   "kind": "form",
   "title": "Application form - Time commitment",
   "url": null,
   "locator": "Founders > Time commitment",
   "retrieved_on": null,
   "quote": "Both full-time since March 2026."
  },
  {
   "id": "F12",
   "kind": "form",
   "title": "Application form - Other investors in conversation",
   "url": null,
   "locator": "Fundraising > Other investors in conversation",
   "retrieved_on": null,
   "quote": "One pre-seed fund."
  },
  {
   "id": "F13",
   "kind": "form",
   "title": "Application form - What have you built?",
   "url": null,
   "locator": "Product and traction > What have you built?",
   "retrieved_on": null,
   "quote": "A call-recording and transcription layer for sales teams, with summaries and CRM field updates."
  },
  {
   "id": "F14",
   "kind": "form",
   "title": "Application form - Customer acquisition",
   "url": null,
   "locator": "Product and traction > Customer acquisition",
   "retrieved_on": null,
   "quote": "Founder-led outbound brought 9 teams, referrals 5 and CRM consultants 2."
  },
  {
   "id": "W1",
   "kind": "web",
   "title": "Inc42 - MeetRecord bags $2.7 Mn funding to enhance AI-powered sales coaching platform (21 Jun 2024)",
   "url": "https://inc42.com/buzz/meetrecord-bags-2-7-mn-funding-to-enhance-ai-powered-sales-coaching-platform",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "with existing investor All In Capital also participating"
  },
  {
   "id": "W2",
   "kind": "web",
   "title": "Outdoo AI press release - MeetRecord Pre-Series A funding (June 2024)",
   "url": "https://www.outdoo.ai/press-release/meetrecord-pre-series-a-funding",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "with additional support from exisiting investor All In Capital."
  },
  {
   "id": "W3",
   "kind": "web",
   "title": "Outdoo AI (formerly MeetRecord; www.meetrecord.com redirects here) - product homepage",
   "url": "https://www.outdoo.ai/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "updates the CRM from the call"
  },
  {
   "id": "W4",
   "kind": "web",
   "title": "Entrackr - Convin raises $6.5 Mn in Series A led by India Quotient (27 Aug 2024)",
   "url": "https://entrackr.com/2024/08/convin-raises-6-5-mn-in-series-a-round-led-by-india-quotient",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Convin has raised $6.5 million in its Series A funding round led by India Quotient"
  },
  {
   "id": "W5",
   "kind": "web",
   "title": "Business Today - How ConvoZen is emerging as NoBroker's new growth engine (24 Feb 2026)",
   "url": "https://www.businesstoday.in/latest/corporate/story/how-convozen-is-emerging-as-nobrokers-new-growth-engine-517791-2026-02-24",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "ConvoZen now handles over 2 million conversations a day across more than 50 enterprises"
  },
  {
   "id": "W6",
   "kind": "web",
   "title": "StartupTalky - Enthu.ai success story",
   "url": "https://startuptalky.com/enthu-ai-success-story/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Enthu is a SaaS-based conversation intelligence platform that turns customer calls into actionable insights."
  },
  {
   "id": "W7",
   "kind": "web",
   "title": "King Stubb & Kasiva - Marketing consent in India: TRAI TCCCPR and DPDP Act",
   "url": "https://ksandk.com/data-protection-and-data-privacy/marketing-consent-india-trai-tcccpr-dpdp-act/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "are scheduled to come into force on 13 May 2027"
  }
 ],
 "produced_by": "claude-code-session (in-session run of prompts/research.md; no API key)",
 "research_notes": "Key finding: MeetRecord (now Outdoo AI), an All In Capital portfolio company per its June 2024 round coverage, does call transcription, summaries and CRM updates; the application does not mention it and claims no India-first competitor exists. Deck vs form: MRR 2.1 L vs 1.9 L (and 1.7 L from seats x price). Sector ticked as consumer tech; actually B2B SaaS. No founder/company footprint found. Web quotes were extracted via a fetch tool and should be re-verified with verify_web."
}
</dossier>

Score every criterion in both lenses (R1-R6, S1-S4) and evaluate gates G1-G4.