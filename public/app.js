/* Contract Commons client script: progress, quizzes, lab log, search, dashboard, placement. Data stays in this browser. */
(function () {
  'use strict';
  var BASE = document.body.getAttribute('data-base') || '.';
  /* Link helper: works on a web server and when the site is opened from disk. */
  function L(p) { var h = ''; var i = p.indexOf('#'); if (i >= 0) { h = p.slice(i); p = p.slice(0, i); } return BASE + p + (/\/$/.test(p) ? 'index.html' : '') + h; }
  var KEY = 'contract-commons-v1';
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { return {}; } }
  var S = load();
  S.done = S.done || {}; S.quiz = S.quiz || {}; S.log = S.log || {}; S.visit = S.visit || {};
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }

  /* Copy buttons */
  $$('.copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = b.parentNode.querySelector('pre').textContent;
      function ok() { b.textContent = 'Copied'; setTimeout(function () { b.textContent = 'Copy'; }, 1500); }
      try { navigator.clipboard.writeText(t).then(ok, function () { fallback(t); ok(); }); } catch (e) { fallback(t); ok(); }
    });
  });
  function fallback(t) { var a = document.createElement('textarea'); a.value = t; document.body.appendChild(a); a.select(); try { document.execCommand('copy'); } catch (e) {} document.body.removeChild(a); }

  /* Search */
  var dlg = $('#search'), idx = null;
  function openSearch() { if (!dlg) return; if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', ''); $('#search-q').focus(); if (!idx) { if (window.CC_SEARCH) { idx = window.CC_SEARCH; run(); } else { var sc = document.createElement('script'); sc.src = BASE + '/search-index.js'; sc.onload = function () { idx = window.CC_SEARCH || []; run(); }; document.head.appendChild(sc); } } }
  function run() {
    var q = ($('#search-q').value || '').toLowerCase().trim(), out = $('#search-res');
    if (!idx) { out.innerHTML = '<li style="padding:12px;color:var(--muted-2)">Loading…</li>'; return; }
    if (!q) { out.innerHTML = '<li style="padding:12px;color:var(--muted-2)">Type to search lessons, labs, tools and glossary terms.</li>'; return; }
    var words = q.split(/\s+/);
    var hits = idx.map(function (it) {
      var t = it.t.toLowerCase(), k = (it.k || '').toLowerCase(), sc = 0;
      for (var i = 0; i < words.length; i++) { var w = words[i]; if (t.indexOf(w) >= 0) sc += 5; else if (k.indexOf(w) >= 0) sc += 1; else return null; }
      return { it: it, sc: sc };
    }).filter(Boolean).sort(function (a, b) { return b.sc - a.sc; }).slice(0, 12);
    out.innerHTML = hits.length ? hits.map(function (h) { return '<li><a href="' + L(h.it.u) + '">' + esc(h.it.t) + '<small>' + esc(h.it.s) + '</small></a></li>'; }).join('') : '<li style="padding:12px;color:var(--muted-2)">No results. Try a tool name such as Remix or Safe.</li>';
  }
  $$('[data-search-open]').forEach(function (b) { b.addEventListener('click', openSearch); });
  var sc = $('[data-search-close]'); if (sc) sc.addEventListener('click', function () { dlg.close(); });
  var sq = $('#search-q'); if (sq) sq.addEventListener('input', run);
  document.addEventListener('keydown', function (e) { if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); openSearch(); } });

  /* Progress marks on any page */
  function marks() {
    $$('[data-lesson-link]').forEach(function (a) {
      var id = a.getAttribute('data-lesson-link');
      if (S.done[id] && !a.querySelector('.done-tick')) {
        var s = document.createElement('span'); s.className = 'cc-chip cc-chip--brand done-tick'; s.textContent = 'Done'; s.style.marginLeft = '6px';
        a.appendChild(s);
      }
    });
    $$('[data-mod-progress]').forEach(function (c) {
      var ids = c.getAttribute('data-mod-progress').split(','), n = ids.filter(function (i) { return S.done[i]; }).length;
      c.textContent = n + ' of ' + ids.length + ' done'; c.className = 'cc-chip' + (n === ids.length ? ' cc-chip--brand' : '');
    });
  }
  marks();

  /* Quizzes. Types: mc (concept), fill (missing logic), fix (wrong line), order (steps). */
  var TYPE = { mc: 'Concept', fill: 'Fill the missing logic', fix: 'Fix the wrong line', order: 'Put steps in order' };
  function pick(data, mix) {
    /* Balanced draw: for each type, take items round-robin across modules. */
    var out = [];
    mix.split(',').forEach(function (part) {
      var kv = part.split(':'), t = kv[0], want = +kv[1];
      var byMod = {};
      shuffle(data.filter(function (q) { return (q.t || 'mc') === t; })).forEach(function (q) { (byMod[q.m] = byMod[q.m] || []).push(q); });
      var mods = shuffle(Object.keys(byMod)), got = [];
      while (got.length < want && mods.some(function (k) { return byMod[k].length; })) {
        mods.forEach(function (k) { if (got.length < want && byMod[k].length) got.push(byMod[k].shift()); });
      }
      out = out.concat(got);
    });
    return shuffle(out);
  }
  function codeBlock(text) {
    return '<pre class="qcode"><code>' + esc(text).replace(/_{4,}/g, '<span class="blank">____</span>') + '</code></pre>';
  }
  function renderQuiz(box) {
    var id = box.getAttribute('data-quiz');
    var data = JSON.parse($('[data-quiz-data="' + id + '"]').textContent);
    var mix = box.getAttribute('data-quiz-mix'), sample = +box.getAttribute('data-quiz-sample') || 0;
    var passMark = +box.getAttribute('data-pass') || 80;
    var qs = mix ? pick(data, mix) : sample ? shuffle(data).slice(0, sample) : shuffle(data);
    var answered = 0, right = 0, n = qs.length;
    box.innerHTML = '';
    function done(card, ex, good, q) {
      card.classList.add('answered'); answered++; if (good) right++;
      ex.innerHTML = (good ? '<b style="color:var(--brand-700)">Correct.</b> ' : '<b style="color:var(--danger-700)">Not quite.</b> ') + q.e;
      if (answered === n) finish();
    }
    function options(card, q, ex, mono, onPick) {
      var order = shuffle(q.o.map(function (_, k) { return k; })), btns = [];
      var wrap = document.createElement('div'); wrap.className = 'opts';
      order.forEach(function (k, pos) {
        var b = document.createElement('button'); b.type = 'button'; b.className = 'opt' + (mono ? ' mono' : '');
        b.innerHTML = '<span class="l">' + 'ABCDEF'[pos] + '</span><span>' + (mono ? esc(q.o[k]) : q.o[k]) + '</span>';
        b.addEventListener('click', function () {
          if (wrap.getAttribute('data-locked')) return; wrap.setAttribute('data-locked', '1');
          btns.forEach(function (x) { x.b.disabled = true; if (x.k === q.a) x.b.classList.add('right'); });
          if (k !== q.a) b.classList.add('wrong');
          onPick(k === q.a);
        });
        btns.push({ b: b, k: k }); wrap.appendChild(b);
      });
      card.appendChild(wrap);
    }
    qs.forEach(function (q, qi) {
      var t = q.t || 'mc';
      var card = document.createElement('div'); card.className = 'q q-' + t;
      card.innerHTML = '<div class="qn"><span>Question ' + (qi + 1) + ' of ' + n + '</span><span class="qtype">' + TYPE[t] + '</span></div><div class="qt">' + q.q + '</div>';
      var ex = document.createElement('div'); ex.className = 'expl'; ex.setAttribute('aria-live', 'polite');
      if (t === 'mc') {
        options(card, q, ex, false, function (g) { done(card, ex, g, q); });
      } else if (t === 'fill') {
        card.insertAdjacentHTML('beforeend', codeBlock(q.code) + '<div class="qhint">Choose what goes in the blank.</div>');
        options(card, q, ex, true, function (g) { done(card, ex, g, q); });
      } else if (t === 'fix') {
        var pre = document.createElement('div'); pre.className = 'qlines'; pre.setAttribute('role', 'group'); pre.setAttribute('aria-label', 'Code lines');
        var hint = document.createElement('div'); hint.className = 'qhint'; hint.textContent = 'Step 1: click the wrong line.';
        var lineOk = false;
        q.code.forEach(function (line, li) {
          var b = document.createElement('button'); b.type = 'button'; b.className = 'qline';
          b.innerHTML = '<span class="ln">' + (li + 1) + '</span><code>' + (esc(line) || ' ') + '</code>';
          b.addEventListener('click', function () {
            if (pre.getAttribute('data-locked')) return; pre.setAttribute('data-locked', '1');
            lineOk = li === q.bad;
            $$('.qline', pre).forEach(function (x, xi) { x.disabled = true; if (xi === q.bad) x.classList.add('right'); });
            if (!lineOk) b.classList.add('wrong');
            hint.innerHTML = (lineOk ? 'Right line. ' : 'The wrong line is line ' + (q.bad + 1) + '. ') + 'Step 2: choose the fix for it.';
            options(card, q, ex, true, function (g) { done(card, ex, lineOk && g, q); });
            card.appendChild(ex);
          });
          pre.appendChild(b);
        });
        card.appendChild(hint); card.appendChild(pre);
      } else if (t === 'order') {
        var idx = q.steps.map(function (_, k) { return k; }), cur;
        do { cur = shuffle(idx); } while (q.steps.length > 1 && cur.join() === idx.join());
        var ol = document.createElement('ol'); ol.className = 'qorder';
        var hintO = document.createElement('div'); hintO.className = 'qhint'; hintO.textContent = 'Use the arrows to put the steps in the right order, then check.';
        function draw(lock) {
          ol.innerHTML = '';
          cur.forEach(function (k, pos) {
            var li = document.createElement('li');
            if (lock) li.className = k === pos ? 'right' : 'wrong';
            li.innerHTML = '<span class="pos">' + (pos + 1) + '</span><span class="st">' + q.steps[k] + '</span>';
            if (!lock) {
              var up = document.createElement('button'), dn = document.createElement('button');
              up.type = dn.type = 'button'; up.className = dn.className = 'mv';
              up.textContent = '↑'; dn.textContent = '↓';
              up.setAttribute('aria-label', 'Move step up'); dn.setAttribute('aria-label', 'Move step down');
              up.disabled = pos === 0; dn.disabled = pos === cur.length - 1;
              up.addEventListener('click', function () { var x = cur[pos - 1]; cur[pos - 1] = cur[pos]; cur[pos] = x; draw(); ol.children[pos - 1].querySelector('.mv').focus(); });
              dn.addEventListener('click', function () { var x = cur[pos + 1]; cur[pos + 1] = cur[pos]; cur[pos] = x; draw(); ol.children[pos + 1].querySelectorAll('.mv')[1].focus(); });
              var g = document.createElement('span'); g.className = 'mvs'; g.appendChild(up); g.appendChild(dn); li.appendChild(g);
            }
            ol.appendChild(li);
          });
        }
        draw();
        var chk = document.createElement('button'); chk.type = 'button'; chk.className = 'cc-btn cc-btn--secondary'; chk.textContent = 'Check order'; chk.style.marginTop = '10px';
        chk.addEventListener('click', function () {
          var good = cur.every(function (k, pos) { return k === pos; });
          draw(true); chk.remove();
          var sol = '<div class="qsol"><b>Right order:</b><ol>' + q.steps.map(function (s) { return '<li>' + s + '</li>'; }).join('') + '</ol></div>';
          done(card, ex, good, { e: q.e + (good ? '' : sol) });
        });
        card.appendChild(hintO); card.appendChild(ol); card.appendChild(chk);
      }
      card.appendChild(ex); box.appendChild(card);
    });
    var res = document.createElement('div'); res.className = 'result'; res.hidden = true; res.setAttribute('aria-live', 'polite'); box.appendChild(res);
    function finish() {
      var pct = Math.round(100 * right / n), pass = pct >= passMark;
      S.quiz[id] = Math.max(S.quiz[id] || 0, pct); if (pass && id !== 'final-exam') S.done[id] = true;
      if (pass && id === 'final-exam') S.examPassed = true;
      save(); lessonStatus(); marks();
      res.hidden = false; res.className = 'result ' + (pass ? 'pass' : 'fail');
      res.innerHTML = '<h3>' + right + ' of ' + n + ' correct (' + pct + '%)</h3><p style="margin:0 0 10px">' + (pass ? (id === 'final-exam' ? 'Passed the final exam.' : 'Passed. This unit is complete.') : 'Not passed yet. Read the steps again, then try again. You need ' + passMark + '%.') + '</p>';
      var again = document.createElement('button'); again.type = 'button'; again.className = 'cc-btn cc-btn--secondary'; again.textContent = (mix || sample) ? 'New questions' : 'Try again';
      again.addEventListener('click', function () { renderQuiz(box); box.scrollIntoView({ block: 'start' }); });
      res.appendChild(again);
    }
  }
  $$('[data-quiz]').forEach(renderQuiz);

  /* Lesson page */
  var lessonEl = $('[data-lesson]');
  function lessonStatus() {
    if (!lessonEl) return;
    var id = lessonEl.getAttribute('data-lesson'), st = $('[data-status]'), bar = $('[data-step-bar]');
    var visited = S.visit[id] || {}, steps = $$('[data-step]'), seen = steps.filter(function (s) { return visited[s.getAttribute('data-step')]; }).length;
    var pct = S.done[id] ? 100 : Math.round(100 * seen / Math.max(steps.length, 1));
    if (bar) bar.style.width = pct + '%';
    if (st) st.textContent = S.done[id] ? 'Complete' + (S.quiz[id] != null ? ' · quiz ' + S.quiz[id] + '%' : '') : (S.quiz[id] != null ? 'Quiz best ' + S.quiz[id] + '%' : (seen ? 'In progress' : 'Not started'));
    $$('[data-step-link]').forEach(function (a) { a.classList.toggle('is-done', !!visited[a.getAttribute('data-step-link')] || !!S.done[id]); });
    var md = $('[data-mark-done]'); if (md) md.textContent = S.done[id] ? 'Completed (undo)' : 'Mark as complete';
  }
  if (lessonEl) {
    var lid = lessonEl.getAttribute('data-lesson');
    S.visit[lid] = S.visit[lid] || {}; S.last = lid; save();
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) return;
          var k = e.target.getAttribute('data-step');
          S.visit[lid][k] = true; save();
          $$('[data-step-link]').forEach(function (a) { a.classList.toggle('is-current', a.getAttribute('data-step-link') === k); });
          lessonStatus();
        });
      }, { rootMargin: '-30% 0px -60% 0px' });
      $$('[data-step]').forEach(function (s) { io.observe(s); });
    }
    var md = $('[data-mark-done]');
    if (md) md.addEventListener('click', function () { S.done[lid] = !S.done[lid]; save(); lessonStatus(); marks(); });
    var form = $('[data-lablog]');
    if (form) {
      var prev = S.log[lid]; if (prev) { form.note.value = prev.note || ''; form.evidence.value = prev.evidence || ''; }
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        S.log[lid] = { note: form.note.value.trim(), evidence: form.evidence.value.trim(), at: new Date().toISOString(), title: $('h1').textContent };
        save(); $('[data-log-status]').textContent = 'Saved to your lab log.';
      });
    }
    lessonStatus();
  }

  /* Labs filter */
  $$('[data-filter]').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.getAttribute('data-filter');
      $$('[data-filter]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      $$('[data-filter-list] > [data-kind]').forEach(function (c) { c.hidden = f !== 'all' && c.getAttribute('data-kind') !== f; });
    });
  });
  /* Glossary filter */
  var gf = $('[data-gloss-filter]');
  if (gf) gf.addEventListener('input', function () {
    var q = gf.value.toLowerCase().trim(), shown = 0;
    $$('[data-term]').forEach(function (c) { c.hidden = !!q && c.getAttribute('data-term').indexOf(q) < 0 && c.textContent.toLowerCase().indexOf(q) < 0; if (!c.hidden) shown++; });
    $$('[data-gloss-group]').forEach(function (g) {
      var any = $$('[data-term]', g).some(function (c) { return !c.hidden; });
      g.hidden = !any;
      var a = $('[data-az="' + g.getAttribute('data-gloss-group') + '"]'); if (a) a.classList.toggle('is-off', !any);
    });
    var ct = $('[data-gloss-count]'); if (ct) ct.textContent = shown + (shown === 1 ? ' term' : ' terms');
    var em = $('[data-gloss-empty]'); if (em) em.hidden = shown > 0;
  });

  /* Dashboard */
  var cd = $('#course-data');
  if (cd) {
    var D = JSON.parse(cd.textContent), byId = {};
    D.lessons.forEach(function (l) { byId[l.id] = l; });
    function dash() {
      var mods = D.modules;
      var modDone = function (m) { return m.lessons.every(function (i) { return S.done[i]; }); };
      var doneMods = mods.filter(modDone).length;
      $('[data-d-path-count]').textContent = doneMods + ' of ' + mods.length + ' modules';
      $('[data-d-path-bar]').style.width = Math.round(100 * doneMods / mods.length) + '%';
      var pathLessons = D.lessons;
      var next = pathLessons.filter(function (l) { return !S.done[l.id]; })[0];
      if (next) {
        $('[data-d-next-title]').textContent = 'Up next: ' + next.code + ' ' + next.title;
        $('[data-d-next-sub]').textContent = 'Module ' + next.mod + ' · ' + (next.kind === 'lesson' ? 'Lesson' : next.kind === 'lab-remix' ? 'Code lab' : 'Tool lab') + (next.minutes ? ' · ' + next.minutes : '');
        $('[data-d-next-link]').href = L('/lessons/' + next.id + '/');
        $('[data-d-next-link]').textContent = S.done && Object.keys(S.done).length ? 'Continue' : 'Start';
      } else { $('[data-d-next-title]').textContent = 'All units complete'; $('[data-d-next-sub]').textContent = 'Take the final exam: 40 questions, pass with 70%.'; $('[data-d-next-link]').href = L('/final-exam/'); $('[data-d-next-link]').textContent = 'Final exam'; }
      var cur = mods.filter(function (m) { return !modDone(m); })[0];
      $('[data-d-path-list]').innerHTML = mods.slice(Math.max(0, mods.indexOf(cur) - 1), Math.max(0, mods.indexOf(cur) - 1) + 3).map(function (m) {
        var d = modDone(m), c = m === cur;
        return '<li style="display:flex;gap:10px;align-items:center;' + (c ? 'font-weight:700' : d ? '' : 'color:#9fc2b4') + '"><span style="width:20px;height:20px;border-radius:50%;box-sizing:border-box;display:grid;place-items:center;font-size:12px;font-weight:800;' + (d ? 'background:var(--brand-300);color:var(--brand-ink)">✓' : c ? 'border:2px solid var(--brand-300)">' : 'border:2px solid rgba(255,255,255,.3)">') + '</span>M' + m.n + ' ' + esc(m.title) + '</li>';
      }).join('');
      var done = D.lessons.filter(function (l) { return S.done[l.id]; }), labs = D.lessons.filter(function (l) { return l.kind.indexOf('lab') === 0; });
      $('[data-d-done]').textContent = done.length + ' / ' + D.lessons.length;
      $('[data-d-done-note]').textContent = done.length ? 'Last: ' + done[done.length - 1].title : 'Start with Module 1';
      $('[data-d-labs]').textContent = labs.filter(function (l) { return S.done[l.id]; }).length + ' / ' + labs.length;
      $('[data-d-labs-note]').textContent = 'Code and tool labs';
      var qv = Object.keys(S.quiz).filter(function (k) { return k !== 'final-exam'; }).map(function (k) { return S.quiz[k]; });
      $('[data-d-quiz]').textContent = qv.length ? Math.round(qv.reduce(function (a, b) { return a + b; }, 0) / qv.length) + '%' : '–';
      var logs = Object.keys(S.log);
      $('[data-d-logs]').textContent = logs.length;
      var cont = pathLessons.filter(function (l) { return !S.done[l.id]; }).slice(0, 2);
      if (S.last && byId[S.last] && !S.done[S.last] && cont.indexOf(byId[S.last]) < 0) cont = [byId[S.last]].concat(cont).slice(0, 2);
      $('[data-d-continue]').innerHTML = cont.length ? cont.map(function (l) {
        var v = S.visit[l.id] || {}, seen = Object.keys(v).length, pct = Math.min(95, seen * 20);
        var chip = l.kind === 'lab-remix' ? 'cc-chip--cs">Code lab' : l.kind === 'lab-gui' ? 'cc-chip--law">Tool lab' : 'cc-chip--brand">Lesson';
        return '<a class="cc-card card-link" href="' + L('/lessons/' + l.id + '/') + '"><div class="meta-chips"><span class="cc-chip ' + chip + '</span><span class="cc-chip">' + l.code + '</span></div><h3 style="font-size:16.5px">' + esc(l.title) + '</h3><div style="display:flex;align-items:center;gap:10px"><div class="cc-progress" style="flex:1"><span style="width:' + pct + '%"></span></div><b style="font-size:13px">' + pct + '%</b></div></a>';
      }).join('') : '<div class="empty">Every unit is complete. Next: the final exam.</div>';
      $('[data-d-log]').innerHTML = logs.length ? '<table><thead><tr><th>Unit</th><th>Notes</th><th>Evidence</th><th>Saved</th></tr></thead><tbody>' + logs.map(function (k) {
        var e = S.log[k];
        return '<tr><td style="font-weight:600"><a href="' + L('/lessons/' + k + '/') + '">' + esc((byId[k] ? byId[k].code + ' ' : '') + (byId[k] ? byId[k].title : e.title)) + '</a></td><td>' + esc(e.note || '') + '</td><td style="font:500 12.5px var(--font-mono);overflow-wrap:anywhere">' + esc(e.evidence || '—') + '</td><td>' + esc((e.at || '').slice(0, 10)) + '</td></tr>';
      }).join('') + '</tbody></table>' : '<div class="empty">No entries yet. Each lab ends with a “Save to your lab log” form.</div>';
      $('[data-d-mods]').innerHTML = D.modules.map(function (m) {
        var n = m.lessons.filter(function (i) { return S.done[i]; }).length;
        return '<li><a href="' + L('/modules/' + m.slug + '/') + '" style="text-decoration:none;color:var(--ink);display:block"><div style="display:flex;justify-content:space-between;gap:8px;font-size:14px"><span style="font-weight:600">' + m.n + '. ' + esc(m.title) + '</span><span style="color:var(--muted-2);font-variant-numeric:tabular-nums">' + n + '/' + m.lessons.length + '</span></div><div class="cc-progress" style="height:6px;margin-top:6px"><span style="width:' + Math.round(100 * n / m.lessons.length) + '%"></span></div></a></li>';
      }).join('');
    }
    dash();
    $('[data-export]').addEventListener('click', function () {
      var t = Object.keys(S.log).map(function (k) { var e = S.log[k]; return (byId[k] ? byId[k].code + ' ' + byId[k].title : k) + '\n' + (e.note || '') + '\nEvidence: ' + (e.evidence || '-') + '\nSaved: ' + (e.at || '') + '\n'; }).join('\n') || 'No lab log entries yet.';
      var st = $('[data-export-status]');
      try { navigator.clipboard.writeText(t).then(function () { st.textContent = 'Copied. Paste it into your team document.'; }, function () { fallback(t); st.textContent = 'Copied.'; }); } catch (e) { fallback(t); st.textContent = 'Copied.'; }
    });
    $('[data-reset]').addEventListener('click', function () { $('[data-reset-confirm]').hidden = false; });
    $('[data-reset-no]').addEventListener('click', function () { $('[data-reset-confirm]').hidden = true; });
    $('[data-reset-yes]').addEventListener('click', function () { S = { done: {}, quiz: {}, log: {}, visit: {} }; save(); location.reload(); });
  }

  /* Placement */
  var pf = $('[data-placement]');
  if (pf) {
    var PD = JSON.parse($('#placement-data').textContent);
    pf.addEventListener('submit', function (e) {
      e.preventDefault();
      var weak = {}, known = 0;
      PD.qs.forEach(function (q, i) { var v = +((pf['q' + i] || {}).value); if (v === q.a) known++; else weak[q.m] = true; });
      var start = PD.modules.filter(function (m) { return weak[m.n]; })[0] || PD.modules[PD.modules.length - 1];
      var skim = PD.modules.filter(function (m) { return m.n < start.n; });
      var r = $('[data-placement-result]'); r.hidden = false;
      r.innerHTML = '<div class="cc-eyebrow">Your result</div><h2 style="font-size:26px;margin:8px 0">' + known + ' of ' + PD.qs.length + ' known · start at Module ' + start.n + '</h2>' +
        '<p style="margin:0 0 12px;color:var(--muted)">Everyone does every module and takes the same final exam. ' + (skim.length ? 'You can move quickly through modules ' + skim.map(function (m) { return m.n; }).join(', ') + ': read them, then pass their quizzes to mark them complete.' : 'Start from the beginning: the foundations are worth it.') + '</p>' +
        '<div class="meta-chips"><a class="cc-btn cc-btn--primary" href="' + L('/lessons/' + start.first + '/') + '">Open Module ' + start.n + ': ' + esc(start.title) + '</a><a class="cc-btn cc-btn--secondary" href="' + L('/dashboard/') + '">See my progress</a></div>';
      r.scrollIntoView({ block: 'start' });
    });
  }
})();
