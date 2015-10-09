import logging

from flask import request, jsonify, render_template, Response, redirect, \
    make_response, abort
from flask.views import MethodView

from kickoff import db
from kickoff.log import cef_event, CEF_WARN, CEF_INFO
from kickoff.model import getReleaseTable, getReleases
from kickoff.views.forms import ReleasesForm, ReleaseAPIForm, getReleaseForm

log = logging.getLogger(__name__)

