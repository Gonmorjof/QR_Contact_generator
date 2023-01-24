# pip install segno
# crea una MeCard

from segno import helpers
qrcode = helpers.make_mecard(name='Morgado Jofré,Gonzalo',
                             email='gonzalo.morgado.j@gmail.com',
                             phone='+56949640966')
qrcode.designator
'3-L'
# Some params accept multiple values, like email, phone, url
'''
qrcode = helpers.make_mecard(name='Doe,John',
                             email=('me@example.org', 'another@example.org'),
                             url=['http://www.example.org', 'https://example.org/~joe'])
                             '''
qrcode.save('my-mecard.svg', scale=4)