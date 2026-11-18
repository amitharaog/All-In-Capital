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
- C003 ((meeting-notes startup), by Kushal / Aditya (partner notes, Meeting 4)): Scored 7 before anyone noticed it overlaps portfolio company MeetRecord. Check every application against the full portfolio list; default is no to competitors unless both founders know. Prefer a false-alarm flag to a miss.  (matched on: consumer_tech, portfolio_overlap)
</partner_corrections>

<dossier>
{
 "company": "Yatrika",
 "slug": "yatrika",
 "one_liner": "AI-drafted family trip itineraries from Tier-2 cities, with local guides, taxis and stays booked and confirmed manually on WhatsApp; earns a 12% commission on booking value.",
 "sector": "consumer_tech",
 "sub_sector": "Travel tech / family holiday packages (agency operations with an LLM itinerary front end)",
 "stage": "Pre-seed",
 "ask": "INR 1.2 Cr at INR 8 Cr post-money (form); the deck states no amount",
 "business_model": "Commission (12%) on total booking value of trips assembled from local guides, taxis and stays; bookings confirmed manually on WhatsApp. Founder-stated GBV INR 38.6 L and revenue INR 4.6 L since launch.",
 "founders": [
  {
   "name": "Manish Joshi",
   "role": "Founder",
   "background_claimed": "10 years running his family's travel agency in Jaipur, which has served over 3,000 families. Prior startup experience: has run a family business.",
   "background_verified": "Not verified. LinkedIn link given is a placeholder (linkedin.com/in/manish-joshi-example). Web search for name + Yatrika + Jaipur returned no matching person or agency; the family agency is not named in the application.",
   "public_footprint": "not_found",
   "source_ids": [
    "D2",
    "F3",
    "F5"
   ]
  },
  {
   "name": "Kavya Nair",
   "role": "Co-founder (Tech)",
   "background_claimed": "3 years as a web developer. No prior startup experience.",
   "background_verified": "Not verified. LinkedIn link is a placeholder (linkedin.com/in/kavya-nair-example). Web search for name + Yatrika + Jaipur + web developer returned nothing matching.",
   "public_footprint": "not_found",
   "source_ids": [
    "D3",
    "F4",
    "F5"
   ]
  }
 ],
 "claims": [
  {
   "text": "Manish Joshi has 10 years running his family's travel agency in Jaipur, which has served over 3,000 families.",
   "source_ids": [
    "D2",
    "F3"
   ],
   "status": "founder_stated",
   "note": "Deck and form agree. Agency name not given; no independent trace found."
  },
  {
   "text": "Kavya Nair (technical co-founder) has 3 years as a web developer and no prior startup experience.",
   "source_ids": [
    "D3",
    "F4",
    "F5"
   ],
   "status": "founder_stated",
   "note": "No ML/AI background is claimed even though the product is pitched as 'planned by AI'."
  },
  {
   "text": "Both founders' LinkedIn links are placeholder URLs; no public footprint for either founder was found on the web.",
   "source_ids": [
    "F3",
    "F4"
   ],
   "status": "unverifiable",
   "note": "Searched name + company + city for both founders; no matching profiles, press or registry hits."
  },
  {
   "text": "Deck says Yatrika has 'served thousands of travellers'; the form states about 1,300 travellers across 410 bookings.",
   "source_ids": [
    "D4",
    "F7"
   ],
   "status": "contradicted",
   "note": "1,300 travellers is not 'thousands'. The deck inflates the only hard traction number the form gives."
  },
  {
   "text": "Deck claims operations across Rajasthan and Uttarakhand and that the company is 'growing across India'; the form gives Jaipur as the only location and describes acquisition as referrals from Manish's earlier agency customers plus Instagram.",
   "source_ids": [
    "D4",
    "D5",
    "F10"
   ],
   "status": "unverifiable",
   "note": "No booking split by region or city is given anywhere; 'strong brand' and 'growing across India' are unevidenced."
  },
  {
   "text": "Deck claims '3x growth' and 'many 5-star reviews' with no baseline, period or review source.",
   "source_ids": [
    "D4"
   ],
   "status": "unverifiable",
   "note": "No monthly bookings series or review platform given; no reviews found online."
  },
  {
   "text": "Total booking value since launch is INR 38.6 L; at a 12% commission revenue is INR 4.6 L.",
   "source_ids": [
    "F8"
   ],
   "status": "founder_stated",
   "note": "Arithmetic is consistent (38.6 L x 12% = 4.63 L). Implied average booking value ~INR 9,400 and commission ~INR 1,130 per booking (410 bookings)."
  },
  {
   "text": "Paid acquisition costs about INR 640 per booking, against implied commission of ~INR 1,130 per booking.",
   "source_ids": [
    "F8",
    "F10",
    "F7"
   ],
   "status": "founder_stated",
   "note": "Our arithmetic: paid CAC consumes ~57% of first-booking commission before guide/taxi/ops costs. Share of bookings that are paid vs referral is not given."
  },
  {
   "text": "14% of families have booked a second trip.",
   "source_ids": [
    "F9"
   ],
   "status": "founder_stated",
   "note": "No cohort window given; many early customers came from the founder's prior agency, which may flatter repeat."
  },
  {
   "text": "The 'AI' is a language model drafting itineraries over 40 hand-built route templates; bookings are confirmed manually on WhatsApp.",
   "source_ids": [
    "F6",
    "D7",
    "D1"
   ],
   "status": "founder_stated",
   "note": "Deck frames trips as 'planned by AI'; the form makes clear the product is templates plus manual operations. Founders themselves list manual operations that do not scale as a key risk."
  },
  {
   "text": "Company incorporated March 2026 (Yatrika Travel Pvt. Ltd.); both founders full-time since March 2026.",
   "source_ids": [
    "F1",
    "F17"
   ],
   "status": "founder_stated",
   "note": "Deck's 'in just 7 months' is consistent with a March 2026 start. No MCA/registry record for 'Yatrika Travel Pvt. Ltd.' surfaced in web search."
  },
  {
   "text": "Team size is 4 (form); the deck names only the two founders and gives no team size.",
   "source_ids": [
    "F2",
    "D2"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Raising INR 1.2 Cr at INR 8 Cr post-money; the deck's ask slide gives no amount, milestones or use-of-funds split.",
   "source_ids": [
    "F12",
    "F13",
    "D6",
    "F16"
   ],
   "status": "founder_stated",
   "note": "Use of funds is a generic list (marketing, technology, hiring, expansion) in both documents."
  },
  {
   "text": "Market sizing is a single top-down number (INR 3 lakh Cr Indian domestic tourism spend) with no SAM/SOM or family/Tier-2 share.",
   "source_ids": [
    "D8"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "The deck repeats the same vision slide twice (slides 7 and 9) and the ask slide precedes the solution slide.",
   "source_ids": [
    "D9"
   ],
   "status": "verified",
   "note": "Deck-quality observation from the file itself."
  },
  {
   "text": "Thrillophilia, an established travel-experience booking platform, is headquartered in Jaipur, Yatrika's home city.",
   "source_ids": [
    "W1"
   ],
   "status": "verified",
   "note": null
  },
  {
   "text": "Experiential-travel competitor WanderOn raised INR 54 Cr Series A in January 2026; press places it alongside Thrillophilia, TravelTriangle, Tripoto and Holidify.",
   "source_ids": [
    "W2"
   ],
   "status": "verified",
   "note": null
  },
  {
   "text": "MakeMyTrip launched a GenAI trip-planning assistant (Myra) in August 2025, live in English and Hindi with more Indian languages planned.",
   "source_ids": [
    "W3"
   ],
   "status": "verified",
   "note": "Free AI itinerary generation is offered by the category leader, so the itinerary itself is not a moat."
  },
  {
   "text": "GuavaTrips (Pune, founded April 2024) offers free AI-generated personalised itineraries with end-to-end booking and concierge support.",
   "source_ids": [
    "W4"
   ],
   "status": "verified",
   "note": "Source is a paid press release."
  },
  {
   "text": "Tier-2 and Tier-3 city travellers are driving a rise in festive travel demand (Thrillophilia Festive Travel Pulse 2025).",
   "source_ids": [
    "W5"
   ],
   "status": "verified",
   "note": "Supports the Tier-2 demand thesis, but the source is a competitor's own report."
  },
  {
   "text": "Founder-listed key risks: quality of local partners, seasonality and manual operations that do not yet scale.",
   "source_ids": [
    "F11"
   ],
   "status": "founder_stated",
   "note": null
  },
  {
   "text": "Sector selected as consumer tech; the business is a commission-based travel agency with a software front end, consistent with consumer_tech.",
   "source_ids": [
    "F15"
   ],
   "status": "founder_stated",
   "note": null
  }
 ],
 "gaps": [
  {
   "what": "Founder identity and background (both founders)",
   "why_it_matters": "The whole edge claimed is Manish's 10-year agency track record and 3,000-family customer base; none of it is independently traceable.",
   "searched": [
    "web: \"Yatrika\" travel Jaipur AI family trips Manish Joshi",
    "web: \"Kavya Nair\" Yatrika web developer Jaipur",
    "LinkedIn links in form (placeholders: *-example)"
   ],
   "ask_founder": "What is the name and GSTIN of the family travel agency, how long has Manish run it, and can you share real LinkedIn/GitHub profiles for both founders?",
   "blocks_criteria": [
    "founder_market_fit",
    "team"
   ]
  },
  {
   "what": "Relationship between Yatrika and the family agency",
   "why_it_matters": "If most of the 410 bookings are the agency's existing customers moved onto WhatsApp, traction measures the old business, not new demand.",
   "searched": [
    "deck",
    "form"
   ],
   "ask_founder": "Of the 410 bookings, how many came from the family agency's prior customers vs Instagram vs paid ads? Is the agency still operating separately, and does it own any Yatrika equity or revenue?",
   "blocks_criteria": [
    "traction"
   ]
  },
  {
   "what": "Company registration and web presence",
   "why_it_matters": "No MCA record, live website (www.yatrika.example is a placeholder), app listing or review page was found to corroborate the company exists as described.",
   "searched": [
    "web: \"Yatrika Travel\" Private Limited Jaipur company registration",
    "web: Yatrika travel Jaipur"
   ],
   "ask_founder": "Please share the CIN, live website/Instagram handle and Google review page.",
   "blocks_criteria": [
    "traction"
   ]
  },
  {
   "what": "Month-by-month bookings and the basis of '3x growth'",
   "why_it_matters": "Seasonality is a stated risk; without a monthly series we cannot tell growth from a festive/summer spike.",
   "searched": [
    "deck slide 4",
    "form Customers/Revenue"
   ],
   "ask_founder": "Share bookings, GBV and revenue by month since launch, and define what grew 3x over what period.",
   "blocks_criteria": [
    "traction"
   ]
  },
  {
   "what": "Contribution margin per booking",
   "why_it_matters": "At ~INR 1,130 commission per booking and INR 640 paid CAC, manual WhatsApp operations and refunds could make each booking loss-making.",
   "searched": [
    "form Revenue, Customer acquisition"
   ],
   "ask_founder": "What is the operations cost (staff time, calls, cancellations/refunds) per booking, and what is contribution margin after CAC?",
   "blocks_criteria": [
    "unit_economics"
   ]
  },
  {
   "what": "Supply side: number and vetting of local partners, especially outside Rajasthan",
   "why_it_matters": "Partner quality is the founders' own top risk and the core of 'led by locals'; deck claims Uttarakhand operations not mentioned in the form.",
   "searched": [
    "deck",
    "form"
   ],
   "ask_founder": "How many guides, taxi operators and stays are on the platform, by state, how are they vetted, and who is liable when a trip goes wrong?",
   "blocks_criteria": [
    "product"
   ]
  },
  {
   "what": "Differentiation vs free AI planners and Jaipur-based Thrillophilia",
   "why_it_matters": "MakeMyTrip's Myra and others give AI itineraries free; the application names no competitors at all.",
   "searched": [
    "web: MakeMyTrip AI trip planner Myra",
    "web: Thrillophilia Jaipur",
    "web: WanderOn/Pickyourtrail/TravelTriangle funding"
   ],
   "ask_founder": "Who do you lose bookings to today, and why would a Tier-2 family book through Yatrika rather than MakeMyTrip Holidays or a local agent?",
   "blocks_criteria": [
    "market",
    "moat"
   ]
  },
  {
   "what": "Milestones for the INR 1.2 Cr raise",
   "why_it_matters": "Neither deck nor form says what the money achieves or how long it lasts.",
   "searched": [
    "deck slide 5",
    "form Fundraising"
   ],
   "ask_founder": "What monthly bookings, cities and contribution margin will INR 1.2 Cr get you to, and over how many months?",
   "blocks_criteria": [
    "capital_efficiency"
   ]
  }
 ],
 "competitors_named": [],
 "competitors_found": [
  "Thrillophilia (Jaipur HQ)",
  "MakeMyTrip (Myra GenAI trip planner)",
  "WanderOn",
  "TravelTriangle",
  "Tripoto",
  "Holidify",
  "GuavaTrips"
 ],
 "keywords": [
  "family trips",
  "trip planning",
  "AI itinerary",
  "holiday packages",
  "travel agency",
  "local guides",
  "taxi booking",
  "hotel stays",
  "WhatsApp booking",
  "Tier-2 travellers",
  "domestic tourism"
 ],
 "founder_contact": "hello@yatrika.example (placeholder domain)",
 "sources": [
  {
   "id": "D1",
   "kind": "deck",
   "title": "Yatrika deck - cover",
   "url": null,
   "locator": "Cover",
   "retrieved_on": null,
   "quote": "Family trips, planned by AI, led by locals"
  },
  {
   "id": "D2",
   "kind": "deck",
   "title": "Yatrika deck - Our team",
   "url": null,
   "locator": "Slide 3 (Our team)",
   "retrieved_on": null,
   "quote": "10 years running his family's travel agency in Jaipur, serving over 3,000 families."
  },
  {
   "id": "D3",
   "kind": "deck",
   "title": "Yatrika deck - Our team",
   "url": null,
   "locator": "Slide 3 (Our team)",
   "retrieved_on": null,
   "quote": "3 years as a web developer."
  },
  {
   "id": "D4",
   "kind": "deck",
   "title": "Yatrika deck - Traction",
   "url": null,
   "locator": "Slide 4 (Traction)",
   "retrieved_on": null,
   "quote": "In just 7 months we have served thousands of travellers across Rajasthan and Uttarakhand, with 3x growth and many 5-star reviews."
  },
  {
   "id": "D5",
   "kind": "deck",
   "title": "Yatrika deck - Traction",
   "url": null,
   "locator": "Slide 4 (Traction)",
   "retrieved_on": null,
   "quote": "We have built a strong brand in Jaipur and are growing across India."
  },
  {
   "id": "D6",
   "kind": "deck",
   "title": "Yatrika deck - The ask",
   "url": null,
   "locator": "Slide 5 (The ask)",
   "retrieved_on": null,
   "quote": "We are raising funds to grow."
  },
  {
   "id": "D7",
   "kind": "deck",
   "title": "Yatrika deck - Our solution",
   "url": null,
   "locator": "Slide 6 (Our solution)",
   "retrieved_on": null,
   "quote": "Families answer 6 questions and get an itinerary in 2 minutes. Trips are confirmed on WhatsApp."
  },
  {
   "id": "D8",
   "kind": "deck",
   "title": "Yatrika deck - Market",
   "url": null,
   "locator": "Slide 8 (Market)",
   "retrieved_on": null,
   "quote": "Domestic travel is growing fast as Tier-2 families travel more. We are well placed to capture this growth."
  },
  {
   "id": "D9",
   "kind": "deck",
   "title": "Yatrika deck - Our vision (appears on slides 7 and 9)",
   "url": null,
   "locator": "Slides 7 and 9 (Our vision)",
   "retrieved_on": null,
   "quote": "To become India's most loved family travel brand."
  },
  {
   "id": "F1",
   "kind": "form",
   "title": "Application form - Time commitment",
   "url": null,
   "locator": "Founders > Time commitment",
   "retrieved_on": null,
   "quote": "Both full-time since March 2026."
  },
  {
   "id": "F2",
   "kind": "form",
   "title": "Application form - Team size",
   "url": null,
   "locator": "Company > Team size",
   "retrieved_on": null,
   "quote": "Team size 4"
  },
  {
   "id": "F3",
   "kind": "form",
   "title": "Application form - Founder 1",
   "url": null,
   "locator": "Founders > Founder 1",
   "retrieved_on": null,
   "quote": "Manish Joshi. 10 years running his family's travel agency in Jaipur, which has served over 3,000 families. linkedin.com/in/manish-joshi-example"
  },
  {
   "id": "F4",
   "kind": "form",
   "title": "Application form - Founder 2",
   "url": null,
   "locator": "Founders > Founder 2",
   "retrieved_on": null,
   "quote": "Kavya Nair. 3 years as a web developer. linkedin.com/in/kavya-nair-example"
  },
  {
   "id": "F5",
   "kind": "form",
   "title": "Application form - Prior startup experience",
   "url": null,
   "locator": "Founders > Prior startup experience",
   "retrieved_on": null,
   "quote": "Manish has run a family business. Kavya has none."
  },
  {
   "id": "F6",
   "kind": "form",
   "title": "Application form - What have you built?",
   "url": null,
   "locator": "Product and traction > What have you built?",
   "retrieved_on": null,
   "quote": "The itinerary uses a language model and 40 hand-built route templates. Bookings are confirmed manually on WhatsApp."
  },
  {
   "id": "F7",
   "kind": "form",
   "title": "Application form - Customers",
   "url": null,
   "locator": "Product and traction > Customers",
   "retrieved_on": null,
   "quote": "410 bookings since launch, covering about 1,300 travellers."
  },
  {
   "id": "F8",
   "kind": "form",
   "title": "Application form - Revenue",
   "url": null,
   "locator": "Product and traction > Revenue",
   "retrieved_on": null,
   "quote": "Total booking value INR 38.6 L. We earn a 12% commission, so revenue is INR 4.6 L."
  },
  {
   "id": "F9",
   "kind": "form",
   "title": "Application form - Repeat",
   "url": null,
   "locator": "Product and traction > Repeat",
   "retrieved_on": null,
   "quote": "14% of families have booked a second trip."
  },
  {
   "id": "F10",
   "kind": "form",
   "title": "Application form - Customer acquisition",
   "url": null,
   "locator": "Product and traction > Customer acquisition",
   "retrieved_on": null,
   "quote": "Referrals from Manish's earlier agency customers and Instagram. Paid acquisition is about INR 640 per booking."
  },
  {
   "id": "F11",
   "kind": "form",
   "title": "Application form - Key risks",
   "url": null,
   "locator": "Product and traction > Key risks",
   "retrieved_on": null,
   "quote": "Quality of local partners, seasonality and manual operations that do not yet scale."
  },
  {
   "id": "F12",
   "kind": "form",
   "title": "Application form - Amount raising",
   "url": null,
   "locator": "Fundraising > Amount raising",
   "retrieved_on": null,
   "quote": "INR 1.2 Cr"
  },
  {
   "id": "F13",
   "kind": "form",
   "title": "Application form - Valuation expectation",
   "url": null,
   "locator": "Fundraising > Valuation expectation",
   "retrieved_on": null,
   "quote": "INR 8 Cr post-money"
  },
  {
   "id": "F14",
   "kind": "form",
   "title": "Application form - Website",
   "url": null,
   "locator": "Company > Website",
   "retrieved_on": null,
   "quote": "www.yatrika.example"
  },
  {
   "id": "F15",
   "kind": "form",
   "title": "Application form - Sector (as selected)",
   "url": null,
   "locator": "Company > Sector (as selected)",
   "retrieved_on": null,
   "quote": "Consumer tech"
  },
  {
   "id": "F16",
   "kind": "form",
   "title": "Application form - Use of funds",
   "url": null,
   "locator": "Fundraising > Use of funds",
   "retrieved_on": null,
   "quote": "Marketing, technology, hiring, expansion."
  },
  {
   "id": "F17",
   "kind": "form",
   "title": "Application form - Company name",
   "url": null,
   "locator": "Company > Company name",
   "retrieved_on": null,
   "quote": "Yatrika (Yatrika Travel Pvt. Ltd.)"
  },
  {
   "id": "W1",
   "kind": "web",
   "title": "Inc42 company profile - Thrillophilia.com",
   "url": "https://inc42.com/company/thrillophilia-com/",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Thrillophilia.com is headquartered in Jaipur, India."
  },
  {
   "id": "W2",
   "kind": "web",
   "title": "Entrepreneur India - WanderOn raises INR 54 Cr Series A (20 Jan 2026)",
   "url": "https://india.entrepreneur.com/news-and-trends/wanderon-raises-inr-54-cr-series-a-to-expand-experiential/502045",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "WanderOn has secured INR 54 crore in a Series A funding round co-led by DSG Consumer Partners and CAAF."
  },
  {
   "id": "W3",
   "kind": "web",
   "title": "The Week (PTI) - MakeMyTrip launches GenAI-enabled trip planning assistant (7 Aug 2025)",
   "url": "https://www.theweek.in/wire-updates/business/2025/08/07/dcm32-biz-brief.html",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "The Beta version of Myra is now live in English and Hindi"
  },
  {
   "id": "W4",
   "kind": "web",
   "title": "The Tribune (press release) - GuavaTrips free AI-powered personalised itineraries (14 Nov 2025)",
   "url": "https://www.tribuneindia.com/news/business/guavatrips-disrupts-indian-travel-with-free-ai-powered-personalized-itineraries",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "the company delivers free custom itineraries, end-to-end booking, and 24/7 concierge support"
  },
  {
   "id": "W5",
   "kind": "web",
   "title": "Hospibuz - Thrillophilia Festive Travel Pulse 2025 (25 Sep 2025)",
   "url": "https://hospibuz.com/travels-opinion/festive-travel-demand-soars-18-thrillophilia-unveils-festive-travel-pulse-2025-10500135",
   "locator": null,
   "retrieved_on": "2026-11-18",
   "quote": "Travellers from Tier-2 and Tier-3 cities, including Surat, Coimbatore, Indore, Nagpur, Vizag, and Vadodara, are fuelling"
  }
 ],
 "produced_by": "claude-code-session (in-session run of prompts/research.md; no API key)",
 "research_notes": "Founder and company searches returned nothing (placeholder *.example links). No MCA hit for Yatrika Travel Pvt. Ltd. (closest: unrelated Yatrik Trails (OPC) Pvt Ltd, Delhi). Deck vs form: 'thousands of travellers' vs ~1,300; deck has no ask amount. Competitive set found via web; the application names none. Web quotes were extracted via a fetch tool and should be re-verified with verify_web."
}
</dossier>

Score every criterion in both lenses (R1-R6, S1-S4) and evaluate gates G1-G4.