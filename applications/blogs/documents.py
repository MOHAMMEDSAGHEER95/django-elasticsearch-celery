from django_elasticsearch_dsl import Index
from django_elasticsearch_dsl.documents import DocType
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import connections, Keyword, Text

from applications.blogs.models import Blog

content = Index('custom_blogs')
# See Elasticsearch Indices API reference for available settings
content.settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}


@content.doc_type
class ContentDocument(DocType):

    class Meta:
        model = Blog
        fields = ['title', 'body']

