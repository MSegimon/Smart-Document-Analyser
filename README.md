# Smart-Document-Analyser

### API/Module for Text NLP Analysis
- spaCy
- OpenAI

#### Requirements of NLP Analysis
- Sentiment Analysis
    - Per Sentence
    - Per Paragraph
    - Per Document
- Keyword Extraction
- Summarization

### API/Module for Secure File Uploader/Ingester
- Filestack
- Build my own in flask
- Web Scrapper

#### Requirements of file uploader
- File Upload
    - File Clean
- File Delete
- File Read

## API Calls
### Hello World
```bash
curl -X GET "http://127.0.0.1:8000/"
```

### User
#### Create User
```bash
curl -X POST "http://127.0.0.1:8000/user" -H "Content-Type: application/json" -d "{\"username\":\"person\", \"password\":\"password\", \"email\":\"email@mail.com\"}"
```

#### Get User by ID
```bash
curl -X GET "http://127.0.0.1:8000/user?id=2"
````

#### Get User by Username
```bash
curl -X GET "http://127.0.0.1:8000/user?username=person"
```

#### Delete User
```bash
curl -X POST "http://127.0.0.1:8000/delete_user?id=4"
```