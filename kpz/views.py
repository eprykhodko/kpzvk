from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from annoying.decorators import render_to
from django.template import RequestContext


import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login

from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from social.apps.django_app.utils import psa


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('/', context_instance=RequestContext(request))


# def context(**extra):
#     return dict({
#         'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
#         'plus_scope': ' '.join(GooglePlusAuth.DEFAULT_SCOPE),
#         'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
#     }, **extra)
#
#
# @render_to('index.html')
# def home(request):
#     """Home view, displays login mechanism"""
#     if request.user.is_authenticated():
#         return redirect('done')
#     return context()
#
#
# @login_required
# @render_to('index.html')
# def done(request):
#     """Login complete view, displays user data"""
#     return context()
#
#
# @render_to('index.html')
# def validation_sent(request):
#     return context(
#         validation_sent=True,
#         email=request.session.get('email_validation_address')
#     )
#
#
# @render_to('index.html')
# def require_email(request):
#     backend = request.session['partial_pipeline']['backend']
#     return context(email_required=True, backend=backend)
#
#
# @psa('social:complete')
# def ajax_auth(request, backend):
#     if isinstance(request.backend, BaseOAuth1):
#         token = {
#             'oauth_token': request.REQUEST.get('access_token'),
#             'oauth_token_secret': request.REQUEST.get('access_token_secret'),
#         }
#     elif isinstance(request.backend, BaseOAuth2):
#         token = request.REQUEST.get('access_token')
#     else:
#         raise HttpResponseBadRequest('Wrong backend type')
#     user = request.backend.do_auth(token, ajax=True)
#     login(request, user)
#     data = {'id': user.id, 'username': user.username}
#     return HttpResponse(json.dumps(data), mimetype='application/json')
#
#


@render_to('index.html')
def index(request, ):
    return {}