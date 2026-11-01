import requests

PORTFOLIO_SERVERS = [
    {"name": "mcp-clean-scraper", "manifest_url": "https://mcp-clean-scraper.vercel.app/mcp/manifest", "repo": "https://github.com/inkbymuntaha-alt/mcp-clean-scraper"},
    {"name": "mcp-agent-mail", "manifest_url": "https://mcp-agent-mail.vercel.app/mcp/manifest", "repo": "https://github.com/inkbymuntaha-alt/mcp-agent-mail"},
    {"name": "mcp-lead-signals", "manifest_url": "https://mcp-lead-signals.vercel.app/mcp/manifest", "repo": "https://github.com/inkbymuntaha-alt/mcp-lead-signals"},
    {"name": "mcp-dep-checker", "manifest_url": "https://mcp-dep-checker.vercel.app/mcp/manifest", "repo": "https://github.com/inkbymuntaha-alt/mcp-dep-checker"}
]

REGISTRY_ENDPOINTS = [
    "https://registry.modelcontextprotocol.io/v1/ping",
    "https://api.smithery.ai/v1/servers/register",
    "https://mcp.so/api/register"
]

def broadcast_all():
    headers = {"Content-Type": "application/json"}
    for server in PORTFOLIO_SERVERS:
        payload = {"manifest_url": server["manifest_url"], "repository": server["repo"], "name": server["name"], "x402_enabled": True}
        for endpoint in REGISTRY_ENDPOINTS:
            try:
                res = requests.post(endpoint, json=payload, headers=headers, timeout=10)
                print(f"[{server['name']}] Broadcasted to {endpoint} -> Status: {res.status_code}")
            except Exception as e:
                print(f"Failed to ping {endpoint}: {e}")

if __name__ == "__main__":
    broadcast_all()
