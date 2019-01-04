{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff\
\
a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc\
\
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b\
\
S = 0xc49d360886e704936a6678e1139d26b7819f7e90\
\
G = 0x046b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c2964fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5\
\
n = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551\
\
h = 0x01\
\
signature = 0x0a7ee30358296bc5ef3e56686988c704b75c0440090ca4b86add461ef697ac418deb0738b54452942f09d36495f6df4842643fc95c24e0e633181a9602a083364bc211b95e69dec436158451d1aa5739494f63e3a76294b471cb4c84e6118da518663b6a68c425cc89a716846d95bc381a225da8f3ec394897e227874998b40b5097740ae9d9c13d1c8a048b51bdf4b20232fe6babf401de0e1ee4e36d8a572911e02aef5ec15c633f6344ebaf2b2f2d9b09709dc351f7297ecdb6c3c794b5b840eb4933cc520d1e01e7f579d72eb2c629521e0bfdacda2e2dcfbb242844fb9692ef83a5ab0c8c22a1e0ed3ba16f1b7dc3a2fb4d8567013d14b3275ae5dd3a13\
\
#65 bytes\
pubkey = 0x04fdc06b1e5673e346198eaa48b37b13bf0b2c79b2059e1c707c97b7726da48b8223d232de50231c3dba6d2b7178f5028bb0840de136553ae4e504ad6e7a6e87df\
\
#64 bytes\
pubkey = 0xfdc06b1e5673e346198eaa48b37b13bf0b2c79b2059e1c707c97b7726da48b8223d232de50231c3dba6d2b7178f5028bb0840de136553ae4e504ad6e7a6e87df\
\
\
pubkey_x = 0xfdc06b1e5673e346198eaa48b37b13bf0b2c79b2059e1c707c97b7726da48b82\
pubkey_y = 0x23d232de50231c3dba6d2b7178f5028bb0840de136553ae4e504ad6e7a6e87df\
\
pubkey_punto = (pubkey_x,pubkey_y)\
#curva = y^2 = x^3-3x+41058363725152142129326129780047268409114441015993725554835256314039467401291\
\
\
""\
"Check prime"\
""\
#(b) Comproveu que el nombre de punts (ordre) de la corba que es fa servir \'b4es primer.\
factor(n)\
n\
#if output1 = output2 -> prime\
\
""\
""\
"Check point belongs to curve"\
""\
pubkey_y^2\
pubkey_x^3 - 3*pubkey_x+41058363725152142129326129780047268409114441015993725554835256314039467401291\
\
Zp= Zmod(p)\
E = EllipticCurve(Zp,[a,b])\
\
E([pubkey_x,pubkey_y])\
""\
""\
"Curve order"\
""\
E.order()\
#Result is equal to variable n (this leads us to the conclusion that it's correct)\
""\
""\
"Point order"\
""\
E(pubkey_punto).order()}