#!/usr/bin/env python3
"""Builds the Emprise Partners multi-page site from shared header/footer."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

MARK = '''<svg class="mk" viewBox="0 0 151 150" aria-hidden="true"><mask id="{id}"><rect width="151" height="150" fill="#fff"/><rect x="37" y="72" width="44" height="42" fill="#000"/></mask><g mask="url(#{id})"><rect x="37" y="0" width="114" height="114" fill="#1a92c1"/><rect x="0" y="36" width="114" height="114" fill="#0c52ac"/><rect x="37" y="36" width="77" height="78" fill="#0e6cb6"/></g></svg><span class="word"><b>Emprise</b><small>PARTNERS</small></span>'''

NAV = [('about.html', 'About'), ('services.html', 'Services'), ('past-performance.html', 'Past performance'),
       ('partners.html', 'Partners'), ('contact.html', 'Contact')]

UEI, CAGE, NAICS = 'VA4LAHDJT2R3', '9V3J1', '561210'

SERVICES = [
    ('janitorial', 'Janitorial & Custodial', 'janitorial',
     'Scheduled cleaning programs for offices, government buildings and multi-site portfolios, plus exterior pressure washing.',
     ['Recurring office and building cleaning', 'Park and restroom custodial service', 'Floor care', 'Exterior pressure washing', 'Window cleaning', 'Multi-site programs']),
    ('grounds', 'Landscaping & Grounds', 'grounds',
     'Landscaping and grounds maintenance for campuses, communities and public sites, delivered to one standard everywhere.',
     ['Mowing and grounds maintenance', 'Landscape and median maintenance', 'Tree trimming and removal', 'Sod installation', 'Irrigation', 'Lot clearing']),
    ('building', 'Building Systems & Trades', 'facility',
     'HVAC, plumbing, painting, roofing, flooring and doors, coordinated and scheduled by Emprise Partners.',
     ['HVAC repair and replacement', 'Plumbing', 'Interior and exterior painting', 'Roofing', 'Flooring', 'Doors and fencing']),
    ('lifesafety', 'Life Safety & Pest Control', 'lifesafety',
     'Fire alarm and sprinkler inspections, service and documentation, alongside integrated pest control.',
     ['Fire alarm inspection and service', 'Sprinkler inspection and service', 'Fire extinguisher inspection', 'Integrated pest management', 'Inspection documentation']),
    ('waste', 'Waste & Sanitation', 'waste',
     'Trash, recycling and roll-off service, debris removal, portable toilets and septic support.',
     ['Trash and recycling collection', 'Roll-off and dumpster service', 'Debris removal and haul-away', 'Portable toilets', 'Septic and grease trap service']),
    ('specialty', 'Security & Specialty', 'security',
     'Security and site support, moving and relocation, courier and other specialty services.',
     ['Unarmed security and site support', 'Moving and relocation', 'Courier services', 'Pool cleaning', 'Event support']),
]

PROJECTS = [
    ('USDA Forest Service', 'Federal', 'Idaho, Colorado & Montana', 'Portable Toilets and Hand Wash Stations Rental', 'Waste & Sanitation',
     'Season-long rental and weekly servicing of portable toilets and handwashing stations supporting fire-season crews across multiple National Forests in Idaho, Colorado and Montana.'),
    ('City of Fort Pierce', 'Municipal', 'Fort Pierce, FL', 'Recreation Center Interior Painting', 'Building Systems & Trades',
     'Interior painting at a City recreation center.'),
    ('City of Plant City', 'Municipal', 'Plant City, FL', 'Traffic Compound Fence Replacement', 'Building Systems & Trades',
     'Removal and replacement of fencing at the City traffic compound.'),
    ('City of Orlando', 'Municipal', 'Orlando, FL', 'Tree Removal Services', 'Landscaping & Grounds',
     'Tree removal services for the City of Orlando.'),
    ('U.S. Department of Agriculture', 'Federal', '', 'Vehicle Services Building Exterior Painting', 'Building Systems & Trades',
     'Exterior painting of a USDA vehicle services building.'),
]

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@300;400;500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
'''

def header(cur):
    links = '\n'.join(f'   <a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a>' for h, t in NAV)
    return f'''<header>
 <nav class="nav" aria-label="Main">
  <a class="logo" href="index.html" aria-label="Emprise Partners home">{MARK.format(id="mkA")}</a>
  <div class="links" id="links">
{links}
  </div>
  <a class="btn pri" href="Emprise_Partners_Capability_Statement.pdf" target="_blank" rel="noopener">Capability statement</a>
  <button class="menu" id="menu" aria-label="Open menu" aria-expanded="false" aria-controls="links">
   <svg width="26" height="26" viewBox="0 0 26 26" aria-hidden="true"><path d="M3 7h20M3 13h20M3 19h20" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
  </button>
 </nav>
</header>
<main id="main">
'''

FOOTER = f'''</main>
<footer>
 <div class="wrap">
  <div class="foot">
   <div>
    <a class="logo" href="index.html">{MARK.format(id="mkB")}</a>
    <p style="margin-top:16px;max-width:40ch">Facility support and site services for government, commercial and institutional clients.</p>
    <p style="margin-top:14px;font-size:13px">UEI {UEI} · CAGE {CAGE} · NAICS {NAICS}</p>
   </div>
   <div><h4>Company</h4><ul><li><a href="about.html">About</a></li><li><a href="services.html">Services</a></li><li><a href="past-performance.html">Past performance</a></li></ul></div>
   <div><h4>Work with us</h4><ul><li><a href="partners.html">Trade partners</a></li><li><a href="services.html#commercial">Commercial</a></li><li><a href="contact.html#faq">FAQ</a></li><li><a href="Emprise_Partners_Capability_Statement.pdf" target="_blank" rel="noopener">Capability statement</a></li></ul></div>
   <div><h4>Contact</h4><ul><li>800.254.0658 (toll-free)</li><li>321.414.8926 (local)</li><li>info@emprise-partners.com</li><li>555 Winderley Place, Suite 300<br>Maitland, FL 32751</li></ul></div>
  </div>
  <div class="legal"><span>© 2026 Emprise Partners LLC. All rights reserved.</span><span><a href="privacy.html">Privacy Policy</a> · <a href="terms.html">Terms of Use</a></span></div>
 </div>
</footer>
<script src="site.js"></script>
</body>
</html>
'''

def phero(img, title, sub):
    return f'''<section class="phero" style="background-image:url(photo-{img}.jpg)">
 <div class="wrap"><h1>{title}</h1><p>{sub}</p></div>
</section>
'''

def codes(cls=''):
    return f'''<div class="codes {cls}" aria-label="Contracting information">
   <div><span>UEI</span><b>{UEI}</b></div>
   <div><span>CAGE code</span><b>{CAGE}</b></div>
   <div><span>Primary NAICS</span><b>{NAICS}</b></div>
   <div><span>Headquarters</span><b>Maitland, Florida</b></div>
  </div>'''

def proj_cards(items):
    return '<div class="projects">' + ''.join(
        f'<article class="proj"><div class="meta"><b>{lvl}</b>{f"<span>{loc}</span>" if loc else ""}<span>{line}</span><span>Completed</span></div>'
        f'<h3>{title}</h3><p class="ag">{ag}</p><p>{scope}</p></article>'
        for ag, lvl, loc, title, line, scope in items) + '</div>'

CTA = '''<section class="band ctaband">
 <div class="wrap">
  <h2>Have a requirement or a solicitation coming up?</h2>
  <div class="ctas"><a class="btn pri" href="contact.html">Contact Emprise Partners</a><a class="btn line" href="partners.html">Become a trade partner</a></div>
 </div>
</section>
'''

def page(fn, cur, title, desc, body):
    open(fn, 'w').write(head(title, desc) + header(cur) + body + FOOTER)

# ---------- HOME ----------
tiles = ''.join(f'<article class="tile"><img src="photo-{img}.jpg" alt="" loading="lazy"><div><h3>{t}</h3><p>{d}</p></div><a href="services.html#{sid}" aria-label="{t}"></a></article>'
                for sid, t, img, d, _ in SERVICES)
home = f'''<section class="hero" aria-label="Introduction">
 <div class="wrap">
  <h1>Facility support and site services for the public sector.</h1>
  <p>Emprise Partners primes municipal, county, state and federal contracts, delivered by a vetted network of trade partners in the field.</p>
  <div class="ctas">
   <a class="btn pri" href="Emprise_Partners_Capability_Statement.pdf" target="_blank" rel="noopener">Capability statement</a>
   <a class="btn line" href="partners.html">Become a trade partner</a>
  </div>
 </div>
</section>

<section class="band statement" aria-label="At a glance">
 <div class="wrap">
  <h2>One partner. Multiple services. Consistent accountability.</h2>
  <div class="facts">
   <div class="wide"><b>Nationwide</b><span>Federal, state, local and commercial work across the United States</span></div>
   <div><b>6</b><span>Core service lines</span></div>
   <div><b>1</b><span>Point of contact per contract</span></div>
  </div>
 </div>
</section>

<section class="band">
 <div class="wrap">
  <div class="head"><div><h2>Services</h2><p class="lede">Six core service lines, all managed through one point of contact, for single properties and multi-location portfolios.</p></div><a class="more" href="services.html">All services</a></div>
  <div class="tiles">{tiles}</div>
 </div>
</section>

<section class="band alt">
 <div class="wrap">
  <div class="head"><div><h2>A few of our completed projects</h2><p class="lede">Recent work for municipal and federal clients.</p></div><a class="more" href="past-performance.html">All past performance</a></div>
  {proj_cards(PROJECTS[:4])}
 </div>
</section>

<section class="band photoband">
 <div class="wrap">
  <h2>Agencies we've served</h2>
  <p class="lede">Federal, municipal and county clients.</p>
  <div class="agency">
   <div><h3>Federal</h3><ul><li>U.S. Department of Agriculture</li><li>National Park Service</li></ul></div>
   <div><h3>Municipal</h3><ul><li>City of Orlando</li><li>City of Fort Pierce</li><li>City of Plant City</li></ul></div>
   <div><h3>County</h3><ul><li>Orange County</li><li>Volusia County</li><li>Seminole County</li><li>Leon County</li><li>Collier County</li></ul></div>
  </div>
  {codes()}
 </div>
</section>
''' + CTA
page('index.html', '', 'Emprise Partners | Facility Support & Site Services',
     'Emprise Partners is a prime contractor providing facility support and site services to municipal, county, state and federal agencies.', home)

# ---------- ABOUT ----------
about = phero('about', 'About Emprise Partners', 'A prime contractor for facility support and site services, serving clients nationwide.') + f'''
<section class="band about">
 <div class="wrap">
  <div class="two">
   <div class="story">
    <h2>One accountable prime contractor</h2>
    <p>Emprise Partners LLC is a facility support and site services company headquartered in Maitland, Florida, serving federal, state, local and commercial clients across the United States.</p>
    <p>We hold the contract and oversee every job, supported by a vetted network of trade partners. Instead of managing multiple vendors, relationships and agreements, our clients work with one accountable prime contractor.</p>
    <p>Our mission is to deliver reliable service, create strong partnerships, and give our clients confidence that their facilities are cared for, no matter the service or location.</p>
   </div>
   <img class="aboutimg" src="photo-government.jpg" alt="Government building exterior" loading="lazy">
  </div>
 </div>
</section>

<section class="band alt" id="how">
 <div class="wrap two">
  <div>
   <h2>How we deliver</h2>
   <p class="lede">Emprise Partners sets the standards, coordinates the work and inspects the results, with one line of communication for every property.</p>
  </div>
  <ol class="steps">
   <li><div><h3>One point of accountability</h3><p>One relationship and one contract across every service you need, with centralized contract administration and a single invoice.</p></div></li>
   <li><div><h3>Oversight and supervision</h3><p>We assign each scope to a qualified partner, set the schedule and standards, and supervise the work through completion.</p></div></li>
   <li><div><h3>Compliance</h3><p>Insurance, licensing and documentation tracked and verified for every partner before they set foot on site.</p></div></li>
   <li><div><h3>Quality assurance</h3><p>Inspections and reporting hold every job to the same standard, at every location.</p></div></li>
   <li><div><h3>Responsiveness</h3><p>Prompt replies, from bid questions to field issues.</p></div></li>
  </ol>
 </div>
</section>

<section class="band">
 <div class="wrap">
  <h2>Contracting information</h2>
  {codes('light')}
 </div>
</section>
''' + CTA
page('about.html', 'about.html', 'About | Emprise Partners', 'About Emprise Partners, a Florida-based prime contractor for facility support and site services.', about)

# ---------- SERVICES ----------
svc_rows = ''.join(f'''<div class="svc" id="{sid}">
   <div class="svcimg"><img src="photo-{img}.jpg" alt="" loading="lazy"></div>
   <div><h2>{t}</h2><p>{d}</p><ul>{''.join(f"<li>{x}</li>" for x in items)}</ul></div>
  </div>
  ''' for sid, t, img, d, items in SERVICES)
services = phero('facility', 'Services', 'Six core service lines, all managed through one point of contact, for single properties and multi-location portfolios.') + f'''
<section class="band">
 <div class="wrap">
  {svc_rows}
 </div>
</section>

<section class="band comm" id="commercial">
 <div class="wrap">
  <h2>Commercial facility services</h2>
  <p class="lede">The same model for property managers, office operators and private facility owners who want one reliable vendor across their portfolio.</p>
  <div class="cols">
   <div><h3>Office and workspace</h3><p>Janitorial, minor repairs and recurring maintenance for multi-site operators.</p></div>
   <div><h3>Property portfolios</h3><p>Grounds, pressure washing and exterior care, scheduled and reported across locations.</p></div>
   <div><h3>Projects and turnovers</h3><p>Moves, cleanouts and debris removal coordinated on your timeline.</p></div>
  </div>
 </div>
</section>
''' + CTA
page('services.html', 'services.html', 'Services | Emprise Partners', 'Janitorial, grounds, building trades, life safety, waste and specialty services from Emprise Partners.', services)

# ---------- PAST PERFORMANCE ----------
pp = phero('government', 'Past performance', 'Recent work for municipal and federal clients, delivered under one accountable prime contract.') + f'''
<section class="band">
 <div class="wrap">
  <h2>A few of our completed projects</h2>
  <p class="lede">A selection of recent work. References are available on request.</p>
  {proj_cards(PROJECTS).replace('class="projects"','class="projects list"',1)}
 </div>
</section>

<section class="band alt">
 <div class="wrap">
  <h2>Agencies we've served</h2>
  <div class="agency light">
   <div><h3>Federal</h3><ul><li>U.S. Department of Agriculture</li><li>National Park Service</li></ul></div>
   <div><h3>Municipal</h3><ul><li>City of Orlando</li><li>City of Fort Pierce</li><li>City of Plant City</li></ul></div>
   <div><h3>County</h3><ul><li>Orange County</li><li>Volusia County</li><li>Seminole County</li><li>Leon County</li><li>Collier County</li></ul></div>
  </div>
  {codes('light')}
 </div>
</section>
''' + CTA
page('past-performance.html', 'past-performance.html', 'Past Performance | Emprise Partners', 'Completed projects and agencies served by Emprise Partners.', pp)

# ---------- PARTNERS ----------
trades = ''.join(f'<div><h3>{t}</h3><p>{items[0]}, {items[1][0].lower()+items[1][1:]}, {items[2][0].lower()+items[2][1:]}</p></div>' for _, t, _, _, items in SERVICES)
partners = phero('infrastructure', 'Become a trade partner', 'Steady public-sector and commercial work for qualified trade partners, plus the past performance and support to grow.') + f'''
<section class="band">
 <div class="wrap two">
  <div>
   <h2>Why partner with Emprise Partners</h2>
   <ul class="checks">
    <li><b>Build your track record.</b> Growing companies can earn real government past performance with us, project by project, and build the portfolio that opens bigger doors.</li>
    <li><b>We handle the paperwork.</b> Bids, compliance, insurance tracking, documentation and reporting are on us, so your crews can focus on what they do best.</li>
    <li><b>Public-sector work without the bid.</b> Municipal, county, state and federal projects, without writing a single proposal.</li>
    <li><b>Prompt, reliable payment</b> on every invoice.</li>
    <li><b>Clear scopes</b> and one point of contact from kickoff to closeout.</li>
   </ul>
   <ol class="steps" style="margin-top:32px">
    <li><div><h3>Submit your interest</h3><p>Tell us your trade, service area and contact details.</p></div></li>
    <li><div><h3>Share your documents</h3><p>We collect your certificate of insurance, W-9 and licenses so you're ready when a contract is awarded.</p></div></li>
    <li><div><h3>Get matched to scopes</h3><p>We bring you projects that fit your trade and location.</p></div></li>
   </ol>
  </div>
  <div>
   <h2>Partner interest form</h2>
   <form data-form="vendor" novalidate>
<div class="hp" aria-hidden="true"><label>Leave this field empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
    <div class="row"><label>Company name<input name="company" required autocomplete="organization"></label><label>Contact name<input name="name" required autocomplete="name"></label></div>
    <div class="row"><label>Email<input name="email" type="email" required autocomplete="email"></label><label>Phone<input name="phone" type="tel" autocomplete="tel"></label></div>
    <div class="row"><label>Primary trade<select name="trade" required><option value="">Choose one</option>{''.join(f"<option>{t}</option>" for _, t, _, _, _ in SERVICES)}<option>Other</option></select></label><label>Service area<input name="area" placeholder="Counties or states" required></label></div>
    <label class="other-trade" hidden>Your service<input name="other_trade" placeholder="Describe the service you provide" maxlength="120"></label>
    <label class="consent"><input type="checkbox" name="consent" required><span>I agree that Emprise Partners may contact me about partnership opportunities. See our <a href="privacy.html">Privacy Policy</a>.</span></label>
    <button class="btn pri" type="submit">Submit partner interest</button>
    <div class="ok" role="status"></div>
   </form>
  </div>
 </div>
</section>

<section class="band alt">
 <div class="wrap">
  <h2>Trades we're recruiting</h2>
  <p class="lede">Nationwide, for federal, state, local and commercial work across the United States.</p>
  <div class="trades">{trades}</div>
 </div>
</section>
'''
page('partners.html', 'partners.html', 'Vendor Partners | Emprise Partners', 'Join the Emprise Partners trade partner network.', partners)

# ---------- CONTACT ----------
contact = phero('about', 'Contact Emprise Partners', 'Contracting officers, procurement teams and commercial clients: tell us what you need and we will be in touch soon.') + f'''
<section class="band">
 <div class="wrap two">
  <div>
   <div class="info" style="margin-top:0">
    <div><span>Toll-free</span><b><a href="tel:+18002540658">800.254.0658</a></b></div>
    <div><span>Local</span><b><a href="tel:+13214148926">321.414.8926</a></b></div>
    <div><span>Email</span><b><a href="mailto:info@emprise-partners.com">info@emprise-partners.com</a></b></div>
    <div><span>Office</span><b>555 Winderley Place, Suite 300<br>Maitland, FL 32751</b></div>
    <div><span>Business hours</span><b>Monday to Friday, 9:00 AM to 5:00 PM ET</b></div>
    <div id="capability"><span>Capability statement</span><b><a href="Emprise_Partners_Capability_Statement.pdf" target="_blank" rel="noopener">Download PDF</a></b></div>
   </div>
  </div>
  <form data-form="inquiry" novalidate style="margin-top:0">
<div class="hp" aria-hidden="true"><label>Leave this field empty<input name="website" tabindex="-1" autocomplete="off"></label></div>
   <div class="row"><label>Name<input name="name" required autocomplete="name"></label><label>Organization<input name="org" required autocomplete="organization"></label></div>
   <div class="row"><label>Email<input name="email" type="email" required autocomplete="email"></label><label>I'm with<select name="type" required><option value="">Choose one</option><option>Government agency</option><option>Commercial / private</option><option>Prime contractor (teaming)</option><option>Other</option></select></label></div>
   <label>Service of interest<select name="service"><option value="">Choose one</option>{''.join(f"<option>{t}</option>" for _, t, _, _, _ in SERVICES)}<option>Multiple services</option><option>Other</option></select></label>
   <label>How can we help?<textarea name="message" required placeholder="Solicitation number, scope, location or timeline"></textarea></label>
   <label class="consent"><input type="checkbox" name="consent" required><span>I agree that Emprise Partners may contact me about this inquiry. See our <a href="privacy.html">Privacy Policy</a>.</span></label>
   <button class="btn pri" type="submit">Send inquiry</button>
   <div class="ok" role="status"></div>
  </form>
 </div>
</section>

<section class="band alt" id="faq">
 <div class="wrap two">
  <div><h2>Frequently asked questions</h2></div>
  <div class="faq">
   <details><summary>What does Emprise Partners do?</summary><p>Emprise Partners is a facility support and site services company. We hold the contract and oversee every job, supported by a vetted network of trade partners.</p></details>
   <details><summary>How is your model different from hiring individual vendors?</summary><p>Instead of managing multiple contracts, invoices and relationships, you work with one accountable prime contractor. Emprise Partners handles contract management, compliance, communication, quality assurance and performance management.</p></details>
   <details><summary>Who do you work with?</summary><p>Federal, state and local government agencies, along with commercial clients such as property management companies and multi-location operators.</p></details>
   <details><summary>Where are you located and what areas do you serve?</summary><p>We're headquartered in Maitland, Florida, and serve federal, state, local and commercial clients across the United States.</p></details>
   <details><summary>How do you ensure quality and compliance?</summary><p>Emprise Partners sets the standards, supervises the work and inspects the results. Every trade partner is vetted for qualifications, licensing and insurance, and we maintain the documentation so you have one point of oversight.</p></details>
   <details><summary>How do I request a proposal?</summary><p>Use the form on this page, email info@emprise-partners.com, or call 800.254.0658. We'll review your needs and follow up to scope the right service program.</p></details>
  </div>
 </div>
</section>
'''
page('contact.html', 'contact.html', 'Contact | Emprise Partners', 'Contact Emprise Partners: 800.254.0658, info@emprise-partners.com, Maitland, Florida.', contact)

# ---------- PRIVACY / TERMS ----------
PRIVACY = phero('government', 'Privacy Policy', 'How Emprise Partners collects, uses and protects information.') + '''
<section class="band"><div class="wrap prose">
<p><b>Effective date:</b> November 2026</p>
<p>Emprise Partners LLC ("Emprise Partners," "we," "us") respects your privacy. This policy explains how we collect, use and protect information when you visit our website or contact us.</p>
<h2>Information we collect</h2>
<p>When you contact us through this website, we may collect your name, organization, email address, phone number, and any details you choose to share about your service needs. When a company submits our trade partner form, we may also collect its company name, primary trade and service area. We may also collect basic technical information, such as browser type and pages visited, to help us improve the website.</p>
<h2>How we use information</h2>
<p>We use the information you provide to respond to inquiries, prepare proposals, evaluate and onboard trade partners, deliver and manage services, communicate about contracts, and improve our website and operations. We do not sell your personal information.</p>
<h2>Sharing of information</h2>
<p>We may share information with qualified trade partners only as needed to scope or deliver services you have requested, with service providers who support our business operations (such as website hosting and the system we use to receive form submissions), or when required by law or government contracting requirements.</p>
<h2>Data security</h2>
<p>We use reasonable administrative, technical and physical safeguards to protect the information we collect. No method of transmission or storage is completely secure, but we work to protect your information.</p>
<h2>Cookies and third-party services</h2>
<p>This website may use cookies or similar technologies to understand how visitors use the site. You can disable cookies through your browser settings. The website also loads fonts from Google Fonts, which may receive your device's IP address when a page loads.</p>
<h2>Your choices</h2>
<p>You may request access to, correction of, or deletion of the personal information you have provided to us by contacting us using the details below.</p>
<h2>Changes to this policy</h2>
<p>We may update this Privacy Policy from time to time. Updates will be posted on this page with a revised effective date.</p>
<h2>Contact us</h2>
<p>Emprise Partners LLC<br>555 Winderley Place, Suite 300, Maitland, FL 32751<br>info@emprise-partners.com · 800.254.0658</p>
</div></section>
'''
page('privacy.html', '', 'Privacy Policy | Emprise Partners', 'Emprise Partners privacy policy.', PRIVACY)

TERMS = phero('government', 'Terms of Use', 'The terms that apply when you use the Emprise Partners website.') + '''
<section class="band"><div class="wrap prose">
<p><b>Effective date:</b> November 2026</p>
<p>By using emprise-partners.com (the "website"), you agree to these Terms of Use. If you do not agree, please do not use the website.</p>
<h2>Purpose of this website</h2>
<p>The website provides general information about Emprise Partners LLC and its services. Content on the website is for informational purposes only and is not an offer, bid, proposal or contract. Any work is governed solely by a written agreement or contract signed by Emprise Partners.</p>
<h2>Information you submit</h2>
<p>When you submit a form, you confirm that the information is accurate and that you are authorized to share it. Submitting the trade partner form does not create a subcontract, guarantee work, or obligate either party. Submitting an inquiry does not create a contract. We handle submitted information as described in our <a href="privacy.html">Privacy Policy</a>.</p>
<h2>Intellectual property</h2>
<p>The Emprise Partners name, logo and website content are owned by or licensed to Emprise Partners LLC. You may not copy, reproduce or use them without our written permission, except to share links to the website or to review our capability statement for procurement purposes.</p>
<h2>Accuracy of information</h2>
<p>We work to keep the website accurate and current, but information may change without notice. Contracting details, certifications and past performance should be confirmed directly with us or through official sources such as SAM.gov.</p>
<h2>Links to other websites</h2>
<p>The website may link to third-party websites. We are not responsible for their content or practices.</p>
<h2>Disclaimer and limitation of liability</h2>
<p>The website is provided "as is" without warranties of any kind. To the fullest extent permitted by law, Emprise Partners LLC is not liable for any damages arising from your use of, or inability to use, the website.</p>
<h2>Governing law</h2>
<p>These Terms of Use are governed by the laws of the State of Florida.</p>
<h2>Changes to these terms</h2>
<p>We may update these Terms of Use from time to time. Updates will be posted on this page with a revised effective date.</p>
<h2>Contact us</h2>
<p>Emprise Partners LLC<br>555 Winderley Place, Suite 300, Maitland, FL 32751<br>info@emprise-partners.com · 800.254.0658</p>
</div></section>
'''
page('terms.html', '', 'Terms of Use | Emprise Partners', 'Emprise Partners website terms of use.', TERMS)
print('built')
