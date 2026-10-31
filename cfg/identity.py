# identity.py ---------------------------------------------------------------------------------------------

# --- config ---
TRACKS = {'a': 'First principles, from scratch', 'b': 'Enterprise-grade, off the shelf'}
IX = dict(bg='#EAF0F7', fg='#14233B', muted='#4A5B75', head_bg='#D5DEEA', head_fg='#14233B', line='#C3CEDC', link='#1D4ED8')

# --- libraries ---
from IPython.display  import HTML

# --- helper ---
def make_cell_id(track, kind, module, task):
    return f'{track}_{kind}_{module}_{task}'.lower()          # a_task_1_1 · b_job_task_1_1

# overall .................................................................................................

FONT = "system-ui,-apple-system,'Segoe UI',sans-serif"

THEMES = {
    'a': dict(head_bg='#EEF2F7', head_fg='#475569', rule='#64748B',
              body_bg='#F8FAFC', body_fg='#1E293B', zebra='#F1F5F9', hover='#E2E8F0',
              ban_fg ='#1E293B', ban_sub='#475569', ban_line='#CBD5E1',
              bar   ='linear-gradient(180deg,#64748B,#334155)', 
              ban_bg='linear-gradient(135deg,#F8FAFC 0%,#EEF2F7 100%)',
              line='#E2E8F0',    outer='#CBD5E1',   shadow='0 1px 3px rgba(15,23,42,.10)'),
    'b': dict(head_bg='#07142A', head_fg='#C8A24A', rule='#C8A24A',
              body_bg='#0B1B33', body_fg='#F4EFE3', zebra='#0E2240', hover='#142C50',
              ban_fg ='#F4EFE3', ban_sub='#B9C2D3', ban_line='#1E3354',
              bar    ='linear-gradient(180deg,#E4C77B 0%,#C8A24A 50%,#8F6F2A 100%)', 
              ban_bg='linear-gradient(135deg,#0B1B33 0%,#07142A 100%)',
              line='#1E3354',    outer='#1E3354',   shadow='0 4px 10px rgba(3,10,25,.35)'),
}

TRACK_CSS = '<style>' + ''.join(
    f".t-{k}{{--bg:{t['body_bg']};--fg:{t['body_fg']};--hbg:{t['head_bg']};--hfg:{t['head_fg']};"
    f"--cd:{t['zebra']};--ln:{t['line']};--rl:{t['rule']};--bar:{t['bar']};--ban:{t['ban_bg']};"
    f"--bt:{t['ban_fg']};--bs:{t['ban_sub']};--bl:{t['ban_line']};--bsh:{t['shadow']}}}"
    for k, t in THEMES.items()
) + """
:is(.t-a,.t-b) :is(h1,h2,h3,h4,h5,h6){color:var(--hfg)!important}
:is(.t-a,.t-b) :is(code,pre){background:var(--cd)!important;color:var(--fg)!important;border:1px solid var(--ln);border-radius:4px}
:is(.t-a,.t-b) code{padding:.1em .35em;font-size:.92em}
:is(.t-a,.t-b) pre{padding:10px 12px;overflow:auto}
:is(.t-a,.t-b) pre code{background:none!important;border:0;padding:0}
:is(.t-a,.t-b) pre code *{color:inherit!important}
:is(.t-a,.t-b).card{background:var(--bg);color:var(--fg);border:1px solid var(--ln);border-radius:8px;
                    box-shadow:inset 4px 0 0 var(--rl);padding:16px 20px;margin:12px 0}
.bn{position:relative;display:flex;flex-direction:column;margin:0 0 12px;padding:16px 22px 16px 30px;
    border:1px solid var(--bl);border-radius:10px;overflow:hidden;background:var(--ban);box-shadow:var(--bsh);
    font-family:system-ui,-apple-system,'Segoe UI',sans-serif}
.bn::before{content:'';position:absolute;inset:0 auto 0 0;width:8px;background:var(--bar)}
.bn-eb{margin-bottom:8px;color:var(--rl);font:600 11px/1 system-ui,-apple-system,'Segoe UI',sans-serif;
       letter-spacing:.16em;text-transform:uppercase}
.bn :is(h1,h2,h3){margin:0;padding:0;border:0;color:var(--bt)!important;font-family:inherit;font-weight:300;letter-spacing:-.01em}
.bn p{margin:6px 0 0;color:var(--bs);font:300 14px/1.4 system-ui,-apple-system,'Segoe UI',sans-serif}
.bn-trk{position:absolute;top:14px;right:18px;display:flex;gap:4px;
        font:600 11px/1 system-ui,sans-serif;letter-spacing:.08em}
.bn-trk i{font-style:normal;padding:6px 12px;border-radius:999px;border:1px solid var(--ln);color:var(--rl)}
.t-a .bn-trk i:first-child,.t-b .bn-trk i:last-child{background:var(--rl);border-color:var(--rl);color:var(--bg)}
</style>"""

display(HTML(TRACK_CSS))
