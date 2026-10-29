import re,sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src,encoding='utf-8').read()
title=re.match(r'# (.+)\n',s).group(1); s=s[len(re.match(r'# .+\n',s).group(0)):]
sub={'₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9','ₓ':'x','ₜ':'t','ᵢ':'i','ₙ':'n'}
s=re.sub('['+''.join(sub)+']+',lambda m:'~'+''.join(sub[c] for c in m.group(0))+'~',s)
s=s.replace('ᵏ','^k^')
# abstract: move "## Abstract" body into YAML abstract
m=re.search(r'## Abstract\n\n(.+?)\n\n(?=## )',s,re.S)
abstract=None
if m: abstract=m.group(1).strip(); s=s.replace(m.group(0),'',1)
else:
    m=re.search(r'\*\*Abstract\.\*\*\s*(.+?)\n\n',s,re.S)
    if m: abstract=m.group(1).strip(); s=s.replace(m.group(0),'',1)
# references: hanging indent
head,_,refs=s.partition('\n## References\n')
fn=''
# keep footnote definitions out of refs section
fns=re.findall(r'^\[\^[^\]]+\]:.*(?:\n(?:    .*|\s*$))*',refs,re.M)
for f in fns: refs=refs.replace(f,'')
paras=[re.sub(r'^-\s+','',p.strip()) for p in refs.split('\n\n') if p.strip()]
paras=[re.sub(r'(?<![<(])(https?://\S+?)([.,;]?)(?=\s|$)',r'<\1>\2',p) for p in paras]
refs='\n\n'.join('\\noindent\\hangindent=1.5em\\hangafter=1 '+p for p in paras)
s=head+'\n\n## References {-}\n\n'+refs+'\n\n'+'\n\n'.join(fns)+'\n'
yaml='---\ntitle: "'+title.replace('"','\\"')+'"\n'+('abstract: |\n  '+abstract.replace('\n','\n  ')+'\n' if abstract else '')+'---\n\n'
open(dst,'w',encoding='utf-8').write(yaml+s)
