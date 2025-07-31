#!/usr/bin/env python3
"""
Simple HTTP server to preview the Jekyll blog locally
This shows the raw markdown files - for full Jekyll experience, you'll need Ruby/Jekyll installed
"""

import http.server
import socketserver
import os
import markdown
from pathlib import Path

class MarkdownHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.md'):
            try:
                # Read the markdown file
                file_path = self.path[1:]  # Remove leading /
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Remove Jekyll front matter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        content = parts[2]
                
                # Convert markdown to HTML
                html_content = markdown.markdown(content, extensions=['extra', 'codehilite'])
                
                # Wrap in basic HTML template
                html_page = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>CAIO Playbook Preview</title>
                    <style>
                        body {{
                            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
                            line-height: 1.7;
                            color: #333;
                            max-width: 900px;
                            margin: 0 auto;
                            padding: 2rem;
                        }}
                        h1, h2, h3 {{ color: #2c3e50; }}
                        h2 {{ border-bottom: 2px solid #ecf0f1; padding-bottom: 0.5rem; }}
                        strong {{ color: #2c3e50; }}
                        code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
                        pre {{ background-color: #f4f4f4; padding: 1rem; overflow-x: auto; }}
                        blockquote {{ 
                            border-left: 4px solid #3498db; 
                            padding-left: 1rem; 
                            color: #555; 
                            font-style: italic;
                        }}
                        a {{ color: #3498db; }}
                    </style>
                </head>
                <body>
                    <nav style="margin-bottom: 2rem;">
                        <a href="/">Home</a> | 
                        <a href="/about.md">About</a> | 
                        <a href="/archive.md">Archive</a> |
                        <a href="/_posts/">Posts</a>
                    </nav>
                    {html_content}
                </body>
                </html>
                """
                
                # Send response
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html_page.encode())
                return
            except Exception as e:
                self.send_error(404, f"File not found: {e}")
                return
        
        # For non-markdown files, use default handler
        super().do_GET()

    def list_directory(self, path):
        # Custom directory listing for _posts
        if path.endswith('_posts'):
            try:
                files = os.listdir(path)
                md_files = [f for f in files if f.endswith('.md')]
                
                html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Blog Posts - CAIO Playbook</title>
                    <style>
                        body {{
                            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
                            line-height: 1.7;
                            color: #333;
                            max-width: 900px;
                            margin: 0 auto;
                            padding: 2rem;
                        }}
                        h1 {{ color: #2c3e50; }}
                        ul {{ list-style-type: none; padding: 0; }}
                        li {{ margin: 1rem 0; }}
                        a {{ color: #3498db; text-decoration: none; font-size: 1.1rem; }}
                        a:hover {{ text-decoration: underline; }}
                    </style>
                </head>
                <body>
                    <h1>Blog Posts</h1>
                    <p><a href="/">← Back to Home</a></p>
                    <ul>
                """
                
                for f in sorted(md_files, reverse=True):
                    html += f'<li><a href="/{path}/{f}">{f}</a></li>\n'
                
                html += """
                    </ul>
                </body>
                </html>
                """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html.encode())
                return
            except Exception as e:
                self.send_error(500, f"Error listing directory: {e}")
                return
        
        return super().list_directory(path)

if __name__ == "__main__":
    PORT = 8000
    
    # Check if markdown module is available
    try:
        import markdown
    except ImportError:
        print("Installing required markdown module...")
        import subprocess
        subprocess.check_call(["pip3", "install", "markdown"])
        import markdown
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MarkdownHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        print(f"View your blog at: http://localhost:{PORT}/index.md")
        print(f"View first post at: http://localhost:{PORT}/_posts/2025-01-31-ai-governance-playbook-strategy-governance.md")
        print("\nPress Ctrl+C to stop the server")
        httpd.serve_forever()