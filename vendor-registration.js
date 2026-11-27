{
  const ENDPOINT = 'https://emprise-partners-ops-division.lovable.app/api/public/vendor-registrations';
  const token = new URLSearchParams(location.search).get('t') || '';
  const form = document.getElementById('vendor-registration');
  const validToken = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(token);
  form.hidden = !validToken;
  document.getElementById('registration-unavailable').hidden = validToken;
  const trade = form.elements.namedItem('trade');
  const other = form.elements.namedItem('other_trade');
  const updateOther = () => {
    const selected = trade.value === 'Other';
    document.getElementById('registration-other').hidden = !selected;
    other.disabled = !selected;
    other.required = selected;
    other.setCustomValidity(selected && !other.value.trim() ? 'Enter the service you provide.' : '');
  };
  trade.addEventListener('change', updateOther);
  other.addEventListener('input', updateOther);
  const isoDate = (value) => {
    if (!value) return '';
    const match = /^(\d{2})\.(\d{2})\.(\d{4})$/.exec(value);
    if (!match) throw new Error('Enter expiration dates as MM.DD.YYYY.');
    const iso = `${match[3]}-${match[1]}-${match[2]}`;
    const date = new Date(`${iso}T00:00:00Z`);
    if (Number.isNaN(date.getTime()) || date.toISOString().slice(0, 10) !== iso) throw new Error('Enter a valid expiration date.');
    return iso;
  };
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    updateOther();
    if (!form.reportValidity()) return;
    const error = document.getElementById('registration-error');
    error.hidden = true;
    const button = form.querySelector('button[type=submit]');
    try {
      const data = new FormData(form);
      data.set('token', token);
      if (trade.value === 'Other') data.set('trade', other.value.trim());
      data.delete('other_trade');
      if (!String(data.get('company_website') || '').trim()) data.delete('company_website');
      for (const name of ['insurance_expires_on', 'license_expires_on']) data.set(name, isoDate(String(data.get(name) || '').trim()));
      const minimums = { w9: 1, insurance: 1, license: 0, reference: 1 };
      const maximums = { w9: 3, insurance: 3, license: 6, reference: 3 };
      let total = 0;
      for (const kind of Object.keys(minimums)) {
        const files = Array.from(form.elements.namedItem(`files_${kind}`).files);
        if (files.length < minimums[kind] || files.length > maximums[kind]) throw new Error(kind === 'reference' ? (files.length < minimums[kind] ? 'Upload your past performance / references.' : 'Upload at most 3 past performance / reference files.') : `Check the number of ${kind} files.`);
        if (kind === 'license' && files.length && !data.get('license_expires_on')) throw new Error('Enter the license expiration date.');
        for (const file of files) {
          if (!['application/pdf', 'image/jpeg', 'image/png'].includes(file.type) || !file.size || file.size > 10 * 1024 * 1024) throw new Error('Each file must be a PDF, JPG or PNG, up to 10 MB.');
        }
        total += files.length;
      }
      if (total > 12) throw new Error('Upload at most twelve files.');
      button.disabled = true;
      button.textContent = 'Sending…';
      const response = await fetch(ENDPOINT, { method: 'POST', body: data, credentials: 'omit' });
      const result = await response.json().catch(() => null);
      if (!response.ok || !result?.ok) throw new Error(result?.error || 'Your registration could not be sent. Please try again.');
      form.hidden = true;
      document.getElementById('registration-complete').hidden = false;
      history.replaceState(null, '', location.pathname);
    } catch (problem) {
      error.textContent = problem instanceof Error ? problem.message : 'Your registration could not be sent. Please try again.';
      error.hidden = false;
    } finally {
      button.disabled = false;
      button.textContent = 'Submit registration';
    }
  });
}
