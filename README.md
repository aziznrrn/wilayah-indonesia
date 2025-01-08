# Wilayah Indonesia

## Deskripsi

Script Python digunakan untuk:

1. **Mengunduh** file SQL dari repository GitHub: [cahyadsn/wilayah](https://github.com/cahyadsn/wilayah).
2. **Ekstraksi** data tabel `wilayah` dari file SQL yang diunduh.
3. **Konversi** data tabel `wilayah` ke file CSV dengan nama `wilayah.csv`.
4. **Pemisahan data** berdasarkan panjang kode:
   - `provinces.csv`: Data wilayah tingkat provinsi (kode panjang 2).
   - `cities.csv`: Data wilayah tingkat kota/kabupaten (kode panjang 4).
   - `sub_districts.csv`: Data wilayah tingkat kecamatan (kode panjang 6).
   - `villages.csv`: Data wilayah tingkat desa (kode panjang 10).

File CSV hasil proses akan disimpan di folder `./output`.

## Penghargaan

Terima kasih kepada [Cahya DSN](https://github.com/cahyadsn) yang telah menyediakan file SQL wilayah Indonesia di repository GitHub-nya. Data ini sangat berguna untuk berbagai keperluan pengolahan data wilayah.

## Catatan

- Script ini otomatis mengganti tanda kutip ganda (`''`) menjadi satu kutip (`'`).
- Script ini juga menghapus tanda titik (`.`) pada kolom kode wilayah.
