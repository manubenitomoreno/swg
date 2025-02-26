import markdown


def get_article_metadata(article: str) -> dict:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])
    md.convert(article)
    return md.Meta