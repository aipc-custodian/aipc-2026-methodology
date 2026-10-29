import re, glob, os, unicodedata, sys
src_dir, paper_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
def norm(t):
    t=unicodedata.normalize('NFKC',t).replace('­','')
    t=re.sub(r'-\s*\n\s*','',t)
    for a,b in [('“','"'),('”','"'),('‘',"'"),('’',"'"),('–','-'),('—','-'),('ﬁ','fi'),('ﬂ','fl')]: t=t.replace(a,b)
    return re.sub(r'\s+',' ',t).lower()
paper=open(paper_path,encoding='utf-8').read()
body=re.split(r'\n## References',paper)[0]
srcs={os.path.basename(p)[:-4]:norm(open(p,encoding='utf-8',errors='ignore').read()) for p in glob.glob(os.path.join(src_dir,'*.txt'))}
rows=[];nf=0
for m in re.finditer(r'"([^"\n]{10,}?)"|“([^”\n]{10,}?)”',body):
    q=m.group(1) or m.group(2)
    ctx=re.sub(r'\s+',' ',body[max(0,m.start()-140):m.start()])
    nq=norm(q).strip(' .,;:')
    hits=[k for k,v in srcs.items() if nq in v]
    st=None
    if hits: st='FOUND: '+', '.join(hits)
    else:
        frags=[f.strip(' .,;:') for f in re.split(r'\.\.\.|…|\[[^\]]*\]|\*',nq) if len(f.split())>=3]
        fh=[k for k,v in srcs.items() if frags and all(f in v for f in frags)]
        if fh: st='FOUND (in fragments): '+', '.join(fh)
        else:
            # near: longest 6-word window present
            w=nq.split(); best=None
            for k,v in srcs.items():
                n=sum(1 for i in range(max(1,len(w)-5)) if ' '.join(w[i:i+6]) in v)
                if n and (best is None or n>best[1]): best=(k,n)
            st='NOT FOUND' + (f' (partial match in {best[0]}: {best[1]} six-word runs)' if best else ' in local sources')
            nf+=1
    rows.append((q,st,ctx))
with open(out,'w',encoding='utf-8') as f:
    f.write(f'# Quotation check\n\n{len(rows)} quotations in final.md checked against the 14 source texts in Sources_1 and Sources_1x. {nf} not matched exactly.\n\n')
    for q,st,ctx in rows: f.write(f'- "{q}"\n  - {st}\n  - before: …{ctx[-120:]}\n')
print(len(rows),'quotations;',nf,'not matched')
