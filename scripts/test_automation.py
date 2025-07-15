#!/usr/bin/env python3
"""
Test script for GitHub automation system
Run this locally to test the automation before deploying
"""

import os
import sys
from update_github_projects import GitHubProjectUpdater

def test_github_api_access():
    """Test GitHub API access and authentication"""
    print("🔍 Testing GitHub API access...")
    
    # Check if GitHub token is available
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        print("⚠️  Warning: GITHUB_TOKEN not found in environment variables")
        print("   Public API will be used (rate limited)")
    else:
        print("✅ GitHub token found")
    
    # Test API connection
    updater = GitHubProjectUpdater()
    repos = updater.fetch_repositories()
    
    if repos:
        print(f"✅ Successfully fetched {len(repos)} repositories")
        return True
    else:
        print("❌ Failed to fetch repositories")
        return False

def test_repository_stats():
    """Test fetching detailed repository statistics"""
    print("\n📊 Testing repository statistics fetching...")
    
    updater = GitHubProjectUpdater()
    
    # Test with known repository
    test_repo = "peakPicker"
    stats = updater.get_repository_stats(test_repo)
    
    if stats:
        print(f"✅ Successfully fetched stats for {test_repo}")
        print(f"   Stars: {stats.get('stars', 0)}")
        print(f"   Forks: {stats.get('forks', 0)}")
        print(f"   Language: {stats.get('language', 'Unknown')}")
        return True
    else:
        print(f"❌ Failed to fetch stats for {test_repo}")
        return False

def test_projects_file_access():
    """Test access to projects.md file"""
    print("\n📄 Testing projects.md file access...")
    
    # Try current directory first, then parent directory
    projects_files = ["projects.md", "../projects.md"]
    
    for projects_file in projects_files:
        if os.path.exists(projects_file):
            print(f"✅ Found {projects_file}")
            
            # Test reading the file
            try:
                with open(projects_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                print(f"✅ Successfully read {len(content)} characters from {projects_file}")
                return True
            except Exception as e:
                print(f"❌ Error reading {projects_file}: {e}")
                return False
    
    print(f"❌ projects.md not found in current or parent directory")
    return False

def test_dry_run():
    """Perform a dry run of the automation system"""
    print("\n🚀 Performing dry run of automation system...")
    
    # Change to the correct directory (projects.md should be in parent directory)
    current_dir = os.getcwd()
    if current_dir.endswith('scripts'):
        os.chdir('..')
        print("📁 Changed to parent directory for projects.md access")
    
    updater = GitHubProjectUpdater()
    
    try:
        # Fetch repositories
        repositories = updater.fetch_repositories()
        if not repositories:
            print("❌ No repositories found")
            return False
        
        # Get detailed stats for a few repositories
        detailed_repos = []
        for repo in repositories[:3]:  # Test with first 3 repos
            if not repo.get('fork', False):
                stats = updater.get_repository_stats(repo['name'])
                if stats:
                    detailed_repos.append(stats)
        
        print(f"✅ Processed {len(detailed_repos)} repositories successfully")
        
        # Test updating projects.md (dry run - don't actually write)
        if os.path.exists('projects.md'):
            print("✅ Dry run completed successfully")
            return True
        else:
            print("❌ projects.md not found for dry run")
            return False
            
    except Exception as e:
        print(f"❌ Dry run failed: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 GitHub Automation System Test Suite")
    print("=" * 50)
    
    tests = [
        ("GitHub API Access", test_github_api_access),
        ("Repository Statistics", test_repository_stats),
        ("Projects File Access", test_projects_file_access),
        ("Dry Run", test_dry_run)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 Test Results Summary:")
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! Automation system is ready to deploy.")
        return True
    else:
        print("⚠️  Some tests failed. Please fix issues before deploying.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)