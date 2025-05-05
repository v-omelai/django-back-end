## Installation

> [!NOTE]  
> Swagger UI will be available at http://127.0.0.1:8000/api/v1/schema/swagger-ui/

### Using Scripts

- `cd scripts`
- **Command Prompt or PowerShell**:`.\run.bat`
- **macOS or Linux Terminal**: `source run.sh`

### Manual Setup

- `sudo apt update`
- `sudo apt upgrade`
- `sudo apt install -y python3-venv python3-pip`
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python populate.py`
- `python manage.py runserver`

## Endpoints

### Posts

- GET `/posts`: Returns a paginated list of posts.
- GET `/posts/{id}`: Retrieves a single post by ID.
- POST `/posts`: Creates a new post.
- PUT `/posts/{id}`: Fully replaces an existing post.
- PATCH `/posts/{id}`: Partially updates an existing post.
- DELETE `/posts/{id}`: Deletes a post.

### Proxy

- GET `/proxy/posts`: Forwards request to the external API’s /posts endpoint, passing all query parameters.
- GET `/proxy/posts/{id}`: Fetches a specific post by ID from the external API.

## Notes

> [!NOTE]  
> See [OBJECTIVES.md](OBJECTIVES.md) for project goals and requirements.

### Technologies Used

- **Caching**: Django's in-memory cache for proxied responses (30 seconds TTL).
- **Rate Limiting**: Django REST Framework's default throttling (per IP).

### Possible improvements

- **Caching**: Switch Django’s cache backend to Redis for distributed caching.
- **Rate Limiting**: Use Redis-backed throttling.
- **Retry Logic**: Implement retry mechanisms.
- **Logging**: Add custom logging to monitor retries, failures, and response times.
- **Monitoring**: Integrate Datadog or Prometheus to track application performance, collect metrics, and set up
  real-time alerts for errors and performance issues.
- **API Key**: Add API authentication if the external API requires it.

## Commands

### Run

- `cd scripts`
- **Command Prompt or PowerShell**:`.\run.bat`
- **macOS or Linux Terminal**: `source run.sh`

### Initialize

- `cd scripts`
- **Command Prompt or PowerShell**:`.\initialize.bat`
- **macOS or Linux Terminal**: `source initialize.sh`

### Venv

- `python -m venv venv`
- **Command Prompt**: `.\venv\Scripts\activate`
- **PowerShell**: `.\venv\Scripts\Activate.ps1`
- **macOS or Linux Terminal**: `source venv/bin/activate`
- `deactivate`

### Pip

- `pip list`
- `pip freeze > requirements.txt`
- `pip install -r requirements.txt`
- `pip uninstall -r requirements.txt -y`

### Django

- `python populate.py`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`
