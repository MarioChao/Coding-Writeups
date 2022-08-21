# Challenge description:
# Surveys are an integral part of every CTF, please fill in ours [here]<https://forms.gle/uYTgGDYf2bp1pnLy7>!
"""
  1. Fill out the survey linked in the challenge description
  2. At the very end of the survey, there is a code "Y29yY3Rme2hvcGVfeW91X2hhZF9mdW59"
  3. Decode the message in base64 as mentioned
"""
import base64
encryptedCode = "Y29yY3Rme2hvcGVfeW91X2hhZF9mdW59"
decryptedCode = base64.b64decode(encryptedCode)
print(str(decryptedCode, 'utf-8'))
