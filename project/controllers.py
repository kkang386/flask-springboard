from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from project.models import User, VideoModel
from project import db, app_cache
import sys

# make new request parser object
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required = True)
video_put_args.add_argument("views", type=str, help="Views of the video is required", required = True)
video_put_args.add_argument("likes", type=str, help="Likes on the video")

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=str, help="Views of the video is required")
video_update_args.add_argument("likes", type=str, help="Likes on the video")


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# create a resource
class Video (Resource):
    @marshal_with(resource_fields) # decorator will help serialize the data to json
    def get(self, video_id):
        cache_key = f"video_id:{video_id}"
        cached_res = app_cache.get(cache_key)
        if cached_res is not None:
            #sys.stderr.write(f"found cache\n")
            return cached_res

        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message=f"Video id {video_id} don't exist.")

        #sys.stderr.write(f"new cache object created\n")
        app_cache.set(cache_key, result)
        return result

    @marshal_with(resource_fields) # decorator will help serialize the data to json
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(name = args['name']).first()
        if result:
            abort(409, message=f"Video id {result.id} '{args['name']}' already exists.")

        video = VideoModel(name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video , 201

    @marshal_with(resource_fields) # decorator will help serialize the data to json
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if not result:
            abort(404, message=f"Video id {video_id} doesn't exists.")
        
        if args["name"]:
            result.name = args['name']
        if args["likes"]:
            result.likes = args['likes']
        if args["views"]:
            result.views = args['views']

        db.session.commit()
        return result

    def delete(self, video_id):
        abort_if_video_id_doesnt_exists(video_id)
        del videos[video_id]
        return '', 204 # 204 means deleted successfully


