#Threat Intelligence

#Sample threat indicators

threat_indicators=[
    "malicious_ip_1",
    "suspicious_domain.com",
    "malware.exe",
    "phishing_attack.doc",
    ]

#Rules for threat indicator analysis

rules={
    "malicious_ip":["malicious_ip_1", "malicious_ip_2", "malicious_ip_3"],
    "malicious_domain":["suspicious_domain.com","evil_domain.net"],
    "malware_file" :["malware.exe","trojan.exe"],
    "phishing_doc":["phishing_attacks","spam.docx"],
    }

#Function to analyze threat indicators

def analyze_threat_indicators(indicators,threat_rules):
        results={}
        for indicator in indicators:
            for rule,rule_indicators in threat_rules.items():
                if indicator in rule_indicators:
                    if rule not in results:
                        results[rule]=[]
                        results[rule].append(indicator)
        return results


#Analyze threat indicators

analysis_results=analyze_threat_indicators(threat_indicators,rules)

#Print the results

for rule,matched_indicators in analysis_results.items():
    print(f"Threat Rule: {rule}")
    print("Matched Indicators:")
    for indicator in matched_indicators:
        print(f" .{indicator}")
    print()
    
        
