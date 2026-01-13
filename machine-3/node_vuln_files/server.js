const express = require('express');
const app = express();
const path = require('path');

app.use(express.json());

const HTML = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vision AI | Real-time Analytics</title>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #00f2ff;
            --bg: #050505;
            --card: #111;
            --text: #e0e0e0;
        }

        body {
            font-family: 'Space Grotesk', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            overflow-x: hidden;
        }

        .gradient-bg {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(circle at 50% 50%, #101827 0%, #050505 100%);
            z-index: -1;
        }

        nav {
            padding: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            letter-spacing: 2px;
            color: var(--primary);
            text-shadow: 0 0 10px var(--primary);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
        }

        .card {
            background: var(--card);
            border: 1px solid #333;
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 2px;
            background: linear-gradient(90deg, transparent, var(--primary), transparent);
        }

        h1 { font-size: 3.5rem; margin-bottom: 1rem; }
        
        textarea {
            width: 100%;
            height: 150px;
            background: #000;
            border: 1px solid #444;
            color: var(--primary);
            padding: 1rem;
            border-radius: 10px;
            font-family: monospace;
            margin-top: 1rem;
        }

        .btn {
            background: var(--primary);
            color: #000;
            border: none;
            padding: 1rem 2rem;
            border-radius: 10px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 1rem;
            transition: 0.3s;
        }

        .btn:hover {
            box-shadow: 0 0 20px var(--primary);
            transform: scale(1.05);
        }

        #result {
            margin-top: 2rem;
            padding: 1rem;
            background: #111;
            border-left: 4px solid var(--primary);
            font-family: monospace;
        }
    </style>
</head>
<body>
    <div class="gradient-bg"></div>
    <nav>
        <div class="logo">VISION_AI</div>
        <div>v4.2.0-STABLE</div>
    </nav>

    <div class="container">
        <div class="grid">
            <div>
                <h1>Neural Data Processing</h1>
                <p>Execute custom business logic filters via our sandbox engine.</p>
                <div class="card">
                    <h3>logic_engine.js</h3>
                    <textarea id="logic">const data = [10, 20, 30];\nreturn data.map(x => x * 2);</textarea>
                    <button class="btn" onclick="execute()">RUN ENGINE</button>
                    <div id="result">Result will appear here...</div>
                </div>
            </div>
            <div>
                <div class="card" style="margin-top: 5rem;">
                    <h3>System Stats</h3>
                    <p style="color: #888">CPU: 12%</p>
                    <p style="color: #888">Latency: 4ms</p>
                    <p style="color: var(--primary)">Uptime: 99.9%</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        async function execute() {
            const code = document.getElementById('logic').value;
            const resDiv = document.getElementById('result');
            resDiv.innerText = 'Processing...';

            const response = await fetch('/api/execute', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code })
            });
            const data = await response.json();
            resDiv.innerText = JSON.stringify(data.result || data.error, null, 2);
        }
    </script>
</body>
</html>
`;

app.get('/', (req, res) => res.send(HTML));

app.post('/api/execute', (req, res) => {
    const { code } = req.body;
    try {
        // VULNERABLE: Direct eval of user input
        // Using a function wrapper to allow return statements
        const result = eval(`(() => { ${code} })()`);
        res.json({ result });
    } catch (e) {
        res.json({ error: e.message });
    }
});

app.listen(3000, () => console.log('Vision AI listening on port 3000'));
