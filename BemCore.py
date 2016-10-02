import sublime, sublime_plugin
from .sublime_bem_create.BemCreate import BemCreateCommand

bem_create = BemCreateCommand

class BemCreateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		bem_create.run(self, edit)