# pip install segno
# crea una VCard

from segno import helpers
qrcode = helpers.make_vcard(
    name='Rojas, Luis Alejandro',
    displayname='Luis Alejandro Rojas',
    email='lrojas@cepia.cl',
    phone='+56942261802',
    org='Cepia Ingenieros Consultores LTDA.',
    title='Gerente de Diseño de Proyectos',
    workphone='712532624'
)

qrcode.designator

# se puede guardar en svg o png
qrcode.save('my-vcard.png', scale=10, dark='#000000', light='#FFFFFF')
qrcode.save('my-vcard.svg', scale=10, dark='#000000', light='#FFFFFF')
# #5493d2 código color cepia

