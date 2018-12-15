import sublime 
import sublime_plugin

class ViewCheatSheetsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        content = self.main_page()
        self.view.show_popup(content, sublime.HTML, location=-1, max_width = 2000 , max_height=2000, on_navigate=self.second_pop_up_window)

    def second_pop_up_window(self, edit):
        self.link_to_path = edit
        content = self.topic()
        self.view.show_popup(content, sublime.HTML, location=-1, max_height=2000, on_navigate=self.insert_code)

    def main_page(self):
        resources = sublime.find_resources("main.html")
        content = sublime.load_resource(resources[0])
        return content
    
    def topic(self):
        path = ""
        
        if self.link_to_path == str(1):
            path = self.first_link
        elif self.link_to_path == str(2):
            path = self.second_link

        resources = sublime.find_resources(path)
        content = sublime.load_resource(resources[0])
        return content

    def insert_code(self, symbol):
        self.view.run_command("insert", {"characters": symbol})
        self.view.hide_popup()

    link_to_path = 0
    first_link = "base_types.html"
    second_link = "image2.html"




