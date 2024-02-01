import pandas as pd

#Load incident handling rules from a csv file

def load_incident_rules(rule_file):
    try:
        return pd.read_csv(rule_file)
    except FileNotFoundError:
        print("Rule file '(rule_file)' not found.")
        return pd.DataFrame(columns=["Alert","Action"])
    
#Automate incident handling files based on rules

    def automate_incident_handling(alert,rules):
        matching_rules=rules[rules["Alert"] == alert]
        if not matching_rules.empty:
            for index,row in matching_rules.itterrows():
                print(f"Handling incident:(alert)-{row['Action']}")
        else:
            print(f"No matching rule found for incident:{alert}")
            
#Main Function

def main():
    rule_file = 'incident_rules.csv'
    incident_rules=load_incident_rules(rule_file)

    while True:
        alert=input("Enter the security alert:")
        if alert.lower() == 'exit':
            break
        automate_incident_handling(alert,incident_rules)

if __name__=='__main__':
    main()
    
    
