from flask import Flask, render_template, request, flash, url_for
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def text_to_ints(text):
    return [ord(c) for c in text]

def ints_to_text(ints):
    return ''.join(chr(i) for i in ints if 0 <= i < 55296)

# Enkripsi + tabel
def elgamal_encrypt_char(m, p, g, y):
    k = random.randint(1, p-2)
    c1 = pow(g, k, p)
    yk = pow(y, k, p)
    c2 = (m * yk) % p
    return c1, c2, k, yk

# Dekripsi + tabel
def elgamal_decrypt_char(c1, c2, p, x):
    s = pow(c1, x, p)
    s_inv = pow(s, p-2, p)
    m = (c2 * s_inv) % p
    return m, s, s_inv

@app.route('/', methods=['GET', 'POST'])
def enkripsi():
    data = {'p': '', 'g': '', 'private_x': '', 'y': '', 'plaintext': '', 'table': [], 'ciphertext': ''}

    if request.method == 'POST':
        try:
            p = int(request.form['p'])
            g = int(request.form['g'])
            private_x = int(request.form['private_x'])
            y = pow(g, private_x, p)
            data.update({'p': p, 'g': g, 'private_x': private_x, 'y': y})

            plaintext = request.form['plaintext'].strip()
            if not plaintext:
                flash("Masukkan plaintext!")
            else:
                ints = text_to_ints(plaintext)
                table = []
                cipher_parts = []
                for i, m in enumerate(ints):
                    c1, c2, k, yk = elgamal_encrypt_char(m, p, g, y)
                    cipher_parts.append(f"{c1},{c2}")
                    table.append({
                        'no': i+1, 'chr': plaintext[i], 'm': m,
                        'k': k, 'yk_mod_p': yk, 'c1': c1, 'c2': c2
                    })
                ciphertext = ";".join(cipher_parts)
                data.update({'table': table, 'ciphertext': ciphertext, 'plaintext': plaintext})
                flash("Enkripsi berhasil!")

        except Exception as e:
            flash(f"Error: {str(e)}")

    return render_template('enkripsi.html', **data, active_page='enkripsi')

@app.route('/dekripsi', methods=['GET', 'POST'])
def dekripsi():
    data = {'p': '', 'private_x': '', 'ciphertext': '', 'table': [], 'plaintext': ''}

    if request.method == 'POST':
        try:
            p = int(request.form['p'])
            private_x = int(request.form['private_x'])
            ciphertext = request.form['ciphertext'].strip()
            
            data.update({'p': p, 'private_x': private_x})

            if not ciphertext:
                flash("Masukkan ciphertext!")
            else:
                pairs = [pair.split(',') for pair in ciphertext.split(';') if pair]
                table = []
                decrypted_ints = []
                for i, (c1_str, c2_str) in enumerate(pairs):
                    c1 = int(c1_str)
                    c2 = int(c2_str)
                    m, s, s_inv = elgamal_decrypt_char(c1, c2, p, private_x)
                    decrypted_ints.append(m)
                    table.append({
                        'no': i+1, 'c1': c1, 'c2': c2,
                        's': s, 's_inv': s_inv, 'm': m,
                        'chr': chr(m) if 0 <= m < 55296 else '?'
                    })
                plaintext = ints_to_text(decrypted_ints)
                data.update({'table': table, 'plaintext': plaintext, 'ciphertext': ciphertext})
                flash("Dekripsi berhasil!")

        except Exception as e:
            flash(f"Error: {str(e)}")

    return render_template('dekripsi.html', **data, active_page='dekripsi')

if __name__ == '__main__':
    app.run(debug=True)