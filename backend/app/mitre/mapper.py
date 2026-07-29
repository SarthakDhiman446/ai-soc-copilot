class MitreMapper:

    MITRE_MAPPING = {

        "Failed Login": {
            "technique_id": "T1110",
            "technique": "Brute Force",
            "tactic": "Credential Access"
        },

        "Successful Login": {
            "technique_id": "T1078",
            "technique": "Valid Accounts",
            "tactic": "Defense Evasion"
        },

        "Port Scan": {
            "technique_id": "T1046",
            "technique": "Network Service Discovery",
            "tactic": "Discovery"
        }

    }

    @classmethod
    def map_event(cls, event_type: str):

        return cls.MITRE_MAPPING.get(
            event_type,
            {
                "technique_id": "Unknown",
                "technique": "Unknown",
                "tactic": "Unknown"
            }
        )