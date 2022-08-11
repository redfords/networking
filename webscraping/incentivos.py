from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
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

    def execute(self):
        # entidad = self._parametros['entidad']
        entidad = "bsc"
        # fecha_informe = self._parametros['fecha_informe'] forma ddmmaaaa
        fecha_informe = "01052022"
        with open('/home/goa/sigma/sigma_session_info_%s.pickle' % entidad.lower(), 'rb') as f:
            logins = pickle.load(f)
        download_dir = "/home/goa/%s/incentivos/Uptime/xls" % entidad
        
        # iniciamos el driver del browser configurado
        driver = webdriver.Firefox(options=self.set_options(), firefox_profile=self.set_firefox_profile(download_dir))

        # entramos a la pagina
        driver.get('https://sigma.redlink.com.ar/monitorup/pages/vistaConsulta.xhtml')

        try:
            element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'j_idt12:myLogin:username')))

        except TimeoutException:
            print("ERROR: No se pudo cargar la pagina web inicial.")
            return 1

        element.send_keys("maciela")
        driver.find_element_by_id("j_idt12:myLogin:password").send_keys("Gobierno15.")
        driver.find_element_by_id("j_idt12:myLogin:loginButton").click()

        try:
            ok_login = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'form:panel:grupos_label')))
        
        except TimeoutException:
            try:
                cambio_pass = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'form:changePasswordComponent:password')))
            
            except TimeoutException:
                print("ERROR: No se pudo ingresar a la pagina")
                return 1

            driver.find_element_by_id("form:changePasswordComponent:password").send_keys(logins.get('password'))
            logins = self.change_password(entidad, logins)

            # ya tengo el password cambiado instanciado en el dic logins
            driver.find_element_by_id("form:changePasswordComponent:newPassword").send_keys(logins.get('password'))
            driver.find_element_by_id("form:changePasswordComponent:newPasswordConfirmed").send_keys(logins.get('password'))
            driver.find_element_by_id("form:changePasswordComponent:j_idt18").click()

            print('<p><span style="color: #008000;"><em><strong>Se cambio satisfactoriamente el password de la entidad %s.</strong></em></span></p>' % entidad.upper())
            return 1

        consultas_por_grupo = 'PrimeFaces.ab({s:"formMainMenu:j_idt32",p:"formMainMenu:j_idt32",f:"formMainMenu"});return false;'
        driver.execute_script(consultas_por_grupo)

        try:
            solapa_por_grupo_ok = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'form:panel:grupos')))
        except TimeoutException:
            print("ERROR: No se pudo cargar la solapa de consultas por grupo.")
            return 1

        # seleccionamos la solapa grupos el indicado
        sleep(3)
        driver.find_element_by_id('form:panel:grupos').click()
        sleep(3)
        driver.find_element_by_id("form:panel:grupos_0").click()
        sleep(3)

        # seleccionamos de la solapa fecha desde y hasta la fecha de ayer
        fecha_desde = driver.find_element_by_id("form:panel:fechaDesdeEv_input")
        fecha_desde.click()
        fecha_desde.send_keys(fecha_informe)
        sleep(3)
        fecha_hasta = driver.find_element_by_id("form:panel:fechaHastaEv_input")
        fecha_hasta.click()
        fecha_hasta.send_keys(fecha_informe)
        sleep(3)

        # apretamos el boton consultar
        script_boton_consultar = 'PrimeFaces.ab({s:"form:panel:consultar",u:"form:panelGrid4 form:panel:actualizacion form:messageGeneral"});return false;'
        driver.execute_script(script_boton_consultar)
        sleep(5)

        # seleccionamos la prestania por terminal
        try:
            last_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'logoLinkfooter')))
        except TimeoutException:
            print("ERROR: No se pudo cargar la solapa de consulta por terminal.")
            return 1

        driver.execute_script("arguments[0].scrollIntoView();", last_element)
        sleep(3)
        excel = driver.find_element_by_id("form:tabView:buttonExportXls2")
        onclick = excel.get_attribute("onclick")
        driver.execute_script(onclick)

        # acepto la alerta
        alert = driver.switch_to.alert
        alert.accept()

        sleep(30)

        if os.path.exists('%s/SIGMA-UP-PorTerminalUptime.xls'%download_dir):
            os.rename('%s/SIGMA-UP-PorTerminalUptime.xls'%download_dir,'%s/%s_SIGMA-UP-PorTerminalUptime_%s.xls'%(download_dir, entidad.upper(), fecha_informe[-4:]+fecha_informe[-6:-4]+fecha_informe[:2]))
        else:
            print('<p><span style="color: #ff0000;"><em><strong>ERROR: El proceso se ejecuto sin errores pero no se encuentra el archivo</strong></em></span></p>')
            return 1
        
        if os.path.exists('%s/%s_SIGMA-UP-PorTerminalUptime_%s.xls'%(download_dir, entidad.upper(), fecha_informe[-4:]+fecha_informe[-6:-4]+fecha_informe[:2])):
            #fecha_mailing = "%s-%s-%s" % (fecha_informe[0:2], fecha_informe[2:4], fecha_informe[4:])
            print('<p><span style="color: #008000;"><em><strong>Se descargo satisfactoriamente el archivo de uptime desde sigma para la entidad.</strong></em></span></p>')
        driver.stop_client()
        driver.close()

        return 0

WebscrappingIncentivos().execute()