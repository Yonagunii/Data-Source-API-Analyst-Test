# GitHub API Documentation

## Endpoints Used
| Endpoint                     | Description                          |
|------------------------------|--------------------------------------|
| `GET /search/repositories`   | Search public repositories.          |
| `GET /repos/{owner}/{repo}/commits` | List commits.               |
| `GET /repos/{owner}/{repo}/contents/{path}` | Get file contents. |

## Authentication
- Requires a personal access token with `repo` and `public_repo` scopes.
