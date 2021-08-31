"""
Модуль с тест приложением python.
"""

from kivy.app import App
import webbrowser


url = "https://edusite.ru/"
url1 = "https://netfolio.ru"

class MyApp(App):
    webbrowser.open_new(url)
    webbrowser.open_new_tab(url1)

if __name__ == "__main__":
    MyApp().run()
