FROM python:3

WORKDIR /usr/src/app

RUN python3 -m venv .venv

RUN pip install 'fastapi[all]' 'pymongo[srv]' python-dotenv

RUN adduser --system --no-create-home nonroot

USER nonroot

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]