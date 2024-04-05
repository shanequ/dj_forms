from django.contrib import admin

from django.urls import path


class DjFormAdmin(admin.AdminSite):
    site_header = 'DjForm Admin'
    logout_template = 'admin/logout.html'

    def get_app_list(self, request, **kwargs):
        # Customize ordering of apps and models.
        # 
        # The default ordering is alphabetical order. Without ordering,
        # the order is based on the order of definitions.
        
        # app_dict format: {
        #     'app_label': {
        #         'name': 'app_name',
        #         'models': [
        #             {''model', xxx, 'name': xxx, 'object_name' xxx, ...},
        #             ...
        #         ]
        #     },
        #     ...
        # }
        #     note: 'app_label' will not be returned.
        #
        app_dict = self._build_app_dict(request)
        if not app_dict:
            # when logout, the app_list can be empty
            return []

        # shorten the name of Django auth app
        app_dict['auth']['name'] = 'Django Auth'
        return [app_dict['accounts'], app_dict['auth']]

    def get_urls(self):
        base_urls = super().get_urls()

        # define URL patterns for custom views
        urlpatterns = [
            path('sys_health/', self.system_health_dashboard, name='sys_health'),
        ]
        return urlpatterns + base_urls

    ###########################
    # additional custom views
    ###########################
    def system_health_dashboard(self, request):

        # set current_app to prevent error in render_to_response
        # when using RequestContext.current_app
        request.current_app = self.name

        # create a context for rendering template
        context = self.each_context(request)
        context['some_var'] = 'some additional variable'

        # can render a template and return.
        return self.index(request)
