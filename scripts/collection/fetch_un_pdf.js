// Run on the record page https://digitallibrary.un.org/record/4082957 once it has loaded.
await (async () => {
  const r = await fetch('https://digitallibrary.un.org/record/4082957/files/S_2025_313-EN.pdf', { credentials: 'include' });
  const b = await r.blob();
  const magic = String.fromCharCode(...new Uint8Array(await b.slice(0, 5).arrayBuffer()));
  if (magic !== '%PDF-') return 'Not a PDF (HTTP ' + r.status + ')';
  const a = document.createElement('a');
  a.href = URL.createObjectURL(b); a.download = '09_OC_2025-05-19_IsraelUN_001.pdf';
  document.body.appendChild(a); a.click(); a.remove();
  return 'Saved ' + b.size + ' bytes';
})()
