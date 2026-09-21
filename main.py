import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QTabWidget, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)
QApplication.setApplicationName('Vortex')

window = QMainWindow()
window.showMaximized()

tabs = QTabWidget()
tabs.setTabsClosable(True)
window.setCentralWidget(tabs)

navbar = QToolBar()
window.addToolBar(navbar)


def current_browser():
    current_widget = tabs.currentWidget()
    if current_widget:
        return current_widget.findChild(QWebEngineView)
    return None


def add_new_tab(url_str='http://google.com', label='New Tab'):
    tab_content = QWidget()
    layout = QVBoxLayout(tab_content)
    layout.setContentsMargins(0, 0, 0, 0)

    browser = QWebEngineView()
    browser.setUrl(QUrl(url_str))
    layout.addWidget(browser)

    index = tabs.addTab(tab_content, label)
    tabs.setCurrentIndex(index)

    browser.urlChanged.connect(lambda q, b=browser: update_url(b, q))
    browser.titleChanged.connect(
        lambda title, i=index: tabs.setTabText(i, title[:15] + "..." if len(title) > 15 else title))


def update_url(browser_instance, q):
    if current_browser() == browser_instance:
        url_bar.setText(q.toString())


# Toolbar actions
back_btn = QAction('Back', window)
back_btn.triggered.connect(lambda: current_browser() and current_browser().back())
navbar.addAction(back_btn)

forward_btn = QAction('Forward', window)
forward_btn.triggered.connect(lambda: current_browser() and current_browser().forward())
navbar.addAction(forward_btn)

reload_btn = QAction('Reload', window)
reload_btn.triggered.connect(lambda: current_browser() and current_browser().reload())
navbar.addAction(reload_btn)

new_tab_btn = QAction('+', window)
new_tab_btn.setToolTip('Open a new tab')
new_tab_btn.triggered.connect(lambda: add_new_tab('http://google.com', 'Google'))
navbar.addAction(new_tab_btn)

url_bar = QLineEdit()
navbar.addWidget(url_bar)


def navigate_to_url():
    brow = current_browser()
    if brow:
        url = url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        brow.setUrl(QUrl(url))


url_bar.returnPressed.connect(navigate_to_url)


def tab_changed(index):
    brow = current_browser()
    if brow:
        url_bar.setText(brow.url().toString())


tabs.currentChanged.connect(tab_changed)


def close_tab(index):
    if tabs.count() > 1:
        tabs.removeTab(index)
    else:
        window.close()


tabs.tabCloseRequested.connect(close_tab)

add_new_tab('http://google.com', 'Google')

sys.exit(app.exec_())
