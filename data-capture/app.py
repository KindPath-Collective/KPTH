from flask import Flask, request, jsonify
import redis
import json
import os
import base64
from cryptography.fernet import Fernet

app = Flask(__name__)

# Load encryption key from environment — NEVER generate at runtime.
# To create a key: python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
# Then set ENCRYPTION_KEY in your .env file.
_raw_key = os.environ.get('ENCRYPTION_KEY')
if not _raw_key:
    raise RuntimeError(
        "ENCRYPTION_KEY environment variable is not set. "
        "Set it in .env before running. "
        "Generate with: python -c \"from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())\""
    )
try:
    cipher = Fernet(_raw_key.encode() if isinstance(_raw_key, str) else _raw_key)
except Exception as e:
    raise RuntimeError(f"ENCRYPTION_KEY is invalid: {e}") from e

_redis_host = os.environ.get('REDIS_HOST', 'localhost')
_redis_port = int(os.environ.get('REDIS_PORT', 6379))
r = redis.Redis(host=_redis_host, port=_redis_port, db=0)

@app.route('/capture', methods=['POST'])
def capture_data():
    data = request.json
    if not data:
        return jsonify({'error': 'No JSON body received'}), 400
    encrypted = cipher.encrypt(json.dumps(data).encode())
    # Send to multiple destinations
    try:
        r.lpush('data_queue', encrypted)
    except Exception as e:
        app.logger.warning(f"Redis unavailable, skipping queue: {e}")
    # Also persist to encrypted file log
    log_path = os.environ.get('DATA_LOG_PATH', 'data.log')
    with open(log_path, 'ab') as f:
        f.write(encrypted + b'\n')
    return jsonify({'status': 'captured'})

if __name__ == '__main__':
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug)