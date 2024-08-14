import pytest

from src.article import Article


@pytest.fixture
def one_article():
    Article.articles = dict()
    return Article.insert('test', 'test')

@pytest.fixture
def two_arcticle():
    Article.articles = dict()
    Article.insert('test', 'test')
    return Article.insert('test', 'test')


def test_insert(one_article):
    """ Тест для проверки, что колличество статей равно 1"""
    assert len(Article.articles) == 1

def test_article_id(one_article):
    """ Тест для проверки установки ID  статьи """
    assert one_article.article_id ==1


def test_increase_id(two_arcticle):
    """ Тест для проверки увеличения  ID статьи """
    assert two_arcticle.article_id == 2

def test_increase_article_count(two_arcticle):
    """ Тест на увеличение списка статей """
    assert len(Article.articles) == 2
