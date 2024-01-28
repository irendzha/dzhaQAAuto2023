import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('dzhambovairyna_repo_not_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_blocked_users_requires_authentication(github_api):
    r = github_api.get_blocked_user('dzhambovairyna')
    assert r['message'] == 'Requires authentication'

@pytest.mark.api
def test_emoji_exists(github_api):
    r = github_api.get_emojis()
    assert 'angry' in r

@pytest.mark.api
def test_emoji_not_exists(github_api):
    r = github_api.get_emojis()
    assert 'haha' not in r

@pytest.mark.api
def test_emoji_has_correct_link(github_api):
    r = github_api.get_emojis()
    assert r['yum'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f60b.png?v8'