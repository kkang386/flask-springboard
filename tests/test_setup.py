# just run pytest
import pytest
import json

from project import app, db
from project.models import User, VideoModel

def test_db_create(setup_test_db):

    video = VideoModel(name="test name", views=101, likes=202)
    db.session.add(video)
    db.session.commit()
    result = VideoModel.query.filter_by(id = 1).first()

    assert result.name == 'test name'
    assert result.views == 101
    assert result.likes == 202
