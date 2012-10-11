
# from reversion.revisions import revision_context_manager

# REVISION_MIDDLEWARE_FLAG = "reversion.revision_middleware_active"


class CustomMiddleware(object):
    
    # """Wraps the entire request in a revision."""
    
    def process_request(self, request):
        print "process_request"
        print request.POST
        print request.GET
        print request.session.keys()
        print "\n\n"
        # """Starts a new revision."""
        # request.META[(REVISION_MIDDLEWARE_FLAG, self)] = True
        # revision_context_manager.start()
        # if hasattr(request, "user") and request.user.is_authenticated():
        #     revision_context_manager.set_user(request.user)
    
    # def _close_revision(self, request):
    #     """Closes the revision."""
    #     if request.META.get((REVISION_MIDDLEWARE_FLAG, self), False):
    #         del request.META[(REVISION_MIDDLEWARE_FLAG, self)]
    #         revision_context_manager.end()
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print "process_view"       
        print request.POST
        print request.GET
        print request.session.keys()
        print "\n\n"
        # print view_func.func_name
        # print view_func.func_dict
        # print view_func.func_globals
        # print view_func.func_code
        # print view_func.func_closure
        # print view_func.func_doc
        # print view_func.func_defaults
        # print view_args
        # print view_kwargs
        return None
        

    def process_response(self, request, response):
        print "process_response"
        print request.POST
        print request.GET
        print request.session.keys()
        print "\n\n"
        # print self
        # print request
        # print response
        # """Closes the revision."""
        # self._close_revision(request)
        return response
        
    # def process_exception(self, request, exception):
    #     """Closes the revision."""
    #     revision_context_manager.invalidate()    
    #     self._close_revision(request)