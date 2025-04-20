import requests

def remix(project_id, bearer_token):
  url = f"https://api.lovable.dev/projects/{project_id}/remix"
  payload = {
    "include_history": "false", # you can only include project history if Lovable has given you authorization, otherwise you will get a 403 error
  }
  headers = {
      "Authorization": f"Bearer {bearer_token}",
      "Content-Type": "application/json"
  }
  return requests.post(url, json=payload, headers=headers)


if __name__ == "__main__":
    project_id = input("Enter project id: ")
    bearer = input("Enter your bearer token: ")
    result = remix(project_id, bearer)
        
    print(result.status_code)
    print(result.json())