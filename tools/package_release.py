#!/usr/bin/env python3
"""Build a ZIP from the explicit release selection manifest after all gates pass."""
import argparse, hashlib, json, shutil, sys, zipfile
from pathlib import Path

REQUIRED_GATES=("rights_review","mastering_measurement","human_listening_approval","metadata_and_artwork_review","human_publication_authorization")

def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",type=Path,default=Path("release/PUBLIC-DISTRIBUTION-SELECTION.json"))
    ap.add_argument("--out",type=Path,default=Path("release-package.zip"))
    ap.add_argument("--allow-pending",action="store_true",help="Create a diagnostic selection report only; never creates a distributable ZIP.")
    a=ap.parse_args()
    m=json.loads(a.manifest.read_text(encoding="utf-8"))
    blockers=[f"{k}={m.get('gates',{}).get(k,'missing')}" for k in REQUIRED_GATES if m.get("gates",{}).get(k)!="approved"]
    selected=[]; missing=[]
    for item in m.get("selected_assets",[]):
        if not item.get("required"): continue
        rel=item.get("path")
        if not rel: missing.append(f"{item.get('role')}: no path"); continue
        p=Path(rel)
        if not p.is_file(): missing.append(f"{item.get('role')}: missing file {rel}"); continue
        selected.append((p,item.get("role","asset"),sha256(p)))
    if blockers or missing:
        print(json.dumps({"status":"blocked","gate_blockers":blockers,"asset_blockers":missing},indent=2))
        if not a.allow_pending: return 2
    if a.allow_pending:
        print(json.dumps({"status":"diagnostic_only","selected":[{"role":r,"path":str(p),"sha256":h} for p,r,h in selected]},indent=2))
        return 0
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(a.out,"w",zipfile.ZIP_DEFLATED) as z:
        for p,role,digest in selected:
            z.write(p,arcname=p.name)
        z.writestr("PACKAGE-CHECKSUMS.json",json.dumps([{"role":r,"file":p.name,"sha256":h} for p,r,h in selected],indent=2)+"\n")
    print(json.dumps({"status":"package_created","file":str(a.out),"assets":len(selected)},indent=2))
    return 0

if __name__=="__main__": sys.exit(main())
