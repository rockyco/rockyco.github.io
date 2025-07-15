#!/usr/bin/env python3
"""
GitHub Repository Monitor and Website Updater
Automatically fetches latest GitHub repository data and updates projects.md
"""

import os
import re
import json
import requests
from datetime import datetime
from typing import Dict, List, Optional

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
    
    def get_repository_stats(self, repo_name: str) -> Dict:
        """Get detailed repository statistics"""
        url = f"{self.api_base}/repos/{self.username}/{repo_name}"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            repo_data = response.json()
            
            # Get latest commits
            commits_url = f"{self.api_base}/repos/{self.username}/{repo_name}/commits"
            commits_response = requests.get(commits_url, headers=self.headers, params={'per_page': 5})
            recent_commits = commits_response.json() if commits_response.status_code == 200 else []
            
            # Get languages
            languages_url = f"{self.api_base}/repos/{self.username}/{repo_name}/languages"
            languages_response = requests.get(languages_url, headers=self.headers)
            languages = languages_response.json() if languages_response.status_code == 200 else {}
            
            return {
                'name': repo_data['name'],
                'description': repo_data.get('description', ''),
                'stars': repo_data['stargazers_count'],
                'forks': repo_data['forks_count'],
                'language': repo_data.get('language', 'Unknown'),
                'languages': languages,
                'url': repo_data['html_url'],
                'created_at': repo_data['created_at'],
                'updated_at': repo_data['updated_at'],
                'recent_commits': recent_commits,
                'topics': repo_data.get('topics', []),
                'size': repo_data['size']
            }
        except requests.RequestException as e:
            print(f"Error fetching repository stats for {repo_name}: {e}")
            return {}
    
    def format_project_section(self, repo_stats: Dict) -> str:
        """Format repository data for projects.md"""
        name = repo_stats['name']
        description = repo_stats.get('description', 'No description available')
        stars = repo_stats['stars']
        forks = repo_stats['forks']
        url = repo_stats['url']
        language = repo_stats.get('language', 'Unknown')
        updated = datetime.fromisoformat(repo_stats['updated_at'].replace('Z', '+00:00'))
        
        # Get primary emoji based on project type
        emoji_map = {
            'peakPicker': '🏆',
            'pulseDetector': '🚀', 
            'llm-fpga-design': '🔧',
            'ImageProcessing': '📊',
            'estFreqOffset': '📡',
            'LabTraining': '🎓'
        }
        emoji = emoji_map.get(name, '⚡')
        
        # Format the section
        section = f"""### {emoji} {name}
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)]({url}) | ⭐ {stars} stars | 🍴 {forks} forks

**{description}**

**Technologies:** {language}  
**Last Updated:** {updated.strftime('%B %Y')}

---
"""
        return section
        
    def update_projects_markdown(self, repositories: List[Dict]) -> bool:
        """Update the projects.md file with latest repository data"""
        projects_file = 'projects.md'
        
        if not os.path.exists(projects_file):
            print(f"Projects file {projects_file} not found")
            return False
            
        try:
            # Read current projects.md
            with open(projects_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Filter repositories (only public repos with stars > 0)
            filtered_repos = [repo for repo in repositories if repo['stars'] > 0 and not repo.get('fork', False)]
            
            # Sort by stars (descending)
            filtered_repos.sort(key=lambda x: x['stars'], reverse=True)
            
            # Generate repository stats section
            stats_section = "\n## 📊 Repository Statistics\n\n"
            total_stars = sum(repo['stars'] for repo in filtered_repos)
            total_forks = sum(repo['forks'] for repo in filtered_repos)
            languages = {}
            
            for repo in filtered_repos:
                lang = repo.get('language', 'Unknown')
                if lang and lang != 'Unknown':
                    languages[lang] = languages.get(lang, 0) + 1
            
            stats_section += f"- **Total Stars**: {total_stars}+ across all repositories\n"
            stats_section += f"- **Total Forks**: {total_forks}+ community contributions\n"
            stats_section += f"- **Active Repositories**: {len(filtered_repos)} public projects\n"
            stats_section += f"- **Primary Languages**: {', '.join(list(languages.keys())[:3])}\n"
            stats_section += f"- **Last Updated**: {datetime.now().strftime('%B %d, %Y')}\n\n"
            
            # Find GitHub Profile section and update stats
            github_profile_pattern = r'(## GitHub Profile.*?)(\n\n|\Z)'
            if re.search(github_profile_pattern, content, re.DOTALL):
                # Update existing GitHub Profile section
                updated_github_section = f"""## GitHub Profile

**Visit my complete GitHub profile**: [https://github.com/{self.username}](https://github.com/{self.username})

**Total Public Repositories**: {len(filtered_repos)} active projects  
**Focus Areas**: FPGA Design, LLM Integration, Signal Processing, Educational Resources  
**Community Impact**: {total_stars}+ total stars, active collaboration and knowledge sharing  
**Development Timeline**: 2+ years of systematic LLM-FPGA research and deployment"""
                
                content = re.sub(github_profile_pattern, updated_github_section, content, flags=re.DOTALL)
            
            # Add repository stats before GitHub Profile section if it doesn't exist
            if "Repository Statistics" not in content:
                github_profile_pos = content.find("## GitHub Profile")
                if github_profile_pos != -1:
                    content = content[:github_profile_pos] + stats_section + content[github_profile_pos:]
            
            # Write updated content
            with open(projects_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Updated {projects_file} with latest GitHub repository data")
            print(f"📊 Stats: {total_stars} stars, {total_forks} forks, {len(filtered_repos)} repositories")
            return True
            
        except Exception as e:
            print(f"Error updating projects.md: {e}")
            return False
    
    def run(self) -> bool:
        """Main execution method"""
        print("🚀 Starting GitHub repository monitoring...")
        
        # Fetch repositories
        repositories = self.fetch_repositories()
        if not repositories:
            print("❌ No repositories found or API error")
            return False
        
        print(f"📦 Found {len(repositories)} repositories")
        
        # Get detailed stats for each repository
        detailed_repos = []
        for repo in repositories:
            if not repo.get('fork', False):  # Skip forked repos
                stats = self.get_repository_stats(repo['name'])
                if stats:
                    detailed_repos.append(stats)
        
        # Update projects.md
        success = self.update_projects_markdown(detailed_repos)
        
        if success:
            print("✅ GitHub repository monitoring completed successfully")
        else:
            print("❌ GitHub repository monitoring failed")
            
        return success

def main():
    """Main function"""
    updater = GitHubProjectUpdater()
    return updater.run()

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)