#To be used by password_spry.py in future code

def frameworkChecker(framework: str) -> bool:
    if framework == "Jinga2" or "jinga2":                    
        csrf = ["{{ csrf_token }}", "{% csrf_token %}"]
        return True      
    if framework == "Django" or "django":                   
        csrf = ["csrf_token", "{% csrf_token %}"]
        return True
    if framework == "ASP.NET" or "asp.net":
        csrf = ["RequestVerificationToken","Html.AntiForgeryToken","__RequestVerificationToken"]
        return True
    #PHP, there isn't much need for PHP as it's easy to work out and there are tons of tools on the web for attacking php sites.
    #if (!$token || $token !== $_SESSION['token']) {
    #// process error
    #}