# db_practice API 사용법

1. git clone을 한다

2. 터미널을 열고 poetry install을 한다.
(만약 poetry가 안깔려있다면, pip install -r requirements.txt를 통해 필요 라이브러리들을 깔도록 한다.)

3. poetry shell 이나 가상환경 실행.

4. uvicorn main:app --reload를 해서 실행한다.

5. http://127.0.0.1:8000/docs에 들아가서 swagger를 확인한다.
