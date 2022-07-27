import requests
import json

url = "https://YOUR-TENANT.webhook.office.com/webhookb2/" \
      "id "

payload = json.dumps({
  "@type": "MessageCard",
  "themeColor": "0072C6",
  "@context": "https://schema.org/extensions",
  "title": "Test einer Messagecard",
  "text": "Click **Learn More** to learn more about Actionable Messages!",
  "potentialAction": [
    {
      "@type": "ActionCard",
      "name": "Send Feedback",
      "inputs": [
        {
          "@type": "TextInput",
          "id": "feedback",
          "isMultiline": True,
          "title": "Let us know what you think about Actionable Messages"
        }
      ],
      "actions": [
        {
          "@type": "HttpPOST",
          "name": "Messagecard validieren",
          "isPrimary": True,
          "target": "https://messagecardplayground.azurewebsites.net/"
        }
      ]
    },
    {
      "@type": "OpenUri",
      "name": "Learn More",
      "targets": [
        {
          "os": "default",
          "uri": "https://docs.microsoft.com/outlook/actionable-messages"
        }
      ]
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
