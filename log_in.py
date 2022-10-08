def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('czb',22,city='Beijing')
d={'city':'Beijing','job':'Student'}
person('czb',22,**d)
person('czb',22,city=d['city'])