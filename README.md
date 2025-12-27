# Web Kriptografi ElGamal

Aplikasi web berbasis Flask untuk melakukan enkripsi dan dekripsi menggunakan **algoritma ElGamal**.

Website ini menyediakan:
- Halaman **Enkripsi** → Masukkan plaintext, key, dan dapatkan ciphertext beserta tabel proses enkripsi.
- Halaman **Dekripsi** → Masukkan ciphertext dan key, dapatkan plaintext beserta tabel proses dekripsi.

---

## 💻 Cara Menjalankan

1. **Pastikan Python 3.x sudah terinstal**  
2. Install dependencies:
```bash
pip install flask

3. Jalankan aplikasi:
```bash
python app.py

4. Buka browser, akses:
```bash
http://127.0.0.1:5000

5. Gunakan menu navigasi:

Enkripsi → Masukkan p, g, private_x, dan plaintext

Dekripsi → Masukkan p, private_x, dan ciphertext
🔑 Penjelasan File

app.py
File utama Flask. Berisi:

Fungsi elgamal_encrypt_char → enkripsi karakter

Fungsi elgamal_decrypt_char → dekripsi karakter

Route / → halaman enkripsi

Route /dekripsi → halaman dekripsi

templates/enkripsi.html
Template halaman enkripsi dengan form input key dan plaintext, tabel proses, serta hasil ciphertext.

templates/dekripsi.html
Template halaman dekripsi dengan form input key dan ciphertext, tabel proses, serta hasil plaintext.

static/style.css
Styling untuk tampilan web agar terlihat menarik dan responsif.

⚡ Cara Penggunaan

Jalankan python app.py

Akses http://127.0.0.1:5000/

Enkripsi

Masukkan p (bilangan prima), g (generator), private_x

Masukkan plaintext

Klik tombol Enkripsi

Lihat tabel proses enkripsi dan ciphertext

Dekripsi

Masukkan p, private_x

Masukkan ciphertext

Klik tombol Dekripsi

Lihat tabel proses dekripsi dan plaintext

📌 Catatan

Pastikan bilangan p yang dimasukkan adalah prima (> 107) agar algoritma ElGamal bekerja dengan benar.

Private key x harus lebih kecil dari p.

Ini adalah aplikasi untuk pembelajaran dan demo, bukan untuk produksi atau penggunaan kriptografi real.
