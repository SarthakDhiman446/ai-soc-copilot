from collections import Counter


class ThreatDetector:

    @staticmethod
    def detect_threats(parsed_events):

        threats = []
        failed_ips = []

        # Collect all failed login IPs
        for event in parsed_events:
            if (
                event["event_type"] == "Failed Login"
                and event["ip_address"]
            ):
                failed_ips.append(event["ip_address"])

        # Count failed logins per IP
        counter = Counter(failed_ips)

        for ip, count in counter.items():

            if count >= 5:
                threats.append({
                    "type": "Brute Force Attack",
                    "severity": "High",
                    "ip": ip,
                    "attempts": count
                })

            elif count >= 3:
                threats.append({
                    "type": "Suspicious Login Activity",
                    "severity": "Medium",
                    "ip": ip,
                    "attempts": count
                })

        return threats