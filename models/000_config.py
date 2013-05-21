# -*- coding: utf-8 -*-

"""
    Machine-specific deployment_settings
    All deployment_settings which are typically edited for a specific machine should be done here

    Deployers should ideally not need to edit any other files outside of their template folder

    Note for Developers:
        /models/000_config.py is NOT in the Git repository, to avoid leaking of
        sensitive or irrelevant information into the repository.
    For changes to be committed, please also edit:
        private/templates/000_config.py
"""

# Remove this line when you have edited this file sufficiently to proceed to the web interface
FINISHED_EDITING_CONFIG_FILE = True

# Select the Template
# - which Modules are enabled
# - PrePopulate data
# - Security Policy
# - Workflows
# - Theme
# - note that you should restart your web2py after changing this setting
deployment_settings.base.template = "RGIMS"

# Database deployment_settings
# Uncomment to use a different database, other than sqlite
#deployment_settings.database.db_type = "postgres"
deployment_settings.database.db_type = "mysql"
# Uncomment to use a different host
deployment_settings.database.host = "localhost"
# Uncomment to use a different port
#deployment_settings.database.port = 3306
#deployment_settings.database.port = 5432
# Uncomment to select a different name for your database
deployment_settings.database.database = "sahana"
# Uncomment to select a different username for your database
deployment_settings.database.username = "sahana"
# Uncomment to set the password
# NB Web2Py doesn't like passwords with an @ in them
deployment_settings.database.password = "sahana"
# Uncomment to use a different pool size
deployment_settings.database.pool_size = 30
# Do we have a spatial DB available? (currently supports PostGIS. Spatialite to come.)
#deployment_settings.gis.spatialdb = True

# Base deployment_settings
#deployment_settings.base.system_name = T("Sahana Eden Humanitarian Management Platform")
#deployment_settings.base.system_name_short = T("Sahana Eden")
# Set this to the Public URL of the instance
#deployment_settings.base.public_url = "http://eden.dswd.gov.ph"

# Switch to "False" in Production for a Performance gain
# (need to set to "True" again when Table definitions are changed)
deployment_settings.base.migrate = False
# To just create the .table files:
#deployment_settings.base.fake_migrate = True

# Set this to True to switch to Debug mode
# Debug mode means that uncompressed CSS/JS files are loaded
# JS Debug messages are also available in the Console
# can also load an individual page in debug mode by appending URL with
# ?debug=1
deployment_settings.base.debug = False

# Uncomment to use Content Delivery Networks to speed up Internet-facing sites
#deployment_settings.base.cdn = True

# This setting will be automatically changed _before_ registering the 1st user
deployment_settings.auth.hmac_key = "eden.dswd.gov.phsahana"

# Email deployment_settings
# Outbound server
#deployment_settings.mail.server = "127.0.0.1:25"
#deployment_settings.mail.tls = True
# Useful for Windows Laptops:
#deployment_settings.mail.server = "smtp.gmail.com:587"
#deployment_settings.mail.tls = True
#deployment_settings.mail.login = "username:password"
# From Address
deployment_settings.mail.sender = "'Sahana' <sahana@your.org>"
# Default email address to which requests to approve new user accounts gets sent
# This can be overridden for specific domains/organisations via the auth_domain table
deployment_settings.mail.approver = "useradmin@your.org"
# Daily Limit on Sending of emails
#deployment_settings.mail.limit = 1000

# Frontpage deployment_settings
# RSS feeds
deployment_settings.frontpage.rss = [
    {"title": "Eden",
     # Trac timeline
     "url": "http://eden.sahanafoundation.org/timeline?ticket=on&changeset=on&milestone=on&wiki=on&max=50&daysback=90&format=rss"
    },
    {"title": "Twitter",
     # @SahanaFOSS
     # Find ID via http://api.twitter.com/users/show/username.json
     "url": "http://twitter.com/statuses/user_timeline/96591754.rss"
     # Hashtag
     #url: "http://search.twitter.com/search.atom?q=%23eqnz"
    }
]

# Enable session store in Memcache to allow sharing of sessions across instances
#deployment_settings.base.session_memcache = '127.0.0.1:11211'

# Fill these to allow users to Login using Facebook
# https://developers.facebook.com/apps
#deployment_settings.auth.facebook_id = ""
#deployment_settings.auth.facebook_secret = ""
# Fill these to allow users to Login using Google
# https://code.google.com/apis/console/
#deployment_settings.auth.google_id = ""
#deployment_settings.auth.google_secret = ""

# Bing API Key (for Map layers)
#deployment_settings.gis.api_bing = ""
# Google API Key (for Earth & MapMaker Layers)
# default works for localhost
#deployment_settings.gis.api_google = ""
# Yahoo API Key (for Geocoder)
#deployment_settings.gis.api_yahoo = ""
# GeoServer (Currently used by GeoExplorer. Will allow REST control of GeoServer.)
# NB Needs to be publically-accessible URL for querying via client JS
#deployment_settings.gis.geoserver_url = "http://localhost/geoserver"
#deployment_settings.gis.geoserver_username = "admin"
#deployment_settings.gis.geoserver_password = ""
# Print Service URL: http://eden.sahanafoundation.org/wiki/BluePrintGISPrinting
#deployment_settings.gis.print_service = "/geoserver/pdf/"

# Twitter deployment_settings:
# Register an app at http://twitter.com/apps
# (select Aplication Type: Client)
# You'll get your consumer_key and consumer_secret from Twitter
#deployment_settings.msg_twitter_oauth_consumer_key = ""
#deployment_settings.msg_twitter_oauth_consumer_secret = ""

# UI options
# Should user be prompted to save before navigating away?
#deployment_settings.ui.navigate_away_confirm = False
# Should user be prompted to confirm actions?
#deployment_settings.ui.confirm = False
# Should potentially large dropdowns be turned into autocompletes?
# (unused currently)
#deployment_settings.ui.autocomplete = True
#deployment_settings.ui.read_label = "Details"
#deployment_settings.ui.update_label = "Edit"

# Audit deployment_settings
# We Audit if either the Global or Module asks us to
# (ignore gracefully if module author hasn't implemented this)
# NB Auditing (especially Reads) slows system down & consumes diskspace
#deployment_settings.security.audit_write = False
#deployment_settings.security.audit_read = False

# =============================================================================
# Import the deployment_settings from the Template
# - note: invalid deployment_settings are ignored
#
path = template_path()
if os.path.exists(path):
    deployment_settings.exec_template(path)

# =============================================================================
# Over-rides to the Template may be done here
#

# e.g.
#deployment_settings.base.prepopulate = ["IFRC_Train"]
#deployment_settings.base.theme = "default"
#deployment_settings.L10n.default_language = "en"
#deployment_settings.security.policy = 7 # Organisation-ACLs
# Enable Additional Module(s)
#deployment_settings.modules["delphi"] = Storage(
#        name_nice = T("Delphi Decision Maker"),
#        restricted = False,
#        module_type = 10,
#    )

# After 1st_run, set this for Production to save 1x DAL hit/request
#deployment_settings.base.prepopulate = 0

# =============================================================================
# A version number to tell update_check if there is a need to refresh the
# running copy of this file
VERSION = 1

# END =========================================================================
