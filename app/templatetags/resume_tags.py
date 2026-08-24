from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def core_skill_areas():
    return [
        {
            "title": "Machine Learning & Modeling",
            "skills": [
                "Python",
                "statistics",
                "machine learning algorithms",
                "PyTorch",
                "scikit-learn",
                "LightGBM",
                "gradient boosting",
                "feature engineering",
                "hyperparameter tuning",
                "regression",
                "classification",
                "clustering",
                "neural networks",
                "model evaluation",
                "Natural Language Processing (NLP)",
                "OCR",
                "embeddings",
                "fastText",
                "sentence-transformers",
                "metric learning",
                "active learning",
                "recommender systems",
                "AutoML",
                "Optuna",
            ],
        },
        {
            "title": "Production ML & MLOps",
            "skills": [
                "MLOps",
                "model deployment",
                "model monitoring",
                "scheduled retraining",
                "model versioning",
                "guardrail metrics",
                "CI/CD",
                "GitLab CI",
                "automated testing",
                "pytest",
                "Docker",
                "FastAPI",
                "Google Cloud Platform (GCP)",
                "PostgreSQL",
                "ClickHouse",
                "SQL",
            ],
        },
        {
            "title": "Search, Matching & Ranking",
            "skills": [
                "product matching",
                "duplicate detection",
                "e-commerce search/catalog",
                "information retrieval",
                "semantic search",
                "similarity search",
                "vector search",
                "vector database",
                "candidate generation",
                "approximate nearest neighbor search",
                "reranking",
                "fuzzy matching",
                "FAISS",
                "Elasticsearch",
            ],
        },
        {
            "title": "LLM, Agents & RAG",
            "skills": [
                "Large Language Models (LLMs)",
                "Retrieval-Augmented Generation (RAG)",
                "AI agents",
                "agentic architecture",
                "agent orchestration",
                "multi-agent systems",
                "prompt engineering",
                "structured output",
                "structured extraction",
                "tool calling",
                "Model Context Protocol (MCP)",
                "context management",
                "Claude API",
                "Claude Code",
                "Claude Agent SDK",
                "OpenAI API",
                "Google Vertex AI",
                "LLM evaluation",
                "automated data labeling",
                "human-in-the-loop workflows",
            ],
        },
        {
            "title": "Anomaly Detection, Pricing & Forecasting",
            "skills": [
                "anomaly detection",
                "price anomaly detection",
                "price regression",
                "uncertainty estimation",
                "confidence scoring",
                "calibration",
                "quantile regression",
                "forecasting",
                "delivery time forecasting",
            ],
        },
        {
            "title": "Data Engineering & Analytics",
            "skills": [
                "Pandas",
                "NumPy",
                "Parquet",
                "scheduled pipelines",
                "Celery",
                "sharding",
                "Apache Superset",
                "data quality analysis",
            ],
        },
        {
            "title": "Software Engineering & Observability",
            "skills": [
                "programming",
                "backend engineering",
                "Python application architecture",
                "API design",
                "REST APIs",
                "system integration",
                "Pydantic",
                "mypy",
                "code review",
                "Sentry",
                "Grafana",
            ],
        },
    ]


@register.inclusion_tag("app/includes/core_skill_areas.html")
def output_core_skill_areas():
    return {"areas": core_skill_areas()}


@register.simple_tag
def black_link(url, text=None):
    if text is None:
        text = url
    return mark_safe(f'<a target="_blank" class="resume-link" href="{url}">{text}</a>')
