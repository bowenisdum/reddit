import json


def test_recent_list_topics(app, db, test_topics):
    assert len(test_topics) == 10
    res = app.get('/home/recent')
    assert res.status_code == 200
    response_json = json.loads(res.data)
    sorted_response = sorted(response_json, key=lambda x: x['created_at'], reverse=True)
    assert response_json == sorted_response
    assert len(response_json) == len(test_topics)


def test_controversial_list_topics(app, db, test_topics, test_controversial_topics):
    assert len(test_topics) == 10
    res = app.get('/home/controversial')
    assert res.status_code == 200
    response_json = json.loads(res.data)
    sorted_response = sorted(response_json, key=lambda x: x['created_at'], reverse=True)
    assert response_json == sorted_response
    assert len(response_json) == len(test_controversial_topics)

def test_search_list_topics_success(app, db, test_topics, test_search_topics):
    res = app.get('/home/search', query_string={'search': "Test Topics"})
    assert res.status_code == 200
    response_json = json.loads(res.data)
    sorted_response = sorted(response_json, key=lambda x: x['created_at'], reverse=True)
    assert response_json == sorted_response
    assert len(response_json) == len(test_search_topics)

def test_search_list_topics_fail(app, db, test_topics, test_search_topics):
    res = app.get('/home/search', query_string={'search': "No test topic"})
    assert res.status_code == 200
    response_json = json.loads(res.data)
    sorted_response = sorted(response_json, key=lambda x: x['created_at'], reverse=True)
    assert response_json == sorted_response
    assert len(response_json) != test_search_topics