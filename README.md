# Research Assistant

This project implements a custom agent that searches the web for information based on user input, summarizes relevant documents, and returns the results.

## Features

- Collects links to relevant documents through Google search.
- Retrieves the content of the collected documents.
- Summarizes the content of the documents and returns it to the user.
- Saves the summarized results to a file.

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Installing Dependencies

Use the following command to install the required packages:

```bash
pip install -r requirements.txt

.
├── research_agent.ipynb  # 메인 코드 파일
├── requirements.txt      # 필요한 패키지 목록
└── README.md             # 프로젝트 설명 파일
```

#### 요약에 사용된 모델

1. Llama 3.1
2. GPT-4o-mini
