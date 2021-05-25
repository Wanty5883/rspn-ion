# TPL - Third Party Libraries
from flask import Flask
from flask import request
from flask_restful import Api
from flask_restful import reqparse
from flask_restful import Resource
# LPL - Local Python Libraries
from lib.core.enums import API


def apiServer():
    # global app  # Might not be used
    app = Flask(API.SERVER_NAME)
    api = Api(app)

    api.add_resource(Weapon, "/weapon")

    app.run(host="localhost", port=API.SERVER_PORT, debug=True)

    # TODO doesn't work, would be nice to find another way
    @app.route("/shutdown", methods=["POST"])
    def serverShutdown():
        shutdown = request.environ.get("{0}.server.shutdown".format(API.SERVER_NAME))
        if shutdown is None:
            raise RuntimeError("The server {0} is not running".format(API.SERVER_NAME))
        else:
            shutdown()


def wpnArgs():
    args = reqparse.RequestParser()
    # Mandaroty arguments
    args.add_argument("rootDirectory", type=str, help="Set the extracted VPK directory", required=True)
    # Function arguments
    args.add_argument("wpnConvertMDL", type=bool, help="Convert a weapon mdl to a defined version")
    args.add_argument("wpnHashMDL", type=bool, help="Hash a weapon model file")
    # General arguments
    args.add_argument("wpnFileType", type=str, help="Choose the 3D model file type (1P, 3P, etc.)")
    args.add_argument("wpnFileVersion", type=str, help="Choose the 3D model file version")
    args.add_argument("wpnFileTarget", type=str, help="Choose the 3D model target file")
    args.add_argument("wpnStructTarget", type=str, help="Choose the 3D model struct target")
    return(args.parse_args())


class Weapon(Resource):
    def get(self):
        pass

    def post(self):
        args = wpnArgs()
        return({"data": args})
