# GET request to this url will redirect to login site
LOGIN = "https://dukecard.duke.edu/mydukecard/"

LOGIN_POST = "https://shib.oit.duke.edu/idp/authn/external"

# site that lets us read flex/food balance
BALANCE = "https://dco31.oit.duke.edu/mydukecard/"

# site to add flex/food -  we need some tokens on this site
ADD_BALANCE_GET = "https://dco31.oit.duke.edu/mydukecard/bursar.aspx"

# POST request to actually add balance. Use our tokens here
ADD_BALANCE_POST = "https://dco31.oit.duke.edu/mydukecard/bursar_transaction.aspx"
