from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def core_skill_areas():
    return [
        {
            "title": "Machine Learning & Modeling",
            "skills": [
                "Python",
                "PyTorch",
                "scikit-learn",
                "LightGBM",
                "feature engineering",
                "gradient boosting",
                "regression",
                "classification",
                "clustering",
                "metric learning",
                "embeddings",
                "fastText",
                "sentence-transformers",
                "active learning",
                "AutoML",
                "Optuna",
                "calibration",
                "model evaluation",
            ],
        },
        {
            "title": "Production ML & MLOps",
            "skills": [
                "MLOps",
                "model deployment",
                "model monitoring",
                "scheduled retraining",
                "validation gates",
                "fallback strategy",
                "model versioning",
                "CI/CD",
                "GitLab CI",
                "automated testing",
                "Docker",
                "FastAPI",
                "PostgreSQL",
                "ClickHouse",
                "SQL",
                "pytest",
            ],
        },
        {
            "title": "Search, Matching & Ranking",
            "skills": [
                "product matching",
                "duplicate detection",
                "information retrieval",
                "semantic search",
                "similarity search",
                "vector search",
                "candidate generation",
                "approximate nearest neighbor search",
                "reranking",
                "pairwise features",
                "fuzzy matching",
                "FAISS",
                "Elasticsearch",
                "ranking metrics",
                "precision-recall analysis",
            ],
        },
        {
            "title": "LLM / RAG & AI Data Workflows",
            "skills": [
                "Large Language Models (LLMs)",
                "Retrieval-Augmented Generation (RAG)",
                "OpenAI API",
                "Google Vertex AI",
                "prompt engineering",
                "structured extraction",
                "JSON schema",
                "tool calling",
                "LLM evaluation",
                "embedding-based retrieval",
                "automated data labeling",
                "human-in-the-loop workflows",
            ],
        },
        {
            "title": "Anomaly Detection, Pricing & Forecasting",
            "skills": [
                "anomaly detection",
                "price anomaly detection",
                "anomaly scoring",
                "price regression",
                "uncertainty estimation",
                "confidence scoring",
                "quantile regression",
                "calibration",
                "forecasting",
                "delivery time forecasting",
                "time-aware validation",
                "temporal features",
            ],
        },
        {
            "title": "Data Engineering & Analytics",
            "skills": [
                "Pandas",
                "NumPy",
                "Parquet",
                "batching",
                "sharding",
                "in-database computation",
                "scheduled pipelines",
                "Celery",
                "Apache Superset",
                "Power BI",
                "data quality analysis",
            ],
        },
        {
            "title": "Software Engineering & Observability",
            "skills": [
                "backend engineering",
                "Python application architecture",
                "API design",
                "REST APIs",
                "system integration",
                "Pydantic",
                "type hints",
                "mypy",
                "testing",
                "code review",
                "Sentry",
                "Grafana",
                "C++",
                "Ruby on Rails",
            ],
        },
        {
            "title": "Technical Ownership & Delivery",
            "skills": [
                "requirements clarification",
                "metric definition",
                "ML pipeline architecture",
                "technical decision-making",
                "stakeholder communication",
                "business trade-off analysis",
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
