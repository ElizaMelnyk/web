from flask import Flask, jsonify
import ssl

app = Flask(__name__)

@app.route('/output')
def hello():
    return jsonify(message='Eliza Melnyk KP-22')

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

    context.load_cert_chain(
        certfile=r'C:\Users\Admin\Web\localhost.pem',
        keyfile=r'C:\Users\Admin\Web\localhost-key.pem'
    )

    context.set_ciphers('RSA')

    app.run(
        ssl_context=context,
        host='0.0.0.0',
        port=443,
        debug=True
    )