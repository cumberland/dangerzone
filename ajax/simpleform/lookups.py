from simpleform.models import ProjectName
from selectable.base import ModelLookup
from selectable.registry import registry, LookupAlreadyRegistered


class EntryLookup(ModelLookup):
	model = ProjectName
	search_field = 'Project__icontains'

try:
	registry.register(EntryLookup)
except LookupAlreadyRegistered:
	pass
