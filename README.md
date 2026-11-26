# Emprise Partners website

A static website. No build step or server code is needed. Upload the whole folder to any web host (Netlify, GoDaddy cPanel `public_html`, Cloudflare Pages, etc.).

## Files

| File | What it is |
|---|---|
| `index.html` | Home |
| `about.html` | About |
| `services.html` | Services (+ commercial section) |
| `past-performance.html` | Completed projects and agencies served |
| `partners.html` | Trade partner page with the **vendor interest form** |
| `contact.html` | Contact page with the **agency/client inquiry form** and FAQ |
| `site.css` | All styles |
| `site.js` | Mobile menu, day/night hero photo, and **form submission handling** |
| `img/` | Photos (Unsplash, free to use) |
| `Emprise_Partners_Capability_Statement.pdf` | Linked from every "Capability statement" button |
| `build.py` | Optional: regenerates the six HTML pages from shared header/footer and content lists. Edit content there and run `python3 build.py`. |

## Connecting the forms to your app

All form handling is in **`site.js`**. At the top:

```js
const FORM_ENDPOINTS = {
  vendor: '',   // Trade partner interest form (partners.html)
  inquiry: ''   // Agency / client inquiry form (contact.html)
};
const FORM_HEADERS = {};
```

1. Put the web address (URL) your app gives you for receiving submissions in each line. They can be the same URL or different ones.
2. If your app requires a key in the request headers, add it to `FORM_HEADERS`, e.g. `{ 'apikey': 'YOUR_PUBLIC_KEY' }`. Only use a **public/anon** key here. Never put a secret or service key in website code; anyone can read it.
3. Upload the updated `site.js`.

Until an address is filled in, that form shows: "This form is not connected yet, so nothing was sent…"

### What the website sends

Each submission is an HTTP `POST` with `Content-Type: application/json`.

**Vendor interest form** (`form: "vendor"`):

```json
{
  "company": "ABC Lawn Care LLC",
  "name": "Jane Smith",
  "email": "jane@abclawn.com",
  "phone": "407-555-0100",
  "trade": "Landscaping & Grounds",
  "area": "Orange, Seminole, Osceola counties",
  "consent": true,
  "form": "vendor",
  "submitted_at": "2026-11-25T18:40:00.000Z",
  "page": "/partners.html"
}
```

`trade` is one of: Janitorial & Custodial, Landscaping & Grounds, Building Systems & Trades, Life Safety & Pest Control, Waste & Sanitation, Security & Specialty.

**Agency / client inquiry form** (`form: "inquiry"`):

```json
{
  "name": "John Doe",
  "org": "City of Example",
  "email": "jdoe@example.gov",
  "type": "Government agency",
  "service": "Janitorial & Custodial",
  "message": "RFQ 26-123 for custodial services at three facilities...",
  "consent": true,
  "form": "inquiry",
  "submitted_at": "2026-11-25T18:40:00.000Z",
  "page": "/contact.html"
}
```

`type` is one of: Government agency, Commercial / private, Prime contractor (teaming), Other.
`service` is one of the six service lines, "Multiple services", "Other", or blank.

### What your app's endpoint must do

- Accept `POST` requests with a JSON body and return any `2xx` status on success. Anything else shows the visitor an error message with your phone number and email.
- Allow requests from your website's domain (CORS). It should respond to the browser's `OPTIONS` pre-flight with headers like:
  ```
  Access-Control-Allow-Origin: https://www.emprise-partners.com
  Access-Control-Allow-Methods: POST, OPTIONS
  Access-Control-Allow-Headers: Content-Type, apikey, authorization
  ```
- Save the submission (e.g. a `vendor_leads` table and an `agency_inquiries` table, or one table using the `form` field).
- Recommended: email a notification (vendor → Partner Specialist; inquiry → Contracts Department) and send the submitter a confirmation email.

### Example: Lovable app on Supabase (Edge Function)

If your Lovable app uses Supabase, a function like this receives both forms:

```ts
// supabase/functions/website-forms/index.ts
import { createClient } from "npm:@supabase/supabase-js@2";

const cors = {
  "Access-Control-Allow-Origin": "https://www.emprise-partners.com",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "content-type, apikey, authorization",
};

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return new Response("Method not allowed", { status: 405, headers: cors });

  const body = await req.json();
  const supabase = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!);
  const table = body.form === "vendor" ? "vendor_leads" : "agency_inquiries";
  const { error } = await supabase.from(table).insert(body);

  return new Response(JSON.stringify({ ok: !error }), {
    status: error ? 500 : 200,
    headers: { ...cors, "Content-Type": "application/json" },
  });
});
```

Then set both lines in `site.js` to `https://YOUR-PROJECT.supabase.co/functions/v1/website-forms`, and add `{ 'apikey': 'YOUR_ANON_KEY' }` to `FORM_HEADERS` if the function requires it. The table columns should match the JSON field names above. You can ask Lovable to "create an edge function that accepts these two JSON payloads and saves them to tables", and paste this README section in.

## Notes

- Forms only send from the live website. The Claude preview link blocks outside requests.
- Privacy and Terms links in the footer are placeholders (`#`) until those pages exist.
