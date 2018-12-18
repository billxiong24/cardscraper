import DukeCardController
import currency

dck = DukeCardController.DukeCardController()
dck.login("dummyuser", "dummypass")
dck.add_balance(currency.Currency.FLEX, 19)
