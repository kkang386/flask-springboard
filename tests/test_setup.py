# just run pytest
import os
import pytest
import json

from project import app, db
from project.models import User, VideoModel

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files',
    )

@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'users.csv'),
    os.path.join(FIXTURE_DIR, 'videos.csv'),
    )
def test_datafile_reads(setup_test_db, datafiles):
    for file_name in datafiles.listdir():
        print("\n file_name: ", file_name)
    pass


def test_db_create(setup_test_db):
    print ("test user creation")
    video = VideoModel(name="test name", views=101, likes=202)
    db.session.add(video)
    db.session.commit()
    result = VideoModel.query.filter_by(id = 1).first()

    assert result.name == 'test name'
    assert result.views == 101
    assert result.likes == 202


