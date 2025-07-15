"""
Configuration file for GitHub website automation
"""

# GitHub Configuration
GITHUB_USERNAME = "rockyco"
GITHUB_API_BASE = "https://api.github.com"

# Repository Monitoring Settings
MONITOR_SETTINGS = {
    # Only monitor repositories with at least this many stars
    "min_stars": 0,
    
    # Exclude forked repositories
    "exclude_forks": True,
    
    # Maximum number of repositories to process
    "max_repositories": 20,
    
    # Languages to highlight in statistics
    "primary_languages": ["C++", "Python", "MATLAB", "C", "Verilog", "JavaScript"],
    
    # Repository categories and their emojis
    "repo_emojis": {
        "peakPicker": "🏆",
        "pulseDetector": "🚀", 
        "llm-fpga-design": "🔧",
        "ImageProcessing": "📊",
        "estFreqOffset": "📡",
        "LabTraining": "🎓"
    }
}

# Website Update Settings
WEBSITE_SETTINGS = {
    # Files to update automatically
    "projects_file": "projects.md",
    
    # Backup original files before updating
    "create_backups": True,
    
    # Sections to update in projects.md
    "update_sections": [
        "repository_statistics",
        "github_profile"
    ]
}

# Commit Message Templates
COMMIT_TEMPLATES = {
    "github_update": """🤖 Auto-update: GitHub repository sync ({timestamp})

- Updated repository statistics and project information
- Synchronized with latest GitHub API data
- Maintained consistent project showcasing

🤖 Generated with GitHub Actions

Co-Authored-By: GitHub Actions <actions@github.com>""",
    
    "manual_update": """🤖 Manual update: Repository data refresh

- Manually triggered repository synchronization
- Updated project metrics and descriptions
- Ensured website accuracy with latest GitHub data

🤖 Generated with GitHub Actions

Co-Authored-By: GitHub Actions <actions@github.com>"""
}

# API Rate Limiting
RATE_LIMIT_SETTINGS = {
    # Delay between API calls (seconds)
    "api_delay": 1,
    
    # Maximum retries for failed requests
    "max_retries": 3,
    
    # Timeout for API requests (seconds)
    "request_timeout": 30
}