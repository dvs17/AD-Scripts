# hashcatmatch
script to match hashcat cracked file to the username of NTLM hashes file

python hashcatmatch.py [DC-Hashes file] [cracked file from hashcat]

# lm-info

To check if users are stored in LM Hash format; use secretsdump to extract hashes

python lm-info.py [DC-Hashes.ntds from secretsdump]

# Enumerating and Analyzing User Description from AD
I tend to use windapsearch.py, https://github.com/ropnop/windapsearch

# Enumerating 
python userdes.py [extracted dump with windapsearch] > user-description

# Analyzing

python udeslyze.py [user-description] [company name i.e. microsoft]
