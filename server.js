const http = require('http');

const requestHandler = (req, res) => {
    // CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }
    
    console.log(`${req.method} ${req.url}`);
    
    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(`
            <!DOCTYPE html>
            <html>
            <head><title>Test App</title></head>
            <body>
                <h1>Test Application</h1>
                <div id="content">Content</div>
                <button id="test-button">Button</button>
            </body>
            </html>
        `);
    } else if (req.url === '/api/data') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'success', data: { id: 1 } }));
    } else if (req.url === '/api/users') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ 
            users: [
                { id: 1, name: 'User1' },
                { id: 2, name: 'User2' }
            ]
        }));
    } else if (req.url === '/api/login' && req.method === 'POST') {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'success', token: 'test-token' }));
    } else {
        res.writeHead(404, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'error', message: 'Not found' }));
    }
};

const server = http.createServer(requestHandler);
const PORT = 3000;

server.listen(PORT, () => {
    console.log(`✅ Server running on port ${PORT}`);
});

// Keep server running
process.on('SIGINT', () => {
    console.log('🛑 Server shutting down');
    server.close();
    process.exit(0);
});