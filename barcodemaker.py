import barcode
hr=barcode.get_barcode_class('ean13')
Hr=hr('1234567890777')
qr=Hr.save('123')