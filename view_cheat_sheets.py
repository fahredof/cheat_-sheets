import sublime 
import sublime_plugin

class ViewCheatSheetsCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        content = self.first_page()
        Text = self.view.show_popup(content, sublime.HTML, location=-1, max_width = 2000 , max_height=2000, on_navigate=self.first_pop_up_window)
        Another = self.view.show_popup(content, sublime.HTML, location=-1, max_width = 2000 , max_height=2000, on_navigate=self.second_pop_up_window)
        items = [Text, Another] 
        self.view.show_popup_menu(items, self.on_done)

    def on_done(self, result):
        print(result)


    def choice(self, edit):
        content = self.main_page()
        if edit == str(1):
            self.view.show_popup(content, sublime.HTML, location=-1, max_width = 2000 , max_height=2000, on_navigate=self.first_pop_up_window)
        
        elif edit == str(2):
            self.view.show_popup(content, sublime.HTML, location=-1, max_width = 2000 , max_height=2000, on_navigate=self.second_pop_up_window)


    def first_pop_up_window(self, edit):
        
        self.link_to_path = edit
        content = self.first_page()
        self.view.show_popup(content, sublime.HTML, location=-1, max_width = 600, max_height=600, on_navigate=self.run)
        
    def second_pop_up_window(self, edit):
        self.link_to_path = edit
        content = self.second_page()
        self.view.show_popup(content, sublime.HTML, location=-1, max_width = 600, max_height=600, on_navigate=self.run)

    def start_page(self):
        resources = sublime.find_resources("start.html")
        content = sublime.load_resource(resources[0])
        return content

    def main_page(self):
        resources = sublime.find_resources("main.html")
        content = sublime.load_resource(resources[0])
        return content
    
    def first_page(self):
        resources = sublime.find_resources("first_page.html")
        content = sublime.load_resource(resources[0])
        return content

    def second_page(self):
        resources = sublime.find_resources("second_page.html")
        content = sublime.load_resource(resources[0])
        return content

    def python_cheat(self):
        path = ""
        
        if self.link_to_path == str(1):
            path = self.first_link
        elif self.link_to_path == str(2):
            path = self.second_link
        elif self.link_to_path == str(3):
            path = self.third_link
        elif self.link_to_path == str(4):
            path = self.fourth_link
        elif self.link_to_path == str(5):
            path = self.fifth_link
        elif self.link_to_path == str(6):
            path = self.sixth_link
        elif self.link_to_path == str(7):
            path = self.seventh_link
        elif self.link_to_path == str(8):
            path = self.eighth_link
        elif self.link_to_path == str(9):
            path = self.ninth_link
        elif self.link_to_path == str(10):
            path = self.tenth_link
            
        resources = sublime.find_resources(path)
        content = sublime.load_resource(resources[0])
        return content

    first_link = "1_base_types.html"
    second_link = "2_сontainer_types.html"
    third_link = "3_name.html"
    fourth_link = "4_transformations.html"
    fifth_link = "5_assignment_to_variables.html"
    sixth_link = "6_Access_to_sequence_elements.html"
    seventh_link = "7_boolean_logic.html"
    eighth_link = "8_instruction_blocks.html"
    ninth_link = "9_math.html"
    tenth_link = "10_conditional_operator.html"

    def link(self):
        path = ""
        
        if self.link_to_path == str(1):
            path = self.first_link
        elif self.link_to_path == str(2):
            path = self.second_link
        elif self.link_to_path == str(3):
            path = self.third_link
        elif self.link_to_path == str(4):
            path = self.fourth_link
        elif self.link_to_path == str(5):
            path = self.fifth_link
        elif self.link_to_path == str(6):
            path = self.sixth_link
        elif self.link_to_path == str(7):
            path = self.seventh_link
        elif self.link_to_path == str(8):
            path = self.eighth_link
        elif self.link_to_path == str(9):
            path = self.ninth_link
        elif self.link_to_path == str(10):
            path = self.tenth_link
            
        resources = sublime.find_resources(path)
        content = sublime.load_resource(resources[0])
        return content

    first_link = "1_base_types.html"
    second_link = "2_сontainer_types.html"
    third_link = "3_name.html"
    fourth_link = "4_transformations.html"
    fifth_link = "5_assignment_to_variables.html"
    sixth_link = "6_Access_to_sequence_elements.html"
    seventh_link = "7_boolean_logic.html"
    eighth_link = "8_instruction_blocks.html"
    ninth_link = "9_math.html"
    tenth_link = "10_conditional_operator.html"

    how_window = 0













