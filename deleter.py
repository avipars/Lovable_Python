import requests

def deleter(project_id, bearer_token):
  url = f"https://api.lovable.dev/projects/{project_id}"

  headers = {
      "Authorization": f"Bearer {bearer_token}",
      "Content-Type": "application/json"
  }
  return requests.delete(url, headers=headers) # If you do not own the project, expect to get a 401 error


if __name__ == "__main__":
    project_id = input("Enter project id: ")
    bearer = input("Enter your bearer token: ")

    result = deleter(project_id, bearer) # will delete your Lovable project
        
    print(result.status_code)
    print(result.json())