from flask_restplus import Namespace

from webservice.api.oslc.cm.rootservices import RootServices

cm_ns = Namespace(name='cm', description='Change Management', path='/cm')

cm_ns.add_resource(RootServices, '/rootservice')
