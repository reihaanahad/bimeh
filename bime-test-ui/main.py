from modpckg.mymodules import*
from modpckg.db import*
def thirdparty():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)
    bime.find_element_by_xpath("//a[contains(@class, 'mr-2 col-auto btn-filled back-surface-color secondary-bk-color d-flex align-items-center')]")
    bime.input('login-input','09389090359')
    bime.find_element_by_Id('check-phone-number')
    bime.input('password-input','rey87310@')
    bime.find_element_by_Id('password-submit-button')
    try:
        time.sleep(2)
        bime.find_element_by_xpath("//div[text()='ریحانه احدزاده']")
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','SignIn', date.today(),current_time, duration, msg)
    
    #1
    
    start_time = datetime.now().replace(microsecond=0)
    bime.find_elements_by_classes('newest-bimeh-bar-item',0)
    try:
        bime.find_element_by_xpath('//*[@class="ant-btn ant-btn-default btn-text primary-color"]')
    except:
        pass
    bime.dropdown("vehicleCategoryId",'ant-select-item-option-content',0)
    bime.dropdown("brands",'ant-select-item-option-content',5)
    bime.dropdown("usingType",'ant-select-item-option-content',15)
    bime.dropdown("productionYear",'ant-select-item-option-content',20)
    bime.dropdown("model",'ant-select-item-option-content',30)
    bime.find_element_by_class("primary-bk-color")
    bime.dropdown("previousInsuranceStatus",'ant-select-item-option-content',0)
    bime.find_elements_by_classes("ant-radio",1)
    bime.dropdown("previousCompany",'ant-select-item-option-content',3)
    bime.dropdown("previousDuration",'ant-select-item-option-content',14)
    bime.find_element_by_class("primary-bk-color")
    bime.dropdown("thirdPartyDiscount",'ant-select-item-option-content',0)
    bime.dropdown("driverDiscount",'ant-select-item-option-content',10)
    bime.find_elements_by_xpaths('//input[@class="ant-radio-input"]',1)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    time.sleep(2)
    bime.find_element_by_xpath("//button[@title='بستن']")
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-buy back-surface-color"]')
    bime.find_element_by_xpath('//label[@class="ant-radio-wrapper mb-1"]')
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color w-125px"]')
    bime.input('firstname','تست')
    bime.input('lastname','فنی')
    bime.find_element_by_Id('year0')
    bime.scroll('rc-virtual-list-holder',7)
    time.sleep(1)
    bime.find_elements_by_classes('ant-select-item-option-content',2)
    bime.dropdown('day0','ant-select-item-option-content',10)
    bime.dropdown('month0','ant-select-item-option-content',20)
    bime.input('nationalCode','0480981604')
    bime.input('mobile','09389090359')
    bime.input('phone','02144169661')
    bime.find_elements_by_classes('ant-radio-input',0)
    bime.find_element_by_xpath('//span[@class="radio-box"]')
    bime.scroll_down(500)
    bime.upload(0)
    bime.upload(1)
    bime.upload(2)
    time.sleep(2)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color d-xs-none"]')
    time.sleep(4)
    bime.scroll_down(500)
    time.sleep(4)
    bime.action('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')
    time.sleep(4)
    bime.scroll_down(300)
    time.sleep(4)
    bime.action('//span[@class="ant-checkbox"]')
    bime.action('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')

    bime.find_elements_by_classes('ant-radio-wrapper',0)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')
    try:
        bime.find_element_by_Id('Cvv2')
        msg='pass'
    except:
        msg='fail'
        pass
  
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','ThirdParty', date.today(), current_time, duration, msg)
    
    
    #2
    
    bime.load('https://bimeh.com/thirdparty')
    
    try:
        bime.find_element_by_xpath('//*[@class="ant-btn ant-btn-default btn-text primary-color"]')
    except:
        pass    
    bime.dropdown("vehicleCategoryId",'ant-select-item-option-content',0)
    bime.dropdown("brands",'ant-select-item-option-content',5)
    bime.dropdown("usingType",'ant-select-item-option-content',15)
    bime.dropdown("productionYear",'ant-select-item-option-content',20)
    bime.dropdown("model",'ant-select-item-option-content',30)
    bime.find_element_by_class("primary-bk-color")
    bime.dropdown("previousInsuranceStatus",'ant-select-item-option-content',0)
    bime.find_elements_by_classes("ant-radio",1)
    bime.dropdown("previousCompany",'ant-select-item-option-content',3)
    bime.dropdown("previousDuration",'ant-select-item-option-content',14)
    bime.find_element_by_class("primary-bk-color")
    bime.dropdown("thirdPartyDiscount",'ant-select-item-option-content',0)
    bime.dropdown("driverDiscount",'ant-select-item-option-content',10)
    bime.find_elements_by_classes("ant-radio",0)
    bime.dropdown("propertyLoss",'ant-select-item-option-content',21)
    bime.dropdown("lifeLoss",'ant-select-item-option-content',25)
    bime.dropdown("driverLoss",'ant-select-item-option-content',28)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')

    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-buy back-surface-color"]')
    bime.find_element_by_xpath('//label[@class="ant-radio-wrapper mb-1"]')
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color w-125px"]')
    bime.input('firstname','تست')
    bime.input('lastname','فنی')
    bime.find_element_by_Id('year0')
    bime.scroll('rc-virtual-list-holder',7)
    time.sleep(1)
    bime.find_elements_by_classes('ant-select-item-option-content',2)
    bime.dropdown('day0','ant-select-item-option-content',10)
    bime.dropdown('month0','ant-select-item-option-content',20)
    bime.input('nationalCode','0480981604')
    bime.input('mobile','09389090359')
    bime.input('phone','02144169661')
    bime.find_elements_by_classes('ant-radio-input',0)
    bime.find_element_by_xpath('//span[@class="radio-box"]')
    bime.scroll_down(500)
    bime.upload(0)
    bime.upload(1)
    bime.upload(2)
    time.sleep(4)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color d-xs-none"]')
    time.sleep(4)
    bime.scroll_down(500)
    time.sleep(4)
    bime.action('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')
    time.sleep(3)
    bime.scroll_down(300)
    time.sleep(3)
    bime.action('//span[@class="ant-checkbox"]')
    bime.action('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')

    bime.find_elements_by_classes('ant-radio-wrapper',0)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')
    try:
         bime.find_element_by_Id('Cvv2')
         msg='pass'
    except:
        msg='fail'
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','ThirdParty-Loss', date.today(), current_time, duration, msg)
    #3
    bime.load('https://bimeh.com/thirdparty')
    start_time = datetime.now().replace(microsecond=0)
    try:
        bime.find_element_by_xpath('//*[@class="ant-btn ant-btn-default btn-text primary-color"]')
    except:
        pass
    bime.dropdown("vehicleCategoryId",'ant-select-item-option-content',0)
    bime.dropdown("brands",'ant-select-item-option-content',5)
    bime.dropdown("usingType",'ant-select-item-option-content',15)
    bime.dropdown("productionYear",'ant-select-item-option-content',20)
    bime.dropdown("model",'ant-select-item-option-content',30)
    bime.find_element_by_class("primary-bk-color")
    bime.dropdown("previousInsuranceStatus",'ant-select-item-option-content',0)
    bime.find_elements_by_classes("ant-radio",0)
    bime.dropdown("previousDuration",'ant-select-item-option-content',4)
    bime.find_elements_by_classes('ant-radio',2)
    bime.find_element_by_class("primary-bk-color")
    bime.dropdown("thirdPartyDiscount",'ant-select-item-option-content',0)
    bime.dropdown("driverDiscount",'ant-select-item-option-content',10)
    bime.find_elements_by_classes("ant-radio",1)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-buy back-surface-color"]')
    bime.find_element_by_xpath('//label[@class="ant-radio-wrapper mb-1"]')
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color w-125px"]')
    bime.input('firstname','تست')
    bime.input('lastname','فنی')
    bime.find_element_by_Id('year0')
    bime.scroll('rc-virtual-list-holder',7)
    time.sleep(1)
    bime.find_elements_by_classes('ant-select-item-option-content',2)
    bime.dropdown('day0','ant-select-item-option-content',10)
    bime.dropdown('month0','ant-select-item-option-content',20)
    bime.input('nationalCode','0480981604')
    bime.input('mobile','09389090359')
    bime.input('phone','02144169661')
    bime.find_elements_by_classes('ant-radio-input',0)
    bime.find_element_by_xpath('//span[@class="radio-box"]')
    bime.scroll_down(500)
    bime.upload(0)
    bime.upload(1)
    bime.upload(2)
    time.sleep(2)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color d-xs-none"]')
    time.sleep(4)
    bime.scroll_down(500)
    time.sleep(4)
    bime.action('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')
    time.sleep(3)
    bime.scroll_down(300)
    time.sleep(3)
    bime.action('//span[@class="ant-checkbox"]')
    bime.action('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')

    bime.find_elements_by_classes('ant-radio-wrapper',0)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')
    try:
         bime.find_element_by_Id('CardNumber_PanString')
         msg='pass'
    except:
        msg='fail'

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','ThirdParty-Owner', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
    thirdparty()
def motor():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    bime.find_element_by_xpath("//a[contains(@class, 'mr-2 col-auto btn-filled back-surface-color secondary-bk-color d-flex align-items-center')]")
    bime.input('login-input','09389090359')
    bime.find_element_by_Id('check-phone-number')
    bime.input('password-input','rey87310@')
    bime.find_element_by_Id('password-submit-button')
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',1)
    bime.dropdown("motorType",'ant-select-item-option-content',0)
    bime.dropdown("productionYear",'ant-select-item-option-content',4)
    bime.find_element_by_class("primary-bk-color")
    bime.dropdown("previousInsuranceStatus",'ant-select-item-option-content',0)
    bime.find_elements_by_classes("ant-radio",1)
    bime.dropdown("previousCompany",'ant-select-item-option-content',3)
    bime.dropdown("previousDuration",'ant-select-item-option-content',14)
    bime.find_element_by_class("primary-bk-color")
    bime.dropdown("thirdPartyDiscount",'ant-select-item-option-content',0)
    bime.dropdown("driverDiscount",'ant-select-item-option-content',10)
    bime.find_elements_by_xpaths('//input[@class="ant-radio-input"]',1)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    bime.find_element_by_xpath("//button[@title='بستن']")
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-buy back-surface-color"]')
    bime.find_element_by_xpath('//label[@class="ant-radio-wrapper mb-1"]')
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color w-125px"]')
    bime.input('firstname','تست')
    bime.input('lastname','فنی')
    bime.find_element_by_Id('year0')
    bime.scroll('rc-virtual-list-holder',7)
    time.sleep(1)
    bime.find_elements_by_classes('ant-select-item-option-content',2)
    bime.dropdown('day0','ant-select-item-option-content',10)
    bime.dropdown('month0','ant-select-item-option-content',20)
    bime.input('nationalCode','0480981604')
    bime.input('mobile','09389090359')
    bime.input('phone','02144169661')
    bime.find_elements_by_classes('ant-radio-input',0)
    bime.find_element_by_xpath('//span[@class="radio-box"]')
    bime.scroll_down(500)
    bime.upload(0)
    bime.upload(1)
    bime.upload(2)
    time.sleep(2)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color d-xs-none"]')
    time.sleep(4)
    bime.scroll_down(500)
    time.sleep(3)
    bime.action('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')
    time.sleep(3)
    bime.scroll_down(300)
    time.sleep(3)
    bime.action('//span[@class="ant-checkbox"]')
    bime.action('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')

    bime.find_elements_by_classes('ant-radio-wrapper',0)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')
    try:
         bime.find_element_by_Id('Cvv2')
         msg='pass'
    except:
        msg='fail'
 
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Motor', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        motor()
def body():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    bime.find_element_by_xpath("//a[contains(@class, 'mr-2 col-auto btn-filled back-surface-color secondary-bk-color d-flex align-items-center')]")
    bime.input('login-input','09389090359')
    bime.find_element_by_Id('check-phone-number')
    bime.input('password-input','rey87310@')
    bime.find_element_by_Id('password-submit-button')
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',2)
    time.sleep(2)
    bime.dropdown("vehicleCategoryId",'ant-select-item-option-content',0)
    bime.dropdown("brands",'ant-select-item-option-content',2)
    time.sleep(1)
    bime.dropdown("using",'ant-select-item-option-content',12)
    bime.dropdown("models",'ant-select-item-option-content',13)
    bime.input('price','5000000000')
    bime.find_element_by_class("primary-bk-color")
    bime.find_elements_by_classes('ant-radio-input',0)
    bime.dropdown('noDamageYear','ant-select-item-option-content',0)
    bime.find_elements_by_classes('ant-radio-input',2)
    bime.dropdown('buildYear','ant-select-item-option-content',7)
    bime.dropdown('buildMonth','ant-select-item-option-content',17)
    bime.find_element_by_class("primary-bk-color")
    bime.dropdown('company','ant-select-item-option-content',0)
    bime.dropdown('thirdPartyDiscount','ant-select-item-option-content',10)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    bime.find_element_by_xpath("//button[@title='بستن']")
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-buy back-surface-color"]')
    bime.find_element_by_xpath('//label[@class="ant-radio-wrapper mb-1"]')
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color w-125px"]')
    bime.input('firstname','تست')
    bime.input('lastname','فنی')
    bime.find_element_by_Id('year0')
    bime.scroll('rc-virtual-list-holder',7)
    time.sleep(1)
    bime.find_elements_by_classes('ant-select-item-option-content',2)
    bime.dropdown('day0','ant-select-item-option-content',10)
    bime.dropdown('month0','ant-select-item-option-content',20)
    bime.input('nationalCode','0480981604')
    bime.input('mobile','09389090359')
    bime.input('phone','02144169661')
    bime.find_element_by_xpath('//span[@class="radio-box"]')
    bime.find_elements_by_xpaths('//*[contains(concat( " ", @class, " " ), concat( " ", "surface-color", " " ))]',1)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')

    bime.scroll_down(500)
    bime.upload(0)
    bime.upload(1)
    bime.upload(2)
    bime.upload(3)

    time.sleep(2)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color d-xs-none"]')
    time.sleep(4)
    bime.scroll_down(500)
    time.sleep(3)
    bime.action('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')
    time.sleep(3)
    bime.scroll_down(300)
    time.sleep(3)
    bime.action('//span[@class="ant-checkbox"]')
    bime.action('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')

    bime.find_elements_by_classes('ant-radio-wrapper',0)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color primary-bk-color"]')
    try:
         bime.find_element_by_Id('CardNumber_PanString')
         msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Body', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        body()
def fire():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',3)
    bime.dropdown("estateType",'ant-select-item-option-content',0)
    bime.find_elements_by_classes('ant-radio-input',1)
    bime.find_element_by_class("primary-bk-color")
    bime.input('totalArea','100')
    bime.input('homeAppliancesValue','5000000000')
    bime.dropdown("areaUnitPrice",'ant-select-item-option-content',3)
    bime.find_element_by_class("primary-bk-color")
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    try:
        txt=bime.find_txt('//*[contains(concat( " ", @class, " " ), concat( " ", "price-bold darker-surface-color", " " ))]')
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Fire', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        fire()
def earthquake():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',4)
    bime.dropdown("estateType",'ant-select-item-option-content',0)
    bime.find_elements_by_classes('ant-radio-input',1)
    bime.find_element_by_class("primary-bk-color")
    bime.input('totalArea','100')
    bime.input('homeAppliancesValue','5000000000')
    bime.dropdown("areaUnitPrice",'ant-select-item-option-content',3)
    bime.find_element_by_class("primary-bk-color")
    try:
        txt=bime.find_txt('//*[contains(concat( " ", @class, " " ), concat( " ", "price-bold darker-surface-color", " " ))]')
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Earthquake', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        earthquake()
def pilgrimage():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',5)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    try:
        txt=bime.find_txt('//*[contains(concat( " ", @class, " " ), concat( " ", "price-bold darker-surface-color", " " ))]')
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Pilgrimage', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        pilgrimage()
def health():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',6)
    bime.find_element_by_Id('year0')
    bime.scroll('rc-virtual-list-holder',10)
    bime.find_elements_by_classes('ant-select-item-option-content',5)
    bime.dropdown('day0','ant-select-item-option-content',10)
    bime.dropdown('month0','ant-select-item-option-content',20)
    bime.dropdown('basicInsurer','ant-select-item-option-content',31)

    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    try:
        txt=bime.find_txt('//*[contains(concat( " ", @class, " " ), concat( " ", "price-bold darker-surface-color", " " ))]')
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Health', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        health()
def travel():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',7)
    bime.find_elements_by_classes('ant-select-selector',0)
    bime.find_elements_by_classes('ant-select-item-option-content',0)
    bime.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "ant-form-item-required", " " ))]')
    bime.find_element_by_class('rmdp-input')
    bime.find_element_by_xpath('//*[contains(text(), "۱۴۰۲")]')
    bime.find_elements_by_classes('rmdp-arrow',0)
    bime.find_elements_by_classes('rmdp-arrow',0)
    bime.find_elements_by_classes('rmdp-day',52)
    bime.find_elements_by_classes('sd ',2)
    bime.dropdown('searchbox_travel_duration','ant-select-item-option-content',10)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    try:
        txt=bime.find_txt('//*[contains(concat( " ", @class, " " ), concat( " ", "price-bold darker-surface-color", " " ))]')
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Travel', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        travel()
def travelPlus():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',8)
    time.sleep(1)
    bime.dropdown('searchbox_travel_countries','ant-select-item-option-content',0)
    bime.dropdown('searchbox_travel_duration','ant-select-item-option-content',10)
    bime.find_element_by_class('rmdp-input')
    bime.find_element_by_xpath('//*[contains(text(), "۱۴۰۲")]')
    bime.find_elements_by_classes('rmdp-arrow',0)
    bime.find_elements_by_classes('rmdp-arrow',0)
    bime.find_elements_by_classes('rmdp-day',52)
    bime.find_elements_by_classes('sd ',2)
    bime.find_elements_by_classes('ant-radio-input',0)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    try:
        txt=bime.find_txt('//*[contains(concat( " ", @class, " " ), concat( " ", "price-bold darker-surface-color", " " ))]')
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','TravelPlus', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        travelPlus()
def doctors():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',9)
    bime.find_elements_by_classes('ant-radio',0)
    #bime.find_element_by_xpath('//span[contains(text(), "پزشکی")]')
    bime.find_element_by_class('ant-select-selection-item')
    bime.find_elements_by_classes('ant-select-item-option-content',7)
    bime.dropdown('noDamageYears','ant-select-item-option-content',12)
    bime.dropdown('schoolStatus','ant-select-item-option-content',19)
    bime.find_elements_by_classes('ant-radio',2)

    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    try:
        txt=bime.find_txt('//*[contains(concat( " ", @class, " " ), concat( " ", "price-bold darker-surface-color", " " ))]')
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Doctors', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        doctors()
def elevator():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',10)
    time.sleep(1)
    bime.dropdown('elevatorUsage','ant-select-item-option-content',0)
    bime.dropdown('elevatorCapacity','ant-select-item-option-content',5)
    bime.dropdown('floorsCount','ant-select-item-option-content',15)
    bime.find_elements_by_classes('ant-radio',0)
    bime.dropdown('elevatorAge','ant-select-item-option-content',25)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    try:
        txt=bime.find_txt('//*[contains(concat( " ", @class, " " ), concat( " ", "price-bold darker-surface-color", " " ))]')
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Elevator', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        elevator()
def sports():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',11)
    bime.find_element_by_Id('year0')
    bime.scroll('rc-virtual-list-holder',10)
    bime.find_elements_by_classes('ant-select-item-option-content',5)
    bime.dropdown('month0','ant-select-item-option-content',10)
    bime.dropdown('day0','ant-select-item-option-content',20)
    bime.dropdown('Careers','ant-select-item-option-content',30)
    bime.find_element_by_xpath('//button[@class="ant-btn ant-btn-default btn-filled back-surface-color  primary-bk-color"]')
    try:
        txt=bime.find_txt('//*[contains(concat( " ", @class, " " ), concat( " ", "price-bold darker-surface-color", " " ))]')
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Sports', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        sports()
def mobile():
    bime=ExampleClass()
    bime.load("https://bimeh.com")
    start_time = datetime.now().replace(microsecond=0)      
    bime.find_elements_by_classes('newest-bimeh-bar-item',12)
    time.sleep(1)
    bime.dropdown('brand','ant-select-item-option-content',0)
    time.sleep(1)
    bime.dropdown('model','ant-select-item-option-content',11)
    bime.input('price','50,000,000')
    bime.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "primary-bk-color", " " ))]')
    try:
        txt=bime.find_txt('//*[contains(concat( " ", @class, " " ), concat( " ", "price-bold darker-surface-color", " " ))]')
        msg='pass'
    except:
        msg='fail'
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    end_time = datetime.now().replace(microsecond=0)
    duration = (end_time-start_time).total_seconds()
    db('Inquiry','Mobile', date.today(), current_time, duration, msg)
    bime.quit()
if __name__=='__main__':
        mobile()

