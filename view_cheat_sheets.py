import sublime 
import sublime_plugin
import webbrowser

class ViewCheatSheetsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        
        content = self.main_page()
        self.view.show_popup(content, sublime.HTML, location=-1, max_width = 2000 , max_height=2000, on_navigate=self.second_pop_up_window)


    def second_pop_up_window(self, edit):
        
        self.link_to_path = edit
        content = self.topic()

        self.view.show_popup(content, sublime.HTML, location=-1, max_width = 600, max_height=600, on_navigate=self.link_in_topic)


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
        
        elif self.link_to_path == str(11):
            path = self.eleventh_link
            
        resources = sublime.find_resources(path)
        content = sublime.load_resource(resources[0])
        return content

    def link_in_topic(self, edit):
        
        if edit == str(1):
            content = self.main_page()
            self.view.show_popup(content, sublime.HTML, location=-1, max_width = 2000 , max_height=2000, on_navigate=self.second_pop_up_window)
        
        elif edit == str(2):
            webbrowser.open('https://geekbrains.ru/posts/python_numpy')
        
        elif edit == str(3):
            webbrowser.open('https://docs.scipy.org/doc/')
        
        elif edit == str(4):
            webbrowser.open('https://pandas.pydata.org')
        
        elif edit == str(5):
            webbrowser.open('https://matplotlib.org')
        
        elif edit == str(6):
            webbrowser.open('https://seaborn.pydata.org')
        
        elif edit == str(7):
            webbrowser.open('https://bokeh.pydata.org/en/latest/')
        
        elif edit == str(8):
            webbrowser.open('https://plot.ly/python/')
        
        elif edit == str(9):
            webbrowser.open('https://scikit-learn.org/stable/')
        
        elif edit == str(10):
            webbrowser.open('http://deeplearning.net/software/theano/')

        elif edit == str(11):
            webbrowser.open('https://www.tensorflow.org')

        elif edit == str(12):
            webbrowser.open('https://keras.io')

        elif edit == str(13):
            webbrowser.open('https://www.nltk.org')


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
    eleventh_link = "11_libraries.html"

