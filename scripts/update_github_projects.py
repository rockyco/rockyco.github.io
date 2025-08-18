#!/usr/bin/env python3
"""
GitHub Repository Monitor and Website Updater
Automatically updates repository statistics in projects.md
"""

import os
import re
import requests
from datetime import datetime
from typing import Dict, List

class GitHubProjectUpdater:
    def __init__(self, username: str = "rockyco"):
        self.username = username
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        if self.github_token:
            self.headers['Authorization'] = f'token {self.github_token}'
        self.api_base = 'https://api.github.com'
        
    def fetch_repositories(self) -> List[Dict]:
        """Fetch all public repositories for the user"""
        url = f"{self.api_base}/users/{self.username}/repos"
        params = {
            'type': 'public',
            'sort': 'updated',
            'per_page': 100
        }
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching repositories: {e}")
            return []
    
    def calculate_repository_stats(self, repositories: List[Dict]) -> Dict:
        """Calculate aggregate statistics from repositories"""
        # Filter out forks and count only meaningful repos
        non_fork_repos = [repo for repo in repositories if not repo.get('fork', False)]
        
        # Calculate totals
        total_stars = sum(repo['stargazers_count'] for repo in non_fork_repos)
        total_forks = sum(repo['forks_count'] for repo in non_fork_repos)
        
        # Count active repositories (with stars or recent updates)
        active_repos = []
        for repo in non_fork_repos:
            if repo['stargazers_count'] > 0:
                active_repos.append(repo)
            else:
                # Check if updated recently (within 90 days)
                try:
                    updated = datetime.fromisoformat(repo['updated_at'].replace('Z', '+00:00'))
                    ninety_days_ago = datetime.now().replace(tzinfo=updated.tzinfo) - timedelta(days=90)
                    if updated > ninety_days_ago:
                        active_repos.append(repo)
                except:
                    pass
        
        # Get language distribution
        languages = {}
        for repo in active_repos:
            lang = repo.get('language')
            if lang:
                languages[lang] = languages.get(lang, 0) + 1
        
        # Sort languages by frequency
        sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
        primary_languages = [lang[0] for lang in sorted_languages[:5]]
        
        return {
            'total_stars': total_stars,
            'total_forks': total_forks,
            'active_count': len(active_repos),
            'total_count': len(non_fork_repos),
            'primary_languages': primary_languages,
            'last_updated': datetime.now().strftime('%B %d, %Y')
        }
    
    def update_repository_statistics(self, stats: Dict) -> bool:
        """Update only the repository statistics in projects.md"""
        # Look for projects.md in parent directory when running from scripts folder
        projects_file = '../projects.md' if os.path.exists('../projects.md') else 'projects.md'
        
        if not os.path.exists(projects_file):
            print(f"Projects file {projects_file} not found")
            return False
            
        try:
            # Read current content
            with open(projects_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update Repository Statistics section
            stats_pattern = r'(## 📊 Repository Statistics\s*\n\n)(.*?)(\n\n##|\Z)'
            
            new_stats_content = f"""- **Total Stars**: {stats['total_stars']}+ across all repositories
- **Total Forks**: {stats['total_forks']}+ community contributions
- **Active Repositories**: {stats['active_count']} public projects
- **Primary Languages**: {', '.join(stats['primary_languages'])}
- **Last Updated**: {stats['last_updated']}"""
            
            if re.search(stats_pattern, content, re.DOTALL):
                # Replace existing stats
                def replace_stats(match):
                    return match.group(1) + new_stats_content + match.group(3)
                
                content = re.sub(stats_pattern, replace_stats, content, flags=re.DOTALL)
                print("✅ Updated Repository Statistics section")
            else:
                print("⚠️  Repository Statistics section not found")
            
            # Update GitHub Profile section
            profile_pattern = r'(## GitHub Profile\s*\n\n.*?)(\*\*Total Public Repositories\*\*: )(\d+)( active projects)'
            if re.search(profile_pattern, content, re.DOTALL):
                content = re.sub(
                    profile_pattern,
                    rf'\g<1>\g<2>{stats["active_count"]}\g<4>',
                    content,
                    flags=re.DOTALL
                )
                print("✅ Updated GitHub Profile repository count")
            
            # Update total stars in GitHub Profile
            profile_stars_pattern = r'(\*\*Community Impact\*\*: )(\d+)\+( total stars)'
            if re.search(profile_stars_pattern, content):
                content = re.sub(
                    profile_stars_pattern,
                    rf'\g<1>{stats["total_stars"]}+\g<3>',
                    content
                )
                print("✅ Updated GitHub Profile star count")
            
            # Write updated content
            with open(projects_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"\n📊 Summary of updates:")
            print(f"  - Total Stars: {stats['total_stars']}+")
            print(f"  - Total Forks: {stats['total_forks']}+")
            print(f"  - Active Repositories: {stats['active_count']}")
            print(f"  - Primary Languages: {', '.join(stats['primary_languages'])}")
            print(f"  - Last Updated: {stats['last_updated']}")
            
            return True
            
        except Exception as e:
            print(f"Error updating projects.md: {e}")
            return False
    
    def run(self) -> bool:
        """Main execution method"""
        print("🚀 Starting GitHub repository statistics update...")
        
        # Fetch repositories
        repositories = self.fetch_repositories()
        if not repositories:
            print("❌ No repositories found or API error")
            return False
        
        print(f"📦 Found {len(repositories)} repositories")
        
        # Calculate statistics
        stats = self.calculate_repository_stats(repositories)
        
        # Update only statistics in projects.md
        success = self.update_repository_statistics(stats)
        
        if success:
            print("\n✅ Repository statistics updated successfully")
        else:
            print("\n❌ Failed to update repository statistics")
            
        return success

def main():
    """Main function"""
    updater = GitHubProjectUpdater()
    return updater.run()

if __name__ == "__main__":
    # Import timedelta here since it's only needed for the stats calculation
    from datetime import timedelta
    success = main()
    exit(0 if success else 1)