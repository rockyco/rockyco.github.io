# Private Repository Setup Guide

This guide explains how to include private repositories in your website's auto-update process.

## Overview

By default, the GitHub auto-update script only fetches public repositories. This is because:
1. The default GitHub Actions token (`GITHUB_TOKEN`) only has access to public repos
2. Private repositories may contain sensitive information not meant for public display

## Enabling Private Repository Access

### Step 1: Create a Personal Access Token (PAT)

1. Go to GitHub Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name like "Website Auto-Update"
4. Select the following scopes:
   - `repo` (Full control of private repositories)
   - `read:user` (Read user profile data)
5. Set an expiration date (recommend 90 days for security)
6. Click "Generate token" and copy the token immediately

### Step 2: Add the PAT to GitHub Secrets

1. Go to your repository settings
2. Navigate to Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `PERSONAL_ACCESS_TOKEN`
5. Value: Paste your PAT from Step 1
6. Click "Add secret"

### Step 3: Update the GitHub Actions Workflow

Edit `.github/workflows/update-website.yml` to use the PAT:

```yaml
- name: 🚀 Update GitHub Repository Data
  run: |
    echo "Starting GitHub repository data update..."
    cd scripts
    python update_github_projects.py --include-private
  env:
    GITHUB_TOKEN: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
```

## Security Considerations

⚠️ **WARNING**: Including private repositories on a public website has security implications:

1. **Repository Names**: Private repo names will be visible
2. **Descriptions**: Any descriptions will be public
3. **Statistics**: Stars, forks, and update times will be shown
4. **URLs**: Direct links to repositories (though they'll still require authentication)

### Best Practices

1. **Review Private Repos**: Before enabling, review all your private repositories
2. **Update Descriptions**: Ensure private repo descriptions don't contain sensitive info
3. **Use Separate PAT**: Don't reuse PATs from other applications
4. **Rotate Regularly**: Set expiration dates and rotate tokens periodically
5. **Monitor Usage**: Check GitHub's security log for PAT usage

## Testing Locally

To test private repository access locally:

```bash
# Set your PAT as an environment variable
export GITHUB_TOKEN="your_personal_access_token_here"

# Run with private repos included
python scripts/update_github_projects.py --include-private

# Run without private repos (default)
python scripts/update_github_projects.py
```

## Visual Indicators

Private repositories will be marked with a 🔒 lock icon in the repository list to indicate they're private.

## Excluding Specific Repositories

If you want more fine-grained control, you can modify the script to exclude specific repositories by name. Edit `update_github_projects.py` and add an exclusion list:

```python
# Add to the filter logic
excluded_repos = ['sensitive-project', 'client-work']
if repo['name'] in excluded_repos:
    continue
```

## Troubleshooting

1. **No private repos showing**: Ensure your PAT has the `repo` scope
2. **Authentication errors**: Check that the secret name matches in the workflow
3. **Rate limits**: PATs have higher rate limits than the default token

## Reverting Changes

To stop including private repositories:
1. Remove `--include-private` from the workflow
2. Optionally, delete the PAT from GitHub secrets
3. The next auto-update will only include public repositories