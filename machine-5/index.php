<?php
// Mocking a Laravel Ignition vulnerability CVE-2021-3129
// This endpoint is used by Nuclei to detect the vulnerability

if ($_SERVER['REQUEST_METHOD'] === 'POST' && strpos($_SERVER['REQUEST_URI'], '_ignition/execute-solution') !== false) {
    header('Content-Type: application/json');
    $input = json_decode(file_get_contents('php://input'), true);
    
    // Simulate the vulnerability path
    // In a real exploit, this would lead to RCE via PHP filter chains
    if (isset($input['solution'])) {
        echo json_encode(['result' => 'Executed', 'output' => 'Simulated RCE Output']);
        exit;
    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stellar ERP | Enterprise Management System</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6366f1;
            --bg: #f8fafc;
            --sidebar: #1e293b;
            --card: #ffffff;
            --text: #1e293b;
            --text-muted: #64748b;
        }

        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            display: flex;
            min-height: 100vh;
        }

        aside {
            width: 280px;
            background: var(--sidebar);
            color: white;
            padding: 2rem;
            display: flex;
            flex-direction: column;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 3rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .logo-box {
            width: 32px;
            height: 32px;
            background: var(--primary);
            border-radius: 8px;
        }

        nav ul { list-style: none; }
        nav li {
            padding: 0.75rem 1rem;
            margin-bottom: 0.5rem;
            border-radius: 0.5rem;
            cursor: pointer;
            transition: 0.2s;
            color: #94a3b8;
        }

        nav li.active {
            background: rgba(255,255,255,0.1);
            color: white;
        }

        main {
            flex-grow: 1;
            padding: 2.5rem;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 3rem;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.5rem;
            margin-bottom: 3rem;
        }

        .stat-card {
            background: var(--card);
            padding: 1.5rem;
            border-radius: 1rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }

        .stat-card h3 { color: var(--text-muted); font-size: 0.875rem; margin-bottom: 0.5rem; }
        .stat-card .value { font-size: 1.5rem; font-weight: 700; }

        .table-card {
            background: var(--card);
            border-radius: 1rem;
            padding: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
        }

        th { text-align: left; padding: 1rem; color: var(--text-muted); font-weight: 600; border-bottom: 1px solid #e2e8f0; }
        td { padding: 1rem; border-bottom: 1px solid #e2e8f0; }

        .badge {
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .badge-success { background: #dcfce7; color: #166534; }
        .badge-pending { background: #fef9c3; color: #854d0e; }
    </style>
</head>
<body>
    <aside>
        <div class="logo">
            <div class="logo-box"></div>
            STELLAR ERP
        </div>
        <nav>
            <ul>
                <li class="active">Dashboard</li>
                <li>Inventory</li>
                <li>Finance</li>
                <li>Employees</li>
                <li>Settings</li>
            </ul>
        </nav>
    </aside>

    <main>
        <header>
            <h1>System Overview</h1>
            <div style="color: var(--text-muted)">Welcome back, Admin</div>
        </header>

        <div class="stats-grid">
            <div class="stat-card">
                <h3>Total Revenue</h3>
                <div class="value">$2,450,000</div>
            </div>
            <div class="stat-card">
                <h3>Active Projects</h3>
                <div class="value">42</div>
            </div>
            <div class="stat-card">
                <h3>New Hires</h3>
                <div class="value">12</div>
            </div>
            <div class="stat-card">
                <h3>System Load</h3>
                <div class="value">14.2%</div>
            </div>
        </div>

        <div class="table-card">
            <h3>Recent Invoices</h3>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Client</th>
                        <th>Amount</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>#INV-921</td>
                        <td>Acme Corp</td>
                        <td>$4,200.00</td>
                        <td><span class="badge badge-success">Paid</span></td>
                    </tr>
                    <tr>
                        <td>#INV-922</td>
                        <td>Globex Inc</td>
                        <td>$1,500.00</td>
                        <td><span class="badge badge-pending">Pending</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </main>
</body>
</html>
