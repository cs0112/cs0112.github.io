################## CHROME ################### 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """Change only if you are using a different browser. Default is google chrome."""
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)
############################################# 

#################### FIREFOX ####################
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def get_driver():
    """ WebDriver for Firefox """
    service = FirefoxService(GeckoDriverManager().install())
    return webdriver.Firefox(service=service)
#################################################

################## SAFARI #######################
# You will need to update permissions on safari.
from selenium import webdriver
def get_driver():
    """ WebDriver for Safari """
    return webdriver.Safari()
#################################################

############### MICROSOFT EDGE #################
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_driver():
    """ WebDriver for Edge """
    service = EdgeService(EdgeChromiumDriverManager().install())
    return webdriver.Edge(service=service)
#################################################

#################### OPERA ######################
from selenium.webdriver.opera.service import Service as OperaService
from webdriver_manager.opera import OperaDriverManager

def get_driver():
    """ WebDriver for Opera """
    service = OperaService(OperaDriverManager().install())
    return webdriver.Opera(service=service)
#################################################
