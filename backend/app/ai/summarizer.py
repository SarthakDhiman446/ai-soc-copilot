class AISummarizer:

    @staticmethod
    def summarize(parsed_events, threats):

        if not parsed_events:
            return {
                "summary": "No security events detected."
            }

        event_count = len(parsed_events)
        threat_count = len(threats)

        highest_severity = "Low"

        for threat in threats:
            severity = threat.get("severity", "Low")

            if severity == "High":
                highest_severity = "High"
                break

            elif severity == "Medium" and highest_severity != "High":
                highest_severity = "Medium"

        summary = (
            f"{event_count} security events were detected. "
            f"{threat_count} threats were identified. "
            f"Overall incident severity is {highest_severity}."
        )

        recommendations = []

        if highest_severity == "High":
            recommendations.extend([
                "Block the suspicious IP address.",
                "Reset affected user passwords.",
                "Enable Multi-Factor Authentication.",
                "Review authentication logs."
            ])

        elif highest_severity == "Medium":
            recommendations.extend([
                "Monitor the source IP.",
                "Review login attempts.",
                "Increase authentication monitoring."
            ])

        else:
            recommendations.append(
                "Continue monitoring the environment."
            )

        return {
            "summary": summary,
            "severity": highest_severity,
            "recommendations": recommendations
        }