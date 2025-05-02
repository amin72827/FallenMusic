from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("19769686"))
API_HASH = getenv("515b64f5d2d955cdd6aa85a808fd4cb4")

BOT_TOKEN = getenv("7128782242:AAENypkyECvS57mm7nGhIQNvqkTWQS2VLeI", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6671591267"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("AgEtqVYAIBz31WyrBBjdK2i8aIYndovh8dymI1u9doyOd5YH73WsXanvTiOw99g7zwVMobNUdfEmAEITi0MIiRReM8HeQj9Ua6t0yNtkenEAdik9L8mplzz7DojXJIdksBtKNuBMNggBrB06yyX_dfMUcB49nJcKnbo-b-7hFITypHiN8aBAxSSRnAsIydX3HSuCqVjztPh1YLDdkwVbaRGz5VmuT3Qhx7GabaThHAXCygszzr6fJKoPN6tS9Xkjdh_de4WOdQel_JFtd0Im7s3dhG6orAgxqNMgOaa-ITseZVk3ZetZWHAHgTklhrDsxqiX39aOzYEMVWRfS8SPOPaor2Yu1gAAAAGC_6I6AA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NergizSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ErSohbetttttt")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7652416346").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
