import re
import os

# Get the base directory
base_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(base_dir, '..', 'frontend')

def convert_to_static(filename, page_id):
    """Convert Django template to static HTML"""
    
    # Read source file
    source_path = os.path.join(frontend_dir, 'public', 'app', filename)
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove Django template tags
    content = re.sub(r'{%\s*extends\s+[^%]+%}', '', content)
    content = re.sub(r'{%\s*load\s+static\s*%}', '', content)
    content = re.sub(r'{%\s*block\s+content\s*%}', '', content)
    content = re.sub(r'{%\s*endblock\s*%}', '', content)
    content = re.sub(r'{{\s*obj_name\s*}}', page_id, content)
    
    # Create HTML with boilerplate
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_id.title()} - NLP Case Detector</title>
    <link rel="icon" href="/static/app/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="/static/app/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/app/user-defined/css/customized.css">
    <link rel="stylesheet" href="/static/app/fa/css/all.css">
    <link rel="stylesheet" href="/static/app/datatables/datatables.min.css">
    <script src="/static/app/scripts/global.js"></script>
    <script src="/static/app/scripts/axios.min.js"></script>
    <script src="/static/app/scripts/vue.min.js"></script>
    <script src="/static/app/bootstrap/js/bootstrap.js"></script>
    <script src="/static/app/jquery/jquery-3.6.0.min.js"></script>
    <script src="/static/app/datatables/datatables.min.js"></script>
    <script>
        if (typeof axios !== 'undefined') {{
            axios.defaults.baseURL = window.location.origin;
        }}
    </script>
</head>
<body style="padding-top: 56px;">
    <div id="navbar-container"></div>
    <div id="sidebar-container"></div>
    <div class="container mt-4">
{content}
    </div>
    <script src="/static/app/bootstrap/js/bootstrap.bundle.js"></script>
    <script>
        async function loadPartial(url, containerId) {{
            try {{
                const response = await fetch(url);
                if (response.ok) {{
                    const html = await response.text();
                    document.getElementById(containerId).innerHTML = html;
                }}
            }} catch (error) {{
                console.error('Error loading ' + url + ':', error);
            }}
        }}
        document.addEventListener('DOMContentLoaded', function() {{
            loadPartial('/static/partials/navbar_static.html', 'navbar-container');
            loadPartial('/static/partials/sidebar_static.html', 'sidebar-container');
        }});
    </script>
</body>
</html>'''
    
    # Write output file
    output_path = os.path.join(frontend_dir, 'static_html', filename.replace('.html', '_static.html'))
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f'Created {filename.replace(".html", "_static.html")}')

# Convert files
convert_to_static('complaints.html', 'complaints-page')
convert_to_static('library.html', 'library-page')
convert_to_static('credibility.html', 'credibility-page')

print('All files converted successfully!')
