from ldap3 import Server,Connection,ObjectDef, AttrDef, Reader, Entry, Attribute, OperationalAttribute
import ldap3
import re
​
​
def AD_user_search(server, search_base, login, passwd):
    server_in_ldap_form=Server(server,  get_info='ALL', port=636, use_ssl=True)
    conn=Connection(server_in_ldap_form,user=str(login),password=str(passwd), raise_exceptions=True)    
​
    #searcher log in
    def searcher():
        is_authorized = 'False'
        try:
            conn.bind()
            is_authorized=True
            print("is_authorized: " + str(is_authorized))
            return(is_authorized)
        except:
            print("is_authorized : " + str(is_authorized))
            return ()
        return()     
    
    #name parser. From 'AM\\myname' -> 'myname'
    def name_parser(login):
        parsed_name=(re.search(r"[^\\]*$",login))
        return parsed_name.group(0)
​
    #if the user is authorized find groups
    def find_the_user():
        if searcher()==True:
            #conn.search('DC=domainlvl1 name,DC=domain lvl2  name,DC=net','(&(objectclass=user)(sAMAccountName=myname))', attributes=['memberOf'])
            filter="(&(objectclass=user)(sAMAccountName=" + name_parser(login) + "))"
            conn.search(search_base,search_filter = filter, attributes=['memberOf'])
            print (conn.entries)
            return conn.entries
    find_the_user()
​
​
​
​
################################################################################################################################################
#Example:
#AD_user_search(server="your domain name/you domain ip",search_base='DC=domain lvl1,DC=domain lvl2,DC=net / or what you have',login='domain lvl 1\\your name',passwd='mypass')
AD_user_search(server=" ",search_base='DC= ,DC= ,DC= ',login=' \\ ',passwd=' ')
​
​
#server - ad server
#search_base-domain
#login, passwd - log and pass of user who is trying to login 
################################################################################################################################################