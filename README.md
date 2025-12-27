# Web Kriptografi ElGamal

Aplikasi web berbasis Flask untuk melakukan enkripsi dan dekripsi menggunakan **algoritma ElGamal**.

Website ini menyediakan:
- Halaman **Enkripsi** → Masukkan plaintext, key, dan dapatkan ciphertext beserta tabel proses enkripsi.
- Halaman **Dekripsi** → Masukkan ciphertext dan key, dapatkan plaintext beserta tabel proses dekripsi.

---

## 💻 Cara Menjalankan

1. **Pastikan Python 3.x sudah terinstal**  
2. **Install dependencies:**
```bash
pip install flask
```
3. **Jalankan aplikasi:**
```bash
python app.py
```
4. **Buka browser, akses:**
```bash
http://127.0.0.1:5000
```


📌 Catatan

Pastikan bilangan p yang dimasukkan adalah prima (> 107) agar algoritma ElGamal bekerja dengan benar.

Private key x harus lebih kecil dari p.
