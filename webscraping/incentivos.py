from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pickle
import re
import os

class WebscrappingIncentivos():
    def set_firefox_profile(self, download_dir):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.dir", "%s" % download_dir)
        profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", True)
        profile.set_preference("browser.download.folderList",2)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream")
        profile.set_preference("browser.download.manager.showWhenStarting",False)
        profile.set_preference("browser.helperApps.neverAsk.openFile","application/csv,application/excel,application/vnd.msexcel,application/vnd.ms-excel,text/anytext,text/comma-separated-values,text/csv,application/vnd.ms-excel,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/octet-stream")
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.download.manager.useWindow", False)
        profile.set_preference("browser.download.manager.focusWhenStarting", False)
        profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
        profile.set_preference("browser.download.manager.showAlertOnComplete", False)
        profile.set_preference("browser.download.manager.closeWhenDone", True)
        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.manager.focusWhenStarting", False)
        profile.set_preference("browser.download.useDownloadDir", True)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
        profile.set_preference("browser.download.manager.closeWhenDone", True)
        profile.set_preference("browser.download.manager.showAlertOnComplete", False)
        profile.set_preference("browser.download.manager.useWindow", False)
        profile.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
        profile.set_preference("pdfjs.disabled", True)
        return profile

    def set_options(self):
        options = Options()
        options.headless = True
        return options

    def change_password(self, entidad, logins):
        print('<p>Se activo el proceso de cambio de password de portal sigma link para la entidad %s:</p>' % entidad.upper())
        login_update = logins
        old_password = login_update.get('password')
        print('<p><strong><span style="background-color: #ff0000; color: #ffffff;">Viejo password: "%s"</span></strong></p>' % old_password)

        # hardcode para primer change de BSF
        if old_password == "Gobierno01" and entidad.upper() in ('BSF', 'BSC'):
            old_password = "Gobierno01."

        # busco numeros en el password y le sumo uno
        numbers_in_password = re.findall('[0-9]+', old_password)
        number_plus_one = int(numbers_in_password[0]) + 1
        number_ready = '0%d' % number_plus_one if len(str(number_plus_one)) == 1 else str(number_plus_one)

        new_password = old_password[:-3] + number_ready + "."
        print('<p><span style="background-color: #008000; color: #ffffff;"><strong>Nuevo password: "%s"</strong></span></p>' % new_password)
        login_update['password'] = new_password

        with open('/home/goa/sigma/sigma_session_info_%s.pickle' % entidad.lower(), 'wb') as f:
            pickle.dump(login_update, f)

        return login_update
        



WebscrappingIncentivos().execute()