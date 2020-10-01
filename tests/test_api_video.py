# just run pytest
import os
import pytest
import json
import csv
import sys

from project import app, db
from project.models import VideoModel

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files',
    )

def test_db_create(setup_test_db):
    print ("test user creation")
    # load test video data from file
    file_name = os.path.join(FIXTURE_DIR, 'videos.csv')
    with open(file_name, newline="\n") as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='"')
        idx = 0
        for row in rows:
            if idx > 0:
                video = VideoModel(name=row[1], views=row[2], likes=row[3])
                db.session.add(video)
            idx += 1

        db.session.commit()

    result = VideoModel.query.filter_by(id = 1).first()

    assert result.name == 'The Force Awakens'
    assert result.views == 100000
    assert result.likes == 99999

def test_get_video_success():
    client = app.test_client()
    url = '/video/1'

    response = client.get(url)
    result = json.loads(response.get_data())
    # sys.stderr.write(f"response content: {result}")
    assert response.status_code == 200
    assert result['name'] == 'The Force Awakens'


