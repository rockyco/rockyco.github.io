# 🤖 Website Automation System

Automated GitHub repository monitoring and website content synchronization system for [rockyco.github.io](https://rockyco.github.io).

## 🌟 Features

- **Automatic Repository Monitoring**: Tracks GitHub repository statistics (stars, forks, activity)
- **Content Synchronization**: Updates website with latest project information
- **Scheduled Updates**: Runs weekly via GitHub Actions
- **Manual Triggers**: On-demand updates when needed
- **Statistics Tracking**: Maintains up-to-date repository metrics

## 📁 Files Overview

| File | Description |
|------|-------------|
| `update_github_projects.py` | Main automation script for GitHub repository monitoring |
| `config.py` | Configuration settings for the automation system |
| `test_automation.py` | Test suite to validate automation functionality |
| `requirements.txt` | Python package dependencies |
| `README.md` | This documentation file |

## 🚀 Setup Instructions

### 1. Repository Configuration

The automation system is already configured in your repository with:
- GitHub Actions workflow in `.github/workflows/update-website.yml`
- Python scripts in `scripts/` directory
- Automatic permissions and token handling

### 2. GitHub Token (Automatic)

The system uses `GITHUB_TOKEN` which is automatically provided by GitHub Actions. No manual setup required.

### 3. Workflow Schedule

- **Automatic**: Runs every Monday at 6:00 AM UTC
- **Manual**: Can be triggered from GitHub Actions tab
- **Push**: Triggers when scripts are updated

## 🧪 Testing Locally

Before deployment, test the automation system:

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Set GitHub token (optional, for higher rate limits)
export GITHUB_TOKEN="your_github_token_here"

# Run test suite
cd scripts
python test_automation.py

# Test the main script
python update_github_projects.py
```

## 📊 What Gets Updated

### Repository Statistics Section
- Total stars across all repositories
- Total forks and community contributions
- Number of active repositories
- Primary programming languages
- Last update timestamp

### GitHub Profile Section
- Updated repository count
- Current star count
- Community impact metrics
- Development timeline

### Individual Project Metrics
- Star and fork counts
- Last update dates
- Technology stacks
- Repository activity

## 🔧 Configuration

### Repository Monitoring Settings

```python
MONITOR_SETTINGS = {
    "min_stars": 0,              # Minimum stars to include
    "exclude_forks": True,       # Skip forked repositories
    "max_repositories": 20,      # Maximum repos to process
    "primary_languages": [...]   # Languages to highlight
}
```

### Customizing Updates

Edit `config.py` to customize:
- Which repositories to monitor
- Emoji assignments for projects
- Update frequency and scope
- Commit message templates

## 📈 Monitoring and Logs

### GitHub Actions Dashboard
- View workflow runs in the "Actions" tab
- Check execution logs and summaries
- Monitor success/failure rates

### Workflow Status
- ✅ **Success**: Changes detected and committed
- ℹ️ **No Changes**: Repository data is current
- ❌ **Failure**: Check logs for error details

## 🔍 Troubleshooting

### Common Issues

1. **API Rate Limiting**
   - Solution: GitHub token is automatically provided
   - Backup: Workflow includes retry logic

2. **No Changes Detected**
   - Expected: Means repository data is current
   - Action: No action needed

3. **Workflow Failure**
   - Check: GitHub Actions logs for specific errors
   - Fix: Update scripts or configuration as needed

### Manual Recovery

If automation fails, manually run:

```bash
# Update repository data
python scripts/update_github_projects.py

# Commit changes
git add -A
git commit -m "🤖 Manual update: Repository data refresh"
git push origin main
```

## 🛡️ Security

- **GitHub Token**: Automatically managed by GitHub Actions
- **Permissions**: Minimal required permissions (contents: write)
- **Data**: Only public repository information is accessed
- **Privacy**: No sensitive data is stored or transmitted

## 🔄 Future Enhancements

Planned improvements:
- LinkedIn post integration
- Google Scholar publication updates
- Advanced project categorization
- Performance metrics tracking
- Multi-platform synchronization

## 📞 Support

If you encounter issues:
1. Check the GitHub Actions logs
2. Run the test suite locally
3. Review configuration settings
4. Update dependencies if needed

## 📝 License

This automation system is part of the personal website project and follows the same license terms.