# 첫 번째 단계: 빌드 환경, 경량화된 파이썬
FROM python:3.11-slim AS builder

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사 (필요한 파일만 복사), 지금 디렉토리 다 /app으로
COPY . .

# 두 번째 단계: 최종 이미지
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    gcc \
    pkg-config \
    libmariadb-dev \
    libmariadb3 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# 빌드 단계에서 설치된 패키지 복사
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# 프로젝트 파일 복사 (필요한 파일만 복사)
COPY --from=builder /app /app

# 불필요한 파일 제거
RUN rm -rf /app/tests /app/docs

# 환경 변수 설정
ENV DJANGO_SETTINGS_MODULE=fisa_django.settings
ENV PYTHONUNBUFFERED=1

# # Gunicorn을 사용하여 애플리케이션 실행
# docker-compose up 파일이랑 둘 중 하나에만 있으면 됨
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fisa_django.wsgi:application"]


# 서버 실행
