# hashcatmatch
script to match hashcat cracked file to the username of NTLM hashes file

python hashcatmatch.py [DC-Hashes file] [cracked file from hashcat]

# lm-info

To check if users are stored in LM Hash format; use secretsdump to extract hashes

python lm-info.py [DC-Hashes.ntds from secretsdump]
