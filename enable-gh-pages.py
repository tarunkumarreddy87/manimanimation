import requests
import os

# GitHub repository details
owner = "tarunkumarreddy87"
repo = "manimanimation"

# You'll need to create a personal access token and set it as an environment variable
# Go to GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)
# Create a new token with 'public_repo' scope and set it as GITHUB_TOKEN environment variable
token = os.environ.get('GITHUB_TOKEN')

if not token:
    print("Please set your GITHUB_TOKEN environment variable")
    exit(1)

# GitHub API URL for enabling GitHub Pages
url = f"https://api.github.com/repos/{owner}/{repo}/pages"

# Headers for the request
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Data to enable GitHub Pages
data = {
    "source": {
        "branch": "main"
    }
}

# Make the request to enable GitHub Pages
response = requests.put(url, headers=headers, json=data)

if response.status_code == 204:
    print("GitHub Pages enabled successfully!")
    print("Your site will be available at: https://tarunkumarreddy87.github.io/manimanimation")
elif response.status_code == 409:
    print("GitHub Pages is already enabled for this repository")
    print("Your site should be available at: https://tarunkumarreddy87.github.io/manimanimation")
else:
    print(f"Failed to enable GitHub Pages. Status code: {response.status_code}")
    print(f"Response: {response.text}")