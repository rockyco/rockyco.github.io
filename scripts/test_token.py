#!/usr/bin/env python3
"""
Quick GitHub token test script
"""

import os
import requests

def test_github_token():
    """Test GitHub token functionality"""
    print("🔍 Testing GitHub Token Access...")
    
    # Get token from environment
    token = os.environ.get('GITHUB_TOKEN')
    
    if not token:
        print("❌ GITHUB_TOKEN not found in environment variables")
        print("💡 Set it with: export GITHUB_TOKEN='your_token_here'")
        return False
    
    print(f"✅ Token found - Length: {len(token)} characters")
    print(f"✅ Token prefix: {token[:4]}...")
    
    # Test API access
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    try:
        # Test authenticated user endpoint
        print("\n🔐 Testing authenticated access...")
        auth_response = requests.get('https://api.github.com/user', headers=headers)
        
        if auth_response.status_code == 200:
            user_data = auth_response.json()
            print(f"✅ Authenticated as: {user_data.get('login', 'Unknown')}")
            print(f"✅ Account type: {user_data.get('type', 'Unknown')}")
            
            # Check rate limits
            rate_limit = auth_response.headers.get('X-RateLimit-Limit', 'Unknown')
            rate_remaining = auth_response.headers.get('X-RateLimit-Remaining', 'Unknown')
            print(f"✅ Rate limit: {rate_remaining}/{rate_limit} remaining")
            
        else:
            print(f"❌ Authentication failed: {auth_response.status_code}")
            print(f"Error: {auth_response.text}")
            return False
        
        # Test repository access
        print("\n📦 Testing repository access...")
        repos_response = requests.get('https://api.github.com/user/repos', headers=headers, params={'per_page': 5})
        
        if repos_response.status_code == 200:
            repos = repos_response.json()
            print(f"✅ Can access {len(repos)} repositories (showing first 5)")
            
            for repo in repos[:3]:
                print(f"   📁 {repo['name']} - ⭐ {repo['stargazers_count']} stars")
                
        else:
            print(f"❌ Repository access failed: {repos_response.status_code}")
            return False
            
        # Test specific repository access
        print("\n🏆 Testing specific repository access...")
        peak_response = requests.get('https://api.github.com/repos/rockyco/peakPicker', headers=headers)
        
        if peak_response.status_code == 200:
            repo_data = peak_response.json()
            print(f"✅ peakPicker access successful")
            print(f"   ⭐ Stars: {repo_data['stargazers_count']}")
            print(f"   🍴 Forks: {repo_data['forks_count']}")
            print(f"   📝 Language: {repo_data.get('language', 'Unknown')}")
        else:
            print(f"❌ peakPicker access failed: {peak_response.status_code}")
            
        print("\n🎉 GitHub token test completed successfully!")
        print("🚀 Your automation system should work perfectly!")
        return True
        
    except requests.RequestException as e:
        print(f"❌ Network error: {e}")
        return False

if __name__ == "__main__":
    success = test_github_token()
    exit(0 if success else 1)