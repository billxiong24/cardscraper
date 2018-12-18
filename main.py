import DukeCardController
import currency

dck = DukeCardController.DukeCardController()
dck.post_login("user", "pass")
dck.add_balance(currency.Currency.FLEX, 19)
