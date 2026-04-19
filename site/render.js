// LLM Wiki Dashboard — render from WIKI_DATA
(function(){
  const $ = (s, r=document) => r.querySelector(s);
  const $$ = (s, r=document) => Array.from(r.querySelectorAll(s));
  const D = window.WIKI_DATA;
  if (!D) { console.error("No WIKI_DATA"); return; }

  // Quartz converts spaces to hyphens in URLs
  function pageUrl(slug) {
    if (!slug) return '#';
    return slug.replace(/ /g, '-');
  }

  // ---------- meta ----------
  $('#meta-pages').textContent = D.meta.total_pages;
  $('#meta-updates').textContent = D.meta.update_count;
  $('#meta-sync').textContent = D.meta.last_sync;

  // ---------- ticker ----------
  function renderTicker() {
    const el = $('#ticker');
    el.innerHTML = D.ticker.map(t =>
      `<span class="t"><span class="k">${t.k}</span><span class="v">${t.v}</span></span>`
    ).join('');
  }

  // ---------- domain tabs ----------
  function selectDomain(k) {
    $$('#domtabs .domtab').forEach(b => b.setAttribute('aria-selected', b.dataset.k === k ? 'true' : 'false'));
    document.documentElement.setAttribute('data-domain', k);
    renderArticles(k);
    renderGraph(k);
    localStorage.setItem('llm-wiki-dom', k);
  }

  function renderArticles(k) {
    const d = D.domains[k];
    if (!d) return;
    $('#focus-title').textContent = d.title;

    const ol = $('#focus-articles');
    ol.innerHTML = d.articles.map(a => {
      const dateStr = a.date ? a.date.slice(5) : '';
      const href = pageUrl(a.slug);
      return `
        <li>
          <span class="date mono">${dateStr}</span>
          <a href="${href}" class="hl serif">${a.hl}
            <span class="sub">${a.entity}</span>
          </a>
          <span class="pill">
            <span class="tag">${a.page_type || ''}</span>
          </span>
        </li>`;
    }).join('');

    const bar = $('#entbar');
    bar.innerHTML = d.entities.map(([name, n]) => {
      const href = pageUrl(`${k}/entities/${name}`);
      return `<a class="entchip" href="${href}"><b>${name}</b><span class="n">${n}</span></a>`;
    }).join('');
  }

  function renderGraph(k) {
    const svg = $('#graph');
    const g = D.domains[k]?.graph;
    if (!g || !g.nodes.length) { svg.innerHTML = ''; return; }
    const ns = 'http://www.w3.org/2000/svg';
    svg.innerHTML = '';

    // dot grid
    const grid = document.createElementNS(ns, 'g');
    grid.setAttribute('opacity', '0.35');
    for (let x = 0; x <= 360; x += 20)
      for (let y = 0; y <= 260; y += 20) {
        const c = document.createElementNS(ns, 'circle');
        c.setAttribute('cx', x); c.setAttribute('cy', y);
        c.setAttribute('r', 0.4); c.setAttribute('fill', 'var(--text-faint)');
        grid.appendChild(c);
      }
    svg.appendChild(grid);

    // links
    const nodeMap = Object.fromEntries(g.nodes.map(n => [n.id, n]));
    const linkG = document.createElementNS(ns, 'g');
    for (const [a, b, w] of g.links) {
      const A = nodeMap[a], B = nodeMap[b];
      if (!A || !B) continue;
      const ln = document.createElementNS(ns, 'line');
      ln.setAttribute('x1', A.x); ln.setAttribute('y1', A.y);
      ln.setAttribute('x2', B.x); ln.setAttribute('y2', B.y);
      ln.setAttribute('stroke', 'var(--accent-dim)');
      ln.setAttribute('stroke-width', 0.5 + w * 0.28);
      ln.setAttribute('stroke-opacity', 0.22 + w * 0.08);
      linkG.appendChild(ln);
    }
    svg.appendChild(linkG);

    // nodes
    const nodeG = document.createElementNS(ns, 'g');
    for (const n of g.nodes) {
      const grp = document.createElementNS(ns, 'g');
      grp.setAttribute('transform', `translate(${n.x} ${n.y})`);
      grp.style.cursor = 'pointer';
      let shape;
      if (n.type === 'ent') {
        shape = document.createElementNS(ns, 'circle');
        shape.setAttribute('r', Math.min(n.size, 20) / 2);
        shape.setAttribute('fill', 'var(--accent)'); shape.setAttribute('fill-opacity', '0.6');
        shape.setAttribute('stroke', 'var(--accent)'); shape.setAttribute('stroke-width', 0.8);
      } else if (n.type === 'con') {
        shape = document.createElementNS(ns, 'circle');
        shape.setAttribute('r', Math.min(n.size, 16) / 2);
        shape.setAttribute('fill', 'var(--bg-elev)');
        shape.setAttribute('stroke', 'var(--text-dim)'); shape.setAttribute('stroke-width', 1);
      } else {
        shape = document.createElementNS(ns, 'rect');
        const s = Math.min(n.size, 14) * 0.72;
        shape.setAttribute('x', -s/2); shape.setAttribute('y', -s/2);
        shape.setAttribute('width', s); shape.setAttribute('height', s);
        shape.setAttribute('transform', 'rotate(45)');
        shape.setAttribute('fill', 'var(--text-dim)'); shape.setAttribute('opacity', 0.7);
      }
      grp.appendChild(shape);
      const tx = document.createElementNS(ns, 'text');
      tx.setAttribute('x', Math.min(n.size, 20) / 2 + 4); tx.setAttribute('y', 3);
      tx.setAttribute('font-size', n.type === 'ent' ? 9.5 : 8.5);
      tx.setAttribute('font-family', 'JetBrains Mono, monospace');
      tx.setAttribute('fill', n.type === 'ent' ? 'var(--text)' : 'var(--text-dim)');
      tx.textContent = n.label;
      grp.appendChild(tx);
      nodeG.appendChild(grp);
    }
    svg.appendChild(nodeG);
    $('#graph-nodes').textContent = g.nodes.length;
    $('#graph-links').textContent = g.links.length;
  }

  // ---------- ledger ----------
  function renderLedger() {
    const ol = $('#ledger');
    ol.innerHTML = D.ledger.map(row => {
      if (row.day) return `<li class="tl-day"><span>${row.day}</span><b>${row.subtotal}</b></li>`;
      const href = pageUrl(row.slug);
      return `
        <li class="tl-row" data-k="${row.k}">
          <span class="marker">§</span>
          <span class="fact">${row.fact} <a class="entity-ref" href="${href}">${row.entity}</a></span>
        </li>`;
    }).join('');
  }

  // ---------- heatmap ----------
  function renderHeatmap() {
    const cells = $('#heatmap');
    cells.innerHTML = D.heatmap.map((l, i) => {
      const d = new Date();
      d.setDate(d.getDate() - (D.heatmap.length - 1 - i));
      return `<span data-l="${l}" title="${d.toISOString().slice(0,10)}"></span>`;
    }).join('');
  }

  // ---------- A-Z index ----------
  const IDX_ORDER = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
  function renderIndex(filterK) {
    const wrap = $('#idx-wrap');
    const out = [];
    IDX_ORDER.forEach(letter => {
      const items = (D.index[letter] || []).filter(it => !filterK || filterK === 'all' || it.k === filterK);
      if (!items.length) return;
      const lis = items.map(it => `
        <li data-k="${it.k}">
          <a href="${pageUrl(it.s)}"><span class="dom">${it.k.toUpperCase()}</span>${it.n} <span class="ind">· ${it.kind}</span></a>
        </li>`).join('');
      out.push(`<div class="idx-group"><h3>${letter}<span class="c">${items.length}</span></h3><ul>${lis}</ul></div>`);
    });
    wrap.innerHTML = out.join('');
  }

  // ---------- backlinks ----------
  function renderBacklinks() {
    const max = D.backlinks_rank.length ? D.backlinks_rank[0][3] : 1;
    $('#bl-rank').innerHTML = D.backlinks_rank.map(r => {
      const [n, k, kind, bk, slug] = r;
      return `
      <li>
        <a class="bl-name" href="${pageUrl(slug)}">${n} <em>${k.toUpperCase()} · ${kind}</em></a>
        <span class="bl-n">${bk}</span>
        <span class="bl-bar"><span style="width:${(bk / max) * 100}%"></span></span>
      </li>`;
    }).join('');
    $('#bl-orphan').innerHTML = D.orphans.map(([n, k]) =>
      `<li><a href="#">${n}</a><span class="m">${k.toUpperCase()}</span></li>`
    ).join('');
    $('#bl-stub').innerHTML = D.stubs.map(([n, k]) =>
      `<li><a href="#">${n}</a><span class="m">${k.toUpperCase()}</span></li>`
    ).join('');
  }

  // ---------- view routing ----------
  const VIEWS = ["feed", "index", "backlinks"];
  function showView(v) {
    if (!VIEWS.includes(v)) v = "feed";
    VIEWS.forEach(k => {
      const el = document.getElementById("view-" + k);
      if (el) el.hidden = k !== v;
    });
    $$("#viewnav a").forEach(a => a.classList.toggle("on", a.dataset.v === v));
    localStorage.setItem("llm-wiki-view", v);
  }
  $$("#viewnav a").forEach(a => {
    a.addEventListener("click", e => { e.preventDefault(); showView(a.dataset.v); });
  });

  // ---------- domain tab fill counts ----------
  for (const k of ['ai', 'crypto', 'macro']) {
    const d = D.domains[k];
    if (!d) continue;
    const tab = $(`.domtab[data-k="${k}"]`);
    if (!tab) continue;
    const counts = tab.querySelector('.dom-counts');
    if (counts) {
      let html = `<span>엔티티 <b>${d.entity_count}</b></span><span>개념 <b>${d.concept_count}</b></span>`;
      if (d.indicator_count) html += `<span>지표 <b>${d.indicator_count}</b></span>`;
      html += `<span>기사 <b>${d.articles.length}</b></span>`;
      counts.innerHTML = html;
    }
  }

  // ---------- tabs ----------
  $$('#domtabs .domtab').forEach(b => {
    b.addEventListener('click', () => selectDomain(b.dataset.k));
  });

  // ---------- index filters ----------
  $$('#idx-domfilter button').forEach(b => {
    b.addEventListener('click', () => {
      $$('#idx-domfilter button').forEach(x => x.classList.remove('on'));
      b.classList.add('on');
      renderIndex(b.dataset.k);
    });
  });

  // ---------- theme ----------
  const root = document.documentElement;
  const savedT = localStorage.getItem('llm-wiki-theme');
  if (savedT) root.setAttribute('data-theme', savedT);
  $('#theme').addEventListener('click', () => {
    const now = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', now);
    localStorage.setItem('llm-wiki-theme', now);
  });

  // ---------- init ----------
  renderTicker();
  selectDomain(localStorage.getItem('llm-wiki-dom') || 'ai');
  renderLedger();
  renderHeatmap();
  renderIndex('all');
  renderBacklinks();
  showView(localStorage.getItem('llm-wiki-view') || 'feed');
})();
