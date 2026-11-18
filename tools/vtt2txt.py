"""Turn a YouTube auto-caption .vtt into clean text, one line per ~15 s: [hh:mm:ss] words."""
import re, sys, pathlib
def clean(path, every=15):
    lines = pathlib.Path(path).read_text(encoding="utf-8", errors="ignore").splitlines()
    out, seen, t, buf, start = [], set(), None, [], None
    for ln in lines:
        m = re.match(r"(\d+):(\d+):(\d+)\.\d+ -->", ln)
        if m:
            t = int(m[1])*3600 + int(m[2])*60 + int(m[3]); continue
        if t is None or not ln.strip() or "-->" in ln: continue
        txt = re.sub(r"<[^>]+>", "", ln).strip()
        if not txt or txt in seen: continue
        seen.add(txt)
        if start is None: start = t
        buf.append(txt)
        if t - start >= every:
            out.append(f"[{start//3600:02d}:{start%3600//60:02d}:{start%60:02d}] " + " ".join(buf)); buf, start = [], None
    if buf: out.append(f"[{start//3600:02d}:{start%3600//60:02d}:{start%60:02d}] " + " ".join(buf))
    return "\n".join(out)
if __name__ == "__main__":
    print(clean(sys.argv[1]))
