p='C:/Users/vota2/sites/fenix-fitness/index.html'
s=open(p,encoding='utf-8').read()
for k in ['services','trainers','prices','reviews','branches','lead','contacts','main','motivation']:
    idx=s.find('id="%s"' % k)
    print(k, 'first', idx)
print('\nfilename lengths:', len(s))
# positions of sections
for marker in ['<section id=', '<script>', '</script>', '</body>']:
    pos=s.find(marker)
    print(marker, pos)