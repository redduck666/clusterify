from django.conf.urls.defaults import *

from views import list_proposed_projects, list_completed_projects, single_project, add_or_edit_project, add_project, join_project, vote_for_project, search_portal, set_completed_confirm, set_completed_doit, post_project_comment, list_comments, recommended_projects, list_projects_as_feed, approve_join, edit_project_comment, list_seeds, post_seed, vote_for_seed, seed_to_project, set_project_admin_confirm, set_project_admin_doit

from tests.data import populate_projects

urlpatterns = patterns('',
		
		# Individual project actions
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/$',
			single_project),
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/join/$',
			join_project),
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/(?P<joining_username>\w+)/approve/$',
			approve_join),
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/edit/$',
			add_or_edit_project),
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/complete/$',
			set_completed_confirm),
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/complete/ok/$',
			set_completed_doit),
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/vote/(?P<vote_type>(completed|proposed))/$',
			vote_for_project),
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/become_admin/$',
			set_project_admin_confirm),
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/become_admin/ok/$',
			set_project_admin_doit),
	   
		# Seeds
		url(r'^seeds/list/(?P<list_type>(new|top))/$',
			list_seeds),
		url(r'^seeds/list/$',
			list_seeds),
		url(r'^seeds/$',
			list_seeds),
		url(r'^seeds/postnew/$',
			post_seed),
		url(r'^seeds/vote/(?P<seed_pk>\d+)/$',
			vote_for_seed),
		url(r'^seeds/toproject/(?P<seed_pk>\d+)/$',
			seed_to_project),
	   
		# Comments
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/postcomment/$',
			post_project_comment),
		url(r'^list/(?P<project_author>\w+)/(?P<project_pk>\d+)/editcomment/(?P<comment_pk>\d+)/$',
			edit_project_comment),
	  
		# rss -- only available for top/new
		url(r'^rss/(?P<completeness>(completed|proposed))/(?P<list_type>(top|new))/$',
			list_projects_as_feed),
		url(r'^rss/(?P<completeness>(completed|proposed))/$',
			list_projects_as_feed),
	   
		# listing projects
		url(r'^completed/(?P<list_type>(top|new))/$',
			list_completed_projects),
		url(r'^proposed/(?P<list_type>(top|new))/$',
			list_proposed_projects),
		url(r'^(?P<completeness>(completed|proposed))/recommend/$',
			recommended_projects),
		url(r'^completed/$',
			list_completed_projects),
		url(r'^proposed/$',
			list_proposed_projects),
		url(r'^list/$',
			list_proposed_projects),
		url(r'^$',
			list_proposed_projects),
	   
		url(r'^search/$',
			search_portal),
		url(r'^comments/$',
			list_comments),
		url(r'^add/$',
			add_project),
	   
		# DEBUG
		#url(r'^populate/$', 
		#	populate_projects),
)
