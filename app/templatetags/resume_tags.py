from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def core_skill_areas():
    return [
        {
            "title": "Machine Learning & Modeling",
            "skills": [
                "Python",
                "machine learning algorithms",
                "statistics",
                "PyTorch",
                "scikit-learn",
                "LightGBM",
                "feature engineering",
                "gradient boosting",
                "regression",
                "classification",
                "clustering",
                "neural networks",
                "Natural Language Processing (NLP)",
                "embeddings",
                "fastText",
                "sentence-transformers",
                "metric learning",
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
                "data quality control",
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
                "prompt engineering",
                "structured extraction",
                "JSON schema",
                "tool calling",
                "embedding-based retrieval",
                "automated data labeling",
                "human-in-the-loop workflows",
                "LLM evaluation",
                "OpenAI API",
                "Google Vertex AI",
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
                "calibration",
                "quantile regression",
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
                "scheduled pipelines",
                "Celery",
                "batching",
                "sharding",
                "in-database computation",
                "Apache Superset",
                "Power BI",
                "data quality analysis",
            ],
        },
        {
            "title": "Software Engineering & Observability",
            "skills": [
                "programming",
                "backend engineering",
                "Python application architecture",
                "computer science fundamentals",
                "API design",
                "REST APIs",
                "system integration",
                "Pydantic",
                "type hints",
                "mypy",
                "automated testing",
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
                "scalable solution design",
                "business trade-off analysis",
                "stakeholder communication",
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
