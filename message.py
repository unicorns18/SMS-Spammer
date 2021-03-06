import vonage
from dotenv import load_dotenv
from colorama import Fore, Back, Style

load_dotenv()

print(Fore.RED + "!!! PUT THE NUMBER IN A E.164 FORMAT !!! " + Fore.GREEN + "(Example: +19998887777)")
print(Fore.RED + "!!! PUT THE NUMBER IN A E.164 FORMAT !!! " + Fore.GREEN + "(Example: +19998887777)")
print(Fore.RED + "!!! PUT THE NUMBER IN A E.164 FORMAT !!! " + Fore.GREEN + "(Example: +19998887777)")
print(Fore.RED + "!!! PUT THE NUMBER IN A E.164 FORMAT !!! " + Fore.GREEN + "(Example: +19998887777)")
print(Fore.RED + "!!! PUT THE NUMBER IN A E.164 FORMAT !!! " + Fore.GREEN + "(Example: +19998887777)")
print(Fore.RED + "!!! PUT THE NUMBER IN A E.164 FORMAT !!! " + Fore.GREEN + "(Example: +19998887777)")
print(Style.RESET_ALL)

phone_number = int(input("What phone number do you want to message: "))
message_body = str(input("What is the message you want to send: "))

api_key = os.environ.get("key")
api_secret = os.environ.get("secret")

# Add your key and secret key from Vonage here! :)
client = vonage.Client(key=api_key, secret=api_secret)
sms = vonage.Sms(client)

# Put search_pattern to whatever you want, don't touch pattern. (1 = if that search pattern is in any of the number)
responseData = client.get_account_numbers(
    {"pattern": '1', "search_pattern": '1'}
)

for number in responseData["numbers"]:
    while True:
        responseData = sms.send_message(
            {
                "from": number["msisdn"],
                "to": "+17086651159",
                "text": message_body,
            }
        )

        print("Message sent successfully.")
    #if responseData["messages"][0]["status"] == "0":
    #else:
        #print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
