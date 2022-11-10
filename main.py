# DrDEV_2022
import sys
import logging
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('COVID19.pkl', 'rb'))
model1 = pickle.load(open('AlergyColdCovidReduced.pkl', 'rb'))
model2 = pickle.load(open('diabetes.pkl', 'rb'))
model3 = pickle.load(open("CVD.pkl", 'rb'))
model4 = pickle.load(open('Comprehensive.pkl', 'rb'))
model5 = pickle.load(open('stroke.pkl', 'rb'))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/covid19")
def covidUI():
    return render_template('COVID19.html')


@app.route('/alergy_flu_cold_covid')
def afccUI():
    return render_template("AlergyColdCovid.html")


@app.route('/diabetes')
def diabetesUI():
    return render_template("Diabetes.html")


@app.route('/cvd')
def cvdUI():
    return render_template("CVD.html")


@app.route('/comprehensive')
def compUI():
    return render_template("Comprehensive.html")


@app.route('/services')
def services():
    return render_template("services.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/book')
def bookUI():
    return render_template("appoinment.html")

@app.route('/query')
def queryUI():
    return render_template("query.html")

@app.route('/query', methods=['POST'])
def query():
    from email.message import EmailMessage
    import ssl
    import smtplib
    import certifi

    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']
    pt_mail = request.form['mail']
    subject = request.form['subject']
    Name = name
    Phone = phone
    Mail = str(pt_mail)
    Message = message
    # msge = "Dept: ", Dept, "Name: ", Name, "Phone: ", Phone, "Date: ", Date, "Slot: ", Slot, "Message: ", Message
    # msge = str(msge)

    email_sender = "drdev.maill@gmail.com"
    email_password = "mmieeonadmnrylqz"
    email_receiver = ["adrushtshetty@gmail.com", "nithishg2005@gmail.com", "pikaa1024@gmail.com",
                      "doctor.dev.ml@gmail.com"]
    subject = subject + ": " + Name + ", Phone No: " + Phone
    body = """
                {pName} has a query on the subject {pSubject}.

                {pName}'s Message:
                {pmessage}
                --------------------------------------------------------

                {pName}
                Phone No.: {pNo}
                Mail Id: {pMail}

                """.format(pName=Name, pSubject=subject, pMail=Mail, pNo=Phone, pmessage=Message)
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    return render_template("index.html")


@app.route('/book', methods=['POST'])
def book():
    dept = request.form['Department']
    slot = request.form['slot']
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']
    date = request.form['date']
    Dept = dept
    Name = name
    Phone = phone
    Date = str(date)
    Slot = slot
    Message = message
    msge = "Dept: ", Dept, "Name: ", Name, "Phone: ", Phone, "Date: ", Date, "Slot: ", Slot, "Message: ", Message
    msge = str(msge)

    from email.message import EmailMessage
    import ssl
    import smtplib
    import certifi

    dept = request.form['Department']
    slot = request.form['slot']
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']
    pt_mail = request.form['mail']
    date = request.form['date']
    Dept = dept
    Name = name
    Phone = phone
    Mail = str(pt_mail)
    Date = str(date)
    Slot = slot
    Message = message
    msge = "Dept: ", Dept, "Name: ", Name, "Phone: ", Phone, "Date: ", Date, "Slot: ", Slot, "Message: ", Message
    msge = str(msge)

    email_sender = "drdev.maill@gmail.com"
    email_password = "mmieeonadmnrylqz"
    email_receiver = ["adrushtshetty@gmail.com", "nithishg2005@gmail.com", "pikaa1024@gmail.com",
                      "doctor.dev.ml@gmail.com"]
    subject = "Appointment on " + Date + ". Slot: " + Slot + " Dept: " + Dept
    body = """
            {pName} needs an appointment in the {pdept} department, 
            on the {pdate} for the {pslot} slot.

            {pName}'s Message:
            {pmessage}
            --------------------------------------------------------

            {pName}
            Phone No.: {pNo}
            Mail Id: {pMail}

            """.format(pName=Name, pdept=Dept, pdate=Date, pMail=Mail, pNo=Phone, pmessage=Message, pslot=Slot)
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    import fileinput
    import shutil
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    name = Name
    dept1 = Dept
    Phone1 = Phone
    pt_mail1 = pt_mail
    date1 = Date
    Slot1 = Slot
    Usr = name

    filename = Usr + '.html'
    shutil.copy('usermail.html', filename)
    print(filename)

    if dept == "Dental":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/qB_QFiGU4NZ3tPnU-XPCfAKNHd3edTGE6k__c7Rbe5rZkKtwKWigqKbhNUlfKP_oTzzC9s-4uz5ns0_T5t0SvOXoqf9kph2ZCV-xoC8zajC4qfOFgMkuouOaDWvfj3SdrPIr5tCHxA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "Cardiology":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/H7wXYjQuxPA3gy_Ayi2ZQyJyZaywgDV911RlvXFdo7jDdQ5ibAfmmIAEu14mtfI_F_tBdOQBSi13MsskjRrAnJnRqQ2VsmhFz00wxd8HSmGYuVBhKiz3hfDue_Z3nUVW0BPCeMcUtw=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "Dermatology":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/TuvNAJINod6EbC_adSeMrYCGwU0w3j2hgKWI3km_W7Hn46arGZCMV5DclyXAHMygxJgqbf4PINTLumemxVQ5iq52SJt_yKLUfzz5GNpWVrU6uik7s6FaLlFfyAAa0yE_HCjuhO0N5g=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "General Check-Up":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/n6ewD4b_HoFU0PcJyotOVFIE9V1L3jgqa20l3FM_zySVfLvhRAtPJMsb4sAqaPADmWd37lOzrBlXafm3CTgw6zbgCqIf5rGTdkPgfppnQc8WC2oLh4KVyh4ym-4Eb9lwJCfFfyk1aA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "Clinical Laboratory":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/CIzu70Ef_aZw_uB3nC_yR1UYpGsMTjAazO4C8dYGF9LgR_bIaOeZCWmiEwElETQkiQqAs71inyx6-q5z5XZZw6Ynt1ARLJ1dsl_71abFBPELdnD0hzqV9exsHC51rEfibLqgX18EsA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "Ophthalmology":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/IXxfw1NvJe52s00wvyA01I-MlRJxLLds_pv6LTDNZml6p4neKzDH_LBDOwuwO4lJSD2xOiRh0tgNf5acz6Ad8B28RozSsEF4Kl2QHfWy0zEPw5Tpw56K6kpn3ZmaOAwJg99jDIA4nw=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "Radiology":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/zi_5Hx9ITyM3YKcuOTtcrb5rda0BkoSlyynjPd6xnpyBgrV9Na2ZX5pAUsW8w8AsGjT4wL49JQON3djNrhDgiodEEou7dhklfBM2lrxSij5_if-LL32tLZKSb4qI1uFRA5jVB1PSwA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')


    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace("<!--Name-->", Usr), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace("<!--Dental-->", dept1), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace("<!--Name1-->", Usr), end='')
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('<!--+91987654321-->', Phone1), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('<!--something@gmail.com-->', pt_mail1), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('<!--2022/11/03-->', date1), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('<!--12:00 - 13:00-->', Slot1), end='')

    file1 = open(filename, 'r')
    Lines = file1.readlines()

    str1 = (''.join(Lines))

    me = "drdev.maill@gmail.com"
    you = pt_mail1
    # you=request.form['Mail']
    print(you)
    # you = "adrushtshetty@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Appointment Confirmation"
    msg['From'] = me
    msg['To'] = you
    html = str1

    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('drdev.maill@gmail.com', 'mmieeonadmnrylqz')
    mail.sendmail(me, you, msg.as_string())
    mail.quit()

    import os
    if os.path.exists(filename):
        os.remove(filename)
    else:
        pass
    return render_template("Appointment_CONFIRM.html", send_name='{}'.format(Name), send_dept='{}'.format(Dept),
                           send_date='{}'.format(Date), send_slot='{}'.format(Slot))


# @app.route('/trial')
# def trial():
#     return render_template("Comprehensive.html")

@app.route('/', methods=['POST'])
def bookAppointment():
    from email.message import EmailMessage
    import ssl
    import smtplib
    import certifi

    dept = request.form['Department']
    slot = request.form['slot']
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']
    pt_mail = request.form['mail']
    date = request.form['date']
    Dept = dept
    Name = name
    Phone = phone
    Mail = str(pt_mail)
    Date = str(date)
    Slot = slot
    Message = message
    msge = "Dept: ", Dept, "Name: ", Name, "Phone: ", Phone, "Date: ", Date, "Slot: ", Slot, "Message: ", Message
    msge = str(msge)

    email_sender = "drdev.maill@gmail.com"
    email_password = "mmieeonadmnrylqz"
    email_receiver = ["adrushtshetty@gmail.com", "noelgjose05@gmail.com", "pikaa1024@gmail.com","doctor.dev.ml@gmail.com"]
    subject = "Appointment on " + Date + ". Slot: " + Slot + " Dept: " + Dept
    body = """
        {pName} needs an appointment in the {pdept} department, 
        on the {pdate} for the {pslot} slot.

        {pName}'s Message:
        {pmessage}
        --------------------------------------------------------

        {pName}
        Phone No.: {pNo}
        Mail Id: {pMail}

        """.format(pName=Name, pdept=Dept, pdate=Date, pMail=Mail, pNo=Phone, pmessage=Message, pslot=Slot)
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    import fileinput
    import shutil
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    name = Name
    dept1=Dept
    Phone1=Phone
    pt_mail1 = pt_mail
    date1=Date
    Slot1 = Slot
    Usr = name


    filename = Usr + '.html'
    shutil.copy('usermail.html', filename)
    print(filename)

    if dept=="Dental":
        srchline='<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline='<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/qB_QFiGU4NZ3tPnU-XPCfAKNHd3edTGE6k__c7Rbe5rZkKtwKWigqKbhNUlfKP_oTzzC9s-4uz5ns0_T5t0SvOXoqf9kph2ZCV-xoC8zajC4qfOFgMkuouOaDWvfj3SdrPIr5tCHxA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "Cardiology":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/H7wXYjQuxPA3gy_Ayi2ZQyJyZaywgDV911RlvXFdo7jDdQ5ibAfmmIAEu14mtfI_F_tBdOQBSi13MsskjRrAnJnRqQ2VsmhFz00wxd8HSmGYuVBhKiz3hfDue_Z3nUVW0BPCeMcUtw=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "Dermatology":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/TuvNAJINod6EbC_adSeMrYCGwU0w3j2hgKWI3km_W7Hn46arGZCMV5DclyXAHMygxJgqbf4PINTLumemxVQ5iq52SJt_yKLUfzz5GNpWVrU6uik7s6FaLlFfyAAa0yE_HCjuhO0N5g=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "General Check-Up":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/n6ewD4b_HoFU0PcJyotOVFIE9V1L3jgqa20l3FM_zySVfLvhRAtPJMsb4sAqaPADmWd37lOzrBlXafm3CTgw6zbgCqIf5rGTdkPgfppnQc8WC2oLh4KVyh4ym-4Eb9lwJCfFfyk1aA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "Clinical Laboratory":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/CIzu70Ef_aZw_uB3nC_yR1UYpGsMTjAazO4C8dYGF9LgR_bIaOeZCWmiEwElETQkiQqAs71inyx6-q5z5XZZw6Ynt1ARLJ1dsl_71abFBPELdnD0hzqV9exsHC51rEfibLqgX18EsA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "Ophthalmology":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/IXxfw1NvJe52s00wvyA01I-MlRJxLLds_pv6LTDNZml6p4neKzDH_LBDOwuwO4lJSD2xOiRh0tgNf5acz6Ad8B28RozSsEF4Kl2QHfWy0zEPw5Tpw56K6kpn3ZmaOAwJg99jDIA4nw=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')
    elif dept == "Radiology":
        srchline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/f1ABfs6pswzdUrSOvLLZ6X0wS4v5XkYrZ9WcXhBJV4TiW7A462GBSAtepUUkFPo2a0AUXNOGHNvDXtXHe7T2ubDjqkv0pbCIrczspkU7pSGjwC0KLJ104MCWY3Y9CzCPakZbXEcsMA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        rplline = '<div align="center" class="alignment" style="line-height:10px"><a href="www.example.com" style="outline:none" tabindex="-1" target="_blank"><img alt="sculptor" class="fullMobileWidth" src="https://lh3.googleusercontent.com/zi_5Hx9ITyM3YKcuOTtcrb5rda0BkoSlyynjPd6xnpyBgrV9Na2ZX5pAUsW8w8AsGjT4wL49JQON3djNrhDgiodEEou7dhklfBM2lrxSij5_if-LL32tLZKSb4qI1uFRA5jVB1PSwA=w2400" style="display: block; height: auto; border: 0; width: 249px; max-width: 100%;" title="sculptor" width="249"/></a></div>'
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace(srchline, rplline), end='')



    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace("<!--Name-->", Usr), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace("<!--Dental-->", dept1), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace("<!--Name1-->",Usr), end='')
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('<!--+91987654321-->',Phone1), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('<!--something@gmail.com-->',pt_mail1), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('<!--2022/11/03-->',date1), end='')

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('<!--12:00 - 13:00-->',Slot1), end='')



    file1 = open(filename, 'r')
    Lines = file1.readlines()

    str1 = (''.join(Lines))

    me = "drdev.maill@gmail.com"
    you = pt_mail1
    # you=request.form['Mail']
    print(you)
    # you = "adrushtshetty@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Appointment Confirmation"
    msg['From'] = me
    msg['To'] = you
    html = str1

    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('drdev.maill@gmail.com', 'mmieeonadmnrylqz')
    mail.sendmail(me, you, msg.as_string())
    mail.quit()

    import os
    if os.path.exists(filename):
        os.remove(filename)
    else:
        pass
    return render_template("Appointment_CONFIRM.html", send_name='{}'.format(Name), send_dept='{}'.format(Dept),
                           send_date='{}'.format(Date), send_slot='{}'.format(Slot))


@app.route('/covid19', methods=['POST'])
def covid():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    if prediction[0] == 1:
        output = "INFECTED"
        msg = "Please take care."
    else:
        output = "Not Infected"
        msg = "Lessgo...!"
    return render_template("COVID_Confirm.html", prediction_text='{}'.format(output), msg_text='{}'.format(msg))


@app.route("/alergy_flu_cold_covid", methods=['POST'])
def afcc():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model1.predict(final_features)
    if prediction[0] == 0:
        output = "Allergy"
        msg = "Its an allergy why don't you get an allergy routine done."
    elif prediction[0] == 1:
        output = "Cold"
        msg = "Lessgo...! at least itsn't one from the rest !"
    elif prediction[0] == 2:
        output = "COVID"
        msg = "Please take care."
    elif prediction[0] == 3:
        output = "Flu"
        msg = "Its the flu go to your nearest doctor and get your self a prescription"
    return render_template("AFCC_Confirm.html", prediction_text='{}'.format(output), msg_text='{}'.format(msg))


@app.route('/diabetes', methods=['POST'])
def diabetes():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model2.predict(final_features)
    if prediction[0] == 0:
        output = "Not Diabetic"
        msg = "lessgo..."
    elif prediction[0] == 1:
        output = "Diabetic"
        msg = "Take care."

    return render_template("DIABETES_Confirm.html", prediction_text='{}'.format(output), msg_text='{}'.format(msg))


@app.route('/cvd', methods=['POST'])
def cvd():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model3.predict(final_features)
    if prediction[0] == 0:
        output = "SAFE"
        msg = "For the next ten years, you are unlikely to have any cardiovascular disease."
    elif prediction[0] == 1:
        output = "CVD"
        msg = "Within the next ten years, you will almost certainly get a CVD. Please exercise cautious and contact your cardiologist right away."
    return render_template("CVD_Confirm.html", prediction_text='{}'.format(output), msg_text='{}'.format(msg))


@app.route('/stroke')
def strokeUI():
    return render_template("Stroke.html")


@app.route('/stroke', methods=['POST'])
def stroke():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model5.predict(final_features)
    if prediction == 1:
        output = "ALERT"
        msg = "You are prone to having a stroke"
    if prediction == 0:
        output = "Safe"
        msg = "You are not prone to having a stroke"

    return render_template("Stroke_CONFIRM.html", prediction_text='{}'.format(output), msg_text='{}'.format(msg))


@app.route('/bmi')
def bmiUI():
    return render_template("BMI.html")


@app.route('/bmi', methods=["POST"])
def bmi():
    heightUnit = request.form['heightUnit']
    height = float(request.form['height'])
    if heightUnit == "cm":
        height = height * 0.01
    elif heightUnit == "ft":
        height = height * 0.3048
    elif heightUnit == "inch":
        height = height * 0.0254
    weight = float(request.form['weight'])
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    return render_template("BMI_Confirm.html", bmi_fv='{}'.format(bmi))


@app.route('/comprehensive', methods=['POST'])
def comp():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model4.predict(final_features)
    if prediction[0] == 15:
        output = "Fungal Infection"
        msg = "You have a fungal infection."
    elif prediction[0] == 4:
        output = "Allergy"
        msg = "You have an allergy."
    elif prediction[0] == 16:
        output = "GERD"
        msg = "You have a Gastroesophageal reflux disease."
    elif prediction[0] == 9:
        output = "Chronic cholestasis"
        msg = "You have a chronic cholestatic disease."
    elif prediction[0] == 33:
        output = "Peptic Ulcer Disease"
        msg = "You have a peptic ulcer disease."
    elif prediction[0] == 14:
        output = "Drug Reaction"
        msg = "You have a nonallergic hypersensitivity reaction or pseudoallergic drug reaction."
    elif prediction[0] == 1:
        output = "AIDS"
        msg = "You have AIDS."
    elif prediction[0] == 12:
        output = "Diabetes"
        msg = "You have diabetes."
    elif prediction[0] == 17:
        output = "Gastroenteritis"
        msg = "You have a stomach flu/gastroenteritis."
    elif prediction[0] == 6:
        output = "Bronchial Asthma"
        msg = "You have bronchial asthma."
    elif prediction[0] == 23:
        output = "Hypertension"
        msg = "You have hypertension."
    elif prediction[0] == 30:
        output = "Migrane"
        msg = "You have a migrane."
    elif prediction[0] == 7:
        output = "Cervical Spondylosis"
        msg = "You have cervical spondylosis."
    elif prediction[0] == 32:
        output = "Paralysis/Brain Hemorrhage"
        msg = "You are prone to brain hemorrhage."
    elif prediction[0] == 28:
        output = "Jaundice"
        msg = "You have jaundice."
    elif prediction[0] == 29:
        output = "Malaria"
        msg = "You might have malaria."
    elif prediction[0] == 8:
        output = "Chicken Pox"
        msg = "You might have chicken pox."
    elif prediction[0] == 11:
        output = "Dengue"
        msg = "You have dengue."
    elif prediction[0] == 37:
        output = "Typhoid"
        msg = "You have typhoid."
    elif prediction[0] == 40:
        output = "Hepatitis A"
        msg = "You have Hepatitis A."
    elif prediction[0] == 19:
        output = "Hepatitis B"
        msg = "You have Hepatitis B."
    elif prediction[0] == 20:
        output = "Hepatitis C"
        msg = "You have Hepatitis C."
    elif prediction[0] == 21:
        output = "Hepatitis D"
        msg = "You have Hepatitis D."
    elif prediction[0] == 22:
        output = "Hepatitis E"
        msg = "You have Hepatitis E."
    elif prediction[0] == 3:
        output = "Alcoholic Hepatitis"
        msg = "You have alcoholic Hepatitis."
    elif prediction[0] == 36:
        output = "Tuberculosis"
        msg = "You have tuberculosis."
    elif prediction[0] == 10:
        output = "Common cold"
        msg = "You have common cold."
    elif prediction[0] == 34:
        output = "Pneumonia"
        msg = "You have pneumonia."
    elif prediction[0] == 13:
        output = "Piles"
        msg = "You have piles."
    elif prediction[0] == 18:
        output = "Heart Attack"
        msg = "You are prone to a heart attack."
    elif prediction[0] == 39:
        output = "Varicose veins"
        msg = "You have varicose veins."
    elif prediction[0] == 26:
        output = "Hypothyroidism"
        msg = "You have Hypothyroidism."
    elif prediction[0] == 24:
        output = "Hyperthyroidism"
        msg = "You have Hyperthyroidism."
    elif prediction[0] == 25:
        output = "Hypoglycemia"
        msg = "You have low blood sugar levels."
    elif prediction[0] == 31:
        output = "Osteoarthritis"
        msg = "You have osteoarthritis."
    elif prediction[0] == 5:
        output = "Arthritis"
        msg = "You have arthritis."
    elif prediction[0] == 0:
        output = "Vertigo"
        msg = "You have vertigo."
    elif prediction[0] == 2:
        output = "Acne"
        msg = "You have Acne."
    elif prediction[0] == 38:
        output = "Urinary tract infection"
        msg = "You have a urinary tract infection"
    elif prediction[0] == 35:
        output = "Psoriasis"
        msg = "You have psoriasis."
    elif prediction[0] == 27:
        output = "Impetigo"
        msg = "You have impetigo."
    return render_template("Comp_CONFIRM.html", prediction_text='{}'.format(output), msg_text='{}'.format(msg))


if __name__ == '__main__':
    app.run(debug=True)