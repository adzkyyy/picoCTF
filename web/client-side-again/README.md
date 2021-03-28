sama seperti challenge "dont-use-client-side", namun source code nya dirubah menjadi satu baris

gunakan http://www.jsnice.org/ agar source code mudah dibaca

terdapat fungsi tertentu yang bila mana dipanggil akan mereturn potongan flag

--use--
browser console (developer tools) => inspect

pada source code, potongan flag tersebut digantikan oleh fungsi. Jadi kita harus mengganti fungsi menjadi potongan flag

---example---
_0x4b5b('0x3') -> "picoCTF{"

--link challenge--
https://jupiter.challenges.picoctf.org/problem/56816/
