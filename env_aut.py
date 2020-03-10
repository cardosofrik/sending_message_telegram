import csv
import selenium.common.exceptions
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
class Automatizado_telegram:

    def __init__(self,numero, msg, arquivo):
        self.pagina_de_login = "https://web.telegram.org/#/login"
        self.numero_celular = numero
        self.enniar = msg
        self.arquivocsv = arquivo
        self.envios(self.numero_celular, self.enniar, self.arquivocsv)

    def webDriver(self):
        try:
            driver = webdriver.Chrome(executable_path=r'mod_auxiliar/__>nao se esqueca<__')
            return driver
        except selenium.common.exceptions.WebDriverException:
            print("local do driver nao encontrado")


    def envios(self,numero_celular,this_msg, arquivoleitura):
        conteudo_cod = self.webDriver()
        try:
            conteudo_cod.get(self.pagina_de_login)
            inicio = conteudo_cod.current_url
            sleep(2)
            meu_numero = conteudo_cod.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/input')
            sleep(9)
            print("adicionando numero")
            meu_numero.send_keys(numero_celular)
            sleep(4)
            conteudo_cod.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[1]/div/a').click()
            sleep(6)
            conteudo_cod.find_element_by_xpath('//*[@id="ng-app"]/body/div[5]/div[2]/div/div/div[2]/button[2]').click()
            sleep(25)
            print("Gerando chave, adicionar codigo. [ adicione o codigo ] ")
            conteudo_cod.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div/div[2]/div[1]/div/a')#0
            sleep(22)
            participantes = open(arquivoleitura)
            for i in csv.reader(participantes):
                if i[0] != "username":
                    uri = "https://web.telegram.org/#/im?p=@{}".format(i[0])
                    if uri != "https://web.telegram.org/#/im?p=@":
                        try:
                            conteudo_cod.get(uri)
                            mensagem_para_usuario = conteudo_cod.find_element_by_class_name('composer_rich_textarea')
                            mensagem_para_usuario.send_keys(this_msg +" "+ Keys.ENTER)
                            sleep(1)
                            _apt = "[ ENV ] - {} : {}".format(str(i[0]), this_msg)
                            print(_apt)
                        except selenium.common.exceptions.ElementNotInteractableException:
                            continue

        except selenium.common.exceptions.NoSuchElementException:
            print("prologo nao iniciado")
        except AttributeError:
            print("Driver nao encontrado")



if __name__ == '__main__':
    arquivo_origem = "lista_usernames.csv" #<--- necessita do nome de usuarios
    mensagem = "hi"
    numero_celular_padrao = 659999999 #<-------- numero do celular :)


    Automatizado_telegram(numero_celular_padrao, mensagem, arquivo_origem)
