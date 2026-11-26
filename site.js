{
 /* ------------------------------------------------------------------
    FORM CONNECTION — edit these two lines to connect your company app.
    Each form posts JSON to its own address. Leave one blank ('') to
    keep that form in "not connected" mode. See README.md for details.
    ------------------------------------------------------------------ */
 const FORM_ENDPOINTS = {
  vendor:  'https://emprise-partners-ops-division.lovable.app/api/public/website-leads',   // Trade partner interest form (partners.html)
  inquiry: 'https://emprise-partners-ops-division.lovable.app/api/public/website-leads'    // Agency / client inquiry form (contact.html)
 };
 // Optional: extra headers your app requires (for example an API key or anon key).
 const FORM_HEADERS = {};

 // Hero photo follows the visitor's local time: day 6am-6pm, night otherwise.
 const hero = document.querySelector('.hero');
 if (hero) { const h = new Date().getHours(); if (h < 6 || h >= 18) hero.classList.add('night'); }

 // Mobile menu
 const menu = document.getElementById('menu'), links = document.getElementById('links');
 if (menu) {
  menu.addEventListener('click', () => { const o = links.classList.toggle('open'); menu.setAttribute('aria-expanded', o); });
  links.addEventListener('click', e => { if (e.target.tagName === 'A') { links.classList.remove('open'); menu.setAttribute('aria-expanded', false); } });
 }

 // Form submission
 const loadedAt = Date.now();
 for (const f of document.querySelectorAll('form[data-form]')) {
  f.addEventListener('submit', async e => {
   e.preventDefault();
   const ok = f.querySelector('.ok'), btn = f.querySelector('button[type=submit]');
   if (!f.checkValidity()) { f.reportValidity(); return; }
   // Spam trap: bots fill the hidden "website" field or submit instantly; pretend success and drop it.
   if ((f.querySelector('[name=website]')?.value || '') !== '' || Date.now() - loadedAt < 3000) {
    ok.textContent = 'Thank you. Emprise Partners will be in touch within one business day.'; ok.classList.add('show'); f.reset(); return;
   }
   const fd = new FormData(f);
   const data = Object.fromEntries(fd);
   delete data.website;
   data.consent = fd.has('consent');
   data.form = f.dataset.form;                 // "vendor" or "inquiry"
   data.submitted_at = new Date().toISOString();
   data.page = location.pathname;
   const url = FORM_ENDPOINTS[data.form];
   const show = msg => { ok.textContent = msg; ok.classList.add('show'); };
   if (!url) { show('This form is not connected yet, so nothing was sent. Please call 800.254.0658 or email info@emprise-partners.com.'); return; }
   btn.disabled = true;
   try {
    const r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json', ...FORM_HEADERS }, body: JSON.stringify(data) });
    if (!r.ok) throw new Error(r.status);
    show('Thank you. Emprise Partners will be in touch within one business day.');
    f.reset();
   } catch (err) {
    show('Something went wrong. Please call 800.254.0658 or email info@emprise-partners.com.');
   } finally { btn.disabled = false; }
  });
 }
}
