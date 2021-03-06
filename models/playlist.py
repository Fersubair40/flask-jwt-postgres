from db import db
import datetime
from sqlalchemy import func


class PlaylistModel(db.Model):
    __tablename__ = 'playlist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, created_at):
        self.name = name
        self.created_at = created_at

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def commit_db(self):
        db.session.commit()

    def delete_from_db(self, id):
        db.session.delete(id)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, playlist_name):
        return cls.query.filter(func.lower(PlaylistModel.name) == playlist_name.lower()).all()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'playlist_id': x.id,
                'playlist_name': x.name,
                'created_at': x.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }

        return {'Playlists': list(map(lambda x: to_json(x), PlaylistModel.query.all()))}

    @classmethod
    def return_two_records(cls):
        def to_json(x):
            return {
                'playlist_id': x.id,
                'playlist_name': x.name,
                'created_at': x.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }

        return {'message': 'More Data can be display if you enter access_token.',
                'Playlists': list(map(lambda x: to_json(x), PlaylistModel.query.limit(2).all()))}

    def json(self):
        return {
            'data': {
                'playlist_id': self.id,
                'playlist_name': self.name,
                'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }
        }

    @classmethod
    def is_data_present(cls):
        return cls.query.first()

