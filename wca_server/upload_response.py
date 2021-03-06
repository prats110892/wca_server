import os, sys

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIRECTORY)

def getReponseBody(responseText) :
	os.remove(os.path.join(CURRENT_DIRECTORY + "/templates/upload_response.html"))
	response_html_body = "<!DOCTYPE html><html><head><title>Upload Data Workflow</title><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta name='description' content=' Upload Data using Twitter Bootstrap Wizard Plugin'><meta name='author' content=' Sarthak Ghosh. Template by Vincent Gabriel'><script type='text/javascript' src='http://code.jquery.com/jquery-latest.js'></script><script type='text/javascript' src='{{ url_for('static', filename='jquery.bootstrap.wizard.js') }}'></script><script type='text/javascript' src='{{ url_for('static', filename='bootstrap/js/bootstrap.min.js') }}'></script><link href='{{ url_for('static', filename='bootstrap/css/bootstrap.min.css') }}' rel='stylesheet'><link href='{{ url_for('static', filename='generalCSS/specialStyles.css') }}' rel='stylesheet'><script>$(document).ready(function() {$('#rootwizard').bootstrapWizard({'tabClass': 'nav nav-tabs'});});</script><style type='text/css'>body {padding-top: 60px;padding-bottom: 40px;}.sidebar-nav {padding: 9px 0;}</style></head><body><nav class='navbar navbar-inverse navbar-fixed-top' role='navigation'><div class='container-fluid'><div class='navbar-header'><a class='navbar-brand' href='/'>WCA Data Manager</a></div><div id='navbar' class='collapse navbar-collapse'><ul class='nav navbar-nav'><li><a href='/upload_data'>Upload New Data</a></li><li><a href='/download_data'>Download Data</a></li><li><a href='/upload_calc'>Upload new Calculations</a></li></ul><ul class='nav navbar-nav' style='float: right;'><li><a href='/help' class='navbar-nav pull-right'>Help</a></li></ul></div><!--/.nav-collapse --></div></nav><div class='container'><div id='response-message' style={color: 'green'}>%s</div></div></body>"%(responseText)
	open(CURRENT_DIRECTORY + "/templates/upload_response.html", "w").close()
	upload_response_html = open(CURRENT_DIRECTORY + "/templates/upload_response.html", "w")
	upload_response_html.write(response_html_body)
	upload_response_html.close()
	return response_html_body
