import os
from flask import Flask, request, render_template_string, jsonify
import subprocess

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexus Cloud Control | Enterprise Management</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text: #f8fafc;
            --text-muted: #94a3b8;
            --success: #10b981;
            --error: #ef4444;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        nav {
            padding: 1.5rem 2rem;
            background: rgba(30, 41, 59, 0.8);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255,255,255,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(to right, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .container {
            max-width: 1000px;
            margin: 3rem auto;
            padding: 0 1rem;
            flex-grow: 1;
        }

        .hero {
            text-align: center;
            margin-bottom: 4rem;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            letter-spacing: -0.025em;
        }

        .hero p {
            color: var(--text-muted);
            font-size: 1.125rem;
        }

        .card {
            background: var(--card-bg);
            border-radius: 1rem;
            padding: 2rem;
            border: 1px solid rgba(255,255,255,0.05);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            transition: transform 0.2s;
        }

        .card:hover {
            transform: translateY(-4px);
        }

        .tool-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }

        .tool-icon {
            width: 40px;
            height: 40px;
            background: var(--primary);
            border-radius: 0.75rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .input-group {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }

        input {
            flex-grow: 1;
            background: #0f172a;
            border: 1px solid #334155;
            color: white;
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            outline: none;
            transition: border-color 0.2s;
        }

        input:focus {
            border-color: var(--primary);
        }

        button {
            background: var(--primary);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }

        button:hover {
            background: var(--primary-hover);
        }

        .output-console {
            background: #000;
            color: #10b981;
            font-family: 'Courier New', Courier, monospace;
            padding: 1.5rem;
            border-radius: 0.5rem;
            min-height: 200px;
            overflow-y: auto;
            border: 1px solid #334155;
            white-space: pre-wrap;
        }

        footer {
            padding: 2rem;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.875rem;
            border-top: 1px solid rgba(255,255,255,0.05);
        }

        .status-dot {
            width: 8px;
            height: 8px;
            background: var(--success);
            border-radius: 50%;
            display: inline-block;
            margin-right: 0.5rem;
            box-shadow: 0 0 8px var(--success);
        }
    </style>
</head>
<body>
    <nav>
        <div class="logo">NEXUS CLOUD</div>
        <div style="display: flex; align-items: center;">
            <span class="status-dot"></span>
            <span style="font-size: 0.875rem; color: var(--text-muted);">System Operational</span>
        </div>
    </nav>

    <div class="container">
        <div class="hero">
            <h1>Infrastructure Health</h1>
            <p>Real-time node diagnostics and reachability testing.</p>
        </div>

        <div class="card">
            <div class="tool-header">
                <div class="tool-icon">
                    <svg width="20" height="20" fill="white" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14.5v-9l6 4.5-6 4.5z"/></svg>
                </div>
                <div>
                    <h3>Network Reachability Tool</h3>
                    <p style="color: var(--text-muted); font-size: 0.875rem;">Verify latency and uptime for remote endpoints.</p>
                </div>
            </div>

            <div class="input-group">
                <input type="text" id="hostInput" placeholder="Enter IP or hostname (e.g. google.com)" value="127.0.0.1">
                <button onclick="checkHealth()">Run Diagnostic</button>
            </div>

            <div class="output-console" id="output">Waiting for input...</div>
        </div>
    </div>

    <footer>
        &copy; 2026 Nexus Cloud Control. Confidential Enterprise Proprietary.
    </footer>

    <script>
        async function checkHealth() {
            const host = document.getElementById('hostInput').value;
            const output = document.getElementById('output');
            output.innerText = 'Initializing diagnostic connection...';
            
            try {
                const response = await fetch(`/api/health?host=${encodeURIComponent(host)}`);
                const data = await response.text();
                output.innerText = data;
            } catch (e) {
                output.innerText = 'Error: Failed to reach internal API';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/api/health')
def health():
    host = request.args.get('host', '127.0.0.1')
    
    # Vulnerable to command injection!
    # The developer tried to be clever but failed.
    cmd = f"ping -c 3 {host}"
    try:
        # Using shell=True makes it vulnerable to ; id, etc.
        # But even without shell=True, if passed as string it's bad.
        # Here we use os.popen or subprocess.check_output with shell=True for demo.
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return output.decode()
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
