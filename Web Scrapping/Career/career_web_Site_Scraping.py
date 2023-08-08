import requests
from bs4 import BeautifulSoup

try:
    #taking website, cheking website and creating soup object
    html_text = requests.get("copyright i cannot write")
    html_text.raise_for_status()
    print("Connecting ####.net ....")
    soup = BeautifulSoup(html_text.text, "lxml")

    #parameters that we want to find
    content = soup.find_all("div", class_="title-wrapper")
    time_details = soup.find_all("div", class_="card-bottom-wrapper")

    #creating all_jobs list for writing and comparing
    all_jobs=[]
    #for loop for reaching sub level of divs
    print("We are searching jobs...")
    for contents,time_details in zip(content,time_details):
        
        job_name = contents.find("div", class_="title-left").text
        company_name = contents.find("div", class_="subtitle").text
        job_details = contents.find("div", class_ = "job-detail").text
        time = time_details.find("div", class_="card-right").text

        if "accessible" or "\n" in job_name:
            job_name = job_name.replace("accessible","")
            job_name = job_name.replace("\n","")
            job_name = job_name.replace("\t","")

        #some commercial jobs dont have date information so i add manually -2      
        if time =="":
            time = "-2"

        all_jobs.append({"is tanimi": job_name,
                         "firma ismi": company_name,
                         "işin detayı": job_details,
                         "Güncelleme tarihi": time
                         })
        
    print("Please wait we are sorting your jobs")
        
    with open("all_jobs_record.txt", "w") as recordfile :

        for index in range(len(all_jobs)):

            if "gün" and not "Son gün" in all_jobs[index]["Güncelleme tarihi"]:

                if"Bugün" in all_jobs[index]["Güncelleme tarihi"]:
                   
                   all_jobs[index]["Güncelleme tarihi"]= all_jobs[index]["Güncelleme tarihi"].replace("Bugün", "0")
                else:
                    
                    all_jobs[index]["Güncelleme tarihi"]=all_jobs[index]["Güncelleme tarihi"].replace("gün", "")
                    all_jobs[index]["Güncelleme tarihi"]= all_jobs[index]["Güncelleme tarihi"].replace(" ", "")
            elif "Son gün" in all_jobs[index]["Güncelleme tarihi"]:
                all_jobs[index]["Güncelleme tarihi"]= all_jobs[index]["Güncelleme tarihi"].replace("Son gün", "-1")

            if "Yeni" in all_jobs[index]["Güncelleme tarihi"]:
                all_jobs[index]["Güncelleme tarihi"]= all_jobs[index]["Güncelleme tarihi"].replace("Yeni","0")
            
            
        all_jobs = sorted(all_jobs, key=lambda x: int(x["Güncelleme tarihi"]))
        
        for index in range(len(all_jobs)):
            recordfile.write(f"İş tanımı:{ all_jobs[index]['is tanimi'] }\n"+
                             f"Firma ismi:{all_jobs[index]['firma ismi']}\n"+
                             f"İşin detayı:{all_jobs[index]['işin detayı']}\n"+
                             f"Güncellenme tarihi:{all_jobs[index]['Güncelleme tarihi']}\n"+
                             f"------------------------------------------------\n")
        print("We found jobs!! Check your notepad!!")
        print("Have a good day")


except Exception as exc:
    print("There was an error %s" %exc)




