from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def core_skill_areas():
    return [
        {
            "title": "Machine Learning",
            "skills": [
                "Python",
                "PyTorch",
                "LightGBM",
                "scikit-learn",
                "gradient boosting",
                "NLP",
                "embeddings",
                "fastText",
                "metric learning",
                "active learning",
                "anomaly detection",
                "forecasting",
                "uncertainty estimation",
                "model evaluation",
            ],
        },
        {
            "title": "Search, Matching & Ranking",
            "skills": [
                "information retrieval",
                "semantic search",
                "vector search",
                "candidate generation",
                "reranking",
                "product matching",
                "duplicate detection",
                "Elasticsearch",
                "FAISS",
            ],
        },
        {
            "title": "LLM & RAG",
            "skills": [
                "Large Language Models (LLMs)",
                "Retrieval-Augmented Generation (RAG)",
                "agent workflows",
                "tool calling",
                "MCP",
                "structured output",
                "prompt engineering",
                "LLM evaluation",
                "guardrails",
                "human-in-the-loop",
                "OpenAI API",
                "Claude Code",
            ],
        },
        {
            "title": "Production & Engineering",
            "skills": [
                "FastAPI",
                "Docker",
                "Kubernetes",
                "Google Cloud Platform (GCP)",
                "CI/CD",
                "model deployment",
                "model monitoring",
                "scheduled retraining",
                "Airflow",
                "PostgreSQL",
                "ClickHouse",
                "SQL",
                "Pandas",
                "Sentry",
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
